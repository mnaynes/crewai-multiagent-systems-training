from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
from event_planning.tools.custom_tool import VenueDetails

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

@CrewBase
class EventPlanningCrew():
	"""EventPlanning crew"""

	@agent
	def venue_coordinator(self) -> Agent:
		return Agent(
			config=self.agents_config['venue_coordinator'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True
		)

	@agent
	def logistics_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['logistics_manager'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True
		)
	
	@agent
	def marketing_communications_agent(self) -> Agent:
		return Agent(
			config=self.agents_config['marketing_communications_agent'],
			tools=[SerperDevTool(), ScrapeWebsiteTool()],
			verbose=True
		)

	@task
	def venue_task(self) -> Task:
		return Task(
			config=self.tasks_config['venue_task'],
			output_json=VenueDetails,
		)

	@task
	def logistics_task(self) -> Task:
		return Task(
			config=self.tasks_config['logistics_task'],
		)

	@task
	def marketing_task(self) -> Task:
		return Task(
			config=self.tasks_config['marketing_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the EventPlanning crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)