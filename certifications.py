def get_certifications(career):

    certifications = {

        "AI Engineer": [
            "Google AI Certification",
            "TensorFlow Developer Certificate",
            "IBM Machine Learning Professional"
        ],

        "Data Analyst": [
            "Microsoft Power BI",
            "Google Data Analytics",
            "Tableau Certification"
        ],

        "Web Developer": [
            "Meta Front-End Developer",
            "JavaScript Certification",
            "React Developer Certification"
        ],

        "Java Developer": [
            "Oracle Java Certification",
            "Spring Boot Certification",
            "Java Professional Certificate"
        ]
    }

    return certifications.get(
        career,
        ["Programming Fundamentals Certification"]
    )