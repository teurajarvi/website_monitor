from distutils.core import setup

# Install website_monitor running below command in your console:
# >cd <root forder of the website_monitor>
# >python setyp.py install

setup(name='website_monitor',
      version='1.0',
      description='Website monitor tool',
      author='Jari-Pekka Teurajarvi',
      author_email='teurajarvi@hotmail.com',
      url='https://github.com/teurajarvi/website_monitor/',
      packages=['.controllers','.models']
     )
