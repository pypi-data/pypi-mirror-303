import sys
import os
import requests
from typing import List, Dict, Any, Optional
from pydantic import BaseModel
import time
import sys
# sys.stdin.reconfigure(encoding='utf-8')
# sys.stdout.reconfigure(encoding='utf-8')

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, root_dir)


QDRANT_SERVER_URL = "http://localhost:8100"
RERANKER_URL = "http://localhost:8010/rerank"

class SearchQuery(BaseModel):
    search_phrase: str = ''
    filter: Optional[Dict[str, Any]] = None
    top_k: int = 20

def get_user_memory(
    search_string: str,
    folders: List[str] = [],
    start_time_unix: int = 0,
    end_time_unix: int = int(time.time()),
    top_k: int = 5,
    image_present: Optional[bool] = None,
    document_present: Optional[bool] = None
) -> List[Dict[str, Any]]:
    search_query = SearchQuery(
        search_phrase=search_string,
        filter={
            "must": [
                {
                    "key": "timestamp_unix",
                    "range": {
                        "gte": start_time_unix,
                        "lte": end_time_unix
                    }
                }
            ]
        },
        top_k=top_k
    )

    # Add image and document filters if specified
    if image_present is not None:
        search_query.filter["must"].append({
            "key": "image_present",
            "match": {"value": image_present}
        })
    
    if document_present is not None:
        search_query.filter["must"].append({
            "key": "document_present",
            "match": {"value": document_present}
        })

            
    result = []
    combined_results_string = ""
    
    for folder in folders:
        try:
            endpoint = f"{QDRANT_SERVER_URL}/search_{folder}"
            response = requests.post(endpoint, json=search_query.dict())
            response.raise_for_status()
            search_result = response.json()
            print(f"{folder.upper()} CONTEXT: ", str(search_result).encode('utf-8'))
            if search_result:
                result.extend(search_result)
                combined_results_string += f"\n[ORIGINAL {folder.upper()} RESULTS]\n"
                combined_results_string += "\n".join([str(item) for item in search_result])
        
        except requests.RequestException as e:
            print(f"Error querying {folder} from Qdrant server: {e}")

    # Rerank the results using Jina reranker
    if result:
        try:
            documents = [item['payload']['content'] for item in result]
            rerank_request = {
                "query": search_string,
                "documents": documents
            }
            rerank_response = requests.post(RERANKER_URL, json=rerank_request)
            rerank_response.raise_for_status()
            scores = rerank_response.json()['scores']
            
            # Combine original results with reranker scores
            reranked_results = []
            for item, score in zip(result, scores[0]):
                reranked_item = item.copy()
                reranked_item['rerank_score'] = score
                reranked_results.append(reranked_item)
            # Sort by rerank score (descending) and take top 5
            reranked_results = sorted(reranked_results, key=lambda x: x['rerank_score'], reverse=True)[:5]
            print(f"RERANKED RESULT: {reranked_results}".encode('utf-8'))
            
            combined_results_string += "\n[RERANKED RESULTS]\n"
            combined_results_string += "\n".join([str(item) for item in reranked_results])
            
            print(f"COMBINED RESULTS:\n{combined_results_string}".encode('utf-8'))
            
        except requests.RequestException as e:
            print(f"Error using Jina reranker: {e}")

    return result, combined_results_string
