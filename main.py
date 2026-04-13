from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

def main():
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    template = PromptTemplate(
        input_variables=["topic"],
        template="Explain {topic} in simple terms"
    )

    chain = LLMChain(llm=llm, prompt=template)

    result = chain.run("LangChain")
    print("Output:\n", result)

if __name__ == "__main__":
    main()
