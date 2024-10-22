from setuptools import setup, find_packages

setup(
    name='pybinlist', 
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Junaid Rahman',  
    author_email='jhackur445@gmail.com',  
    description='A Python Wrapper for BIN lookup using the Binlist API',
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown',
    url='https://github.com/Junaid433/pybinlist', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
