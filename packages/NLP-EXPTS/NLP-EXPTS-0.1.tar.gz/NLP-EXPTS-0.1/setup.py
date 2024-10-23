import os
import pprint
from setuptools import setup, find_packages

# Define the setup parameters
setup(
    name="NLP-EXPTS",
    version="0.1",
    description="NLP Expts",
    author="Ishannaik",
    author_email="ishannaik7@gmail.com",
    packages=find_packages(),
    package_data={
        "NLP-EXPTS": ["*.pdf", "*.py"],
    },  # Include all files in the CC_EXPTS package
)


# pypi-AgEIcHlwaS5vcmcCJDI0YjYyYWEzLWZlZWEtNDA1Ny04ZGNiLWQ2NDBkOTI3M2NmOQACEFsxLFsiY2MtZXhwdHMiXV0AAixbMixbIjExNGU1NzMwLTllOWQtNDM1Yi1hY2JkLTM1NDI2N2IwMDJlZCJdXQAABiD2dwrhdAyftapd4whYrkELAlaEAREg9c974gq1nEXOqQ
