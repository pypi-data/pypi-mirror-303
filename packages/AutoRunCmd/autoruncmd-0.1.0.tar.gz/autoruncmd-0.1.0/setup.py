
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="AutoRunCmd",
    version="0.1.0",
    description="Runs multi scripts with a simple line of prompt with a config dot file in your environment",
    url="https://github.com/rakeshkanna-rk/pyautorun/",
    author="Rakesh Kanna",
    author_email='rakeshkanna0108@gmail.com',
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=[
    "automation",
    "build tools",
    "makefile",
    "python scripts",
    "task runner",
    "command-line tool",
    "config file"
    ],
    python_requires=">=3.6",
    install_requires= ['textPlay'],
    project_urls={
        'GitHub': 'https://github.com/rakeshkanna-rk/pyautorun/',
        'PyPI' : 'https://pypi.org/project/pyautorun/'
    },
    entry_points={
        "console_scripts":["pyauto = pyautorun:cli"]
        },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Software Distribution",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
        "Typing :: Typed",
        "Environment :: Console",
        "Natural Language :: English",
    ]
)
