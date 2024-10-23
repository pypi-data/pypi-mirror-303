from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11'
]

setup(
    name='MayLeaSports',
    version='0.0.1',
    description='Pakcage for sports teams and leagues',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Sam Johnson',
    author_email='samjj02@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=[],
)