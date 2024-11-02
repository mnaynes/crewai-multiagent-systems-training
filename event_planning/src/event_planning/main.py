#!/usr/bin/env python
import sys
from event_planning.crew import EventPlanningCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'event_topic': "Tech Innovation Conference",
        'event_description': "A gathering of tech innovators and industry leaders to explore future technologies.",
        'event_city': "San Francisco",
        'tentative_date': "2024-12-20",
        'expected_participants': 500,
        'budget': 20000,
        'venue_type': "Conference Hall"
    }
    EventPlanningCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'event_topic': "Tech Innovation Conference",
        'event_description': "A gathering of tech innovators and industry leaders to explore future technologies.",
        'event_city': "San Francisco",
        'tentative_date': "2024-12-20",
        'expected_participants': 500,
        'budget': 20000,
        'venue_type': "Conference Hall"
    }
    try:
        EventPlanningCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        EventPlanningCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'event_topic': "Tech Innovation Conference",
        'event_description': "A gathering of tech innovators and industry leaders to explore future technologies.",
        'event_city': "San Francisco",
        'tentative_date': "2024-12-20",
        'expected_participants': 500,
        'budget': 20000,
        'venue_type': "Conference Hall"
    }
    try:
        EventPlanningCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
