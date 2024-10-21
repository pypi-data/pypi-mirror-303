import sys
import yaml, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from aistack.version import __version__

from rich import print
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
load_dotenv()
import autogen
config_list = [
    {
        'model': os.environ.get("OPENAI_MODEL_NAME", "gpt-4o"),
        'base_url': os.environ.get("OPENAI_API_BASE", "https://api.openai.com/v1"),
    }
]

def generate_crew_and_kickoff(agent_file, framework=None):
    with open(agent_file, 'r') as f:
        config = yaml.safe_load(f)

    topic = config['topic']  
    framework = framework or config.get('framework')

    agents = {}
    tasks = []
    if framework == "autogen":
        # Load the LLM configuration dynamically
        print(config_list)
        llm_config = {"config_list": config_list}
        
        for role, details in config['roles'].items():
            agent_name = details['role'].format(topic=topic).replace("{topic}", topic)
            agent_goal = details['goal'].format(topic=topic)
            # Creating an AssistantAgent for each role dynamically
            agents[role] = autogen.AssistantAgent(
                name=agent_name,
                llm_config=llm_config,
                system_message=details['backstory'].format(topic=topic)+". Reply \"TERMINATE\" in the end when everything is done.",
            )

            # Preparing tasks for initiate_chats
            for task_name, task_details in details.get('tasks', {}).items():
                description_filled = task_details['description'].format(topic=topic)
                expected_output_filled = task_details['expected_output'].format(topic=topic)
                
                chat_task = {
                    "recipient": agents[role],
                    "message": description_filled,
                    "summary_method": "last_msg", 
                }
                tasks.append(chat_task)


        user = autogen.UserProxyAgent(
            name="User",
            human_input_mode="NEVER",
            is_termination_msg=lambda x: (x.get("content") or "").rstrip().endswith("TERMINATE"),
            code_execution_config={
                "work_dir": "coding",
                "use_docker": False,
            },
        )
        response = user.initiate_chats(tasks)
        result = "### Output ###\n"+response[-1].summary if hasattr(response[-1], 'summary') else ""
    else:
        for role, details in config['roles'].items():
            role_filled = details['role'].format(topic=topic)
            goal_filled = details['goal'].format(topic=topic)
            backstory_filled = details['backstory'].format(topic=topic)
            
            # Assume tools are loaded and handled here as per your requirements
            agent = Agent(role=role_filled, goal=goal_filled, backstory=backstory_filled)
            agents[role] = agent

            for task_name, task_details in details.get('tasks', {}).items():
                description_filled = task_details['description'].format(topic=topic)
                expected_output_filled = task_details['expected_output'].format(topic=topic)

                task = Task(description=description_filled, expected_output=expected_output_filled, agent=agent)
                tasks.append(task)

        crew = Crew(
            agents=list(agents.values()),
            tasks=tasks,
            verbose=2
        )

        result = crew.kickoff()
    return result

def main(args=None):
    if args is None:
        args = sys.argv[1:]  

    invocation_cmd = "aistack"
    version_string = f"AIStack version {__version__}"
    framework = "crewai"  # Default framework

    if "--framework" in args:
        framework_index = args.index("--framework")
        framework = args[framework_index + 1]
        args = args[:framework_index] + args[framework_index + 2:]

    if args:
        agent_file = args[-1]  # Assuming the last argument is the agent file
    else:
        agent_file = "agents/example.yaml"

    result = generate_crew_and_kickoff(agent_file, framework)
    print(result)
    
if __name__ == "__main__":
    main()
