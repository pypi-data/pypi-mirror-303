from setuptools import setup, find_packages  # Importing functions from setuptools: `setup` handles package info, `find_packages` automatically discovers all packages/subpackages.

setup(
    name='BazaarWrapper',  # The name of your package on PyPI. This must be unique and not already taken.
    
    version='0.0.1',  # The current version of your package. Follow semantic versioning (Major.Minor.Patch).
    
    packages=find_packages(),  # Automatically find all packages inside your project directory.
    
    install_requires=['requests'],  # List dependencies here.
    
    description='My personal Wrapper package for Hypixel Skyblock Bazaar',  # A short description of what your package does.
    
    long_description=open('README.md').read(),  # This provides a detailed description, typically from the README file.
    
    long_description_content_type='text/markdown',  # Specify the format of the long description (e.g., Markdown, reStructuredText).
    
    url='https://github.com/Mrmii321/SoapBazaarWrapper',  # The URL to the homepage of your project (e.g., GitHub repo).
    
    author='soapchan',  # Your name, the package author.
    
    author_email='noahfoxgaming@gmail.com',  # Your contact email address.
    
    license='MIT',  # The license for your package (e.g., MIT, GPL, Apache).
    
    python_requires='>=3.6',  # Ensure compatibility with specific Python versions.
)
