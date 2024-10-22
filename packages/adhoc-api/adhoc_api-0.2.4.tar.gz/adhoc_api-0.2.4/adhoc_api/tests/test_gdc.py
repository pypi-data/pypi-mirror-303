from pathlib import Path
import pytest
here = Path(__file__).resolve().parent

import pdb

def get_cases(filename:str) -> list[str]:
    return (here/filename).read_text().strip().split('\n')

def truncate(s:str, n:int=20) -> str:
    if len(s) <= n + 3:
        return s
    return f'{s[:n]}...'

raw_cases = get_cases('queries_(raw).txt')
processed_cases = get_cases('queries_(processed).txt')

# DEBUG just test one case
raw_cases = raw_cases[:1]
processed_cases = []

@pytest.mark.parametrize('case', raw_cases + processed_cases, ids=truncate)
def test_case(case:str):
    from adhoc_api.tool import AdhocApi
    from archytas.tools import PythonTool
    from archytas.react import ReActAgent
    from asyncio import run
    python = PythonTool()
    adhoc_api = AdhocApi()#(run_code=python.run)
    agent = ReActAgent(model='gpt-4o', tools=[], verbose=True)
    res = run(adhoc_api.use_api('gdc', case, agent))
    print(f'{case=}\n{res=}')


if __name__ == "__main__":
    print(get_cases('queries_(processed).txt'))
    print(get_cases('queries_(raw).txt'))