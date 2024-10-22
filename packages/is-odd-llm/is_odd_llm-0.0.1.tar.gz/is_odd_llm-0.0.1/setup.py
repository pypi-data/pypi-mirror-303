from setuptools import setup

setup(
    name="is-odd-llm",
    version="0.0.1",
    author="yenslife",
    author_email="77geo5rge6@gmail.com",
    description="A Python package using LLM to determine if a number is odd",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yenslife/is-odd-llm",
    packages=["is_odd_llm"],
    install_requires=["openai>=1.40.6"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
