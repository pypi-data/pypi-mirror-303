from setuptools import setup, find_packages

setup(
    name='sobjanta_api_package',
    version='0.21',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    author='Imran Nur',
    author_email='imrannur@techknowgram.com',
    description='A Python client for interacting with a specific API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
