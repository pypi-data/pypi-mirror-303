from setuptools import setup, find_packages

setup(
    name="LS5",  # Package name
    version="0.1.3",  # Package version
    description="A web scraping tool using Selenium for scraping connections, profiles, posts, chats and applications.",
    long_description=open('README.md').read(),  # Pulls from README.md (make sure you have one)
    long_description_content_type='text/markdown',  # Ensures markdown rendering on PyPI
    url="https://github.com/DeadmanXXXII/Scraped",  # GitHub repo URL
    author="Deadman",
    author_email="themadhattersplayground@gmail.com",  # Your email
    license="MIT",  # License type
    packages=find_packages(),  # Automatically finds package folders
    install_requires=[
        "selenium==4.10.0",
        "webdriver-manager==3.8.6",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10.0",  # Minimum Python version
)
