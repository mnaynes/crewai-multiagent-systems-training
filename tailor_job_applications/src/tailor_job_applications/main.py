#!/usr/bin/env python
import sys
from tailor_job_applications.crew import TailorJobApplicationsCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
        'github_url': 'https://github.com/joaomdmoura',
        'personal_writeup': """Noah is an accomplished Software
        Engineering Leader with 18 years of experience, specializing in
        managing remote and in-office teams, and expert in multiple
        programming languages and frameworks. He holds an MBA and a strong
        background in AI and data science. Noah has successfully led
        major tech initiatives and startups, proving his ability to drive
        innovation and growth in the tech industry. Ideal for leadership
        roles that require a strategic and innovative approach."""
    }
    TailorJobApplicationsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
        'github_url': 'https://github.com/joaomdmoura',
        'personal_writeup': """Noah is an accomplished Software
        Engineering Leader with 18 years of experience, specializing in
        managing remote and in-office teams, and expert in multiple
        programming languages and frameworks. He holds an MBA and a strong
        background in AI and data science. Noah has successfully led
        major tech initiatives and startups, proving his ability to drive
        innovation and growth in the tech industry. Ideal for leadership
        roles that require a strategic and innovative approach."""
    }
    try:
        TailorJobApplicationsCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TailorJobApplicationsCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'job_posting_url': 'https://jobs.lever.co/AIFund/6c82e23e-d954-4dd8-a734-c0c2c5ee00f1?lever-origin=applied&lever-source%5B%5D=AI+Fund',
        'github_url': 'https://github.com/joaomdmoura',
        'personal_writeup': """Noah is an accomplished Software
        Engineering Leader with 18 years of experience, specializing in
        managing remote and in-office teams, and expert in multiple
        programming languages and frameworks. He holds an MBA and a strong
        background in AI and data science. Noah has successfully led
        major tech initiatives and startups, proving his ability to drive
        innovation and growth in the tech industry. Ideal for leadership
        roles that require a strategic and innovative approach."""
    }
    try:
        TailorJobApplicationsCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
