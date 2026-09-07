
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
vectors = model.encode(["car", "carpet", "automobile"])


def similarity(a,b):
    answer =np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return answer

print(f"Car and Carpet: {similarity(vectors[0],vectors[1])}")

print(f"Car and automobile: {similarity(vectors[0],vectors[2])}")

print(f"Carpet and automobile: {similarity(vectors[1],vectors[2])}")

print(np.linalg.norm(vectors[1]))