from setuptools import setup, find_namespace_packages

setup(name='clean-folder',
      version='1',
      description='Script for organizing your "download" or "trash" folders',
      url='https://github.com/Eskual/mod-6',
      author='Eskual',
      author_email='panichukd@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})