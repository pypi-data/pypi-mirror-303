from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        README = f.read()
    return README
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='playertracker',
  version='0.0.4',
  description='A playertracker that checks a code',
  long_description=readme(),
  long_description_content_type="text/markdown",
  url='',  
  author='Sate',
  author_email='sateywatey@proton.me',
  license='MIT', 
  classifiers=classifiers,
  keywords='playertracker', 
  packages=find_packages(),
  install_requires=['requests', 'datetime'] 
)