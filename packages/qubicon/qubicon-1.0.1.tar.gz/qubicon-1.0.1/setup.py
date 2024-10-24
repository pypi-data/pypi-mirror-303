from setuptools import setup, find_packages

setup(
    name='qubicon',
    version='1.0.1',
    description='Python library for the Qubicon Platform API',
    author='Stephan Karas',
    author_email='stephan.karas@qubicon-ag.com',
    url='https://git.qub-lab.io/qub-client/qubicon-python-library',
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        'requests>=2.25.1',
        'rapidfuzz>=2.0.11',
        'pandas>=2.1.1',
        'tabulate>=0.9.0',
        'rich>=13.5.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
