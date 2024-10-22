from setuptools import setup, find_packages
from os import rename, chmod
from os.path import join
from platform import system
from subprocess import call
from setuptools.command.install import install

version = "0.1.4"
with open("README.md") as readme:
    long_description = readme.read()


class CustomInstallCommand(install):
    def run(self):
        match system():
            case 'Windows':
                call(['pyinstaller', '--onefile', 'ftp_brute_force/ftp_brute_force.py'])
                scripts_dir = join(self.install_scripts, 'ftp_brute_force.exe')
                rename('dist/ftp_brute.exe', scripts_dir)

            case 'Linux' | 'Darwin':
                call(['pyinstaller', '--onefile', 'ftp_brute_force/ftp_brute_force.py'])
                scripts_dir = join(self.install_scripts, 'ftp_brute_force')
                rename('dist/ftp_brute', scripts_dir)
                chmod(scripts_dir, 0o755)

        install.run(self)


setup(
    name="ftp_brute",
    version=version,
    author="Jackson Ja",
    author_email="jackson2937703346@163.com",
    description="A FTP brute force tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacksonjapy/ftp_brute_force",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[],
)
