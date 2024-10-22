# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['neso_utils',
 'neso_utils.assessment_report',
 'neso_utils.assessment_report.kafka',
 'neso_utils.assessment_report.utils',
 'neso_utils.synthetic_data_generator',
 'neso_utils.synthetic_data_generator.configs',
 'neso_utils.synthetic_data_generator.generator',
 'neso_utils.synthetic_data_generator.sampling',
 'neso_utils.synthetic_data_generator.utils']

package_data = \
{'': ['*']}

install_requires = \
['fastavro==1.9.1',
 'geopandas==1.0.1',
 'jmxquery==0.6.0',
 'numpy==1.24.1',
 'randomname==0.2.1',
 'rdflib==6.3.2',
 'setuptools==68.2.2',
 'shapely==2.0.6']

setup_kwargs = {
    'name': 'neso-utils',
    'version': '0.0.10',
    'description': 'Library of utilities for NESO.',
    'long_description': "<!-- <p align='center'>\n    <img src='./.docs/cctv.png' width='20%' height='20%'>\n</p> -->\n\n<h1 align='center'>\n    <strong> neso-utils </strong>\n</h1>\n\n<p align='center'>\n    Library of utilities for NESO.\n</p>\n\n### **1. Installation**\n\n```bash\npip install neso-utils\n```\n\n### **2. Utilities**\n\n- [Synthetic Data Generator](./neso_utils/synthetic_data_generator/README.md) [![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen) ![tests](https://img.shields.io/badge/tests-35%20passed%2C%200%20failed-brightgreen) ![python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)]\n\n- [Assessment Report](./neso_utils/assessment_report/README.md) [![coverage](https://img.shields.io/badge/coverage-98%25-brightgreen) ![tests](https://img.shields.io/badge/tests-14%20passed%2C%200%20failed-brightgreen) ![python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)]\n\n### **3. Example of Usage**\n\n#### **3.1. Synthetic Data Generator**\n\n```python\nfrom neso_utils import SyntheticDataGenerator\n```\n\n#### **3.2. Assessment Report**\n\n```python\nfrom neso_utils import AssessmentReport\n```\n\n### **4. Documentation [TBC]**\n\n[Documentation](https://neso-utils.readthedocs.io/en/latest/)\n",
    'author': 'Joao Nisa',
    'author_email': 'joao.nisa@mesh-ai.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
