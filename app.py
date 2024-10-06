from flask import Flask, request, jsonify
from models import User, JobPosting, Session
from recommendation import calculate_relevance_score

app = Flask(__name__)

@app.route('/user-profile', methods=['POST'])
def add_user_profile():
    data = request.get_json()
    session = Session()

    user = User(
        name=data['name'],
        skills=data['skills'],
        experience_level=data['experience_level'],
        preferences=data['preferences']
    )
    session.add(user)
    session.commit()
    session.close()
    return jsonify({'message': 'User profile added successfully'}), 201

@app.route('/recommendations/<int:user_id>', methods=['GET'])
def get_recommendations(user_id):
    session = Session()
    user = session.query(User).filter(User.id == user_id).first()
    jobs = session.query(JobPosting).all()

    recommendations = []
    for job in jobs:
        score = calculate_relevance_score(user, job)
        if score > 0:
            recommendations.append({
                'job_title': job.job_title,
                'company': job.company,
                'location': job.location,
                'job_type': job.job_type,
                'required_skills': job.required_skills,
                'experience_level': job.experience_level,
                'score': score
            })

    # Sort recommendations by score
    recommendations.sort(key=lambda x: x['score'], reverse=True)
    session.close()
    return jsonify(recommendations), 200

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'message': str(error)}), 400

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'message': 'Resource not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal Server Error', 'message': 'An unexpected error occurred'}), 500


if __name__ == '__main__':
    app.run(debug=True)
