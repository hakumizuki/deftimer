from setuptools import setup, find_packages
import pathlib


# Get the long description from the README file
here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='deftimer',
    version='0.0.3',
    description='A very simple Python tool for process inspection and timer. (alpha)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hakumizuki/deftimer',
    author='Taichi Masuyama',
    author_email='montanha.masu536@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    keywords='python, algorithms, timer, tools',
    package_dir={'': 'deftimer'},
    packages=find_packages(where='deftimer'),
    python_requires='>=3.6, <4',
    install_requires=['pathlib==1.0.1'],
    extras_require={
        'dev': [],
        'test': ['flake8'],
    },
    project_urls={
        'Bug Reports': 'https://github.com/hakumizuki/deftimer/issues',
        'Source': 'https://github.com/hakumizuki/deftimer/',
    },
)
