from agenticos.connectors import BaseWorkflowConfig, CrewaiWorkflowConfig
from agenticos.node.models import AgenticConfig

workflows : dict[BaseWorkflowConfig] = {}

# Example workflow
# Import the Crew class. If you used the flow from CrewAI docs the following import should work
# If you are getting any erros please correct the import path
from {{folder_name}}.crew import {{class_name}}Crew as Crew

# Define workflows here
# key is the workflow name
workflows["crewai"] = CrewaiWorkflowConfig(
    # Description of the workflow
    description="A crew for running AI tasks",
    # Inputs for the workflow
    inputs={"topic": "The topic to joke about"},
    # The crew class to be used
    crew_cls=Crew,
)

# Create the config object. Change the name to the name of your node
config = AgenticConfig(name="Test Node", workflows=workflows)
