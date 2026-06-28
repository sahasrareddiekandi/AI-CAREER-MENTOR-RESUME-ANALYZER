print("skill_gap loaded")

def get_missing_skills(career):

    roadmap = {
        "AI Engineer": ["Deep Learning", "TensorFlow", "PyTorch"],
        "Data Analyst": ["Power BI", "Excel", "Tableau"],
        "Web Developer": ["React", "Node.js", "MongoDB"],
        "Java Developer": ["Spring Boot", "Hibernate", "MySQL"]
    }

    return roadmap.get(career, [])