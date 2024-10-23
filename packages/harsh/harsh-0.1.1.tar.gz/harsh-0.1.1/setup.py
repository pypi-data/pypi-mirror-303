# setup.py
from setuptools import setup, find_packages

setup(
    name='harsh',
    version="0.1.1",
    description='Text Manipulation and Analysis Package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Jayesh Jain',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/harsh',  # Your GitHub repo
    packages=find_packages(),  # Automatically find the package folders
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)


