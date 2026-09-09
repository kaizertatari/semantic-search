from pathlib import Path
from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

model = SentenceTransformer("all-MiniLM-L6-v2")

file_data = []

def similarity(a,b):
    answer =np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return answer

for p in Path("docs").glob("*.txt"):
    content = p.read_text(encoding = "utf-8")
    file = p.name

    for para in content.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        file_data.append({"text":para,"filename":file})

chunks = [item["text"]for item in file_data]

vectors = model.encode(chunks)
for item, value in zip(file_data, vectors):
    item.update({"vector":value})

query = "how do you find a bug"
vquery = model.encode(query)

for record in file_data:
    record.update({"score":similarity(record["vector"],vquery)})

file_data = sorted(file_data, key=lambda data: data["score"], reverse = True)

for data in file_data[:3]:
    print(f"Score: {data["score"]} Text: {data["text"]} Filename: {data["filename"]}")

"""
print(file_data[0].keys())
print(file_data[0].get("vector").shape)
print(file_data[0].get("score"))
print(np.array_equal(file_data[0]["vector"], file_data[5]["vector"]))
"""