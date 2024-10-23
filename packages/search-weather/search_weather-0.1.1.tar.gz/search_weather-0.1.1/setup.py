from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call


def download_ko_core_news_sm():
    check_call(["python", "-m", "spacy", "download", "ko_core_news_sm"])


class PostDevelopCommand(develop):
    def run(self):
        develop.run(self)
        download_ko_core_news_sm()


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        download_ko_core_news_sm()


setup(
    name="search_weather",
    version="0.1.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "geopy",
        "spacy>=3.0.0,<4.0.0",
    ],
    extras_require={
        "dev": ["pytest", "flake8"],
    },
    python_requires=">=3.6",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for searching weather information",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/search_weather",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)
