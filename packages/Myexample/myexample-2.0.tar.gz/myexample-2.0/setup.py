from setuptools import setup, Extension
 
module = Extension('Myexample', #python module name
                   sources=['Myexample_module.cpp'],
                   extra_compile_args=['-std=c++11'])

setup(name='Myexample', #python module name
      version='2.0',
      author='lfpu',
      author_email='pulongfei@outlook.com',
      description='Example package with C++ extension',
      long_description=open('README.md').read(),
      long_description_content_type='text/markdown',
      url='https://github.com/lfpu',
      classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
      ],
      ext_modules=[module]
)