from setuptools import setup, find_packages

setup(
    name='online-store',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'online-store=online_store.__main__:main_menu',
        ],
    },
)
