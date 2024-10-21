# -*- encoding: utf-8 -*-
import os
import re
from setuptools import setup
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        # Proceed with standard install
        install.run(self)
        # Activate nbgrader's extensions
        os.system("jupyter nbextension install --sys-prefix --py nbgrader")
        os.system("jupyter nbextension enable --sys-prefix --py nbgrader")
        os.system("jupyter serverextension enable --sys-prefix --py nbgrader")


version_file = os.path.join("methnum", "__init__.py")
verstrline = open(version_file, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    current_version = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (version_file,))
print(f"methnum version is {current_version}")

setup(
    name="methnum",
    version=current_version,
    description="Required software for using the MethNum course material",
    url="https://gitlab.dsi.universite-paris-saclay.fr/MethNum",
    author="Jérémy Neveu, Nicolas M. Thiéry et al.",
    author_email="jeremy.neveu@universite-paris-saclay.fr",
    license="CC",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Information Technology",
        "Topic :: Scientific/Engineering",
        "Programming Language :: Python",
    ],  # classifiers list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
    scripts=["bin/methnum"],
    packages=["methnum"],
    cmdclass={
        "install": CustomInstallCommand,
    },
    install_requires=[
          'travo[jupyter]>=1.0', 'nbgrader>=0.9.1', 'jupytext'
      ],
    data_files=[
        ("etc/jupyter", ["nbgrader_config.py"]),
        ("etc/jupyter/labconfig/", ["default_setting_overrides.json"]),
    ],
)
