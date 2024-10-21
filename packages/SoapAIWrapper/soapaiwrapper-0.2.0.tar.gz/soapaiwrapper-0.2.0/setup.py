from setuptools import setup, find_packages  # Importing functions from setuptools: `setup` handles package info, `find_packages` automatically discovers all packages/subpackages.

setup(
    name='SoapAIWrapper',  # The name of your package on PyPI. This must be unique and not already taken.
    
    version='0.2.0',  # The current version of your package. Follow semantic versioning (Major.Minor.Patch).
    
    packages=find_packages(),  # Automatically find all packages inside your project directory.
    
    install_requires=['openai'],  # List dependencies here. For example: ['numpy', 'requests']. Empty if no dependencies.
    
    description='My personal OpenAI Wrapper',  # A short description of what your package does.
    
    long_description=open('README.md').read(),  # This provides a detailed description, typically from the README file.
    
    long_description_content_type='text/markdown',  # Specify the format of the long description (e.g., Markdown, reStructuredText).
    
    url='https://github.com/Mrmii321/soapAiWrapper',  # The URL to the homepage of your project (e.g., GitHub repo).
    
    author='soapchan',  # Your name, the package author.
    
    author_email='noahfoxgaming@gmail.com',  # Your contact email address.
    
    license='MIT',  # The license for your package (e.g., MIT, GPL, Apache). Ensure you include a `LICENSE` file.
)
