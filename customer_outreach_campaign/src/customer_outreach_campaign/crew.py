from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from customer_outreach_campaign.tools.custom_tool import SentimentAnalysisTool

# Check our tools documentations for more information on how to use them
from crewai_tools import DirectoryReadTool, FileReadTool, SerperDevTool

@CrewBase
class CustomerOutreachCampaignCrew():
	"""CustomerOutreachCampaign crew"""

	@agent
	def sales_rep_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['sales_rep_agent'],
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True
		)

	@agent
	def lead_sales_rep_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['lead_sales_rep_agent'],
			verbose=True
		)

	@task
	def lead_profiling_task(self) -> Task:
		return Task(
			config=self.tasks_config['lead_profiling_task'],
			tools=[DirectoryReadTool(directory='./instructions'),FileReadTool(),SerperDevTool()]
		)

	@task
	def personalized_outreach_task(self) -> Task:
		return Task(
			config=self.tasks_config['personalized_outreach_task'],
			tools=[SentimentAnalysisTool(),SerperDevTool()],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CustomerOutreachCampaign crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			memory=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)