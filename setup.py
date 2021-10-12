from setuptools import find_packages, setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='arcgis_clustering',
    package_dir={"": "src"},
    packages=find_packages('src'),
    version='0.0.0',
    description='Demographic clutering using ArcGIS Business Analyst data.',
    long_description=long_description,
    author='Joel McCune',
    license='Apache 2.0',
)
