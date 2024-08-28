import getpass
import os

# Set your Anthropic API key
os.environ["ANTHROPIC_API_KEY"] = getpass.getpass()

# Set your Google API key
os.environ["GOOGLE_API_KEY"] = getpass.getpass()

# You can get an API key here https://financialdatasets.ai/
os.environ["FINANCIAL_DATASETS_API_KEY"] = getpass.getpass()

# You can create an API key here https://smith.langchain.com/settings
os.environ["LANGCHAIN_TRACING_V2"] = "True"
os.environ["LANGCHAIN_API_KEY"] = getpass.getpass()