def calculate_relevance_score(user, job):
    score = 0
    # Skill matching
    skill_matches = set(user.skills) & set(job.required_skills)
    score += len(skill_matches) * 5  # Assign 5 points per matching skill

    # Experience level match
    if user.experience_level == job.experience_level:
        score += 10

    # Location preference match
    if job.location in user.preferences['locations']:
        score += 5

    # Job type match
    if user.preferences['job_type'] == job.job_type:
        score += 5

    # Desired roles match
    if job.job_title in user.preferences['desired_roles']:
        score += 5

    return score
