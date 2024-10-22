# Copyright (c) AffectLog SAS
# Licensed under the MIT License.

import os

import setuptools

# Version will be read from version.py
version = ""
# Fetch Version
with open(os.path.join('al360_taiwidgets', '__version__.py')) as f:
    code = compile(f.read(), f.name, 'exec')
    exec(code)

# Fetch ReadMe
with open("README.md", "r") as fh:
    long_description = fh.read()

# Use requirements.txt to set the install_requires
with open('requirements.txt') as f:
    install_requires = [line.strip() for line in f] + \
        ["al360_trustworthyai==%s" % version]

setuptools.setup(
    name="al360_taiwidgets",
    version=version,
    author="Roman Lutz, Ilya Matiach, Ke Xu",
    author_email="al360_taiwidgets-maintain@affectlog.com",
    description="Interactive visualizations to assess fairness, explain "
                "models, generate counterfactual examples, analyze "
                "causal effects and analyze errors in "
                "Machine Learning models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/affectlog360/affectlog360",
    packages=setuptools.find_packages(),
    python_requires='>=3.7',
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    include_package_data=True,
    package_data={
        '': [
            'widget/**'
        ]
    },
    zip_safe=False,
)
