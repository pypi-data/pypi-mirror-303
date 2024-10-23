from setuptools import setup, find_packages

version = '0.1.0'

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flask_header_log_request_id',
    version=version,
    author='Shatru',
    author_email='shatrugnakorukanti@gmail.com',
    description='Python Flask Middleware to log and set Request ID in the HTTP header',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Shatrugna-Strife/flask-header-log-request-id',
    license='MIT',
    install_requires=[
        'Flask',
    ],
    packages=find_packages(exclude=['tests']),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)