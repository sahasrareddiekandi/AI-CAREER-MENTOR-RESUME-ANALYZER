import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from skill_detector import detect_skills
from resume_score import calculate_score
from career_predictor import predict_career
from pdf_reader import extract_text
from interview_questions import get_questions
from course_recommender import get_courses
from certifications import get_certifications

st.set_page_config(
    page_title="AI Career Mentor Pro",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Mentor Pro")
st.caption("Intelligent Resume Analysis and Career Guidance System")

st.markdown("""
### Welcome to AI Career Mentor Pro

✅ Analyze Resumes

✅ Detect Skills

✅ Predict Careers

✅ Find Missing Skills

✅ Generate Learning Roadmaps

✅ Visualize Career Readiness
""")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Resume Upload",
        "Skill Detection"
    ]
)

# ==========================
# DASHBOARD
# ==========================

if page == "Dashboard":

    st.header("📊 AI Career Mentor Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Career Roles",
            "25+"
        )

    with col2:
        st.metric(
            "Skills Database",
            "150+"
        )

    with col3:
        st.metric(
            "Interview Questions",
            "200+"
        )

    with col4:
        st.metric(
            "Learning Resources",
            "100+"
        )

    st.divider()

    st.subheader("🚀 Platform Features")

    features = [
        "Resume Analysis",
        "Skill Detection",
        "Career Prediction",
        "Interview Preparation",
        "Learning Roadmap",
        "Course Recommendation",
        "Certification Recommendation",
        "Skill Analytics"
    ]

    for feature in features:
        st.success(feature)

    st.divider()

    st.subheader("📈 Career Domains Supported")

    domains = [
        "Artificial Intelligence",
        "Data Analytics",
        "Web Development",
        "Java Development",
        "Software Engineering"
    ]

    for domain in domains:
        st.info(domain)

    st.divider()

    st.subheader("🎯 Project Objective")

    st.write(
        """
        AI Career Mentor Pro helps students analyze resumes,
        identify skills, discover career opportunities,
        improve employability, and prepare for placements.
        """
    )
    
    st.subheader("📊 Career Opportunities Overview")

    career_data = pd.DataFrame({
        "Career": [
            "AI",
            "Data",
            "Web",
            "Java"
        ],
        "Demand": [
            95,
            85,
            80,
            75
        ]
    })

    fig, ax = plt.subplots()

    ax.bar(
        career_data["Career"],
        career_data["Demand"]
    )

    ax.set_ylabel("Demand Score")

    ax.set_title(
        "Career Demand Analysis"
    )

    st.pyplot(fig)

    st.success(
        "System Ready For Analysis"
    )

# ==========================
# RESUME UPLOAD
# ==========================

elif page == "Resume Upload":

    st.header("📄 Resume Upload")

    uploaded_file = st.file_uploader(
        "Upload Resume (PDF)",
        type=["pdf"]
    )

    if uploaded_file is not None:

        text = extract_text(uploaded_file)

        st.success("Resume Uploaded Successfully")

        st.subheader("📄 Resume Preview")

        st.text_area(
            "Extracted Resume Text",
            text,
            height=250
        )

        skills = detect_skills(text)

        score = calculate_score(skills)

        career = predict_career(skills)

        st.subheader("🧠 Detected Skills")
        st.write(skills)

        st.subheader("📊 Resume Score")
        st.progress(score / 100)
        st.metric("Score", f"{score}/100")

        st.subheader("🎯 Recommended Career")
        st.success(career)

        if career == "AI Engineer":
            missing_skills = [
                "Deep Learning",
                "TensorFlow",
                "PyTorch"
            ]

        elif career == "Data Analyst":
            missing_skills = [
                "Power BI",
                "Excel",
                "Tableau"
            ]

        elif career == "Web Developer":
            missing_skills = [
                "React",
                "Node.js",
                "MongoDB"
            ]

        else:
            missing_skills = [
                "DSA",
                "Git",
                "Problem Solving"
            ]

        st.subheader("📈 Missing Skills")

        for skill in missing_skills:
            st.warning(skill)

        st.subheader("🛣️ Personalized Learning Roadmap")

        if career == "AI Engineer":

            roadmap = [
                "Learn Python Fundamentals",
                "Learn Data Structures",
                "Study Machine Learning",
                "Learn Deep Learning",
                "Master TensorFlow",
                "Master PyTorch",
                "Build AI Projects",
                "Apply for AI Roles"
            ]

        elif career == "Data Analyst":

            roadmap = [
                "Learn Excel",
                "Learn SQL",
                "Learn Python",
                "Learn Data Cleaning",
                "Learn Power BI",
                "Learn Tableau",
                "Create Dashboards",
                "Apply for Analyst Jobs"
            ]

        elif career == "Web Developer":

            roadmap = [
                "Learn HTML",
                "Learn CSS",
                "Learn JavaScript",
                "Learn React",
                "Learn Backend",
                "Learn MongoDB",
                "Build Projects",
                "Apply for Jobs"
            ]

        else:

            roadmap = [
                "Learn Programming",
                "Practice DSA",
                "Learn GitHub",
                "Build Projects",
                "Practice Aptitude",
                "Prepare Resume",
                "Mock Interviews",
                "Apply for Jobs"
            ]

        for step, item in enumerate(roadmap, start=1):
            st.success(f"Step {step}: {item}")

