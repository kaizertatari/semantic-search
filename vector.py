
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = model.encode(["car", "carpet", "automobile"])


def output():
    print (len(vectors[0]))


output()