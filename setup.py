from setuptools import setup
from setuptools import find_packages

version = __import__('pelican_vimeo').__version__
download_url = 'https://github.com/looprock/pelican_slideshare/archive/{}.zip'.format(version)

setup(name='pelican_slideshare',
      version=version,
      url='https://github.com/kura/pelican_slideshare',
      download_url=download_url,
      author="Douglas Land",
      author_email="dsl@looprock.com",
      maintainer="Douglas Land",
      maintainer_email="dsl@looprock.com",
      description="Easily embed Slideshare slides in your posts",
      long_description=open("README.rst").read(),
      license='MIT',
      platforms=['linux'],
      packages=find_packages(exclude=["*.tests"]),
      package_data={'': ['LICENSE', ]},
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.1',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: Implementation :: CPython',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Text Processing',
      ],
      zip_safe=True,
      )
