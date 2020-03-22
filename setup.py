from distutils.core import setup
setup(
  name = 'pyfluxc',         
  packages = ['pyfluxc'],  
  version = '0.1',      
  license='agpl-3.0',  
  description = 'influxdb flux query language client',
  author = 'Samuele Sabella',                   
  author_email = 'samueleunipi@gmail.com',      
  url = 'https://github.com/samuelesabella/pyfluxc',   
  download_url = 'https://github.com/samuelesabella/pyfluxc/archive/v_01.tar.gz',    
  keywords = ['influxdb', 'flux', 'client'],   
  install_requires=[            
          'requests',
          'pandas',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
  ],
)
