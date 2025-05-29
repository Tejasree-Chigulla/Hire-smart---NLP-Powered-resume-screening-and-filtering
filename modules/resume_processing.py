import os
import docx2txt
import PyPDF2
import re

# ✅ Predefined Skills Set
SKILL_SET = {"python", "java", "machine learning", "data science", "javascript", "sql", "cloud computing"}

# ✅ Extract text from PDFs
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

# ✅ Extract text from DOCX files
def extract_text_from_docx(docx_path):
    return docx2txt.process(docx_path).strip()

# ✅ Unified Text Extraction Function
def extract_text(file_path):
    ext = file_path.split(".")[-1].lower()
    return extract_text_from_pdf(file_path) if ext == "pdf" else extract_text_from_docx(file_path)

# ✅ Extract Skills
def extract_skills(text):
    words = set(re.findall(r'\b\w+\b', text.lower()))
    return list(SKILL_SET.intersection(words)) if words else ["No relevant skills found"]

# ✅ Extract Experience in Years
def extract_experience(text):
    match = re.search(r'(\d+)\s*(?:years?|yrs?)\s*(?:of)?\s*experience', text, re.IGNORECASE)
    return int(match.group(1)) if match else 0  # Default to 0 if no experience found

# ✅ Calculate ATS Score
def calculate_ats_score(resume_text, job_description):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())

    matched_keywords = resume_words.intersection(job_words)
    score = round(len(matched_keywords) / len(job_words) * 100, 2) if job_words else 0
    return score, list(matched_keywords) if matched_keywords else ["No matching keywords found"]

    
    return render_template("ats_score.html", resumes=resumes)
# ✅ Predict Salary
def predict_salary(experience, skills):
    base_salary = 30000
    skill_bonus = 2000 * len(skills)
    experience_bonus = 5000 * experience
    return base_salary + skill_bonus + experience_bonus

# ✅ Resume Formatting Score
def rate_resume_format(resume_text):
    score = 100
    if resume_text.count("•") > 20: score -= 10
    if "education" not in resume_text.lower(): score -= 15
    if "experience" not in resume_text.lower(): score -= 15
    if len(resume_text) < 500: score -= 20
    return max(0, score)

# ✅ Predict Job Category
def predict_category(resume_text):
    job_categories = {
        "INFORMATION-TECHNOLOGY": ["developer", "programming", "software", "database"],
        "ENGINEERING": ["mechanical", "civil", "electrical", "systems"],
        "FINANCE": ["investment", "banking", "auditing", "wealth management"],
    }
    categories_matched = {}
    for category, keywords in job_categories.items():
        for keyword in keywords:
            if keyword in resume_text.lower():
                categories_matched[category] = categories_matched.get(category, 0) + 1
    return max(categories_matched, key=categories_matched.get) if categories_matched else "OTHER"

# ✅ Extract Education Level
def extract_education(text):
    degrees = ["Bachelor", "Master", "PhD", "Diploma", "Associate", "MBA"]
    for degree in degrees:
        if degree.lower() in text.lower():
            return degree
    return "Not Mentioned"

# ✅ Extract Certifications
def extract_certifications(text):
    certs = ["AWS Certified", "PMP", "CFA", "Cisco Certified", "Google Cloud"]
    matched_certs = [cert for cert in certs if cert.lower() in text.lower()]
    return matched_certs if matched_certs else ["None"]

# ✅ Extract Projects & Achievements
def extract_projects(text):
    projects = re.findall(r"(?:Project|Achievement):\s*(.*)", text, re.IGNORECASE)
    return projects if projects else ["Not Mentioned"]
