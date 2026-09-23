from pathlib import Path
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")

file_data = []

def similarity(a,b):
    answer =np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))
    return answer

for p in (Path(__file__).parent/"docs").glob("*.txt"):
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

def search(question):
    vquestion = model.encode(question)
    for record in file_data:       
        record.update({"score":similarity(record["vector"],vquestion)})
    top_chunks = sorted(file_data, key=lambda data: data["score"], reverse = True)[:3]
    datalist =[]
    for data in top_chunks:
        datalist.append(f"Score: {data["score"]} Text: {data["text"]} Filename: {data["filename"]}")
    return datalist