#!/usr/bin/env python3
"""Use pymongo to get deets on nginx logs"""

from pymongo import MongoClient

# Create a MongoClient
client = MongoClient('mongodb://localhost:27017')

# Access the "logs" database
db = client.logs

# Access the "nginx" collection
nginx_collection = db.nginx

# Count the total number of documents
total_logs = nginx_collection.count_documents({})

# Print the total number of documents
print(f"Total logs: {total_logs} logs")

# Define the methods to count
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

# Print the counts for each method
print("Methods:")
for method in methods:
    count = nginx_collection.count_documents({"method": method})
    print(f"\t{method}: {count} logs")

# Count the number of documents with method=GET and path=/status
count_status = nginx_collection.count_documents({"method": "GET", "path": "/status"})

# Print the count for method=GET and path=/status
print(f"{count_status} status check")

# Close the MongoDB connection
client.close()
