import os
import json
from dotenv import load_dotenv
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import TavilySearchTool

# Import custom tools
from .tools import (
    SentimentAnalysisTool,
    ChaosMeterTool,
    MotivationalQuoteTool,
    RoastGeneratorTool,
    StatisticsFinderTool
)

load_dotenv()

@CrewBase
class ChaosOracle7DeadlyPersonasCrew:
    """ChaosOracle7DeadlyPersonas crew"""

    # === AGENTS ===

    @agent
    def doomer(self) -> Agent:
        return Agent(
            config=self.agents_config["doomer"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=True,  # A2A: Can challenge Hype Bro's optimism
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="openrouter/x-ai/grok-4.1-fast:free",
                base_url="https://openrouter.ai/api/v1",
                temperature=0.7,
                api_key=os.environ.get("OPENROUTER_API_KEY")
            ),
        )

    @agent
    def hype_bro(self) -> Agent:
        return Agent(
            config=self.agents_config["hype_bro"],
            tools=[MotivationalQuoteTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=True,  # A2A: Can counter Doomer's pessimism
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="openrouter/x-ai/grok-4.1-fast:free",
                base_url="https://openrouter.ai/api/v1",
                temperature=0.7,
                api_key=os.environ.get("OPENROUTER_API_KEY")
            ),
        )

    @agent
    def roast_master(self) -> Agent:
        return Agent(
            config=self.agents_config["roast_master"],
            tools=[RoastGeneratorTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=True,  # A2A: Can roast other agents' responses
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="openrouter/x-ai/grok-4.1-fast:free",
                base_url="https://openrouter.ai/api/v1",
                temperature=0.7,
                api_key=os.environ.get("OPENROUTER_API_KEY")
            ),
        )

    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            config=self.agents_config["fact_checker"],
            tools=[TavilySearchTool(), StatisticsFinderTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="openrouter/x-ai/grok-4.1-fast:free",
                base_url="https://openrouter.ai/api/v1",
                temperature=0.7,
                api_key=os.environ.get("OPENROUTER_API_KEY")
            ),
        )

    @agent
    def the_gremlin(self) -> Agent:
        return Agent(
            config=self.agents_config["the_gremlin"],
            tools=[ChaosMeterTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="openrouter/x-ai/grok-4.1-fast:free",
                base_url="https://openrouter.ai/api/v1",
                temperature=0.7,
                api_key=os.environ.get("OPENROUTER_API_KEY")
            ),
        )

    @agent
    def prophet(self) -> Agent:
        return Agent(
            config=self.agents_config["prophet"],
            tools=[SentimentAnalysisTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=True,  # A2A: Can ask agents to clarify or debate
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="openrouter/x-ai/grok-4.1-fast:free",
                base_url="https://openrouter.ai/api/v1",
                temperature=0.7,
                api_key=os.environ.get("OPENROUTER_API_KEY")
            ),
        )

    # === TASKS ===

    @task
    def doomer_response(self) -> Task:
        return Task(
            config=self.tasks_config["doomer_response"],
            markdown=False,
        )

    @task
    def hype_bro_response(self) -> Task:
        return Task(
            config=self.tasks_config["hype_bro_response"],
            markdown=False,
        )

    @task
    def roast_master_response(self) -> Task:
        return Task(
            config=self.tasks_config["roast_master_response"],
            markdown=False,
        )

    @task
    def fact_checker_response(self) -> Task:
        return Task(
            config=self.tasks_config["fact_checker_response"],
            markdown=False,
        )

    @task
    def gremlin_chaos(self) -> Task:
        return Task(
            config=self.tasks_config["gremlin_chaos"],
            markdown=False,
        )

    @task
    def prophet_final_verdict(self) -> Task:
        return Task(
            config=self.tasks_config["prophet_final_verdict"],
            markdown=False,
        )

    # === CREW ===

    @crew
    def crew(self) -> Crew:
        """Creates the ChaosOracle7DeadlyPersonas crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

    # === HELPERS ===

    def _load_response_format(self, name):
        with open(os.path.join(self.base_directory, "config", f"{name}.json")) as f:
            json_schema = json.loads(f.read())

        return SchemaConverter.build(json_schema)
