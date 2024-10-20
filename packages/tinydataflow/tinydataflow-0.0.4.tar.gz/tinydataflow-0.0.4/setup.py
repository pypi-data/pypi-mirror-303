# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


from setuptools import setup
from setuptools import find_packages

from tinydataflow import __version__
    
def parse_requirements(filename):
    with open(filename, encoding='utf-16') as f:
        return f.read().splitlines()

setup(name='tinydataflow',
    version=__version__,
    license='MIT',
    author='Ismael Nascimento',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author_email='ismaelnjr@icloud.com.br',
    keywords='data flow transformation pipeline',
    description=u'biblioteca Python simples e extensível que facilita a criação e execução de pipelines de transformação de dados e automação de processos',
    url='https://github.com/ismaelnjr/tinyflow-project.git',
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    install_requires=parse_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)


