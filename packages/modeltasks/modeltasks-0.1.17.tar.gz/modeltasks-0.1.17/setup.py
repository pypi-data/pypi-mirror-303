import os
from setuptools import setup, find_packages


if os.environ.get('CI_COMMIT_TAG'):
    version = os.environ['CI_COMMIT_TAG'].replace('v', '').replace('-release', '')
else:
    version = os.environ.get('CI_JOB_ID')

setup(
    name='modeltasks',
    packages=find_packages(exclude=['tests', 'examples']),
    version=version,
    license='MIT',
    description='A lightweight workflow management system and task graph',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author=os.environ.get('SETUP_PACKAGE_AUTHOR', ''),
    author_email=os.environ.get('SETUP_PACKAGE_EMAIL', ''),
    url=os.environ.get('CI_PROJECT_URL', ''),
    keywords=[
        'Tasks',
        'Model',
        'DAG',
        'Graph',
        'Model',
        'Processing',
        'Workflow management'
    ],
    install_requires=[
        'networkx',
        'matplotlib',
        'python-dotenv'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
    ]
)
