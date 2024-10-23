from setuptools import setup, find_packages
import codecs

with codecs.open('README.md', 'r', 'utf-8') as f:
    long_description = f.read()

setup(
    name='gpulr',
    version='1.9',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    entry_points={
        'console_scripts': [
            'gpu-script=GPU.script:main',  # Remplacez 'GPU.script:main' par le chemin vers votre fonction principale
        ],
    },
    author='DOYON Paulin',
    author_email='contact@paulinodoyn.fr',
    description='Module pour gérer les connexions et récupérer des informations depuis le site GPU',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Paulin17/GPU_Python_Module',  # Remplacez par l'URL de votre repository
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)