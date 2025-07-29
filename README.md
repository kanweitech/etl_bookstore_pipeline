# 📚 Bookstore ETL Pipeline

![header](https://github.com/kanweitech/etl_bookstore_pipeline/blob/main/static/1753757002567.jpg)

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

![loading_image](https://github.com/kanweitech/etl_bookstore_pipeline/blob/main/static/1753757242939.jpg)

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
`git clone https://github.com/kanweitech/etl_bookstore_pipeline.git`

# Create a virtual environment (optional)
`python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate`

# Install dependencies
`pip install -r requirements.txt`
## ▶️ Usage
```
python book_store_etl_logic.py
```
If successful, you'll see:
```
ETL script executed successfully
```
## 🧪 Sample API Endpoint
This project uses the following API:
`https://full-stack-bookstore-mern-backend.vercel.app/api/books`

## 📄 License
This project is open source and available under the MIT License.

## 👤 Author
Kanwei Edward

GitHub: @kanweitech

## 📚 ETL Bookstore Pipeline

[![Kanwei's GitHub Stats](https://github-readme-stats.vercel.app/api/pin/?username=kanweitech&repo=etl_bookstore_pipeline&theme=default)](https://github.com/kanweitech/etl_bookstore_pipeline)

> 🛠️ A lightweight ETL pipeline that extracts bookstore data from a public API, transforms it using `pandas`, and loads it into MongoDB with support for `.env` secrets.
> 
