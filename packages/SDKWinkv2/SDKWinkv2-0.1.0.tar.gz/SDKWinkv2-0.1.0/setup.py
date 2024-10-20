from setuptools import setup, find_packages

setup(
    name="SDKWinkv2",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="SDK for Wink Service to register, use and refill API request count",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/SDKWink",
    packages=find_packages(),  # Automatically finds all packages
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
