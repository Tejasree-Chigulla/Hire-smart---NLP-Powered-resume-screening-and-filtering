# HireSmart - NLP Powered Resume Screening and Filtering

HireSmart is an AI-powered web application that uses Natural Language Processing (NLP) to screen, parse, and rank resumes for recruitment purposes. It helps streamline hiring by automating resume analysis, skills extraction, and ATS scoring.

## 🚀 Features

- Resume upload and parsing
- Skill extraction and matching
- ATS (Applicant Tracking System) score calculation
- Salary prediction
- Resume formatting suggestions
- Candidate dashboard and job category classification

## 🖥️ Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite
- **Libraries**: Flask, Pandas, Scikit-learn, NLTK, spaCy, PyPDF2, etc.

## 📁 Project Structure

```bash
├── app.py                  # Main Flask app
├── config.py               # Configuration settings
├── routes.py               # Flask routes
├── processing.py           # Resume parsing and processing logic
├── resume_processing.py    # NLP-based resume utilities
├── static/                 # Static files (CSS, JS, images)
├── templates/              # HTML templates
├── uploads/                # Uploaded resumes (excluded from Git)
├── database.db             # SQLite DB (excluded from Git)
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files/folders
