"""Jinja2 environment config for Gandula."""

from jinja2 import Environment, PackageLoader, select_autoescape

env = Environment(loader=PackageLoader('gandula'), autoescape=select_autoescape())
