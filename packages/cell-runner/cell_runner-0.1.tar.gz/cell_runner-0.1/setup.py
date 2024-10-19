# setup.py
from setuptools import setup, find_packages

setup(
    name='cell_runner',
    version='0.1',
    packages=find_packages(),
    install_requires=[],
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': [
            'cell_runner=cell_runner.runner:main',  # Command to run in CLI
        ],
    },
    author='Chintha Sai Charan',
    author_email='saicharanchintha8888@gmail.com',
    description='A package to run Jupyter notebook cells from the command line.',
    url='https://github.com/chinthasaicharan/jupyter-cell-runner',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',

)