from pathlib import Path
import pytest
from traceback import print_tb

from adhoc_api.tool import AdhocApi
from adhoc_api.examples.gdc import gdc_api
from archytas.tools import PythonTool

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
    adhoc_api = AdhocApi(
        apis=[gdc_api],
        drafter_config={'model': 'gemini-1.5-pro-001'},
        finalizer_config={'model': 'gpt-4-turbo'},
    )
    code = adhoc_api.use_api('Genomics Data Commons', case)

    # attempt to run the code
    python = PythonTool()
    try:
        res = python.run(code)
    except Exception as e:
        print_tb(e.__traceback__)
        print(f'Encountered an error while running the code: {e}. The original code is provided below:\n\n{code}\n')
        raise

    # TODO: even if code runs, need better way to check results
    if res:
        print(f'code output: {res}')
