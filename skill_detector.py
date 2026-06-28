def detect_skills(text):

    skills_db = [
        "python",
        "java",
        "html",
        "css",
        "javascript",
        "sql",
        "machine learning",
        "artificial intelligence",
        "data science",
        "react",
        "node.js"
    ]

    found = []

    for skill in skills_db:

        if skill.lower() in text.lower():

            found.append(skill)

    return found