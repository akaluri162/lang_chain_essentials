
import os
import openai

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

load_dotenv()  # This loads the environment variables from the .env file

openai.api_key = os.environ['OPENAI_API_KEY']
llm_model = "gpt-3.5-turbo"

chat = ChatOpenAI(temperature=0.0, model=llm_model)

template_string = """Tell me a fun fact about \
the country: \
{country}.
"""

prompt_template = ChatPromptTemplate.from_template(template_string)

country = "India"
prompt_country = prompt_template.format_messages(country = country)

gpt_response = chat(prompt_country)
print(gpt_response.content)