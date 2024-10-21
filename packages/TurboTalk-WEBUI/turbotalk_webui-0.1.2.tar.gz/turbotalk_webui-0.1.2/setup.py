from setuptools import setup, find_packages

setup(
    name='TurboTalk_WEBUI',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'Flask',          # Add any other dependencies you have
        'g4f'             # Replace with actual dependency names
    ],
    entry_points={
        'console_scripts': [
            'TurboTalk_WEBUI = TurboTalk_WEBUI:main',  # Adjust if you have a main function
        ],
    },
)
