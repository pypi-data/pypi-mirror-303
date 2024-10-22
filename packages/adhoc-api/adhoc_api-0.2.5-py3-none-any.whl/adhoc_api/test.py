from archytas.react import ReActAgent, FailedTaskError
from archytas.tools import PythonTool
from easyrepl import REPL
from .tool import AdhocApi, DrafterConfig, FinalizerConfig, APISpec
from pathlib import Path

import pdb

here = Path(__file__).parent

GDC_ADDITONAL_INFO = '''
The code should be performing a request for data related to a disease types.
The GDC database has a strict set of disease types that can be used to filter data.
Please correct the usage of any disease type filters to either a matching, or the closest valid disease types if it is not in the below list.
- 'adenomas and adenocarcinomas'
- 'ductal and lobular neoplasms'
- 'myeloid leukemias'
- 'epithelial neoplasms, nos'
- 'squamous cell neoplasms'
- 'gliomas'
- 'lymphoid leukemias'
- 'cystic, mucinous and serous neoplasms'
- 'nevi and melanomas'
- 'neuroepitheliomatous neoplasms'
- 'acute lymphoblastic leukemia'
- 'plasma cell tumors'
- 'complex mixed and stromal neoplasms'
- 'mature b-cell lymphomas'
- 'transitional cell papillomas and carcinomas'
- 'not applicable'
- 'osseous and chondromatous neoplasms'
- 'germ cell neoplasms'
- 'mesothelial neoplasms'
- 'not reported'
- 'acinar cell neoplasms'
- 'paragangliomas and glomus tumors'
- 'chronic myeloproliferative disorders'
- 'neoplasms, nos'
- 'thymic epithelial neoplasms'
- 'myomatous neoplasms'
- 'complex epithelial neoplasms'
- 'soft tissue tumors and sarcomas, nos'
- 'lipomatous neoplasms'
- 'meningiomas'
- 'fibromatous neoplasms'
- 'specialized gonadal neoplasms'
- 'unknown'
- 'miscellaneous tumors'
- 'adnexal and skin appendage neoplasms'
- 'basal cell neoplasms'
- 'mucoepidermoid neoplasms'
- 'myelodysplastic syndromes'
- 'nerve sheath tumors'
- 'leukemias, nos'
- 'synovial-like neoplasms'
- 'fibroepithelial neoplasms'
- 'miscellaneous bone tumors'
- 'blood vessel tumors'
- 'mature t- and nk-cell lymphomas'
- '_missing'

Additionally, any data downloaded should be downloaded to the './data/' directory. 
Please ensure the code makes sure this location exists, and all downloaded data is saved to this location.
'''

drafter_config: DrafterConfig = {
    # 'model': 'gemini-1.5-flash-001', 
    'model': 'gemini-1.5-pro-001',
    'ttl_seconds': 1800
}
finalizer_config: FinalizerConfig = {
    'model': 'gpt-4o'
}

gdc_api: APISpec = {
    'name': "Genomics Data Commons",
    'cache_key': 'api_assistant_gdc_david_testing',
    'description': """\
The NCI's Genomic Data Commons (GDC) provides the cancer research community with a repository and computational 
platform for cancer researchers who need to understand cancer, its clinical progression, and response to therapy.
The GDC supports several cancer genome programs at the NCI Center for Cancer Genomics (CCG), including The Cancer
Genome Atlas (TCGA) and Therapeutically Applicable Research to Generate Effective Treatments (TARGET).""",
    'documentation': (here/'api_documentation'/'gdc.md').read_text(),
    'proofread_instructions': GDC_ADDITONAL_INFO
}


def main():
    python = PythonTool()
    adhoc_api = AdhocApi(
        apis=[gdc_api],
        drafter_config=drafter_config,
        finalizer_config=finalizer_config,
        # run_code=python.run  # don't include so top level agent will run the code itself
    )

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

