import os
import sys
from unittest.mock import MagicMock

import docker
import et_engine

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../etcli'))

#sys.path.insert(0, os.path.dirname(docker.__file__))
#sys.path.insert(0, os.path.dirname(et_engine.__file__))

#print("test")

# # Mock modules
# class Mock(MagicMock):
#     @classmethod
#     def __getattr__(cls, name):
#         return MagicMock()

# MOCK_MODULES = ['docker', 'et_engine', 'et_engine.config']
# sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# # Specify the package name for autodoc
# autodoc_mock_imports = ['docker', 'et_engine']

project = 'Command Line Interface'
copyright = '2024, Alex Miltenberger, Tyler Hall'
author = 'Alex Miltenberger, Tyler Hall'
release = '0.0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinxcontrib.httpdomain',
    'sphinx_click'
]

autosummary_generate = True
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

html_theme = 'furo'

# intersphinx_mapping = {
#     'docker': ('https://docker-py.readthedocs.io/en/stable/', None),
# #    'et_engine': ('https://et-engine-docs-url.com', None),  # Replace with actual URL
# }