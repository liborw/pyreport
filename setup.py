from setuptools import setup

setup(name='pyreport',
      version='0.1',
      description='Simple reports from python',
      author='Libor Wagner',
      author_email='libor.wagner@cvut.cz',
      url='https://gitlab.ciirc.cvut.cz/b635-incubator/pyreport',
      packages=['pyreport'],
      package_dir={'pyreport': 'src/pyreport'},
      install_requires=[
            'jinja2'
          ]
      )
