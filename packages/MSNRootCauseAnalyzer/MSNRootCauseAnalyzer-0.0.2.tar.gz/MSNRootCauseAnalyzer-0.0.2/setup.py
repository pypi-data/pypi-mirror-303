from setuptools import setup, find_packages

setup(
    name='MSNRootCauseAnalyzer',
    version='0.0.2',
    author='MSN CSDATA',
    author_email='yankunwang@microsoft.com',
    description='A Python library for root cause analysis',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        # dependencies
        'numpy>=1.21.0',
        'pandas>=1.3.0'
    ],
)
