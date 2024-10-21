from setuptools import setup, find_packages

setup(
    name='TurboTalk_WEBUI',
    version='0.1.4',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'g4f',  # Replace with actual dependency names
    ],
    entry_points={
        'console_scripts': [
            'TurboTalk_WEBUI = TurboTalk_WEBUI:main',
        ],
    },
)