# ==========================
# SKILL DETECTION
# ==========================

elif page == "Skill Detection":

    st.header("🧠 AI Resume Analyzer")

    resume_text = st.text_area(
        "Paste Resume Text Here"
    )

    if st.button("Analyze Resume"):

        skills = detect_skills(resume_text)

        st.subheader("✅ Detected Skills")
        st.write(skills)

        score = calculate_score(skills)

        st.subheader("📊 Resume Score")
        st.progress(score / 100)
        st.metric("Score", f"{score}/100")

        career = predict_career(skills)

        st.subheader("🎯 Recommended Career")
        st.success(career)

        

        

        st.subheader("🤖 AI Career Recommendations")

        recommendations = {
            "AI Engineer":
                "Focus on Deep Learning, TensorFlow, PyTorch and build at least 3 AI projects.",

            "Data Analyst":
                "Master SQL, Power BI, Excel and Dashboard Development.",

            "Web Developer":
                "Build Full Stack Projects using React, Node.js and MongoDB."
        }

        st.info(
            recommendations.get(
                career,
                "Improve DSA, Git, Communication and Project Development."
            )
        )

        st.subheader("🛣️ Personalized Career Roadmap")

        roadmap = {
            "AI Engineer": [
                "Phase 1: Learn Python Advanced",
                "Phase 2: Study Machine Learning",
                "Phase 3: Learn Deep Learning",
                "Phase 4: Build AI Projects",
                "Phase 5: Deploy AI Models"
            ],

            "Data Analyst": [
                "Phase 1: Learn Excel",
                "Phase 2: Master SQL",
                "Phase 3: Learn Power BI",
                "Phase 4: Create Dashboards",
                "Phase 5: Analyze Real Datasets"
            ],

            "Web Developer": [
                "Phase 1: Learn HTML & CSS",
                "Phase 2: Learn JavaScript",
                "Phase 3: Master React",
                "Phase 4: Learn Backend Development",
                "Phase 5: Build Full Stack Projects"
            ]
        }

        steps = roadmap.get(
            career,
            [
                "Phase 1: Learn DSA",
                "Phase 2: Learn Git & GitHub",
                "Phase 3: Build Projects",
                "Phase 4: Practice Aptitude",
                "Phase 5: Apply for Internships"
            ]
        )

        for step in steps:
            st.success(step)

        st.subheader("🎤 Interview Questions")

        questions = get_questions(career)

        for q in questions:
            st.info(q)

        

    

           


        
  
        st.subheader("📚 Recommended Courses")
        st.write("Predicted Career:", career)
        courses = get_courses(career)

        if courses:
            for course in courses:
                st.success(course)
        else:
            st.warning("No recommended courses available for this career.")

          

        
        
         

        


            

        

        

        # ==========================
# SKILL ANALYTICS
# ==========================

        st.subheader("📊 Skill Analytics")

        skill_scores = []

        for skill in skills:

            if skill.lower() in [
                "python",
                "java",
                "machine learning",
                "sql"
            ]:
                skill_scores.append(90)

            elif skill.lower() in [
                "html",
                "css",
                "javascript"
            ]:
                skill_scores.append(75)

            else:
                skill_scores.append(60)

        df = pd.DataFrame({
            "Skills": skills,
            "Score": skill_scores
        })

        fig, ax = plt.subplots(figsize=(10,5))

        ax.bar(
            df["Skills"],
            df["Score"]
        )

        ax.set_title("Professional Skill Assessment")
        ax.set_xlabel("Skills")
        ax.set_ylabel("Score")

        plt.xticks(rotation=45)

        st.pyplot(fig)

        st.subheader("📥 Download AI Report")

        report = f"""
AI CAREER MENTOR PRO REPORT

Recommended Career:
{career}

Detected Skills:
{skills}

Resume Score:
{score}/100

"""

        st.download_button(
            label="📄 Download Report",
            data=report,
            file_name="AI_Career_Report.txt",
            mime="text/plain"
        )
