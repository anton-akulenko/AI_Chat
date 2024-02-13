import os
from elasticsearch import Elasticsearch
from dotenv import load_dotenv

load_dotenv()
# basic_auth=(os.getenv('ELASTIC_LOGIN'), os.getenv('ELASTIC_PASSWORD'))
#es_api_key=ELASTIC_API_KEY
connection = Elasticsearch(cloud_id=os.getenv('ELASTIC_CLOUD_ID'), api_key=os.getenv('ELASTIC_API_KEY'))#, basic_auth=(os.getenv('ELASTIC_LOGIN'), os.getenv('ELASTIC_PASSWORD')))

print(os.getenv('ELASTIC_CLOUD_ID'))
print(os.getenv('ELASTIC_LOGIN'))
print(os.getenv('ELASTIC_PASSWORD'))
def record_context(id_: str, context: str, connection: Elasticsearch) -> None:
    try:
        print(context)
        print(connection.ping())

        connection.index(index='contexts', id=id_, body={'context': context})
    except Exception as e:
        print(f"Error adding record with id {id_}: {e}")


def get_context(id_: str, connection: Elasticsearch = connection) -> dict:
    # # Initialize Elasticsearch client
    # es = Elasticsearch(["https://llm.es.us-central1.gcp.cloud.es.io"],
    #                    api_key=os.getenv('ELASTIC_API_KEY'))
    #
    # # Get cluster health
    # cluster_health = es.cluster.health()
    #
    # # Print cluster health information
    # print("Cluster Health:")
    # print("Cluster Name:", cluster_health['cluster_name'])
    # print("Status:", cluster_health['status'])
    # print("Number of Nodes:", cluster_health['number_of_nodes'])
    # print("Number of Data Nodes:", cluster_health['number_of_data_nodes'])
    # print("Active Shards:", cluster_health['active_shards'])
    # print("Active Primary Shards:", cluster_health['active_primary_shards'])
    # print("Unassigned Shards:", cluster_health['unassigned_shards'])
    #
    # print(id_, connection)
    # print(connection.ping())
    try:

        result = connection.get(index='contexts', id=id_)

        # print(result['_source'])
        return result['_source']['context']
    except Exception as e:
        return print(e)
    

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