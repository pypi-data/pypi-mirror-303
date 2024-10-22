# © N.Sikharulidze (https://ubix.pro/)
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="loggerbot",
    version="2.8.8",
    author="N.Sikharulidze",
    author_email="info@ubix.pro",
    description="A Telegram logging library with rate limiting and message queuing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ubix.pro/",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
    ],
    project_urls={
        "Bug Tracker": "https://github.com/NSb0y/loggerbot/issues",
        "Documentation": "https://github.com/NSb0y/loggerbot",
        "Page": "https://ubix.pro",
    },
)
