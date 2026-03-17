# MongoDB Text Search — Python Examples

This repository contains the code samples for the "How to Use MongoDB's Text Search" tutorial. It covers six text search operations:

- basic text search
- multi-field search
- fuzzy matching
- excluding a term from results
- combining search conditions with the `compound` operator
- relevance score ranking

The operations are implemented in Python using a MongoDB Atlas free tier cluster.

## Clone the Repository

Run the following command to clone the repository to your machine:

```bash
git clone https://github.com/activus-d/mongodb-text-search.git
```

## Set Up Your Environment

Navigate into the project folder:

```bash
cd mongodb-text-search
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

On Windows, activate the virtual environment with:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
python -m pip install pymongo
```

## Insert the Sample Data and Create the Search Index

Before you run any file, replace the `<USERNAME>`, `<PASSWORD>`, and `<HOST>` placeholders in the connection string with your Atlas credentials and cluster hostname.

Run `insert_data.py` once before running any other file. It inserts the sample book catalog into your cluster and creates the search index:

```bash
python insert_data.py
```

## Run the Files

Before you run any file, replace the `<USERNAME>`, `<PASSWORD>`, and `<HOST>` placeholders in the connection string with your Atlas credentials and cluster hostname.

Each file demonstrates one search operation. Run them individually with the following commands:

```bash
python basic_search.py
```

```bash
python multi_field_search.py
```

```bash
python fuzzy_search.py
```

```bash
python exclude_term_search.py
```

```bash
python compound_search.py
```

```bash
python search_with_scores.py
```

Refer to the tutorial for a full explanation of what each script does and when to use each operation.
