from setuptools import find_packages, setup

from py2fa import VERSION

with open('README.md', encoding='utf-8') as f:
    readme = f.read()

setup(name='py2fa-cli',
      version=VERSION,
      description='Command-line application for calculating one-time passwords for 2FA.',
      long_description=readme,
      long_description_content_type="text/markdown",
      author='arcctgx',
      author_email='arcctgx@o2.pl',
      url='https://github.com/arcctgx/py2fa-cli',
      license='GPLv3',
      classifiers=[
          'Development Status :: 5 - Production/Stable', 'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Natural Language :: English', 'Programming Language :: Python :: 3 :: Only'
      ],
      packages=find_packages(),
      entry_points={'console_scripts': ['py2fa = py2fa.py2fa:main']},
      python_requires='>=3.7',
      install_requires=['pyotp', 'pyxdg'])
