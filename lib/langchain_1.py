
import os
import openai

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI

load_dotenv()  # This loads the environment variables from the .env file

openai.api_key = os.environ['OPENAI_API_KEY']
llm_model = "gpt-3.5-turbo"


