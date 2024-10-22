from setuptools import setup

setup(
    name='tsb_encoder_decoder',
    version='1.0.4',
    description='Encodes and decodes TSB messages',
    long_description=open('README.md', 'r').read(),
    author='cristophvigneri',
    author_email='cristophvigneri@gmail.com',
    packages=['tsb_encoder_decoder'],
    install_requires=['cobs', 'crcmod'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)