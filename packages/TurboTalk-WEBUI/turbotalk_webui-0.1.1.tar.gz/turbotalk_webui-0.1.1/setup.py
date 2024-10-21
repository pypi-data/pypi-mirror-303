from setuptools import setup, find_packages

setup(
    name='TurboTalk_WEBUI',
    version='0.1.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'g4f',  # Ensure to list all dependencies your app uses
    ],
)
 
