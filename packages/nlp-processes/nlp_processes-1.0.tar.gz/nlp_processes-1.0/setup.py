from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys

class PostInstallCommand(install):
    """Post-installation for installing spacy language model"""
    def run(self):
        install.run(self)
        # Ensure spacy is installed before downloading the model
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "spacy"])
        except subprocess.CalledProcessError:
            print("Failed to install SpaCy")
        subprocess.check_call([sys.executable, "-m", "spacy", "download", "en_core_web_trf"])

setup(
    name='nlp_processes',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'spacy>=3.0.0',
        'matplotlib',
        'spacy_cleaner',
        'tqdm'
    ],
    author='Sina Heydari',
    author_email='sinaa.heydari.76@gmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.10, <3.11',
    cmdclass={
        'install': PostInstallCommand,
    }
)

