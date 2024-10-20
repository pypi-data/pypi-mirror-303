from setuptools import setup, find_packages

setup(
    name='finance_calculator_kolya_super',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'finance_calculator=finance_calculator_kolya_super.__main__:main'
        ]
    },
    description='Krutoi packege',
    author='Nikolai',
    author_email='kolaleuhin@gmail.com'
)

