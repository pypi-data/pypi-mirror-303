from setuptools import setup, find_packages

setup(
    name="VGenEval",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
    ],
    author="Yuhang Yang",
    author_email="yangyuhang.edu@gmail.com",
    description="A package for loading prompts for video generation evaluation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AILab-CVC/VideoGen-Eval",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)