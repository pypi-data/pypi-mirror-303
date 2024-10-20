# setup.py

from setuptools import setup, find_packages

setup(
    name='pyotp_generator',
    version='0.1.0',
    author='Katsurameen',
    author_email='almawahib083@example.com',
    description='A simple OTP generator using pyotp',
    packages=find_packages(),
    install_requires=[
        'pyotp',
    ],
    entry_points={
        'console_scripts': [
            'otp-generator=pyotp_generator.main:main', 
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
