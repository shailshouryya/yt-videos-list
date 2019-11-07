# https://test.pypi.org/pypi?%3Aaction=list_classifiers
from setuptools import setup, find_packages

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='yt_videos_list',
    version='0.2.01',
    description='Python package to extract YouTube video titles and URLs for a specific channel',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Shail-Shouryya/yt_videos_list',
    author='Shail-Shouryya',
    author_email='tbd@gmail.com',
    license='Apache License 2.0',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Free for non-commercial use',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Database :: Front-Ends',
        'Topic :: Home Automation',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Multimedia :: Video',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    
    keywords='YoutTube videos URL scraping automation',
    
    packages=find_packages(),
#    packages=find_packages(),
    
#    package_dir={'':'src'},
    
    python_requires='>=3.6.*, <4',
    
    install_requires=['selenium>=3.141.0'],  # Optional
    # https://packaging.python.org/discussions/install-requires-vs-requirements/
    
    # If there are data files included in your packages that need to be
    # installed, specify them here.
    #
    # If using Python 2.6 or earlier, then these have to be included in
    # MANIFEST.in as well.
    package_data={  # Optional
        # 'sample': ['package_data.dat'],
    },
    
    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    #
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional

    
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # `pip` to create the appropriate form of executable for the target
    # platform.
    #
    # For example, the following would provide a command called `yt_videos_list` which
    # executes the function `script` from this package when invoked:
#    entry_points={  # Optional
#        'console_scripts': [
#            'sample=yt_videos_list:script',
#        ],
#    },
    
    project_urls={
        'Source': 'https://github.com/Shail-Shouryya/yt_videos_list',
    },
)
