from datetime import datetime

from crewai_resume_screening.crew import CrewaiResumeScreening


def run():
    """
    Run the Smart Job Application Analyzer crew.
    """

    # 🔹 Inputs expected by tasks (matches YAML + problem statement)
    inputs = {
        "job_description": "Backend Developer with Python, Django, REST APIs, and SQL. "
                           "Responsible for building scalable backend services, "
                           "integrating databases, and writing clean APIs. "
                           "2+ years of experience preferred.",

        "candidate_skills": "Python, Flask, SQL, Basic Docker",

        "current_year": str(datetime.now().year)
    }

    try:
        # 🔹 Create crew instance and start execution
        CrewaiResumeScreening().crew().kickoff(inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


if __name__ == "__main__":
    run()
