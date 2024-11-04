from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from send_marketing_emails.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import WebsiteSearchTool

@CrewBase
class SendMarketingEmailsCrew():
	"""SendMarketingEmails crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[WebsiteSearchTool()],
			verbose=True
		)

	# @agent
	# def email_marketing_specialist(self) -> Agent:
	# 	return Agent(
	# 		config=self.agents_config['email_marketing_specialist'],
	# 		verbose=True
	# 	)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	# @task
	# def email_marketing_task(self) -> Task:
	# 	return Task(
	# 		config=self.tasks_config['email_marketing_task'],
	# 		output_file='report.md'
	# 	)

	@crew
	def crew(self) -> Crew:
		"""Creates the SendMarketingEmails crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)