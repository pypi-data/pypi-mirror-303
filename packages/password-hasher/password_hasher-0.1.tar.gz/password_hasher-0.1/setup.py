from setuptools import setup, find_packages

setup(
    name='password_hasher',
    version='0.1',
    packages=find_packages(),
    description='A package for hashing and salting passwords.',
    author='Katsurameen',
    author_email='almawahib083@gmail.com',
    install_requires=[
        'bcrypt',
    ],
)
