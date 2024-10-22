from setuptools import setup, find_packages

setup(
    name="abhi_scraper",  # Package name
    version="1.0.0",
    description="A Python package to scrape Flipkart product details",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Abhishek Kumar",
    author_email="your-email@example.com",
    url="https://github.com/your-github/flipkart_scraper",  # Replace with your GitHub URL
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
