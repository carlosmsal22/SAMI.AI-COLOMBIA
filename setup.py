
from setuptools import setup, find_packages

setup(
    name='sami_colombia',
    version='1.0.0',
    description='Colombian market intelligence toolkit for government, retail, food, and more',
    author='SAMI.AI',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'geopandas',
        'requests',
        'scrapy',
        'plotly',
        'streamlit'
    ],
    python_requires='>=3.7'
)
