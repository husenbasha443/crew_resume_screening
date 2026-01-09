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
            config=self.agents_config['job_analyst_agent'], 
            verbose=True
        )

    @agent
    def skill_matching_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['skill_matching_agent'], 
            verbose=True
        )
    @agent
    def interview_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['interview_planner_agent'], 
            verbose=True
        )

    @task
    def job_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['job_analysis_task'], 
        )

    @task
    def skill_matching_task(self) -> Task:
        return Task(
            config=self.tasks_config['skill_matching_task'], 
           
        )
    @task
    def interview_question_task(self) -> Task:
        return Task(
            config=self.tasks_config['interview_question_task'], 
            output_file = "blogs/blog.md"
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewaiResumeScreening crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
            trace=True,
            # process=Process.hierarchical, 
        )
