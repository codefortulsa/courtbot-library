from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(name='courtbot',
      version='0.0.0.0',
      description='Generic Court Scraper for Courbot system use',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/codefortulsa/courtbot-library',
      author='Code for Tulsa',
      author_email='code-for-tulsa@googlegroups.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      install_requires=[
          'requests',
          'beautifulsoup4',
          ],
      classifiers=[
          'Programming Language :: Python',
          'Programming Language :: Python :: 3.7',
          ],
      )
