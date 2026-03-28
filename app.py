from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
# Enable CORS so our frontend index.html can communicate with this backend
CORS(app)

# In-memory storage for interview submissions
interview_submissions = []

job_listings = [
    { "id": 1, "title": "Frontend Developer", "description": "Build modern UI with React & Vue" },
    { "id": 2, "title": "Backend Developer", "description": "Build robust APIs with Python & Node.js" },
    { "id": 3, "title": "UI/UX Designer", "description": "Create accessible and stunning user experiences" },
    { "id": 4, "title": "Product Manager", "description": "Lead product vision from ideation to launch" },
    { "id": 5, "title": "Data Scientist", "description": "Analyze large datasets and train machine learning models" },
    { "id": 6, "title": "DevOps Engineer", "description": "Manage cloud infrastructure and CI/CD pipelines" },
    { "id": 7, "title": "Full Stack Engineer", "description": "Develop end-to-end features on web and mobile" },
    { "id": 8, "title": "HR Manager", "description": "Drive talent acquisition and company culture" },
    { "id": 9, "title": "Marketing Specialist", "description": "Grow user engagement through targeted campaigns" },
    { "id": 10, "title": "QA Tester", "description": "Ensure high-quality software through automated testing" }
]

@app.route('/api/status', methods=['GET'])
def get_status():
    return jsonify({"message": "Python Backend is running!", "status": "success"})

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    return jsonify(job_listings)

@app.route('/api/interview/submit', methods=['POST'])
def submit_interview():
    data = request.json
    role = data.get('role', 'Unknown')
    githubUrl = data.get('githubUrl', '')
    answer = data.get('answer', '')
    codingAnswer = data.get('codingAnswer', '')
    testScore = data.get('testScore', 'Not Run')
    grade = data.get('grade', 'Pending')

    if not answer or not githubUrl or not codingAnswer:
        return jsonify({"error": "Missing GitHub URL, Experience Answer, or Coding Test Answer"}), 400

    submission = {
        "id": int(datetime.now().timestamp() * 1000),
        "role": role,
        "githubUrl": githubUrl,
        "answer": answer,
        "codingAnswer": codingAnswer,
        "testScore": testScore,
        "grade": grade,
        "submittedAt": datetime.now().isoformat()
    }

    interview_submissions.append(submission)
    print(f"New submission received: {submission}")

    return jsonify({
        "success": True,
        "message": "Interview submitted successfully!",
        "data": submission
    }), 201

@app.route('/api/interview/submissions', methods=['GET'])
def get_submissions():
    return jsonify(interview_submissions)

if __name__ == '__main__':
    print("Starting Python backend on http://localhost:5000")
    app.run(port=5000, debug=True)
