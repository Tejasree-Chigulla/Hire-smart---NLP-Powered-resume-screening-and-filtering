from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, session
import os
import uuid
from werkzeug.utils import secure_filename
from config import Config
from modules.resume_processing import (
    extract_text, extract_skills, calculate_ats_score, predict_salary,
    predict_category, rate_resume_format, extract_experience,
    extract_education, extract_certifications, extract_projects
)

main = Blueprint("main", __name__)

# ✅ Home Page
@main.route("/")
def home():
    return render_template("index.html")

# ✅ About Page
@main.route("/about")
def about():
    return render_template("about.html")

# ✅ Help Page
@main.route("/help")
def help_page():
    return render_template("help.html")

# ✅ Contact Page
@main.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        flash("Your issue has been submitted. Our team will get back to you.", "success")
    return render_template("contact.html")

# ✅ Resume Upload and Processing
@main.route("/upload", methods=["GET", "POST"])
def upload_resume():
    if request.method == "POST":
        job_description = request.form.get("job_description", "").strip()
        uploaded_files = request.files.getlist("resumes")

        if not uploaded_files or all(f.filename == "" for f in uploaded_files):
            flash("Please upload at least one resume.", "danger")
            return redirect(request.url)

        resumes = []
        for file in uploaded_files:
            if file and Config.allowed_file(file.filename):
                unique_filename = f"{uuid.uuid4().hex}_{secure_filename(file.filename)}"
                file_path = os.path.join(Config.UPLOAD_FOLDER, unique_filename)
                file.save(file_path)

                resume_text = extract_text(file_path)
                skills = extract_skills(resume_text)
                ats_score, matched_keywords = calculate_ats_score(resume_text, job_description)
                experience = extract_experience(resume_text)
                salary = predict_salary(experience, skills)
                job_category = predict_category(resume_text)
                resume_relevance = rate_resume_format(resume_text)
                education = extract_education(resume_text)
                certifications = extract_certifications(resume_text)
                projects = extract_projects(resume_text)

                resumes.append({
                    "filename": file.filename,
                    "ats_score": ats_score,
                    "matched_keywords": matched_keywords,
                    "skills": skills,
                    "experience": experience,
                    "job_category": job_category,
                    "education": education,
                    "certifications": certifications,
                    "projects": projects,
                    "salary_prediction": salary,
                    "resume_relevance": resume_relevance
                })

        resumes = sorted(resumes, key=lambda x: (x["ats_score"], x["experience"], x["salary_prediction"], x["resume_relevance"]), reverse=True)

        session["top_resumes"] = resumes
        session.modified = True  

        return redirect(url_for("main.result"))

    return render_template("upload.html")

# ✅ Result Page (Displays Processed Resumes)
@main.route("/result")
def result():
    resumes = session.get("top_resumes", [])
    if not resumes:
        flash("No resumes processed yet. Please upload a resume first.", "warning")
        return redirect(url_for("main.upload_resume"))
    
    return render_template("result.html", resumes=resumes)

# ✅ Top Resumes Page (NEWLY ADDED)
@main.route("/top_resumes")
def top_resumes():
    resumes = session.get("top_resumes", [])
    if not resumes:
        flash("No resumes processed yet. Please upload a resume first.", "warning")
        return redirect(url_for("main.upload_resume"))

    return render_template("top_resumes.html", resumes=resumes)

# ✅ ATS Score Page
@main.route("/ats_score")
def ats_score():
    resumes = session.get("top_resumes", [])
    return render_template("ats_score.html", resumes=resumes)

# ✅ Dashboard Page
@main.route("/dashboard")
def dashboard():
    resumes = session.get("top_resumes", [])
    return render_template("dashboard.html", resumes=resumes)
