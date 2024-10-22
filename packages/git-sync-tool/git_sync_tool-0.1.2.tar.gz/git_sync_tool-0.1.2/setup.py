from setuptools import setup, find_packages

setup(
    name='git_sync_tool',
    version='0.1.2',
    description='Easily sync repos across devices',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Miguel Flores-Acton',
    author_email='mfacton1@gmail.com',
    url='https://github.com/mfacton/git-sync-tool',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'prettytable',
        'tqdm',
        'gitpython',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'gsync=gsync:main',
        ],
    },
)
