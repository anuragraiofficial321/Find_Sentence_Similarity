from sentence_transformers import SentenceTransformer
from sklearn.metrics import pairwise_distances

model = SentenceTransformer("bert-base-nli-mean-tokens")


def question_similarity(q1, q2):
    embeddings = model.encode([q1, q2])
    cosine_similarity = 1 - pairwise_distances(embeddings, metric="cosine")[0][1]
    euclidean_distance = pairwise_distances(embeddings, metric="euclidean")[0][1]
    manhattan_distance = pairwise_distances(embeddings, metric="manhattan")[0][1]
    return cosine_similarity, euclidean_distance, manhattan_distance


q1 = "capital of France?"
q2 = "Which city is the capital of France?"

cosine_similarity, euclidean_distance, manhattan_distance = question_similarity(q1, q2)

print(f"The cosine similarity between '{q1}' and '{q2}' is {cosine_similarity:.2f}")
print(f"The Euclidean distance between '{q1}' and '{q2}' is {euclidean_distance:.2f}")
print(f"The Manhattan distance between '{q1}' and '{q2}' is {manhattan_distance:.2f}")
