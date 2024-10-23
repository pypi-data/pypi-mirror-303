from setuptools import setup, find_packages

setup(
    name='taxcore',
    version='0.1.3',
    description='A comprehensive technical analysis library for Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YavuzAkbay/taxcorelib',
    author='Yavuz',
    author_email='akbay.yavuz@example.com',
    license='GPLv3',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
