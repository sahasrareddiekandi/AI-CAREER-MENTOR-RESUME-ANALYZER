def get_courses(career):

    courses = {

        "AI Engineer": [
            "Python for AI",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch"
        ],

        "Data Analyst": [
            "Excel",
            "SQL",
            "Power BI",
            "Tableau",
            "Data Analytics"
        ],

        "Web Developer": [
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js"
        ],

        "Java Developer": [
            "Core Java",
            "OOP",
            "Spring Boot",
            "Hibernate",
            "MySQL"
        ]
    }

    return courses.get(career, [])