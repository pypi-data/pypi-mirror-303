from setuptools import setup, find_packages

# Read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PoroPilot',
    version='0.2.6',
    description='Wrapper Interface for Riot API',
    url='https://github.com/anuiit/PoroPilot',
    author='anuiit',
    author_email='',
    keywords=['Riot', 'API', 'wrapper', 'Poro', 'Pilot', 'League of Legends', 'LoL', 'game', 'gaming', 'esports', 'riotgames', 'riot-api', 'riot-api-wrapper', 'riot-api-python', 'riot-api'],
    license='MIT',
    packages=find_packages(),
    install_requires=['requests', 'requests-cache'],
    long_description=long_description,
    long_description_content_type='text/markdown',
)