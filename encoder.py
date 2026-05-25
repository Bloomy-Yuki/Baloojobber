import torch
from sentence_transformers import CrossEncoder

model = CrossEncoder("BAAI/bge-reranker-v2-m3")

def Encode(cv, jd):
    torch.mps.empty_cache()
    score = model.predict([jd,cv])
    return int(round(float(score),2)*100)

