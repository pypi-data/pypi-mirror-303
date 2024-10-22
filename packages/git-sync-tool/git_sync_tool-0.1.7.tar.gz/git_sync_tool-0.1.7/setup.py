from setuptools import setup, find_packages

setup(
    name='git_sync_tool',
    version='0.1.7',
    description='Easily sync repos across devices',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license="The Unlicense",
    author='Miguel Flores-Acton',
    author_email='mfacton1@gmail.com',
    url='https://github.com/mfacton/git-sync-tool',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'colorama',
        'prettytable',
        'tqdm',
        'gitpython',
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Utilities",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'gsync=git_sync.main:main',
        ],
    },
)
