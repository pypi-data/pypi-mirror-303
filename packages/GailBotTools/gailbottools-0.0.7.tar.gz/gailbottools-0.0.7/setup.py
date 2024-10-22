from setuptools import setup, find_packages

setup(
    name='GailBotTools',  
    version='0.0.7', 
    author='HiLab', 
    author_email='hil@elist.tufts.edu',  
    description='A set of tools for handling data to create GailBot plugins',  
    long_description=open('README.md').read(),  
    long_description_content_type='text/markdown', 
    url='https://github.com/GailBot-System/GailBotPlugins',  
    packages=find_packages(),  
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
    install_requires=[
        'lxml',
        'gailbot',
        'pydantic==1.10.9',
        'toml',
        'six',
        'pyannote.core',
        'google',
        'dict-to-dataclass',
    ],
    extra_require={
        'whisperx': ['git+https://github.com/m-bain/whisperx.git'],
    }
)
