from setuptools import setup, find_packages

setup(
    name="APIWinkSDK",
    version="0.1.1",
    author="Your Name",
    author_email="your.email@example.com",
    description="SDK for APIWink Service to register, use and refill API request count",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/APIWinkSDK",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
