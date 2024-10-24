from setuptools import setup, find_packages

setup(
    name="omnicrawlers",  # Replace with your library's name
    version="0.1.0",
    author="Vinayak Pratap",
    author_email="Vinayakpratap606@gmail.com",
    description="A Python library for crawling LinkedIn and GitHub profiles.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/your_library_name",  # Your GitHub repo link
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List any external dependencies here, e.g.:
        "requests",
        "bs4",
        "selenium",
        "webdriver_manager",

    ],

)
