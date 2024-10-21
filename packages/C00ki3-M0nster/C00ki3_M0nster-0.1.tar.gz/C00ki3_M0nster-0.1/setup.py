from setuptools import setup, find_packages

setup(
    name='C00ki3_M0nster',  # Package name
    version='0.1',          # Package version
    description='A tool for extracting and analyzing cookies and tokens from websites',
    long_description=open('README.md').read(),  # Long description from README file
    long_description_content_type='text/markdown',
    author='DeadmanXXXII',   # Updated author name
    author_email='themadhattersplayground@gmail.com',  # Updated author email
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        'requests==2.28.2',
        'beautifulsoup4==4.12.2',
        'base64',  # Added base64 to dependencies
    ],
    entry_points={
        'console_scripts': [
            'cookie-monster=Cookie_Monster:main',  # Entry point for command line
        ],
    },
    url='https://github.com/DeadmanXXXII/Cookie_Monster',  # Your repo URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version
)
