from setuptools import setup, find_packages

setup(
    name='reqease',
    version='0.1.1',
    description='Reqease is a lean and clean library for performing basic HTTP operations with minimal overhead, designed to simplify common tasks like GET and POST requests',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DanielRodriguez-SS/reqease.git',
    author='Daniel Rodriguez',
    author_email='danielrodriguezmarin@me.com',
    license='MIT',
    packages=find_packages(),  # Automatically finds subpackages
    install_requires=[
        'certifi',
    ],  # List of dependencies
    classifiers=[  # Classifiers for PyPI
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)