# Setup File
import os
import re
from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_package_data(package):
    """
    Return all files under the root package, that are not in a
    package themselves.
    """
    walk = [(dirpath.replace(package + os.sep, '', 1), filenames)
            for dirpath, dirnames, filenames in os.walk(package)
            if not os.path.exists(os.path.join(dirpath, '__init__.py'))]

    filepaths = []
    for base, filenames in walk:
        filepaths.extend([os.path.join(base, filename)
                          for filename in filenames])
    return {package: filepaths}

version = get_version('OpinioDelivery')

setup(name='opiniohll',
      version=version,
      description='OpinioApp Delivery Python SDK',
      url='http://github.com/anistark/opiniohll',
      author='Kumar Anirudha',
      author_email='kumar.anirudha@opinioapp.com',
      license='MIT',
      packages=['OpinioDelivery'],
      package_data=get_package_data('OpinioDelivery'),
      install_requires=[
          'requests >= 2.9.1',
          'ujson >= 1.35'
      ],
      zip_safe=False,
      keywords=['opinio', 'hll', 'OpinioDelivery'],
      classifiers=[
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Topic :: Internet :: WWW/HTTP',
      ])
