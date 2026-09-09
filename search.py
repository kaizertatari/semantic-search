from pathlib import Path
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


file_data = []

for p in Path("docs").glob("*.txt"):
    content = p.read_text(encoding = "utf-8")
    file = p.name

    for para in content.split("\n\n"):
        para = para.strip()
        if not para:
            continue
        file_data.append({"text":para,"filename":file})

for chunks in file_data:
    print(repr(chunks["text"]))
    print(chunks["filename"])
print(len(file_data))

