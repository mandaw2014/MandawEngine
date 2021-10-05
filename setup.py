from distutils.core import setup

setup(name='Mandaw',
      version='1.1.4',
      description='A Game Engine Made In Python',
      author='mandaw2014',
      keywords="python 2d game development",
      author_email='mandawbuisness@gmail.com',
      url='https://github.com/mandaw2014/MandawEngine',
      packages=['mandaw'],
      package_dir={'mandaw': 'mandaw'},
      install_requires=["pygame"]
      )
