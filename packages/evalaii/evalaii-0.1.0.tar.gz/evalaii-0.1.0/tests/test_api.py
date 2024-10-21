import pytest
import json
from unittest.mock import patch, MagicMock, AsyncMock, ANY
from evalai import EvalHelper
import os
from datetime import datetime

@pytest.fixture(scope="module")
def eval_helper():
    return EvalHelper()

@pytest.fixture(scope="function")
def registered_user(eval_helper):
    return "24ab799b03f6e4c5ecb48c560c884874a7f3f1b457a232867a081bdebb2c0080"

def test_get_models(eval_helper, registered_user):
    api_key = registered_user

    # Mock the database response
    mock_user = {
        "apiKey": api_key,
        "username": "1",
        "models": [
            {
                "model_id": "1_model_1729372891522",
                "model_name": "gpt-4o-mini",
                "model_type": "custom",
                "file_path": None,
                "model_link": None,
                "uploaded_at": datetime(2024, 10, 19, 21, 21, 31, 522000),
                "model_api_token": "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"
            }
        ]
    }
    eval_helper.users_collection.find_one = MagicMock(return_value=mock_user)

    result = eval_helper.get_models(api_key)
    assert result["success"] == True
    assert result["status"] == 200
    assert isinstance(result["models"], list)
    assert len(result["models"]) == 1
    
    model = result["models"][0]
    assert model["model_id"] == "testuser_model_1729372450872"
    assert model["model_name"] == "gpt-4o"
    assert model["model_type"] == "custom"
    assert model["file_path"] is None
    assert isinstance(model["uploaded_at"], datetime)
    assert model["model_api_token"].startswith("sk-proj-TojUkxA5wEF3zdu6Rh30GkPcWBr4vQc6dkZY2Exx25Corlkwf1mEZehKCtBrsT")

    # Try to get models with an invalid API key
    eval_helper.users_collection.find_one = MagicMock(return_value=None)
    result = eval_helper.get_models("invalid_api_key")
    assert result["success"] == False
    assert result["status"] == 401
    assert "Invalid API key" in result["error"]

@pytest.mark.asyncio
async def test_evaluate_text_input(eval_helper, registered_user):
    api_key = registered_user
    model_id = "user_model_1"

    # Mock user and model data
    mock_user = {
        "apiKey": api_key,
        "username": "testuser",
        "models": [
            {
                "model_id": model_id,
                "model_name": "gpt-4o-mini",
                "model_type": "custom"
            }
        ]
    }
    eval_helper.users_collection.find_one = MagicMock(return_value=mock_user)

    # Prepare test data
    test_data = [
        {
            "prompt": {
                "prompt": "Summarize the Industrial Revolution."
            },
            "context": "The Industrial Revolution was a period of major industrialization and innovation during the late 18th and early 19th century."
        }
    ]

    # Mock OpenAI and database responses
    with patch.object(eval_helper.openai_client.chat.completions, 'create', new_callable=AsyncMock) as mock_create, \
         patch.object(eval_helper.db["evaluation_results"], 'insert_many', new_callable=MagicMock) as mock_insert_many:

        # Mock the OpenAI completion response
        mock_completion = MagicMock()
        mock_completion.choices = [MagicMock(
            message=MagicMock(
                content=json.dumps({
                    "Accuracy": {"score": 0.8, "explanation": "Good accuracy"},
                    "Hallucination": {"score": 0.9, "explanation": "Low hallucination"},
                    "Groundedness": {"score": 0.85, "explanation": "Well grounded"},
                    "Relevance": {"score": 0.95, "explanation": "Highly relevant"},
                    "Recall": {"score": 0.75, "explanation": "Good recall"},
                    "Precision": {"score": 0.85, "explanation": "High precision"},
                    "Consistency": {"score": 0.9, "explanation": "Consistent response"},
                    "BiasDetection": {"score": 0.95, "explanation": "Low bias detected"}
                })
            )
        )]
        mock_create.return_value = mock_completion

        result = await eval_helper.evaluate_text_input(api_key, model_id, test_data)

    assert result["success"] == True
    assert result["status"] == 200
    assert len(result["results"]) == 1

    evaluation = result["results"][0]
    assert "_id" in evaluation
    assert evaluation["username"] == "testuser"
    assert evaluation["modelName"] == "gpt-4o-mini (custom)"
    assert "factors" in evaluation
    assert all(factor in evaluation["factors"] for factor in ["Accuracy", "Hallucination", "Groundedness", "Relevance", "Recall", "Precision", "Consistency", "BiasDetection"])

    # Check if the result is saved in the database
    mock_insert_many.assert_called_once_with([evaluation])  # Changed this line

    # Try to evaluate with an invalid API key
    eval_helper.users_collection.find_one = MagicMock(return_value=None)
    result = await eval_helper.evaluate_text_input("invalid_api_key", model_id, test_data)
    assert result["success"] == False
    assert result["status"] == 401
    assert "Invalid API key" in result["error"]

    # Try to evaluate with a non-existent model
    eval_helper.users_collection.find_one = MagicMock(return_value=mock_user)
    result = await eval_helper.evaluate_text_input(api_key, "non_existent_model_id", test_data)
    assert result["success"] == False
    assert result["status"] == 404
    assert "Model not found" in result["error"]

