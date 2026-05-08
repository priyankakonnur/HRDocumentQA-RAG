from langchain_text_splitters import RecursiveCharacterTextSplitter
def chunk_text(text):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,              #it uses both recersive and sliding window
        chunk_overlap=100
    )

    return splitter.split_text(text)


#Kubernetes is a container orchestration platform widely used in cloud native applications.
#It helps automate deployment, scaling and management of containers.

#chunk1 = Kubernetes is a container orchestration platform
#chunk2 = orchestration platform widely used in cloud native
#chunk3 = in cloud native applications.It helps automate


#first breakdown with Recursive text splitter and then apply the concept of slidng window

#Kubernetes is a container orchestration platform,

# widely used in cloud native applications.

#It helps automate deployment, scaling and management of containers.

