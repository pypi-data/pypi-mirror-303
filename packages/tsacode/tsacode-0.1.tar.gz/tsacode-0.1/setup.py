from setuptools import setup, find_packages

setup(
    name='tsacode',  # Package name
    version='0.1',  # Version number
    packages=find_packages(),  # Automatically find all packages
    description='A simple package for TSA Practical',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',  # To use Markdown for README
    author='Alb Tech',
    author_email='albtech.in@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
