import setuptools

from dj_db_conn_pool import (
    __version__,
    __author__,
    __author_email__,
    __description__
)

if __name__ == '__main__':
    setuptools.setup(
        name='django-db-connection-pool',
        license='MIT',
        version=__version__,
        description=__description__,
        long_description=open('README.md').read(),
        author=__author__,
        author_email=__author_email__,
        url='https://github.com/altairbow/django-db-connection-pool',
        download_url='https://pypi.python.org/pypi/django-db-connection-pool/',
        packages=setuptools.find_packages(),
        include_package_data=True,
        install_requires=[
            'SQLAlchemy>=1.2.15'
        ],
        classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Topic :: Software Development :: Libraries :: Python Modules',
        ],
        keywords=['django', 'db', 'database', 'persistent', 'connection', 'pool'],
    )
