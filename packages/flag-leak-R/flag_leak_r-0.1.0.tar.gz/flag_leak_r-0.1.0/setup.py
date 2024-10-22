from setuptools import setup, find_packages

setup(
    name="flag_leak_R",  # Your package name
    version="0.1.0",  # Initial version
    author="Your Name",
    author_email="your_email@example.com",
    description="Leaking environment variables via HTTP requests",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    py_modules=["flag"],
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
