"""Simple example of grabbing the HTML content of an API documentation page and converting it to a markdown file"""

from archytas.react import ReActAgent, FailedTaskError
from archytas.tools import PythonTool
from easyrepl import REPL
from adhoc_api.tool import AdhocApi, APISpec

from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md


def get_joke_api_documentation() -> str:
    """Download the HTML of the joke API documentation page with soup and convert it to markdown."""
    url = 'https://sv443.net/jokeapi/v2/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    markdown = md(str(soup))
    
    return markdown


def main():
    
    # set up the API spec for the JokeAPI
    gdc_api: APISpec = {
        'name': "JokesAPI",
        'description': 'JokeAPI is a REST API that serves uniformly and well formatted jokes.',
        'documentation': get_joke_api_documentation(),
        # set a key if the docs are large and you want to cache them in the LLM context
        # 'cache_key': 'adhoc_joke_api',
        # set proofread instructions if there are specific features you want the output code to conform to (beyond general code correctness)
        # 'proofread_instructions': 'The request code should be related to fetching a joke from the Jokes API. Please make sure any output is to the console'
    }

    # set up the Adhoc API tool and Python tool (for performing the API request)
    adhoc_api = AdhocApi(
        apis=[gdc_api],
        drafter_config={'model': 'gemini-1.5-flash-001', 'ttl_seconds': 1800},
        finalizer_config={'model': 'gpt-4o'}
    )
    python = PythonTool()

    tools = [adhoc_api, python]
    agent = ReActAgent(model='gpt-4o', tools=tools, verbose=True)
    print(agent.prompt)

    # REPL to interact with agent
    for query in REPL(history_file='.chat'):
        try:
            answer = agent.react(query)
            print(answer)
        except FailedTaskError as e:
            print(f"Error: {e}")




if __name__ == "__main__":
    main()