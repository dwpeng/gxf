from setuptools import setup
from setuptools import find_packages

__version__ = '0.0.1'
__author__ = 'dwpeng'
__email__ = '1732889554@qq.com'

with open('README.md', 'r') as fp:
    readme = fp.read()

setup(
    name='gxf',
    version=__version__,
    author=__author__,
    author_email=__email__,
    maintainer=__author__,
    maintainer_email=__email__,
    description='A first gtf/gff parser.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/dwpeng/gxf',
    keyword='GFF',
    packages=find_packages(),
    install_requires=[
        'pandas',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ]
)


print(find_packages())
