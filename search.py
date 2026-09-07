from pathlib import Path
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


file_data = []

for p in Path("docs").glob("*.txt"):
    content = p.read_text(encoding = "utf-8")
    file = p.name
    charcount = len(content)

    file_data.append({"text":content,"filename":file,"length":charcount})

print(file_data[1])

