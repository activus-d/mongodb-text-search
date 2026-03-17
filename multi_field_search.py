from pymongo import MongoClient

# Replace the placeholder values with your Atlas credentials and cluster hostname:
client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@<HOST>/",
    appname="devrel-tutorial-python-text-search"
)
db = client["bookstore"]
books = db["books"]

# Search title, description, and genre for the term "fiction":
results = books.aggregate([
    {
        "$search": {
            "text": {
                "query": "fiction",
                "path": ["title", "description", "genre"]
            }
        }
    },
    {
        # Return title, genre, and description — suppress _id:
        "$project": {
            "_id": 0,
            "title": 1,
            "genre": 1,
            "description": 1
        }
    }
])

for doc in results:
    print(doc)