from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from langchain_openai import ChatOpenAI

# Uncomment the following line to use an example of a custom tool
# from financial_analysis_collab.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

@CrewBase
class FinancialAnalysisCollabCrew():
	"""FinancialAnalysisCollab crew"""

	@agent
	def data_analyst_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['data_analyst_agent'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True
		)

	@agent
	def trading_strategy_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['trading_strategy_agent'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True
		)

	@agent
	def execution_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['execution_agent'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True
		)

	@agent
	def risk_management_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['risk_management_agent'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True
		)

	@task
	def data_analysis_task(self) -> Task:
		return Task(
			config=self.tasks_config['data_analysis_task'],
		)

	@task
	def strategy_development_task(self) -> Task:
		return Task(
			config=self.tasks_config['strategy_development_task'],
		)

	@task
	def execution_planning_task(self) -> Task:
		return Task(
			config=self.tasks_config['execution_planning_task'],
		)

	@task
	def risk_assessment_task(self) -> Task:
		return Task(
			config=self.tasks_config['risk_assessment_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the FinancialAnalysisCollab crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			# process=Process.sequential,
			verbose=True,
			process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
			manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
		)
