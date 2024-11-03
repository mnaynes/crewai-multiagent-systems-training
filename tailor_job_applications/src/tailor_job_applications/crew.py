from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from tailor_job_applications.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, FileReadTool, PDFSearchTool, ScrapeWebsiteTool

file = 'C:/Users/Michael Naynes/Documents/Programming/Python/tailor_job_applications/src/tailor_job_applications/cv_naynes.pdf'
read_resume = FileReadTool(file_path=file)
semantic_search_resume = PDFSearchTool(file_path=file)
scrape_website = ScrapeWebsiteTool()
search_engine = SerperDevTool()

@CrewBase
class TailorJobApplicationsCrew():
	"""TailorJobApplications crew"""

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			tools=[search_engine, scrape_website],
			verbose=True
		)

	@agent
	def profiler(self) -> Agent:
		return Agent(
			config=self.agents_config['profiler'],
			tools=[search_engine, read_resume, semantic_search_resume, scrape_website],
			verbose=True
		)

	@agent
	def resume_strategist(self) -> Agent:
		return Agent(
			config=self.agents_config['resume_strategist'],
			tools=[search_engine, read_resume, semantic_search_resume, scrape_website],
			verbose=True
		)

	@agent
	def interview_preparer(self) -> Agent:
		return Agent(
			config=self.agents_config['interview_preparer'],
			tools=[search_engine, read_resume, semantic_search_resume, scrape_website],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def profile_task(self) -> Task:
		return Task(
			config=self.tasks_config['profile_task'],
		)

	@task
	def resume_strategy_task(self) -> Task:
		return Task(
			config=self.tasks_config['resume_strategy_task'],
		)

	@task
	def interview_preparation_task(self) -> Task:
		return Task(
			config=self.tasks_config['interview_preparation_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TailorJobApplications crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)