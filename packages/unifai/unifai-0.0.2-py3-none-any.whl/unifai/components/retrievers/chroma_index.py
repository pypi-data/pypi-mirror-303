from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Literal, Self
from itertools import zip_longest

if TYPE_CHECKING:
    from chromadb.api.models.Collection import Collection as ChromaCollection

from ...types import Embedding, EmbeddingProvider, VectorDBGetResult, VectorDBQueryResult
from .._base_component import convert_exceptions
from ..base_adapters.chroma_base import ChromaExceptionConverter
from ._base_vector_db_index import VectorDBIndex


class ChromaIndex(ChromaExceptionConverter, VectorDBIndex):
    provider = "chroma"
    wrapped: ChromaCollection
    
    @convert_exceptions
    def count(self, **kwargs) -> int:
        return self.wrapped.count()
    
    @convert_exceptions
    def modify(self, 
               new_name: Optional[str]=None, 
               new_metadata: Optional[dict]=None,
               embedding_provider: Optional[EmbeddingProvider] = None,
               embedding_model: Optional[str] = None,
               dimensions: Optional[int] = None,
               distance_metric: Optional[Literal["cosine", "euclidean", "dotproduct"]] = None,               
               metadata_update_mode: Optional[Literal["replace", "merge"]] = "replace",
               **kwargs
               ) -> Self:
        
        if new_name is not None:
            self.name = new_name
        if new_metadata is not None:
            if metadata_update_mode == "replace":
                self.metadata = new_metadata
            else:
                self.metadata.update(new_metadata)
                
        self.wrapped.modify(name=self.name, metadata=self.metadata, **kwargs)
        return self

            
    @convert_exceptions
    def add(self,
            ids: list[str],
            metadatas: Optional[list[dict]] = None,
            documents: Optional[list[str]] = None,
            embeddings: Optional[list[Embedding]] = None,
            **kwargs
            ) -> Self:
        
        self.wrapped.add(
            ids=ids, 
            metadatas=metadatas, 
            documents=documents, 
            embeddings=embeddings,
            **kwargs
        )
        return self

    @convert_exceptions
    def update(self,
                ids: list[str],
                metadatas: Optional[list[dict]] = None,
                documents: Optional[list[str]] = None,
                embeddings: Optional[list[Embedding]] = None,
                **kwargs
                ) -> Self:
          
        self.wrapped.update(
            ids=ids, 
            metadatas=metadatas, 
            documents=documents, 
            embeddings=embeddings,
            **kwargs
        )
        return self
    
    @convert_exceptions
    def upsert(self,
                ids: list[str],
                metadatas: Optional[list[dict]] = None,
                documents: Optional[list[str]] = None,
                embeddings: Optional[list[Embedding]] = None,
                **kwargs
                ) -> Self:
        
        self.wrapped.upsert(
            ids=ids, 
            metadatas=metadatas, 
            documents=documents, 
            embeddings=embeddings,
            **kwargs
        )
        return self
    
    @convert_exceptions
    def delete(self, 
               ids: list[str],
               where: Optional[dict] = None,
               where_document: Optional[dict] = None,
               **kwargs
               ) -> None:
        return self.wrapped.delete(ids=ids, where=where, where_document=where_document, **kwargs)


    @convert_exceptions
    def get(self,
            ids: Optional[list[str]] = None,
            where: Optional[dict] = None,
            limit: Optional[int] = None,
            offset: Optional[int] = None,
            where_document: Optional[dict] = None,
            include: list[Literal["embeddings", "metadatas", "documents"]] = ["metadatas", "documents"],
            **kwargs
            ) -> VectorDBGetResult:
        
        get_result = self.wrapped.get(
            ids=ids, 
            where=where, 
            limit=limit, 
            offset=offset, 
            where_document=where_document, 
            include=include,
            **kwargs
        )
        return VectorDBGetResult(
            ids=get_result["ids"],
            metadatas=get_result["metadatas"],
            documents=get_result["documents"],
            embeddings=get_result["embeddings"],
            included=["ids", *get_result["included"]] 
        )
    

    def query(self,              
              query_text: Optional[str] = None,
              query_embedding: Optional[Embedding] = None,
              n_results: int = 10,
              where: Optional[dict] = None,
              where_document: Optional[dict] = None,
              include: list[Literal["metadatas", "documents", "embeddings", "distances"]] = ["metadatas", "documents", "distances"],
              **kwargs
              ) -> VectorDBQueryResult:
        if query_text is not None:
            query_texts = [query_text]
            query_embeddings = None
        elif query_embedding is not None:
            query_texts = None
            query_embeddings = [query_embedding]
        else:
            raise ValueError("Either query_text or query_embedding must be provided")
        return self.query_many(query_texts, query_embeddings, n_results, where, where_document, include, **kwargs)[0]

    
    @convert_exceptions
    def query_many(self,
              query_texts: Optional[list[str]] = None,
              query_embeddings: Optional[list[Embedding]] = None,              
              n_results: int = 10,
              where: Optional[dict] = None,
              where_document: Optional[dict] = None,
              include: list[Literal["metadatas", "documents", "embeddings", "distances"]] = ["metadatas", "documents", "distances"],
              **kwargs
              ) -> list[VectorDBQueryResult]:
        
        if query_texts is None and query_embeddings is None:
            raise ValueError("Either query_texts or query_embeddings must be provided")

        query_result = self.wrapped.query(
            query_embeddings=query_embeddings, 
            query_texts=query_texts, 
            n_results=n_results, 
            where=where, 
            where_document=where_document, 
            include=include,
            **kwargs
        )

        included = query_result["included"]
        empty_tuple = ()
        return [
            VectorDBQueryResult(
                ids=ids,
                metadatas=metadatas,
                documents=documents,
                embeddings=embeddings,
                distances=distances,
                included=["ids", *included]
            ) for ids, metadatas, documents, embeddings, distances in zip_longest(
                query_result["ids"],
                query_result["metadatas"] or empty_tuple,
                query_result["documents"] or empty_tuple,
                query_result["embeddings"] or empty_tuple,
                query_result["distances"] or empty_tuple,
                fillvalue=None
            )
        ]    
    


    def list_ids(self, **kwargs) -> list[str]:
        return self.get(include=[], **kwargs).ids


    def delete_all(self, **kwargs) -> None:
        self.delete(ids=self.list_ids(), **kwargs)    