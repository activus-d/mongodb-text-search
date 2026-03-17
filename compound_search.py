from pymongo import MongoClient

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
                # Must: the genre field must contain the token "fiction"
                "must": [
                    {
                        "text": {
                            "query": "fiction",
                            "path": "genre"
                        }
                    }
                ],
                # MustNot: exclude any book whose description mentions "astronaut"
                "mustNot": [
                    {
                        "text": {
                            "query": "astronaut",
                            "path": "description"
                        }
                    }
                ],
                # Should: boost books whose description mentions "library"
                "should": [
                    {
                        "text": {
                            "query": "library",
                            "path": "description"
                        }
                    }
                ],
                # Filter: only include books published in 1979 or later (no score impact)
                "filter": [
                    {
                        "range": {
                            "path": "year",
                            "gte": 1979
                        }
                    }
                ]
            }
        }
    },
    {
        "$project": {
            "_id": 0,
            "title": 1,
            "genre": 1,
            "description": 1,
            "year": 1,
        }
    }
])

for doc in results:
    print(doc)