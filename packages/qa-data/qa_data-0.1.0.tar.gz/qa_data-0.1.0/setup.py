from setuptools import setup, find_packages

setup(
    name='qa-data',  
    version='0.0.1',   
    author='Um Changyong', 
    author_email='eum6211@gmail.com', 
    description='generate dataset to fine-tune llm', 
    packages=find_packages(include=["qa_data", "qa_data.*"]), 
    install_requires=[ 
        "langchain-core>=0.3.12",
        "pydantic>=2.9.2",
    ],
    keywords=[
        "llm", "fine-tune", "generate data", "dataset"
    ]
)