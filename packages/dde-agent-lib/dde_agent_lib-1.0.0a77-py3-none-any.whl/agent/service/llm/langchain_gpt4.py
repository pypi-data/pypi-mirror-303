import os
from io import StringIO

from langchain.schema import (
    HumanMessage,
    SystemMessage,
    AIMessage
)

from langchain_openai import ChatOpenAI

from agent.init_env_val import OPENAI_API_KEY


class LangchainGpt4:

    def __init__(self, endpoint, *, streaming=True, model="qwen2-72b-tianwen", history=None, retrieve_doc_context: str, temperature=0.7, top_p=0.8, system_prompt = "AstroOne is an open-source, non-profit astronomy research project with the goal of providing astronomers with innovative capabilities and tools enhanced by AI. "):
        os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
        os.environ["OPENAI_BASE_URL"] = endpoint.strip()
        llm = ChatOpenAI(temperature=temperature, top_p=top_p,streaming=streaming)
        llm.model_name = model
        self.llm = llm
        self.input = ""
        if (retrieve_doc_context is None) or (retrieve_doc_context==""):
            self.input = "Please answer the professional question: {} in the field of astronomy. "
        else:
            self.input = "Please answer the professional question: {} in the field of astronomy based on following reference: " + retrieve_doc_context + ". \n If the reference is not relevant to the question, answer according to your own expertise. "
        messages = []
        system = SystemMessage(content=system_prompt)
        messages.append(system)
        if history is None:
            history = []
        for item in history:
            if item[1] is not None:
                hum_msg = HumanMessage(item[0])
                ass_msg = AIMessage(item[1])
                messages.append(hum_msg)
                messages.append(ass_msg)
        self.messages = messages

    is_ok: bool = False

    def invoke(self, prompt: str):
        self.deal_prompt(prompt)
        return self.llm.invoke(self.messages)

    async def astream(self, prompt: str):
        self.deal_prompt(prompt)
        with StringIO() as str_io:
            async for msg in self.llm.astream(self.messages):
                msg = msg.content
                str_io.write(msg)
                # if self.is_target(msg):
                yield str_io.getvalue()

    def is_target(self, msg: str) -> bool:
        target = [".", "!", "?", "。", "！", "？"]
        return msg in target

    def deal_prompt(self, prompt):
        hum_msg = HumanMessage(self.input.format(prompt))
        ass_msg = AIMessage("")
        self.messages.append(hum_msg)
        self.messages.append(ass_msg)
