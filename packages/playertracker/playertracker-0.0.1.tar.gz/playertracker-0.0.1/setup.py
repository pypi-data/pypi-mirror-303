from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='playertracker',
  version='0.0.1',
  description='A playertracker that checks a code',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Sate',
  author_email='sateywatey@proton.me',
  license='MIT', 
  classifiers=classifiers,
  keywords='playertracker', 
  packages=find_packages(),
  install_requires=['requests', 'datetime'] 
)