# setup.py

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='TickBox',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'tickbox=todo_manager.cli:main',
            'tick=todo_manager.cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    author='Abhinav',
    author_email='upstage.barrier_0x@icloud.com',
    description='A terminal-based TO-DO list manager with rich functionality.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/abhinavhooda/todo-manager',
    license='MIT',
)
