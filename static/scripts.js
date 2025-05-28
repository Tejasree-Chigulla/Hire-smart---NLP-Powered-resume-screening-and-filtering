// ✅ Help Page: Show Answer Based on Selected Question
document.addEventListener("DOMContentLoaded", function () {
    const questionDropdown = document.getElementById("questionSelect");
    if (questionDropdown) {
        questionDropdown.addEventListener("change", function () {
            const answers = {
                "ats_tips": "Use job-specific keywords, simple formatting, and standard fonts to increase your ATS score.",
                "best_format": "Use a reverse chronological format, starting with your most recent experience.",
                "length": "Keep your resume 1-2 pages long for best readability.",
                "keywords": "Extract keywords from the job description and include them naturally in your resume.",
                "common_mistakes": "Avoid typos, long paragraphs, and excessive personal details.",
                "skills": "List skills relevant to the job, categorized under technical and soft skills.",
                "experience": "Use bullet points and action verbs to describe your work experience.",
                "education": "Place your education section after experience unless you are a recent graduate.",
                "certifications": "Include relevant certifications to strengthen your qualifications.",
                "projects": "Showcase impactful projects, especially those relevant to the job.",
                "salary_tips": "Highlight skills and achievements that justify a higher salary.",
                "formatting": "Use clear headings, bullet points, and avoid images or tables.",
                "custom_resume": "Customize your resume for each job by emphasizing relevant experience.",
                "bullet_points": "Use bullet points to list responsibilities and achievements concisely.",
                "contact_info": "Include your name, email, phone number, and LinkedIn (optional).",
                "achievements": "Quantify achievements with metrics (e.g., increased sales by 30%).",
                "cover_letter": "A cover letter is recommended but not always required.",
                "grammar": "Proofread your resume carefully to avoid grammar mistakes.",
                "design": "Avoid excessive colors, graphics, or fancy fonts—keep it simple and readable.",
                "best_practices": "Tailor your resume, keep it concise, and optimize for ATS."
            };

            const selectedQuestion = this.value;
            const answerBox = document.getElementById("answerBox");

            if (selectedQuestion) {
                answerBox.innerHTML = `<p>${answers[selectedQuestion]}</p>`;
            } else {
                answerBox.innerHTML = "";
            }
        });
    }
});

// ✅ Smooth Scrolling for Navigation Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener("click", function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute("href"));
        if (target) {
            target.scrollIntoView({ behavior: "smooth" });
        }
    });
});

// ✅ File Upload Validation (Restrict to PDF & DOCX)
document.addEventListener("DOMContentLoaded", function () {
    const fileInput = document.getElementById("resume");
    if (fileInput) {
        fileInput.addEventListener("change", function () {
            const allowedExtensions = ["pdf", "docx"];
            const files = this.files;
            let valid = true;

            for (let file of files) {
                const fileExtension = file.name.split(".").pop().toLowerCase();
                if (!allowedExtensions.includes(fileExtension)) {
                    alert("Only PDF and DOCX files are allowed!");
                    this.value = ""; // Clear invalid file
                    valid = false;
                    break;
                }
            }

            if (valid && files.length > 0) {
                alert("Files uploaded successfully!");
            }
        });
    }
});

// ✅ Dashboard: Show Recent Uploads in Local Storage (Simulated)
document.addEventListener("DOMContentLoaded", function () {
    const dashboardContainer = document.querySelector(".dashboard-container");
    if (dashboardContainer) {
        let uploadedFiles = JSON.parse(localStorage.getItem("recentUploads")) || [];

        const fileList = document.getElementById("recentUploadsList");
        if (fileList) {
            fileList.innerHTML = uploadedFiles.length
                ? uploadedFiles.map(file => `<li>${file}</li>`).join("")
                : "<p>No recent uploads.</p>";
        }
    }
});

// ✅ Home Page: Dim background on "Get Started" click
document.addEventListener("DOMContentLoaded", function () {
    const btn = document.querySelector(".btn-primary");
    const overlay = document.getElementById("dimOverlay");

    if (btn && overlay) {
        btn.addEventListener("click", function (e) {
            e.preventDefault(); // Prevent navigation for visual effect
            overlay.style.display = "block"; // Show the dim background overlay

            // Redirect after 2 seconds
            setTimeout(() => {
                window.location.href = btn.href;
            }, 2000);
        });
    }
});
