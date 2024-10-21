from .config import (
    DB_NAME,
    USERS_COLLECTION,
    MONGODB_URI,
    OPENAI_API_KEY,
    PINECONE_API_KEY,
    PINECONE_ENVIRONMENT,
    PINECONE_INDEX_NAME
)
from pymongo import MongoClient
from bson import json_util, ObjectId
import json
from datetime import datetime
import asyncio
from openai import AsyncOpenAI
from pinecone import Pinecone
import uuid
import aiohttp

class EvalAI:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client[DB_NAME]
        self.users_collection = self.db[USERS_COLLECTION]
        self.evaluation_results_collection = self.db["evaluation_results"]
        self.openai_client = AsyncOpenAI(api_key=OPENAI_API_KEY)
        
        # Initialize Pinecone
        self.pc = Pinecone(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIRONMENT)
        self.pinecone_index = self.pc.Index(PINECONE_INDEX_NAME)
        
        # Initialize HTTP session for Anthropic and Gemini
        self.http_session = aiohttp.ClientSession()

    def get_user_by_api_key(self, api_key: str):
        return self.users_collection.find_one({"apiKey": api_key})

    def get_models(self, api_key: str):
        user = self.get_user_by_api_key(api_key)
        if not user:
            return {"success": False, "error": "Invalid API key", "status": 401}
        
        models = user.get("models", [])
        return {"success": True, "models": models, "status": 200}

    async def evaluate_text_input(self, api_key: str, model_id: str, test_data: list):
        user = self.get_user_by_api_key(api_key)
        if not user:
            return {"success": False, "error": "Invalid API key", "status": 401}

        model = next((m for m in user.get("models", []) if m["model_id"] == model_id), None)
        if not model:
            return {"success": False, "error": "Model not found", "status": 404}

        formatted_model_name = model['model_name']

        evaluation_results = []
        for entry in test_data:
            prompt = entry["prompt"]["prompt"] if isinstance(entry["prompt"], dict) else entry["prompt"]
            context = entry.get("context", "")
            response = entry.get("response", "")
            
            result = await self._evaluate_response(prompt, context, response, user["username"], formatted_model_name)
            if result:
                formatted_result = {
                    "_id": ObjectId(),
                    "prompt": result["prompt"],
                    "context": result["context"],
                    "response": result["response"],
                    "factors": result["factors"],
                    "username": result["username"],
                    "modelName": result["modelName"],
                    "evaluatedAt": result["evaluatedAt"]
                }
                evaluation_results.append(formatted_result)

        if evaluation_results:
            self.evaluation_results_collection.insert_many(evaluation_results)

        return {"success": True, "results": evaluation_results, "status": 200}

    async def _get_embedding(self, text: str):
        response = await self.openai_client.embeddings.create(
            model="text-embedding-ada-002",
            input=text,
            encoding_format="float"
        )
        return response.data[0].embedding

    async def _evaluate_response(self, prompt: str, context: str, response: str, username: str, model_name: str):
        evaluation_start_time = datetime.now()

        evaluation_prompt = f"""
        Evaluate the following response based on the given prompt and context. 
        Rate each factor on a scale of 0 to 1, where 1 is the best (or least problematic for negative factors like Hallucination and Bias).
        Please provide scores with two decimal places, and avoid extreme scores of exactly 0 or 1 unless absolutely necessary.

        Context: {context}
        Prompt: {prompt}
        Response: {response}

        Factors to evaluate:
        1. Accuracy: How factually correct is the response?
        2. Hallucination: To what extent does the response contain made-up information? (Higher score means less hallucination)
        3. Groundedness: How well is the response grounded in the given context and prompt?
        4. Relevance: How relevant is the response to the prompt?
        5. Recall: How much of the relevant information from the context is included in the response?
        6. Precision: How precise and focused is the response in addressing the prompt?
        7. Consistency: How consistent is the response with the given information and within itself?
        8. BiasDetection: To what extent is the response free from bias? (Higher score means less bias)

        Provide the evaluation as a JSON object. Each factor should be a key mapping to an object containing 'score' and 'explanation'. 
        Do not include any additional text, explanations, or markdown formatting.
        """

        try:
            completion = await self.openai_client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are an expert evaluator of language model responses."},
                    {"role": "user", "content": evaluation_prompt},
                ],
                temperature=0
            )

            content = completion.choices[0].message.content.strip()

            if not content.startswith('{') or not content.endswith('}'):
                print('Teacher evaluation did not return a valid JSON object.')
                print(f'Response content: {content}')
                return None

            evaluation = json.loads(content)

            required_factors = [
                'Accuracy', 'Hallucination', 'Groundedness', 'Relevance',
                'Recall', 'Precision', 'Consistency', 'BiasDetection'
            ]

            for factor in required_factors:
                if factor not in evaluation:
                    print(f'Missing factor in evaluation: {factor}')
                    return None

            evaluation_end_time = datetime.now()
            evaluation_latency = (evaluation_end_time - evaluation_start_time).total_seconds() * 1000  # in milliseconds

            return {
                "prompt": prompt,
                "context": context,
                "response": response,
                "factors": evaluation,
                "username": username,
                "modelName": model_name,
                "evaluatedAt": evaluation_end_time
            }

        except Exception as e:
            print(f'Error in teacher evaluation: {e}')
            return None

    def add_model(self, api_key: str, model_name: str, model_type: str, custom_api_key: str = None):
        user = self.get_user_by_api_key(api_key)
        if not user:
            return {"success": False, "message": "Invalid API key.", "status": 401}

        allowed_model_names = ["gpt-4o", "gpt-4o-mini", "claude-3.5-sonnet", "gemini"]
        if model_name not in allowed_model_names:
            return {"success": False, "message": f"Invalid model name. Allowed names are: {', '.join(allowed_model_names)}", "status": 400}

        if model_type.lower() != "custom":
            return {"success": False, "message": "Invalid model type. Must be 'custom'.", "status": 400}

        if not custom_api_key:
            return {"success": False, "message": "API Key is required for custom models.", "status": 400}

        model_id = f"{user['username']}_model_{int(datetime.now().timestamp())}"

        model_data = {
            "model_id": model_id,
            "model_name": model_name,
            "model_type": model_type,
            "file_path": None,
            "uploaded_at": datetime.utcnow(),
            "model_api_token": custom_api_key
        }

        try:
            result = self.users_collection.update_one(
                {"apiKey": api_key},
                {"$push": {"models": model_data}}
            )

            if result.modified_count == 1:
                return {
                    "success": True,
                    "message": f"Model '{model_name}' added successfully as {model_id}!",
                    "model_id": model_id,
                    "status": 201
                }
            else:
                return {"success": False, "message": "Failed to add model. User not found or database error.", "status": 500}
        except Exception as e:
            print(f"Error adding model: {e}")
            return {"success": False, "message": "An error occurred while adding the model.", "status": 500}

    async def model_response(self, api_key: str, model_name: str, prompt: str):
        user = self.get_user_by_api_key(api_key)
        if not user:
            return {"success": False, "message": "Invalid API key.", "status": 401}

        model = next((m for m in user.get("models", []) if m["model_name"] == model_name), None)
        if not model:
            return {"success": False, "message": "Model not found.", "status": 404}

        custom_api_key = model.get("model_api_token")

        if model_name in ["gpt-4o", "gpt-4o-mini"]:
            completion = await self.openai_client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0
            )
            return completion.choices[0].message.content.strip()
        
        elif model_name == "claude-3.5-sonnet":
            headers = {
                "Authorization": f"Bearer {custom_api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "claude-3.5",
                "prompt": prompt,
                "max_tokens_to_sample": 150
            }
            async with self.http_session.post("https://api.anthropic.com/v1/complete", headers=headers, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("completion", "").strip()
                else:
                    error = await response.text()
                    print(f"Anthropic API Error: {response.status} - {error}")
                    return ""
        
        elif model_name == "gemini":
            headers = {
                "Authorization": f"Bearer {custom_api_key}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "gemini-1",
                "prompt": prompt,
                "max_tokens": 150
            }
            async with self.http_session.post("https://api.gemini.com/v1/chat/completions", headers=headers, json=payload) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("choices", [{}])[0].get("text", "").strip()
                else:
                    error = await response.text()
                    print(f"Gemini API Error: {response.status} - {error}")
                    return ""
        
        else:
            print(f"Unsupported model: {model_name}")
            return ""

    async def add_context(self, api_key: str, model_name: str, context_file_path: str):
        user = self.get_user_by_api_key(api_key)
        if not user:
            return {"success": False, "message": "Invalid API key.", "status": 401}

        model = next((m for m in user.get("models", []) if m["model_name"] == model_name), None)
        if not model:
            return {"success": False, "message": "Model not found.", "status": 404}

        try:
            with open(context_file_path, 'r') as file:
                context = file.read()

            # Generate embedding for the context
            embedding = await self._get_embedding(context)

            # Create a unique ID for this context
            context_id = str(uuid.uuid4())

            # Upload to Pinecone
            namespace = f"{user['username']}_{model_name}"
            self.pinecone_index.upsert(
                vectors=[(context_id, embedding, {"context": context})],
                namespace=namespace
            )

            return {
                "success": True,
                "message": f"Context added successfully for model '{model_name}'.",
                "context_id": context_id,
                "status": 201
            }
        except Exception as e:
            print(f"Error adding context: {e}")
            return {"success": False, "message": "An error occurred while adding the context.", "status": 500}

    def _chunk_text(self, text, max_tokens=1000):
        tokens = self.tokenizer.encode(text)
        chunks = []
        for i in range(0, len(tokens), max_tokens):
            chunk = self.tokenizer.decode(tokens[i:i + max_tokens])
            chunks.append(chunk)
        return chunks

    async def get_context(self, api_key: str, model_name: str, prompt: str):
        user = self.get_user_by_api_key(api_key)
        if not user:
            return {"success": False, "message": "Invalid API key.", "status": 401}

        model = next((m for m in user.get("models", []) if m["model_name"] == model_name), None)
        if not model:
            return {"success": False, "message": "Model not found.", "status": 404}

        try:
            # Generate embedding for the prompt
            prompt_embedding = await self._get_embedding(prompt)

            # Query Pinecone for similar contexts
            namespace = f"{user['username']}_{model_name}"
            query_result = self.pinecone_index.query(
                vector=prompt_embedding,
                top_k=1,  # Retrieve the most similar context
                namespace=namespace,
                include_metadata=True
            )

            if query_result.matches:
                context = query_result.matches[0].metadata['context']
                return {
                    "success": True,
                    "context": context,
                    "status": 200
                }
            else:
                return {
                    "success": False,
                    "message": "No relevant context found.",
                    "status": 404
                }

        except Exception as e:
            print(f"Error retrieving context: {e}")
            return {"success": False, "message": "An error occurred while retrieving the context.", "status": 500}

    async def evaluate(self, api_key: str, model_name: str, prompt: str):
        user = self.get_user_by_api_key(api_key)
        if not user:
            return {"success": False, "message": "Invalid API key.", "status": 401}

        model = next((m for m in user.get("models", []) if m["model_name"] == model_name), None)
        if not model:
            return {"success": False, "message": "Model not found.", "status": 404}

        # Retrieve context
        context_response = await self.get_context(api_key, model_name, prompt)
        if context_response["success"]:
            context = context_response["context"]
        else:
            context = ""  # Default to empty context if not found

        # Combine context and prompt
        combined_prompt = f"{context}\n{prompt}" if context else prompt

        # Get model response
        response = await self.model_response(api_key, model_name, combined_prompt)

        # Prepare evaluation data
        evaluation_data = [{
            "prompt": prompt,
            "context": context,
            "response": response
        }]

        # Evaluate the response
        eval_result = await self.evaluate_text_input(api_key, model["model_id"], evaluation_data)

        return {
            "success": True,
            "response": response,
            "evaluation": eval_result,
            "status": 200
        }

    async def close(self):
        await self.http_session.close()

    async def process_prompts_file(self, api_key: str, model_name: str, prompts_file_path: str):
        user = self.get_user_by_api_key(api_key)
        if not user:
            return {"success": False, "message": "Invalid API key.", "status": 401}

        model = next((m for m in user.get("models", []) if m["model_name"] == model_name), None)
        if not model:
            return {"success": False, "message": "Model not found.", "status": 404}

        try:
            with open(prompts_file_path, 'r') as file:
                prompts = json.load(file)

            results = []
            for prompt in prompts:
                evaluation_result = await self.evaluate(api_key, model_name, prompt)
                results.append({
                    "prompt": prompt,
                    "result": evaluation_result
                })

            return {
                "success": True,
                "results": results,
                "status": 200
            }
        except Exception as e:
            print(f"Error processing prompts file: {e}")
            return {"success": False, "message": "An error occurred while processing the prompts file.", "status": 500}

