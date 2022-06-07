from os import path as os_path
from setuptools import setup, find_packages
this_directory = os_path.abspath(os_path.dirname(__file__))


def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]

setup(
    name='sparse_lut',
    python_requires='>=3.7.0', # python version
    version= '1.0.0', # package version
    description="Sparse Look-Up-Table",  # introduction, displayed on PyPI
    long_description=read_file('README.PyPI.md'), # Readme
    long_description_content_type="text/markdown",  # markdown
    author="Bowen XU",
    author_email='xubowen@pku.edu.cn',
    url='https://github.com/bowen-xu/SparseLUT',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'), 
    include_package_data=True,
    # package_data={
    #     '': ['*.txt'], 
        # '': ['*.json', '*.lark', '*.txt'], 
        # 'pynars.utils.SparseLUT': ['*.pyd', '*.pyi'], 
        # },
    license="MIT",
    keywords=['SparseLUT', 'Sparse', 'Look-Up Table'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
)