from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class CrewaiResumeScreening():
    """CrewaiResumeScreening crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    
    ###Define the Config paths
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

   
    @agent
    def job_analyst_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['job_analyst_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def skill_matching_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['skill_matching_agent'], # type: ignore[index]
            verbose=True
        )
    @agent
    def interview_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_planner_agent'], # type: ignore[index]
            verbose=True
        )

    @task
    def job_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_analysis_task'], # type: ignore[index]
        )

    @task
    def skill_matching_task(self) -> Task:
        return Task(
            config=self.tasks_config['skill_matching_task'], # type: ignore[index]
           
        )
    @task
    def interview_question_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_question_task'], # type: ignore[index]
            output_file = "blogs/blog.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiResumeScreening crew"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            trace=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
