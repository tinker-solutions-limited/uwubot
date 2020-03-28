#! /usr/bin/python3

from setuptools import setup
from shutil import copyfile
from setuptools.command.install import install
import os.path

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        if (not os.path.isfile("./.env")):
            print("creating .env")
            copyfile("./shadow.env", "./.env")

setup(name='uwubot',
    version='0.0.1',
    description='I am the bot of puwe cancew uwu',
    url='https://github.com/m3chanical/uwubot',
    author='m3chanical and friends',
    author_email='',
    license='UNLICENSED',
    packages=[],
    install_requires=['discord.py', 'python-dotenv'],
    cmdclass={
        'install': PostInstallCommand,
    },
    zip_safe=False,
)
