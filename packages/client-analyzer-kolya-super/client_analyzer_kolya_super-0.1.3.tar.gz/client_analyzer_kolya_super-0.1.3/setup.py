from setuptools import setup, find_packages

setup(
    name='client_analyzer_kolya_super',
    version='0.1.3',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'client_analyzer=client_analyzer_kolya_super.__main__:main'
        ]
    },
    description='Krutoi packege',
    author='Nikolai',
    author_email='kolaleuhin@gmail.com'
)

