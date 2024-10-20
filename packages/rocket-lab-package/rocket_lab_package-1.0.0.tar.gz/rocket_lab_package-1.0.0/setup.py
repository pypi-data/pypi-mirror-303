from setuptools import setup

setup(
   name='rocket_lab_package',
   version='1.0.0',
   author='Guerinik Abderrahmane',
   author_email='ca.guerinik@esi-sba.dz',
   packages=['rocket_lab_package'],
   url='http://pypi.python.org/pypi/rocket/',
   license='LICENSE.txt',
   description='LAB package for academic learning purposes.',
   long_description=open('README.md').read(),
   long_description_content_type="text/markdown",
   install_requires=['rocket_lab_package']
)

