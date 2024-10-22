from setuptools import setup

import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))
path_to_readme = os.path.join(here, "README.md")

long_description = """# Package auto assembler

Package auto assembler is a tool that meant to streamline creation of single module packages.
Its purpose is to automate as many aspects of python package creation as possible,
to shorten a development cycle of reusable components, maintain certain standard of quality
for reusable code. It provides tool to simplify the process of package creatrion
to a point that it can be triggered automatically within ci/cd pipelines,
with minimal preparations and requirements for new modules.

"""

if os.path.exists(path_to_readme):
  with codecs.open(path_to_readme, encoding="utf-8") as fh:
      long_description += fh.read()

setup(
    name="package_auto_assembler",
    packages=["package_auto_assembler"],
    install_requires=['mkdocs==1.6.0', 'uvicorn', 'pip_audit==2.7.3', 'numpy==1.26.0', 'requests', 'pyyaml', 'pandas==2.1.1', 'nbconvert==7.16.4', 'attrs>=22.2.0', 'packaging', 'fastapi', 'stdlib-list', 'click==8.1.7', 'nbformat', 'mkdocs-material==9.5.30'],
    classifiers=['Development Status :: 3 - Alpha', 'Intended Audience :: Developers', 'Intended Audience :: Science/Research', 'Programming Language :: Python :: 3', 'Programming Language :: Python :: 3.9', 'Programming Language :: Python :: 3.10', 'Programming Language :: Python :: 3.11', 'License :: OSI Approved :: MIT License', 'Topic :: Scientific/Engineering'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="Kyrylo Mordan",
    author_email="parachute.repo@gmail.com",
    description="A tool to automate package creation within ci based on just .py and optionally .ipynb file.",
    keywords="['python', 'packaging', 'aa-paa-tool']",
    license="mit",
    url="https://kiril-mordan.github.io/reusables/package_auto_assembler/",
    version="0.5.10",
    entry_points = {'console_scripts': ['paa = package_auto_assembler.cli:cli']},
    include_package_data = True,
    package_data = {'package_auto_assembler': ['mkdocs/**/*', 'artifacts/package_licenses.json', 'artifacts/package_mapping.json', '.paa.tracking/version_logs.csv', '.paa.tracking/release_notes.md', '.paa.tracking/lsts_package_versions.yml', '.paa.tracking/notebook.ipynb', '.paa.tracking/package_mapping.json', '.paa.tracking/package_licenses.json', '.paa.tracking/.paa.config', '.paa.tracking/.paa.version']} ,
    )
