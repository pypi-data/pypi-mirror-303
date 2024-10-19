from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="twdownloader",
    version="0.2.3",  # Increment the version number
    author="hosseinam",
    author_email="hoss.rezaei98@gmail.com",
    description="A package for downloading from Telewebion",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=requirements,  # Add this line to include dependencies
)