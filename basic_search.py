from pymongo import MongoClient

# Replace the placeholder values with your Atlas credentials and cluster hostname:
client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@<HOST>/",
    appname="devrel-tutorial-python-text-search"
)
db = client["bookstore"]
books = db["books"]

# Search the description field for the term "space":
results = books.aggregate([
    {
        "$search": {
            "text": {
                "query": "space",
                "path": "description"
            }
        }
    },
    {
        # Return title, author, and description — suppress _id:
        "$project": {
            "_id": 0,
            "title": 1,
            "author": 1,
            "description": 1
        }
    }
])

for doc in results:
    print(doc)