from typing import List, Union

from rank_bm25 import BM25Okapi
import faiss
from mecab import MeCab
import numpy as np
from collections import defaultdict

from utils import embed, rerank, info

class FaissIndexer():
    def __init__(self, ):
        self.tokenizer = MeCab()

    def save_index(self, documents:List[str], path:str):
        pass

    def create_inverted_index_per_document(self, doc, path) -> None:
        inverted_index = defaultdict(list)
        words = self.tokenizer.morphs(doc.lower())
        for word in set(words):
            inverted_index[word].append(path)
        return inverted_index

class FaissRetriever():
    def __init__(self, path:Union[str, List]):
        self.index = self._load_index(path)
        self.tokenizer = Mecab()

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
        # self.
        # return self.
        pass

    def hybridsearch(self, q, ):
        pass

if __name__ == "__main__":
    sample = FaissIndexer()
    print(sample.tokenizer.morphs("나는 여기에서 뭐하고 있는거징"))