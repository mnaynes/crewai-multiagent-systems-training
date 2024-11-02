#!/usr/bin/env python
import sys
from financial_analysis_collab.crew import FinancialAnalysisCollabCrew

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'stock_selection': 'AAPL',
        'initial_capital': '100000',
        'risk_tolerance': 'Medium',
        'trading_strategy_preference': 'Day Trading',
        'news_impact_consideration': True
    }
    FinancialAnalysisCollabCrew().crew().kickoff(inputs=inputs)


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'stock_selection': 'AAPL',
        'initial_capital': '100000',
        'risk_tolerance': 'Medium',
        'trading_strategy_preference': 'Day Trading',
        'news_impact_consideration': True
    }
    try:
        FinancialAnalysisCollabCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        FinancialAnalysisCollabCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'stock_selection': 'AAPL',
        'initial_capital': '100000',
        'risk_tolerance': 'Medium',
        'trading_strategy_preference': 'Day Trading',
        'news_impact_consideration': True
    }
    try:
        FinancialAnalysisCollabCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
