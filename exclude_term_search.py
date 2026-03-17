from pymongo import MongoClient

# Replace the placeholder values with your Atlas credentials and cluster hostname:
client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@<HOST>/",
    appname="devrel-tutorial-python-text-search"
)
db = client["bookstore"]
books = db["books"]

results = books.aggregate([
    {
        "$search": {
            "compound": {
                # Must: the description field must contain "woman":
                "must": [
                    {
                        "text": {
                            "query": "woman",
                            "path": "description"
                        }
                    }
                ],
                # MustNot: exclude any book whose description contains "death":
                "mustNot": [
                    {
                        "text": {
                            "query": "death",
                            "path": "description"
                        }
                    }
                ]
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