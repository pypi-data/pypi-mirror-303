from setuptools import setup, find_packages

setup(
    name='ipakyuli',
    version='0.1.0',
    description='A brief description',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Bank Transaction',
    author_email='islomjon2702@gmail.com',
    url='https://github.com/islombeknv/ipakyulibank.git',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose your license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
