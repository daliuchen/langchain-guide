import uvicorn
from fastapi import FastAPI
from langserve import add_routes

# 创建FastAPi app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)


# 创建chain
def translate_chain():
    # 将上面的代码包装在这里
    import os
    from langchain_openai import ChatOpenAI
    # os.environ["OPENAI_API_KEY"] = "sk-****"
    # os.environ["OPENAI_API_BASE"] = "https://ai-yyds.com/v1"

    model = ChatOpenAI(model="gpt-4")
    from langchain_core.output_parsers import StrOutputParser
    parser = StrOutputParser()
    from langchain_core.prompts import ChatPromptTemplate

    # 定义system message
    system_template = "将下面的文本翻译为{language}:"
    # 创建 ChatPromptTemplate，分为user和system
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{input}")]
    )
    return prompt_template | model | parser


# 绑定chain
add_routes(
    app,
    translate_chain(),
    path="/chain",
)
if __name__ == '__main__':
    # 启动
    uvicorn.run(app, host="localhost", port=8000)