from resume_processing import extract_text_from_pdf, extract_text_from_docx, extract_skills, calculate_ats_score, predict_category, extract_experience, rate_resume_format, predict_salary

def process_resume(file_path, job_description):
    if file_path.endswith(".pdf"):
        resume_text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        resume_text = extract_text_from_docx(file_path)
    else:
        return None

    skills = extract_skills(resume_text)
    ats_score, matched_keywords = calculate_ats_score(resume_text, job_description)
    job_category = predict_category(resume_text)
    experience = extract_experience(resume_text)
    format_score = rate_resume_format(resume_text)
    salary = predict_salary(experience, skills)

    return {
        "filename": file_path.split("/")[-1],
        "ats_score": ats_score,
        "skills": skills,
        "experience": experience,
        "job_category": job_category,
        "salary_prediction": salary,
        "resume_relevance": format_score
    }
