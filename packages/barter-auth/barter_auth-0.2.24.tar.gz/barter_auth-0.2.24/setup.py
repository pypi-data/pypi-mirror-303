

import os

from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


setup(
    name='barter-auth',
    version='0.2.24',
    include_package_data=True,
    license='BSD',
    description='Django bulk admin enables you to bulk add, bulk edit, bulk upload and bulk select in django admin.',
    long_description=README,
    long_description_content_type='text/markdown',
    url='https://github.com/kabilovtoha/barter_auth',
    author='akatoha',
    author_email='kabilov2011@gmail.com',
    install_requires=[
        'Django>=3.2',
        'six>=1.15.0',
        'pydantic-settings>=2.1.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',

        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)