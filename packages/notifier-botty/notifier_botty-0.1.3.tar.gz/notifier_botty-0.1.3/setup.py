from setuptools import setup, find_packages

setup(
    name="notifier_botty",  # Package name
    version="0.1.3",  # Initial version
    packages=find_packages(),
    install_requires=[
        "selenium",  # List dependencies here
        "pytz",
        "requests",
    ],
    description="A package for automating experts login and notifications",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Dharshan",
    author_email="dharshanspn@mail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
