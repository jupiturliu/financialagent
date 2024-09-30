import os
from dotenv import load_dotenv

def set_api_keys():
    load_dotenv()  # Load environment variables from .env file
    os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
    os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
    os.environ["FINANCIAL_DATASETS_API_KEY"] = os.getenv("FINANCIAL_DATASETS_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2", "True")
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")