#
# 1.	基本的Flask應用:
#

from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobsite.db'
db = SQLAlchemy(app)

# 模型定義
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

# 路由
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/explore_job_meaning')
def explore_job_meaning():
    return render_template('job_meaning.html')

@app.route('/resume_management')
def resume_management():
    return render_template('resume.html')

# 運行應用
if __name__ == '__main__':
    app.run(debug=True)
#
# 2.	簡單的職位匹配演算法：
#

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_job(resume, job_descriptions):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume] + job_descriptions)
    similarities = cosine_similarity(vectors[0:1], vectors[1:])
    return similarities[0]
#
# 3.	基本的資料加密：
#

from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    return generate_password_hash(password)

def verify_password(hashed_password, password):
    return check_password_hash(hashed_password, password)
#
# 4.	簡單的API介面示例：
#

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{'id': job.id, 'title': job.title} for job in jobs])

@app.route('/api/apply', methods=['POST'])
def apply_job():
    data = request.json
    # 處理申請邏輯
    return jsonify({'status': 'success'})
