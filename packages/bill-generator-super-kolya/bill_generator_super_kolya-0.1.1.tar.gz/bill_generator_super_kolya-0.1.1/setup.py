from setuptools import setup, find_packages

setup(
    name='bill_generator_super_kolya',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'bill_generator=bill_generator_super_kolya.__main__:main'
        ]
    },
    description='Krutoi packege',
    author='Nikolai',
    author_email='kolaleuhin@gmail.com'
)

