from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='oripy',
  version='3.0.0',
  description='Orisyne is a powerful and flexible computation package designed to streamline complex operations in data processing. With an intuitive interface and robust performance, Orisyne enables developers to efficiently handle intricate calculations, making it an essential tool for advanced data manipulation and analysis.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Bluemon Cybersec',
  author_email='bluemoncybersec@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='oripy', 
  packages=['oripy'],
  package_data={'oripy': ['*.py']},
  install_requires=[
    'numpy',
    'pandas',
    'scikit-learn',
    'matplotlib'
  ] 
  )