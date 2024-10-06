from models import JobPosting, Session

job_postings_data = [
    # ... (Include all the job postings from the mock data provided)
]

session = Session()
for job_data in job_postings_data:
    job = JobPosting(
        job_title=job_data['job_title'],
        company=job_data['company'],
        required_skills=job_data['required_skills'],
        location=job_data['location'],
        job_type=job_data['job_type'],
        experience_level=job_data['experience_level']
    )
    session.add(job)
session.commit()
session.close()
