#!/usr/bin/env python
import sys
from send_marketing_emails.crew import SendMarketingEmailsCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    keys = ['life insurance training', 'USA', 'Florida']
    new_keys = []
    for key in keys:
        new_keys.append('https://www.linkedin.com/search/results/content/?keywords=' + key.replace(' ', '%20'))

    inputs = {
        'social_media': 'LinkedIn',
        'keywords': new_keys,
        # 'offer': 'free consultation'
    }
    SendMarketingEmailsCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'social_media': 'LinkedIn',
        'keywords': ['life insurance training', 'USA', 'Florida'],
    }
    try:
        SendMarketingEmailsCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SendMarketingEmailsCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'social_media': 'LinkedIn',
        'keywords': ['life insurance training', 'USA', 'Florida'],
    }
    try:
        SendMarketingEmailsCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
