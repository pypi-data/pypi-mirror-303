from setuptools import setup, find_packages

setup(
    name='midlab',
    version='0.4.0',
    packages=find_packages(),
    description='For Lab',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Malik Talha',
    author_email='mtnaqshbandi2003@gmail.com',
    url='https://github.com/MalikTalha03/midlab',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
