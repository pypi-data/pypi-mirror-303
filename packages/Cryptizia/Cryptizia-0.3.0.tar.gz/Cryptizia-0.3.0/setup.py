from setuptools import setup, find_packages

setup(
    name='Cryptizia',
    version='0.3.0',
    author='Zia Ur Rehman',
    author_email='engrziaurrehman.kicsit@gmail.com',  # Replace with your email
    description='A Python library for various cipher techniques including the Caesar cipher and Playfair cipher examples.',
    long_description=open('README.md').read(),  # Assumes you have a README.md file
    long_description_content_type='text/markdown',
    # url='https://github.com/your_username/cryptizia',  # Replace with your GitHub repository URL
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'termcolor',  # List your library dependencies here
    ],
)
