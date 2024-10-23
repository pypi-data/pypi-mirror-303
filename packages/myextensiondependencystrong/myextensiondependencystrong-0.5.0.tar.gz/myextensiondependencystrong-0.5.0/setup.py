from setuptools import setup, find_packages

setup(
    name='myextensiondependencystrong',
    version='0.5.0',
    description='A simple example package',
    author='Erdi Aktan',
    author_email='erdiaktan@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
