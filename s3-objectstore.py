from mapr.ojai.storage.ConnectionFactory import ConnectionFactory

# Replace these variables with your MapR Object Store details
mapr_url = "mapr-x.x.x:5678"  # Replace with your MapR server URL
volume_name = "/your/volume"   # Replace with your MapR volume path
container_name = "your-container"  # Replace with your MapR container name
file_path = "/path/to/your/file.txt"  # Replace with the path to your local file
document_id = "/path/to/your/document-id"  # Replace with your desired document ID

# Create a connection to the MapR Object Store
connection_str = f"ojai:mapr:{mapr_url}?volume={volume_name}&container={container_name}"
connection = ConnectionFactory.get_connection(connection_str)

# Get a DocumentStore reference
document_store = connection.get_store("/path/to/your/document-store")

# Read the content of the local file
with open(file_path, "rb") as file:
    file_content = file.read()

# Create a Document and set the file content as its value
document = connection.new_document(dictionary={
    "_id": document_id,
    "content": file_content
})

# Insert or update the document in the MapR Object Store
document_store.insert_or_replace(document_id, document)

# Close the connection
connection.close()
