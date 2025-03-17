import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# 示例使用者行為資料
user_data = {
    'user_id': [1, 2, 3, 4, 5],
    'course_id': [101, 102, 103, 104, 105],
    'progress': [80, 50, 70, 90, 60]  # 學習進度百分比
}

# 將資料轉換為DataFrame
df = pd.DataFrame(user_data)

# 創建一個推薦系統模型
class RecommenderSystem:
    def __init__(self, data):
        self.data = data
        self.model = NearestNeighbors(n_neighbors=2, metric='cosine')
    
    def fit(self):
        self.model.fit(self.data[['progress']])
    
    def recommend(self, user_id):
        user_index = self.data.index[self.data['user_id'] == user_id].tolist()[0]
        distances, indices = self.model.kneighbors(self.data[['progress']].iloc[user_index].values.reshape(1, -1))
        recommendations = self.data.iloc[indices[0]]['course_id'].tolist()
        recommendations.remove(self.data.iloc[user_index]['course_id'])
        return recommendations

# 產生實體推薦系統並進行推薦
recommender = RecommenderSystem(df)
recommender.fit()
recommended_courses = recommender.recommend(user_id=1)
print("Recommended courses for user 1:", recommended_courses)
