from setuptools import setup, find_packages

setup(
    name='medvoice-ai',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],  # Add project dependencies here
    author='arken80',
    description='A package for MedVoice AI project',
    url='https://github.com/arken80/MediVoice-AI',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)