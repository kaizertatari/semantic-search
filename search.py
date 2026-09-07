from pathlib import Path
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


file_data = []

for p in Path("docs").glob("*.txt"):
    content = p.read_text(encoding = "utf-8")
    file = p.name

    for para in content.split("\n\n"):
        file_data.append({"text":para,"filename":file})

print(file_data[1])
print(len(file_data))
print(len(file_data[1]))

