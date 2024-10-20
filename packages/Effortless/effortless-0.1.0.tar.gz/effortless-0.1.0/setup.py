# setup.py

from setuptools import setup, find_packages

setup(
    name="Effortless",
    version="0.1.0",
    packages=find_packages(),
    description="Databases should be Effortless.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bboonstra/Effortless",
    author="Ben Boonstra",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Natural Language :: English",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database :: Database Engines/Servers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
    ],
    python_requires=">=3.9",
    install_requires=[],
    keywords="database, effortless, simple storage, beginner, easy, db",
    project_urls={
        "Bug Tracker": "https://github.com/bboonstra/Effortless/issues",
        "Documentation": "https://github.com/bboonstra/Effortless",
        "Source Code": "https://github.com/bboonstra/Effortless",
    },
    include_package_data=True,
)
