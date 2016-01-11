from setuptools import setup

setup(
    name='troposphere_sugar',
    version='0.0.1',
    description='Common utilities on top of troposphere and boto for ease of clouformation template creation',
    author='Enric Lluelles',
    author_email='enric@lluel.es',
    packages=['troposphere_sugar'],
    install_requires=['troposphere>=2.0.0']
)