from setuptools import setup

setup(
   name='rocket-1.1.1',
   version='1.0.0',
   author='ha115',
   author_email='h.benghenima@esi-sba.dz',
   packages=['rocket'],
   url='http://pypi.python.org/pypi/rocket/',
   license='LICENSE.txt',
   description='An awesome package that does something',
   long_description=open('README.md').read(),
   long_description_content_type="text/markdown",
   install_requires=['rocket']
)