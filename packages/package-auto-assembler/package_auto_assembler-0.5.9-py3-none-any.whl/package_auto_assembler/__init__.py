
"""
Package auto assembler is a tool that meant to streamline creation of single module packages.
Its purpose is to automate as many aspects of python package creation as possible,
to shorten a development cycle of reusable components, maintain certain standard of quality
for reusable code. It provides tool to simplify the process of package creatrion
to a point that it can be triggered automatically within ci/cd pipelines,
with minimal preparations and requirements for new modules.
"""
from .package_auto_assembler import *
