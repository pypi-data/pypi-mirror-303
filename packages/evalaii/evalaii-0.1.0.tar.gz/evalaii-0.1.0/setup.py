from setuptools import setup, find_packages

setup(
    name="evalaii",
    version="0.1.0",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        "pymongo",
        "bcrypt",
        "openai",
        "pinecone-client",
        "aiohttp",
    ],
    author="Pushpender Solanki",
    author_email="pushpendersolanki895@gmail.com",
    description="A helper library for handling LLM evaluation systems",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/poemsforaphrodite/eval",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
