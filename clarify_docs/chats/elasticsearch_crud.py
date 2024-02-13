import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()

connection = Elasticsearch(cloud_id=os.getenv('ELASTIC_CLOUD_ID'), basic_auth=(os.getenv('ELASTIC_LOGIN'), os.getenv('ELASTIC_PASSWORD')))


def record_context(id_: str, context: str, connection: Elasticsearch) -> None:
    try:
        connection.index(index='contexts', id=id_, body={'context': context})
    except Exception as e:
        print(f"Error adding record with id {id_}: {e}")


def get_context(id_: str, connection: Elasticsearch = connection) -> dict:
    try:
        result = connection.get(index='contexts', id=id_)
        return result['_source']['context']
    except Exception as e:
        return None
    

def view_all_documents(connection: Elasticsearch, index_name: str = 'contexts') -> None:
    try:
        result = connection.search(index=index_name, body={"query": {"match_all": {}}})

        for hit in result['hits']['hits']:
            print(f"ID: {hit['_id']}, Context: {hit['_source']['context']}")
    except Exception as e:
        print(f"Error viewing all documents: {e}")
     

def delete_context(id_: str, connection: Elasticsearch) -> None:
    try:
        connection.delete(index='contexts', id=id_)
        print(f"Record with id {id_} deleted successfully.")
    except Exception as e:
        print(f"Error deleting record with id {id_}: {e}")