from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='pyshooter2d',
    version='0.0.2',
    description='A package for easier and faster development of 2d shooters with pygame',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Freddy Frolov',
    author_email='freddyfrolov383@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords='shooter engine',
    packages=find_packages(),
    install_requiers=['pygame', 'math']
)