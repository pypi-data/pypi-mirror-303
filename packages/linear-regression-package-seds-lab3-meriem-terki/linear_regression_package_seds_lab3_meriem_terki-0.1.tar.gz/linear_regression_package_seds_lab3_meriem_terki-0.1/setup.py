from setuptools import setup, find_packages

setup(
    name="linear_regression_package_seds_lab3_meriem_terki",
    version="0.1",
    packages=find_packages(),
    install_requires=['numpy'],
    author="Meriem Terki",
    author_email="m.terki@esi.dz",
    description="A simple linear regression model implemented from scratch",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
