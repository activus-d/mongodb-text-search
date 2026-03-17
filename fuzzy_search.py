from pymongo import MongoClient

# Replace the placeholder values with your Atlas credentials and cluster hostname:
client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@<HOST>/",
    appname="devrel-tutorial-python-text-search"
)
db = client["bookstore"]
books = db["books"]

# Search for terms similar to "librery" — allow up to one character edit:
results = books.aggregate([
    {
        "$search": {
            "text": {
                "query": "librery",
                "path": "description",
                "fuzzy": {
                    # maxEdits controls how many character changes MongoDB tolerates:
                    "maxEdits": 1
                }
            }
        }
    },
    {
        # Return title and description — suppress _id:
        "$project": {
            "_id": 0,
            "title": 1,
            "description": 1
        }
    }
])

for doc in results:
    print(doc)