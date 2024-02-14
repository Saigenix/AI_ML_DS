from langchain import PromptTemplate, LLMChain
from langchain.llms import GPT4All
from langchain.schema import (
    HumanMessage,AIMessage
)
import gradio as gr


template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate(template=template, input_variables=["question"])
local_path = (
    "D:\Coding\AI_ML_DS\Models\llama-2-7b-chat.ggmlv3.q4_0.bin" 
)

def predict(message, history):
    if history is not None:
        history_langchain_format = []
        for human, ai in history:
            history_langchain_format.append(HumanMessage(content=human))
            history_langchain_format.append(AIMessage(content=ai))
        history_langchain_format.append(HumanMessage(content=message))
        gpt_response = GPT4All(model=local_path,verbose=True)
        res = gpt_response.generate("hi")
        print(res)
        return res


demo = gr.ChatInterface(predict).queue()

if __name__ == "__main__":
    demo.launch()




# Verbose is required to pass to the callback manager
# llm = GPT4All(model="D:\Coding\Open Source\ML\models\llama-2-7b-chat.ggmlv3.q4_0.bin",streaming = True, callbacks=callbacks, verbose=True)

# # If you want to use a custom model add the backend parameter
# # Check https://docs.gpt4all.io/gpt4all_python.html for supported backends
# llm = GPT4All(model=local_path, backend="gptj", callbacks=callbacks, verbose=True)

# llm_chain = LLMChain(prompt=prompt, llm=llm)

# question = "write a big poem about coding"

# llm_chain.run(question)


    
    



