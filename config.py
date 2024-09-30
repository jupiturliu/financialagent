import getpass
import os

def set_api_keys():
    os.environ["ANTHROPIC_API_KEY"] = getpass.getpass("Enter your Anthropic API key: ")
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google API key: ")
    os.environ["FINANCIAL_DATASETS_API_KEY"] = getpass.getpass("Enter your Financial Datasets API key: ")
    os.environ["LANGCHAIN_TRACING_V2"] = "True"
    os.environ["LANGCHAIN_API_KEY"] = getpass.getpass("Enter your LangChain API key: ")