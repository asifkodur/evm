from setuptools import setup

setup(name='evm',
      version='0.2',
      description='Electronic Voting Machine',
      long_description='A simple and intutive software to conduct Elections in Schools',
      classifiers=[
        'License :: GPL',
        'Programming Language :: Python :: 2.7',
        'Topic :: Education :: Election',
      ],
      keywords='school election evm voting kerala ',
      url='https://github.com/asifkodur/evm',
      author='Asif Kodur',
      author_email='asif.kodur@gmail.com',
      license='GPL',
      packages=['evm'],
      install_requires=[
          'fpdf','pygame','wxPython','wxPython-common',
      ],
      include_package_data=True,
      zip_safe=False)




