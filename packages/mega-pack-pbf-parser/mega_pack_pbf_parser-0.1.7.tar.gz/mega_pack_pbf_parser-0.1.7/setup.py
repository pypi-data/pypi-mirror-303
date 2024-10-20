from setuptools import setup, find_packages

setup(
    name='mega_pack_pbf_parser', 
    version='0.1.7',
    author='John Nastala',  
    description='Collects song information from BB Projects',
    long_description=open("README.md").read(),
    long_description_content_type='text/plain',
    url='https://github.com/rjcannizzo/mega-pack-pbf-parser',
    packages=find_packages(),
    include_package_data=True,    
)





