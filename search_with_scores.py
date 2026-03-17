from pymongo import MongoClient

# Replace the placeholder values with your Atlas credentials and cluster hostname:
client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@<HOST>/",
    appname="devrel-tutorial-python-text-search"
)
db = client["bookstore"]
books = db["books"]

# Search the description field for the term "woman":
results = books.aggregate([
    {
        "$search": {
            "text": {
                "query": "woman",
                "path": "description"
            }
        }
    },
    {
        # Include the relevance score alongside each document:
        "$project": {
            "_id": 0,
            "title": 1,
            "description": 1,
            "score": {"$meta": "searchScore"}
        }
    },
    {
        # Return results from highest to lowest score:
        "$sort": {"score": -1}
    }
])

for doc in results:
    print(doc)