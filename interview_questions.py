def get_questions(career):

    questions = {

        "AI Engineer": [

            "EASY: What is Artificial Intelligence?",
            "EASY: What is Machine Learning?",
            "EASY: Difference between AI and ML?",

            "MEDIUM: What is Deep Learning?",
            "MEDIUM: Explain Supervised Learning.",
            "MEDIUM: What is TensorFlow?",
            "MEDIUM: What is Overfitting?",

            "HARD: Explain CNN.",
            "HARD: Explain RNN.",
            "HARD: What is Transfer Learning?",
            "HARD: How would you deploy an AI model?"
        ],

        "Data Analyst": [

            "EASY: What is Data Analysis?",
            "EASY: What is SQL?",
            "EASY: What is Excel used for?",

            "MEDIUM: What is Data Cleaning?",
            "MEDIUM: Explain SQL JOIN.",
            "MEDIUM: What is Power BI?",
            "MEDIUM: What is Tableau?",

            "HARD: Explain ETL Process.",
            "HARD: What is Data Warehousing?",
            "HARD: Difference between OLTP and OLAP?",
            "HARD: Explain Dashboard Design Principles."
        ],

        "Web Developer": [

            "EASY: What is HTML?",
            "EASY: What is CSS?",
            "EASY: What is JavaScript?",

            "MEDIUM: What is React?",
            "MEDIUM: What is Bootstrap?",
            "MEDIUM: What is Node.js?",
            "MEDIUM: Explain REST API.",

            "HARD: What is Virtual DOM?",
            "HARD: Explain Authentication vs Authorization.",
            "HARD: Explain JWT.",
            "HARD: How does React Rendering work?"
        ],

        "Java Developer": [

            "EASY: What is Java?",
            "EASY: What is OOP?",
            "EASY: What is JVM?",

            "MEDIUM: Explain Inheritance.",
            "MEDIUM: Explain Polymorphism.",
            "MEDIUM: What is Exception Handling?",
            "MEDIUM: What is Collection Framework?",

            "HARD: Explain Multithreading.",
            "HARD: What is Spring Boot?",
            "HARD: What is Hibernate?",
            "HARD: Difference between HashMap and Hashtable?"
        ]
    }

    return questions.get(
        career,
        [
            "EASY: What is Programming?",
            "MEDIUM: Explain Object Oriented Programming.",
            "HARD: Solve a Data Structures problem."
        ]
    )