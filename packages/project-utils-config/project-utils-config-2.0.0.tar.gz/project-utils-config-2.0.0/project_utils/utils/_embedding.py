import torch

from typing import List

from langchain_huggingface import HuggingFaceEmbeddings


class Embeddings:
    __embedding: HuggingFaceEmbeddings

    def __init__(self, model_path: str, is_m1: bool = False):
        device: str
        if is_m1:
            device = "mps"
        else:
            device = "cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu"
        self.__embedding = HuggingFaceEmbeddings(model_name=model_path, model_kwargs={"device": device})

    def embed_text(self, text: str):
        return self.__embedding.embed_query(text)

    def embed_texts(self, texts: List[str]):
        return self.__embedding.embed_documents(texts)

    async def async_embed_text(self, text: str):
        return await self.__embedding.aembed_query(text)

    async def async_embed_texts(self, texts: List[str]):
        return await self.__embedding.aembed_documents(texts)


if __name__ == '__main__':
    embedding: Embeddings = Embeddings(
        "/Users/mylx2014/Project/mylx2014/new-utils/new-utils-config/data/models/bge-large-zh", is_m1=False)
    embedding.embed_query("我是一个小小小小的沙口路光华科技啊收到货国际卡打撒憨八嘎会计啊干哈饭卡搭嘎可代发花洒国际卡干哈户籍卡大厦估计啊都发干哈开发是噶")
