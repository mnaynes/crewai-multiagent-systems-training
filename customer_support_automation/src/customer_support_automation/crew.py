from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from customer_support_automation.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import ScrapeWebsiteTool

@CrewBase
class CustomerSupportAutomationCrew():
	"""CustomerSupportAutomation crew"""

	@agent
	def support_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['support_agent'],
			verbose=True
		)

	@agent
	def support_quality_assurance_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['support_quality_assurance_agent'],
			verbose=True
		)

	@task
	def inquiry_resolution(self) -> Task:
		return Task(
			config=self.tasks_config['inquiry_resolution'],
			tools=[ScrapeWebsiteTool(website_url="https://docs.crewai.com/concepts/crews")],
			output_file='report.md'
		)

	@task
	def quality_assurance_review(self) -> Task:
		return Task(
			config=self.tasks_config['quality_assurance_review'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CustomerSupportAutomation crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			memory=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)