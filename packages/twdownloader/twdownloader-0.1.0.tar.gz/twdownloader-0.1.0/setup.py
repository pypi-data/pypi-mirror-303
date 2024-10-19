from setuptools import setup, find_packages

setup(
    name="twdownloader",                  # Package name
    version="0.1.0",                          # Package version
    author="hosseinam",                       # Your name
    author_email="hoss.rezaei98@gmail.com",    # Your email
    description="A package",  # Short description
    long_description=open("README.md").read(), # Long description (from README)
    long_description_content_type="text/markdown",  # README format
    packages=find_packages(),                 # Automatically find package directories
    classifiers=[                             # Classifiers for PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",                  # Python version requirement
)
