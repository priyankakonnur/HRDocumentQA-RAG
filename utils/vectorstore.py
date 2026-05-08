from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
import uuid
#setup collection
def setup_collection(client, collection_name, vector_size):

    client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(
            size=vector_size,
            distance=Distance.COSINE
        )
    )

#store embeddings and chunks in collection
def ingest_chunks(client, collection_name, chunks, embeddings):

    points = []

    for chunk, vector in zip(chunks, embeddings):

        points.append(
            PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={"text": chunk}
            )
        )

    client.upsert(
        collection_name=collection_name,
        points=points
    )

    # (1234,Integrity – We act with honesty and transparency in all professional dealings,0.324)
    # Based on the cosine simalirity the chunks will be picked up
    #768 dimnesions refer to defining your chunks in 768d