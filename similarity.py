from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("bert-base-nli-mean-tokens")


def question_similarity(q1, q2):
    embeddings = model.encode([q1, q2])
    return cosine_similarity(embeddings)[0][1]


q1 = "Best Book?"
q2 = "Which city is the capital of France?"

similarity_score = question_similarity(q1, q2)

print(f"The similarity score between '{q1}' and '{q2}' is {similarity_score:.2f}")
