from setuptools import setup, find_packages

setup(
    name='upycli',
    version='0.2.10',
    packages=find_packages(),
    
    # Descriptions
    description='A microscopic library to turn any function into a CLI.',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    
    # Details
    maintainer="Alisamar Husian",
    maintainer_email="zrthxn@gmail.com",
    url="https://github.com/zrthxn/uPyCLI",
    
    # CLI
    entry_points = {
        'console_scripts': ['ucli=upycli:ucli'],
    }
)
