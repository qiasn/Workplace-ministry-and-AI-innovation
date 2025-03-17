import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SimpleRAG:
    def __init__(self, documents):
        self.documents = documents
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(documents)
    
    def retrieve(self, query, k=3):
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        top_k_indices = similarities.argsort()[-k:][::-1]
        return [self.documents[i] for i in top_k_indices]
    
    def generate_answer(self, query):
        relevant_docs = self.retrieve(query)
        # 這裡你需要實現一個簡單的答案生成邏輯
        # 提示：你可以使用檢索到的文檔來構建一個簡單的回答
        # 例如，你可以返回最相關文檔的第一句話
        return relevant_docs[0].split('.')[0] + '.'

# 示例使用
documents = [
    "The sky is blue. The sun is bright.",
    "Grass is green. Trees have leaves.",
    "Water is essential for life. Most of Earth is covered in water."
]

rag_system = SimpleRAG(documents)
query = "What color is the sky?"
answer = rag_system.generate_answer(query)
print(f"Query: {query}")
print(f"Answer: {answer}")
