from setuptools import setup, find_packages

setup(
    name='frshodan',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4',
    ],
    author='Thomas Haddad',
    author_email='haddad.thomas19@gmail.com',
    description='A library for querying Shodan IP addresses with no API key.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LavedenC1/frshodan',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'frshodan=frshodan.frshodan_cmd:main',
        ],
    },
)