@pytest.mark.asyncio
async def test_add_model(eval_helper, registered_user):
    api_key = registered_user

    # Mock user data
    mock_user = {
        "apiKey": api_key,
        "username": "testuser",
        "models": []
    }
    eval_helper.users_collection.find_one = MagicMock(return_value=mock_user)

    # Mock the update_one method
    with patch.object(eval_helper.users_collection, 'update_one', return_value=MagicMock(modified_count=1)) as mock_update:
        # Test adding a Custom model without API key
        model_name = "custom-model"
        model_type = "custom"
        custom_api_key = None

        result = eval_helper.add_model(api_key, model_name, model_type, custom_api_key=custom_api_key)
        assert result["success"] == False
        assert result["status"] == 400
        assert "API Key is required for custom models." in result["message"]

        # Test adding a Custom model with API key
        model_name = "custom-model"
        custom_api_key = "custom_api_key_12345"
        model_type = "custom"

        # Mock the datetime to ensure consistent model_id and uploaded_at
        fixed_datetime = datetime(2023, 1, 1, 12, 0, 0)
        with patch("evalai.api.datetime") as mock_datetime:
            mock_datetime.now.return_value = fixed_datetime
            mock_datetime.utcnow.return_value = fixed_datetime
            mock_datetime.side_effect = lambda *args, **kw: datetime(*args, **kw)

            result = eval_helper.add_model(api_key, model_name, model_type, custom_api_key=custom_api_key)
            assert result["success"] == True
            assert result["status"] == 201
            assert f"Model '{model_name}' added successfully as testuser_model_{int(fixed_datetime.timestamp())}!" in result["message"]
            mock_update.assert_called_once_with(
                {"apiKey": api_key},
                {"$push": {
                    "models": {
                        "model_id": f"testuser_model_{int(fixed_datetime.timestamp())}",
                        "model_name": model_name,
                        "model_type": model_type,
                        "file_path": None,
                        "uploaded_at": fixed_datetime,
                        "model_api_token": custom_api_key
                    }
                }}
            )

        # Test adding a model with invalid model type
        model_type = "invalid_type"
        result = eval_helper.add_model(api_key, model_name, model_type)
        assert result["success"] == False
        assert result["status"] == 400
        assert "Invalid model type. Must be 'custom'." in result["message"]

    # Test adding a model with invalid API key
    eval_helper.users_collection.find_one = MagicMock(return_value=None)
    result = eval_helper.add_model("invalid_api_key", "model", "custom", custom_api_key="key")
    assert result["success"] == False
    assert result["status"] == 401
    assert "Invalid API key." in result["message"]

def test_custom_context_file_exists():
    assert os.path.exists('tests/custom_context.txt'), "custom_context.txt file should exist in the tests directory"

def test_custom_context_file_not_empty():
    with open('tests/custom_context.txt', 'r') as f:
        content = f.read()
    assert len(content) > 0, "custom_context.txt should not be empty"

def test_prompts_json_file_exists():
    assert os.path.exists('tests/prompts.json'), "prompts.json file should exist in the tests directory"

def test_prompts_json_file_structure():
    with open('tests/prompts.json', 'r') as f:
        prompts = json.load(f)
    
    assert isinstance(prompts, list), "prompts.json should contain a list"
    assert len(prompts) > 0, "prompts.json should not be empty"
    
    for prompt in prompts:
        assert isinstance(prompt, dict), "Each item in prompts.json should be a dictionary"
        assert "prompt" in prompt, "Each prompt should have a 'prompt' key"
        assert isinstance(prompt["prompt"], str), "The 'prompt' value should be a string"
