# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['exasol', 'exasol.nb_connector']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=2.1.0',
 'exasol-bucketfs>=0.9.0,<1.0.0',
 'exasol-integration-test-docker-environment>=2.0.0',
 'exasol-saas-api>=0.9.0,<1.0.0',
 'exasol-sagemaker-extension>=0.10.0,<1.0.0',
 'exasol-script-languages-container-tool>=0.19.0',
 'exasol-transformers-extension>=2.0.0,<3.0.0',
 'ibis-framework[exasol]>=9.1.0,<10.0.0',
 'ifaddr>=0.2.0,<0.3.0',
 'pyexasol>=0.24.0',
 'requests>=2.31.0,<2.32.0',
 'sqlalchemy-exasol>=4.6.0',
 'transformers[torch]>=4.36.2,<5.0.0',
 'types-requests>=2.31.0.6,<3.0.0.0']

extras_require = \
{':sys_platform == "darwin"': ['sqlcipher3>=0.5.0'],
 ':sys_platform == "linux"': ['sqlcipher3-binary>=0.5.0']}

setup_kwargs = {
    'name': 'exasol-notebook-connector',
    'version': '0.4.0',
    'description': 'Components, tools, APIs, and configurations in order to connect Jupyter notebooks to Exasol and various other systems.',
    'long_description': '# Exasol Notebook Connector\n\nConnection configuration management and additional tools for Jupyter notebook applications provided by Exasol company.\n\n[![PyPI Version](https://img.shields.io/pypi/v/exasol-notebook-connector)](https://pypi.org/project/exasol-notebook-connector/)\n[![License](https://img.shields.io/pypi/l/exasol-notebook-connector)](https://opensource.org/licenses/MIT)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/exasol-notebook-connector)](https://pypi.org/project/exasol-notebook-connector)\n[![Last Commit](https://img.shields.io/github/last-commit/exasol/notebook-connector)](https://pypi.org/project/exasol-notebook-connector/)\n\n## Features\n\nExasol Notebook Connector (ENC) currently contains a **Secret Store** that can be used in Jupyter notebook applications to store arbitrary credentials and configuration items, such as user names, passwords, URLs, etc.\n\nBy that users of such notebook applications\n* need to enter their credentials and configuration items only once\n* can store them in a secure, encrypted, and persistent file based on SQLite and [coleifer/sqlcipher3](https://github.com/coleifer/sqlcipher3)\n* can use these credentials and configuration items in their notebook applications\n\n## Usage\n\n```python\nfrom pathlib import Path\nfrom exasol.nb_connector.secret_store import Secrets\n\nfile = "password_db.sqlite"\nsecrets = Secrets(Path(file), "my secret password")\nkey = "my key"\nsecrets.save(key, "my value")\nvalue = secrets.get(key)\n```\n\n#### Constraints and Special Situations\n\n* If file does not exist then SecretStore will create it.\n* If password is wrong then SecretStore will throw an exception.\n* If file contains key from a session in the past then method `secrets.save()` will overwrite the value for this key.\n* If key is not contained in file then SecretStore returns `None`.\n* Saving multiple keys can be chained: `secrets.save("key-1", "A").save("key-2", "B")`\n',
    'author': 'Christoph Kuhnke',
    'author_email': 'christoph.kuhnke@exasol.com',
    'maintainer': 'Christoph Kuhnke',
    'maintainer_email': 'christoph.kuhnke@exasol.com',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
