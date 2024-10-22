from setuptools import setup, find_packages

setup(
    name='yuseful_prompts',
    version='4.0.5',
    packages=find_packages(),
    install_requires=[
        'langchain-core',
        'langchain-community',
        'langchain-ollama',
        'pytest'
    ],
    author='yactouat',
    author_email='yactouat@yactouat.com',
    description='tested chains for common use-cases of the markets-agent.com using open LLMs with ollama and Langchain',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/markets-agent/yuseful_prompts',
    license='MIT',
)
