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
      url='http://github.com/storborg/funniest',
      author='Asif Kodur',
      author_email='asif.kodur@gmail.com',
      license='GPL',
      packages=['evm'],
      install_requires=[
          'fpdf==1.7.2','pygame===1.9.1release','wxPython==2.8.12.1','wxPython-common==2.8.12.1',
      ],
      include_package_data=True,
      zip_safe=False)




