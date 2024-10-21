from setuptools import setup

setup(
   name='rocket-pkg-mrkhaldi',
   version='1.0.0',
   author='KHALDI Mohamed Rafik',
   author_email='mr.khaldi@esi-sba.dz',
   packages=['rocket'],
   url='http://pypi.python.org/pypi/rocket/',
   license='LICENSE.txt',
   description='An awesome package that does something',
   long_description=open('README.md').read(),
   long_description_content_type="text/markdown",
   install_requires=['rocket']
)