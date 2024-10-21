from setuptools import setup, find_packages

setup(
    name='aistack',
    version='0.0.1',
    author='Team AIStack',
    author_email='team@aistack.run',
    description='AIStack application combines AutoGen and CrewAI or similar frameworks into a low-code solution for building and managing multi-agent LLM systems, focusing on simplicity, customization, and efficient human-agent collaboration.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/aistackhq/aistack',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    install_requires=[
        'pyautogen',
        'rich',
        'crewai',
    ],
)
