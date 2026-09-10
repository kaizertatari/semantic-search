from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
import numpy as np

datalist = ["Good Morning", "How is your afternoon","This is amazing","The fridge is cold","Computer Science is great"]


query = "What is a good compliment"

vectors = model.encode(datalist)
vquery = model.encode(query)

def Similarity(a,b):
    answer = np.dot(a,b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return answer
querylist = []
for data,scores in zip(datalist,vectors):
    querylist.append({"text":data,"score":Similarity(vquery,scores)})

querylist = sorted(querylist, key=lambda item:item["score"],reverse=True)

print(querylist)
print(len(querylist))
print(f"Text: {querylist[0].get("text")} Score: {querylist[0].get("score")}")