from setuptools import setup, find_packages

setup(
    name="rufus_crawler",  # Name of your package on PyPI
    version="0.1.1",
    description="A web crawler and content filtering tool using OpenAI.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Amanul Rahiman Attar",
    author_email="attar.aman29@gmail.com",
    url="https://github.com/amanattar/rufus_crawler",  # Your GitHub repo URL
    license="MIT",
    packages=find_packages(),  # This will automatically find 'rufus' and other packages
    include_package_data=True,  # Include non-Python files (README, LICENSE, etc.)
    install_requires=[
        "beautifulsoup4",
        "requests",
        "openai",
        "selenium",
        "webdriver-manager",
        "PyYAML"
    ],
    entry_points={
        'console_scripts': [
            'rufus_crawler=scripts.run_rufus:main',  # Command-line entry point
        ]
    },
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
