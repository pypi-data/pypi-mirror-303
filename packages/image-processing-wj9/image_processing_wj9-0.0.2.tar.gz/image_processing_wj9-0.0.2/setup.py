from setuptools import setup, find_packages

setup(
    name='image_processing_wj9',
    version='0.0.2',
    description='Biblioteca de processamento de imagens',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Wilson99',
    author_email='wilsonjusti16no@gmail.com',
    packages=find_packages(),
     install_requires=[
        'numpy',
        'scikit-image==0.18.3',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
