# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sofa', 'sofa.models', 'sofa.plots', 'sofa.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3',
 'gseapy>=1.0.4',
 'matplotlib>=3.5.2',
 'muon>=0.1.3',
 'numba>=0.55.2',
 'numpy>=1.22.4',
 'pandas>=1.4.2',
 'pyro-ppl<1.8.4',
 'pytest',
 'scikit-learn>=1.1.1',
 'scipy>=1.8.1',
 'sphinxcontrib-bibtex>=2.5.0,<3.0.0',
 'toml>=0.10.2',
 'torch>=1.13.1,<2.0.0']

extras_require = \
{'docs': ['Sphinx==4.2.0',
          'sphinx-rtd-theme==1.0.0',
          'sphinxcontrib-napoleon==0.7',
          'nbsphinx==0.8.9'],
 'notebook': ['jupyter']}

setup_kwargs = {
    'name': 'biosofa',
    'version': '0.7.1',
    'description': 'Probabilistic factor analysis model with covariate guided factors',
    'long_description': '# Semi-supervised Omics Factor Analysis (SOFA)\n\n\n[![PyPI version](https://badge.fury.io/py/biosofa.svg)](https://badge.fury.io/py/biosofa)\n\n# Introduction\n\nHere we present semi-supervised probabilistic Factor Analysis (SOFA), a multi-omics integration method, which infers a set of low dimensional latent factors that represent the main sources of variability. SOFA enables the discovery of primary sources of variation while adjusting for known covariates and simultaneously disentangling variation that is shared between multiple omics modalities and specific to single modalities. The SOFA method is implemented in python using the Pyro framework for probabilistic programming.\n\n\n# Installation\n\nTo install `SOFA` first create `Python 3.8` environment e.g. by\n\n```\nconda create --name sofa-env python=3.8\nconda activate sofa-env\n```\n\nand install the package using \n\n```\npip install biosofa\n```\n\n\n\n# How to use `SOFA` for multi-omics analyses\n\nA detailed manual with examples and how to use `SOFA` can be found here https://tcapraz.github.io/SOFA/index.html.\n\n\n# How to cite `SOFA`\n\n> **Semi-supervised Omics Factor Analysis (SOFA) disentangles known sources of variation from latent factors in multi-omics data**\n>\n> Capraz, T., Vöhringer, H.S. and Huber, W.\n>\n> *bioRxiv* 2024. doi: [10.1101/2024.10.10.617527](https://doi.org/10.1101/2024.10.10.617527).\n',
    'author': 'capraz',
    'author_email': 'tuemayc@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8.1,<3.11.6',
}


setup(**setup_kwargs)
