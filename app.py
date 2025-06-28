from dotenv import load_dotenv
import getpass
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers  import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

messages = [
    SystemMessage("Traduza o seguinte texto para o {idioma}:"),
    HumanMessage("Resposta: {response}"),
]

if not os.environ.get("GROQ_API_KEY"):
  os.environ["GROQ_API_KEY"] = getpass.getpass("Enter API key for Groq: ")

from langchain.chat_models import init_chat_model

model = init_chat_model("llama3-8b-8192", model_provider="groq")
parser = StrOutputParser()
chain = model | parser

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "Traduza o seguinte texto para o {language}"),
    ("user", "Resposta: {text}"),
])

chain = prompt_template | model | parser

# texto = chain.invoke({"language": "português", "text": "Hello, how are you?"})
# print(texto)
