from setuptools import find_packages, setup

setup(
    name="mcqgenerator",
    version="0.0.1",
    author="Naincy",
    author_email="nainachourasia098@gmail.com",
    install_requires=[
        "openai",
        "python-dotenv",
        "streamlit",
        "PyPDF2",
        "langchain",
    ],
    packages=find_packages()
)