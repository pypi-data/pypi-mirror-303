import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(
    name='corona-bluexpress-logistica',
    version='1.5.12',
    packages=['bluexpress'],
    description='Django Bluexpress Integration',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Corona Development Team',
    author_email='rolguin@corona.cl',
    url='https://gitlab.com/linets-projects/python-libraries/django-bluexpress/',
    license='MIT',
    python_requires=">=3.7",
    install_requires=[
        'Django>=3',
        'zeep>=4.0.0',
        'xmltodict==0.12.0',
        'requests>=2.25.1'
    ]
)
