# -*- coding: utf-8 -*-

import os
import sys
import ast
import codecs
from setuptools import setup

PROJECT_ROOT = os.path.dirname(__file__)


class VersionFinder(ast.NodeVisitor):
    def __init__(self):
        self.version = None

    def visit_Assign(self, node):
        try:
            if node.targets[0].id == 'version':
                self.version = node.value.s
        except:
            pass


def read_version():
    """Read version from sure/__init__.py without loading any files"""
    finder = VersionFinder()
    path = os.path.join(PROJECT_ROOT, 'w1thermsensor', '__init__.py')
    with codecs.open(path, 'r', encoding='utf-8') as fp:
        file_data = fp.read().encode('utf-8')
        finder.visit(ast.parse(file_data))

    return finder.version


setup_args=dict(
    name="w1thermsensor",
    version=read_version(),
    license="MIT",
    description="This little pure python module provides a single class to get the temperature of a w1 sensor",
    author="Timo Furrer",
    author_email="tuxtimo@gmail.com",
    maintainer="Timo Furrer",
    maintainer_email="tuxtimo@gmail.com",
    platforms=["Linux"],
    url="http://github.com/timofurrer/w1thermsensor",
    download_url="http://github.com/timofurrer/w1thermsensor",
    packages=["w1thermsensor"],
    install_requires=["click"],
)

if sys.version_info.major == 3:
    setup_args["entry_points"] = {"console_scripts": ["w1thermsensor = w1thermsensor.cli:cli"]}

setup(**setup_args)
