from typing import List, Union

from rank_bm25 import BM25kapi
import faiss
from konlpy.tag import Mecab
import numpy as np

from utils import embed, rerank

class FaissIndexer():
    def __init__(self, ):
        self.tokenizer = Mecab()
        pass

    def save_index(self, documents:List[str], path:str):
        pass

class FaissRetriever():
    def __init__(self, path:Union[str, List]):
        self.index = self._load_index(path)
        self.tokenizer = Mecab()
        pass

    def _load_index(self, path:Union[str, List]):
        shard_index = faiss.IndexShards() ## TODO: add shape
        
        if isinstance(path, List):
            for p in path:
                with open(p, 'rb') as f:
                    bin_data = f.read()
                    index = faiss.deserialize_index_binary(bin_data)
                shard_index.add_shard(p)
        else:
            with open(path, 'rb'):
                index = faiss.deserialize_index_binary(f.read())
            shard_index.add_shard(index)
        
        return shard_index

    def vectorsearch(self, q, ):
        return self.index.search(embed(q))

    def textsearch(self, q, ):
        self.
        return self.

    def hybridsearch(self, q, ):
        pass