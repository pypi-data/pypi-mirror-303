# setup.py
from setuptools import setup, find_packages

setup(
    name='xasdesvid',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'pymorphy2',
    ],
    description='Библиотека для определения вида связи в словосочетаниях.',
    author='XasdesNew',
    author_email='nikakovnikak574@gmail.com',
    url='https://github.com/XasdesST/xasdesvid',  # Укажите URL вашего репозитория
)
