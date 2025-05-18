from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

from functions.commands import *

command_embeddings = model.encode(list(commands.keys()))


def find_closest_command(user_input, threshold=0.5):
    input_embedding = model.encode(user_input).reshape(1, -1)
    similarities = cosine_similarity(input_embedding, command_embeddings)
    best_match_index = similarities.argmax()
    confidence = similarities[0][best_match_index]

    if confidence >= threshold:
        return commands[list(commands.keys())[best_match_index]], confidence
    else:
        return None, confidence
