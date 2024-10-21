# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['gitlab_docs']

package_data = \
{'': ['*']}

install_requires = \
['jq>=1.8.0,<2.0.0',
 'markdown-analysis',
 'oyaml',
 'prettytable',
 'pytablewriter>=1.2.0,<1.3.0',
 'semver>=3.0.2,<4.0.0',
 'setuptools',
 'typer>=0.12.5,<0.13.0']

entry_points = \
{'console_scripts': ['gitlab-docs = gitlab_docs.app:main']}

setup_kwargs = {
    'name': 'gitlab-docs',
    'version': '0.0.38',
    'description': 'A tool that automatically generates gitlab documentation from yaml files',
    'long_description': '# Gitlab Docs\n## How to install\nGitlab Docs is portable utility based in python so any system that supports python3 you will be able to install it.\n### Python\n```bash\npip3 install --user gitlab-docs\n```\n\n### Docker\n```bash\ndocker run -v ${PWD}:/gitlab-docs charlieasmith93/gitlab-docs\n```\n### Precommit Hook\n<!-- ```yml\n\n``` -->',
    'author': 'Charlie Smith',
    'author_email': 'me@charlieasmith.co.uk',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
