from setuptools import setup, find_packages

setup(
    name='heat_transfer_calculator',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/AmirGuliyev/Heat_transfer_calculator',
    license='MIT',
    author='KusmasVinya',
    author_email='guliyevamir@yahoo.com',
    description='A basic heat transfer calculator for undergraduate textbook problems',
    install_requires=['numpy', 'fluidprop'],
)