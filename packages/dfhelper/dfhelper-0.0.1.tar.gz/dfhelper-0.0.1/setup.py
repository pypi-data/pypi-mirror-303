from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r', encoding='utf-8') as f:
        return f.read()


setup(
  name='dfhelper',
  version='0.0.1',
  author='kodurd',
  author_email='koldunov.eduard1@gmail.com',
  description='dfhelper is a Python package that simplifies data preprocessing and visualization in Jupyter Notebooks.',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/kodurd/dfhelper',
  packages=find_packages(),
  install_requires=['pandas>=2.2.2', 'ipython>=8.28.0'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
  ],
  keywords='preprocessing visualization',
  project_urls={
    'GitHub': 'https://github.com/kodurd/dfhelper'
  },
  python_requires='>=3.9'
)
