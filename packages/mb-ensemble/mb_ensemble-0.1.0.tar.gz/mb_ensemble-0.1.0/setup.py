from setuptools import setup, find_packages

setup(
    name='mb_ensemble',  # Replace with your package name
    version='0.1.0',          # Version of your package
    author='Neel Iyer',       # Your name
    author_email='neeliyer14@gmail.com',  # Your email
    description='A library for analyzing media bias through NLP metrics.',
    long_description=open('README.md').read(),  # Long description from README
    long_description_content_type='text/markdown',
    packages=find_packages(),  # Automatically find packages in your project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose the appropriate license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
    install_requires=[          # List of dependencies
        'textblob',
        'vaderSentiment',
        'textstat',
        'matplotlib',
        'nltk',      # Use readability-lxml instead of readability
    ],
)
