from setuptools import setup, find_packages

setup(
    name='llm-task-agents',
    version='0.1.1',
    description='A collection of preset efficient prompts packaged into LLM agents.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Alfred Wallace',
    author_email='alfred.wallace@netcraft.fr',
    url='https://github.com/alfredwallace7/llm-task-agents',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'ollama',
        'sqlalchemy',
        'mysqlclient',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
