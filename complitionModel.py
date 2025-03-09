import argparse
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel,  RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


parser = argparse.ArgumentParser()
parser.add_argument("--task", default="print the first 10 numbers")
parser.add_argument("--language", default="python")  
args = parser.parse_args()  

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


code_prompt = PromptTemplate(
    template="Write a very short {language} function that will {task}.\n",
    input_variables=["language", "task"]
)

test_prompt = PromptTemplate(
    template="Write a test for the following {language} code:\n{code}.",
    input_variables=["language", "code"]
)

code_chain = code_prompt | llm | {"code": StrOutputParser()}

test_chain = test_prompt | llm | {"test": StrOutputParser()}

chain = RunnableParallel({
    "language": RunnablePassthrough(),
    "code": code_chain
}) | (lambda result: {
    "language": result["language"]["language"],  # Extract language correctly
    "code": result["code"]["code"],
    **test_chain.invoke(result)
})

result = chain.invoke({
    "language": args.language,
    "task": args.task
})

print(result)
