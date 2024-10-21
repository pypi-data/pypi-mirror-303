from setuptools import setup, find_packages

setup(
    name='typers',
    version='0.1.0',
    author='Sébastien GARCIA',
    author_email='sebastien.works@outlook.com',
    description='A utility package for performing various validation checks on values.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/striatp/typers',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)