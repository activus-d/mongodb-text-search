from pymongo import MongoClient
import time

client = MongoClient(
    "mongodb+srv://<USERNAME>:<PASSWORD>@<HOST>/",
    appname="devrel-tutorial-python-text-search"
)
db = client["bookstore"]
books = db["books"]

# Drop the collection to start clean on each run:
books.drop()

books.insert_many([
    {
        "title": "The Midnight Library",
        "author": "Matt Haig",
        "genre": "fiction",
        "description": "A woman discovers a library between life and death that contains books representing all the lives she could have lived.",
        "year": 2020
    },
    {
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "self-help",
        "description": "A practical guide to building good habits and breaking bad ones through small, incremental changes.",
        "year": 2018
    },
    {
        "title": "Project Hail Mary",
        "author": "Andy Weir",
        "genre": "science fiction",
        "description": "An astronaut wakes up alone in space with no memory and must figure out how to save Earth from an extinction-level threat.",
        "year": 2021
    },
    {
        "title": "Educated",
        "author": "Tara Westover",
        "genre": "memoir",
        "description": "A woman reflects on her isolated rural childhood and her journey to educate herself and earn a PhD from Cambridge.",
        "year": 2018
    },
    {
        "title": "The Hitchhiker's Guide to the Galaxy",
        "author": "Douglas Adams",
        "genre": "science fiction",
        "description": "An ordinary man is swept across the universe after Earth is demolished to make way for a hyperspace expressway.",
        "year": 1979
    }
])

print("Sample data inserted.")

# Drop any existing search index named 'default' before creating a new one:
try:
    books.drop_search_index("default")
    time.sleep(5)
except Exception:
    pass

# Create a search index with dynamic mappings:
books.create_search_index({
    "name": "default",
    "definition": {
        "mappings": {
            "dynamic": True
        }
    }
})

print("Search index created. Waiting for it to go active...")

# Poll until the index is ready:
while True:
    indexes = list(books.list_search_indexes())
    if indexes and indexes[0].get("status") == "READY":
        print("Search index is active. You're ready to run queries.")
        break
    time.sleep(3)