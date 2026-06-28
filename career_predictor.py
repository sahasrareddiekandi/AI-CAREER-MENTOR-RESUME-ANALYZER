def predict_career(skills):

    skills = [s.lower() for s in skills]

    if (
        "machine learning" in skills
        or
        "artificial intelligence" in skills
    ):
        return "AI Engineer"

    elif (
        "python" in skills
        and
        "sql" in skills
    ):
        return "Data Analyst"

    elif (
        "html" in skills
        and
        "css" in skills
        and
        "javascript" in skills
    ):
        return "Web Developer"

    elif "java" in skills:
        return "Java Developer"

    return "Software Engineer"