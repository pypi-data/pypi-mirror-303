import os
import pprint
from setuptools import setup, find_packages

# Define the setup parameters
setup(
    name="NLP-EXPTS",
    version="0.3",
    description="NLP Expts",
    author="Ishannaik",
    author_email="ishannaik7@gmail.com",
    packages=find_packages(),
    package_data={
        "NLP-EXPTS": ["*.pdf", "*.py", ".docx"],
    },  # Include all files in the CC_EXPTS package
)


# pypi-AgEIcHlwaS5vcmcCJDYyNzAyODU1LWZhMWEtNDFjNy1hN2RjLWE2MWJjNTJkYWUzOAACKlszLCIyNjYzYmUxNy00ZWZkLTRhZjAtOGY5Yy1lM2I4Y2M2OTNiZmMiXQAABiBJbpr91ty6nq70V6hXy9aL_kO1BO7Kw0OJvDUE7T8pVQ
