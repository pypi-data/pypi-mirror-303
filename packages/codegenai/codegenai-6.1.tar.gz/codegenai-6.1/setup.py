from setuptools import setup, find_namespace_packages

setup(name = 'codegenai',
      version = '6.1',
      description = "AI Algorithms And Computer Network Related Code",
      author = 'Anonymus',
      package_data={'':['licence.txt', 'README.md', 'data\\**']},
      include_package_data = True,
      install_requires = ['networkx','matplotlib','tqdm','numpy','scipy','scikit-learn','seaborn'],
      packages = find_namespace_packages(),
      zip_safe = False)