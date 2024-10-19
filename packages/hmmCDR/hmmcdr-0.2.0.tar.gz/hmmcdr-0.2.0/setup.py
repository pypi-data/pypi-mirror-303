from setuptools import setup, find_packages

setup(
    name='hmmCDR',
    version='0.2.0',
    description="Find CDR locations using bedmethyl file and CenSat annotations. (REQUIRES BEDTOOLS INSTALLED)",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/jmenendez98/hmmCDR",
    author='Julian Menendez',
    author_email='jmmenend@ucsc.edu',
    license="MIT",
    packages=find_packages(),
    project_urls={
        'GitHub': 'https://github.com/jmenendez98/hmmCDR',
        'Lab Website': 'https://migalab.com/',
    },
    install_requires=[
        'numpy>=1.21.5',
        'pandas>=1.3.5',
        'pybedtools>=0.8.1',
        'hmmlearn>=0.3.0',
    ],
    entry_points={
        'console_scripts': [
            'hmmCDR=hmmCDR.hmmCDR:main',
            'find_priors=hmmCDR.find_priors:main',
            'profile_plot=hmmCDR.profile_plot:main',
        ]
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)