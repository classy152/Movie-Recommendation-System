from setuptools import setup

with open("READ.md","rb",encoding="utf-8") as fh:
    long_des=fh.read()

AUTHOR_NAME = 'Chandana Lokhande'
SCR_REPO ='src'
LIST_OF_REQUIREMENT = ['streamlit']

setup(
    name=SCR_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='chandanalokhande15@gmail.com',
    description='A simple and begginer level project, named as Movies Recommendation System ',
    long_description=long_des,
    long_description_content_type='text/markdown',
    package=[SCR_REPO],
    
)