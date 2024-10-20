from langchain_ollama import ChatOllama
from .ai_searcher import AdvancedAISearcher

from .query_master import SearchRetriever

from langchain_huggy import HuggyLLM
# query  = "explain me Design of ACM , better if we use arxiv paper"
def ai_search(query,verbose: bool|str= False,
              llm = None,
              chunk_overlap=25,
              chunk_size=250,
              max_urls=5,
              n_key_sentences=25,
              topk=10,
              n_web_queries_to_generate = 5
              ):
    rtr = AdvancedAISearcher(
        chunk_overlap=chunk_overlap,
        chunk_size=chunk_size,
        max_urls=max_urls,
        n_key_sentences=n_key_sentences,
        topk=topk
    )
    if isinstance(verbose,str): verbose = verbose.lower() == 'true'
    res = rtr.generate_final_answer(llm, query,verbose=verbose,n_splits=n_web_queries_to_generate)
    return res

def search(query,verbose: bool|str = False,
           llm= None):
    rtr = AdvancedAISearcher()
    if isinstance(verbose,str): verbose = verbose.lower() == 'true'
    res = rtr.search(llm,query,verbose=verbose)
    return res

def fast_search(query,verbose: bool|str = False,
                llm= None):
    rtr = AdvancedAISearcher(chunk_overlap=20,
                             chunk_size=100,
                             max_urls=2,
                             n_key_sentences=10)
    if isinstance(verbose,str): verbose = verbose.lower() == 'true'
    res = rtr.search(llm,query,verbose=verbose)
    return res

def google_search(query,verbose: bool|str = False):
    retriever = SearchRetriever(
        chunk_overlap=20,
        chunk_size=100,
        max_urls=2,
    )
    if isinstance(verbose,str): verbose = verbose.lower() == 'true'
    results = retriever.query_based_content_retrieval(query, topk=5,verbose=verbose)
    return "\n".join(results.topk_chunks)

def deep_google_search(query,verbose: bool|str = False):
    retriever = SearchRetriever()
    if isinstance(verbose,str): verbose = verbose.lower() == 'true'
    results = retriever.query_based_content_retrieval(query, topk=5,verbose=verbose)
    return "\n".join(results.topk_chunks)

