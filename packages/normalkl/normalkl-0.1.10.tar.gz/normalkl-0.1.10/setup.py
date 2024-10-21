from setuptools import setup, find_packages

setup(
    name='normalkl',         # name of the package
    version='0.1.10',                     # version number
    description='A PyTorch package for computing KL divergences between normal distributions.',  # short description
    long_description=open('README.md').read(),  # detailed description (from README)
    long_description_content_type='text/markdown',
    author='Tycho van der Ouderaa',
    author_email='tychovdo@gmail.com',
    url='https://github.com/tychovdo/normal-kl',  # project URL
    license='MIT',
    packages=find_packages(),          # automatically finds your package
    install_requires=[
        'torch',                       # specify PyTorch as a dependency
        # other dependencies
    ],
    classifiers=[                      # optional classifiers
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',           # specify Python version compatibility
)
