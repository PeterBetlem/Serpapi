from serpapi import GoogleSearch
import os
import json
from pathlib import Path


def search_scholar():
    params = {
    "api_key": os.environ.get("serpapi_token"),
    "engine": "google_scholar_author",
    "hl": "en",
    "author_id": "vdV4YxIAAAAJ"
    }
  
    search = GoogleSearch(params)
    results = search.get_dict()
    print(results)
    table = dict((key,d[key]) for d in results["cited_by"]["table"] for key in d)
    graph = dict((year,d['citations']) for d in results["cited_by"]["graph"] for key,year in d.items() if not key == "citations")


    #Path("output").mkdir()
    with open('GScholartable.json', 'w') as f:
        json.dump(table, f, indent=2)
    with open('GScholargraph.json', 'w') as f:
        json.dump(graph, f, indent=2)


if __name__ == "__main__":
    search_scholar()
