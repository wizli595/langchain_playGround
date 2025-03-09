import json
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage

load_dotenv()


class JSONChatMessageHistory:
    """Manages chat history using a JSON file for persistence."""

    def __init__(self, session_id, file_path="chat_history.json"):
        self.session_id = session_id
        self.file_path = file_path
        self._load_history() 
    def _load_history(self):
        """Load JSON history file or initialize a new one."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = {}  
        else:
            data = {}

        self.messages = data.get(self.session_id, [])

    def _save_history(self):
        """Save the updated history to the JSON file."""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
            except json.JSONDecodeError:
                data = {}  
        else:
            data = {}

      
        data[self.session_id] = self.messages
        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def add_messages(self, messages: list[BaseMessage]):
        """Corrected method to add multiple messages at once."""
        self.messages.extend(msg.model_dump() for msg in messages)
        self._save_history()

    def get_messages(self):
        """Retrieve conversation history as LangChain message objects."""
        return [self._convert_to_message(msg) for msg in self.messages]

    def _convert_to_message(self, msg_dict):
        """Convert JSON dictionary back to LangChain message object."""
        if msg_dict["type"] == "human":
            return HumanMessage(content=msg_dict["content"])
        elif msg_dict["type"] == "ai":
            return AIMessage(content=msg_dict["content"])
        return BaseMessage(content=msg_dict["content"])


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Answer all questions to the best of your ability."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{content}"),
    ]
)


model = ChatOpenAI(model="gpt-3.5-turbo")

chain = prompt | model | StrOutputParser()


def get_session_history(session_id):
    return JSONChatMessageHistory(session_id=session_id)


chat_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="content",
    history_messages_key="chat_history",
)


while True:
    content = input(">> ")
    if content.lower() in ["exit", "quit"]:
        break

    result = chat_with_history.invoke(
        {"content": content},
        {"configurable": {"session_id": "dummy"}},  
    )
    print("AI:", result)
