from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of your README file
here = Path(__file__).parent
long_description = (here / 'README.md').read_text()

setup(
    name='ProjectManager_C2',
    version='0.1',
    packages=find_packages(),
    scripts=[
        'scripts/helper.sh',
        'scripts/main.sh',
        'scripts/llm.py'
    ],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type='text/markdown',
)
