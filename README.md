# 📚 Bookstore ETL Pipeline

This is a simple ETL (Extract, Transform, Load) project that extracts book data from an external API and loads it into a MongoDB database. The goal is to demonstrate basic data engineering logic using Python and MongoDB.

---

## 📌 Features

- Extracts data from a public REST API
- Transforms and flattens nested JSON using `pandas`
- Loads data into a MongoDB collection
- Uses environment variables for secure credentials

---

## 🛠️ Tech Stack

- Python 🐍  
- MongoDB 🍃  
- Pandas 📊  
- Requests 🌐  
- Dotenv 🔐  

---

## 🚀 How It Works

1. **Extract**: Makes a GET request to a bookstore API.
2. **Transform**: Parses and flattens the JSON response using `pandas`.
3. **Load**: Inserts the cleaned records into a MongoDB collection.

---

## 📂 Project Structure

```bash
.
├── book_store_etl_logic.py
├── .env
├── requirements.txt
└── README.md
```
## ⚙️ Environment Variables
Create a `.env` file in the root directory and add the following:

```
CONNECTION_STRING=your_mongodb_connection_string
DB_NAME=your_database_name
```

## 📦 Installation
# Clone the repo
`git clone https://github.com/kanweitech/etl_bookstore_pipeline/tree/main`

# Create a virtual environment (optional)
`python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate`

# Install dependencies
`pip install -r requirements.txt`
```
