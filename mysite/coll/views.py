from django.shortcuts import render
from pymongo import MongoClient

client = MongoClient()

# Create your views here.
def index(request): 
    #results = settings.vali_collection.find({'index': []  })
    results = {"name": "Travel & Leisure", "i": 
        [{"name": "name1", "sector": "sector1"}, 
        {"name": "name2", "sector": "sector2"}, 
        {"name": "name3", "sector": "sector3"}]} 
    #json_docs = [json.dumps(doc, default=json_util.default) for doc in results]
    return render(request, 'coll/db.html', {'results': results})
