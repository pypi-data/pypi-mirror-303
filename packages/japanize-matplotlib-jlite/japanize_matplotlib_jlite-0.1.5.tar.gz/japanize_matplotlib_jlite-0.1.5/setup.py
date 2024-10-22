# encoding: utf8
import glob
from setuptools import find_packages, setup

additional_files = []
for filename in glob.iglob('./japanize_matplotlib_jlite/**', recursive=True):
    additional_files.append(filename.replace('./japanize_matplotlib_jlite/', ''))


setup(name='japanize-matplotlib-jlite',
      version='0.1.5',
      description='JupyterLiteでmatplotlibのフォント設定を自動で日本語化する',
      author='spring-haru',
      author_email='tetsu.yes@gmail.com',
      url='https://github.com/spring-haru/japanize-matplotlib-jlite',
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      license='MIT License',
      packages=find_packages(),
      package_dir={'japanize_matplotlib_jlite': './japanize_matplotlib_jlite'},
      install_requires=['matplotlib'],
      include_package_data=True,
      package_data={'japanize_matplotlib_jlite': additional_files})
