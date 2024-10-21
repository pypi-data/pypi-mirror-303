from setuptools import setup, find_packages

setup(
    name="unique_id_package",  # The name of your package
    version="0.2.0",
    description="A package to generate unique IDs",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Abhishek Kumar",
    author_email="your-email@example.com",
    url="https://github.com/your-github/unique_id_package",  # Update with your GitHub URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
