from setuptools import setup, find_packages

setup(
    name='DriniChlor',
    version='0.0.3',
    author='Valdrin Beluli',  
    author_email='valdrinengineer@gmail.com',  
    description='An engineering tool for measurements and analyzes the necessary chlorine level for disinfecting water, depending on measured values for DO, temperature, and NTU.',  
    long_description=open('README.md').read(), 
    long_description_content_type='text/markdown',  
    url='https://github.com/ValdrinBeluli/DriniChlor', 
    packages=find_packages(),  
    classifiers=[
        'Programming Language :: Python :: 3',  
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',  
    ],
    python_requires='>=3.6',  
    install_requires=[  
        'matplotlib',
        'numpy',
        
    ],
)
