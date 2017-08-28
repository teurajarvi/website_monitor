try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Install website_monitor with commands:
# >cd [folder website_monitor-master]
# >python setup.py install
# run the application with command:
# Windows:
# >main.py
# Linux:
# >python main.py
# Check the config.ini file to change the application values
# Check the monitor_log.log file to track user logs

setup(
    name='website_monitor',
    version='1.0',
    description='application to monitor website response time and simple text content validation',
    author='Jari-Pekka Teurajarvi',
    author_email='teurajarvi@hotmail.com',
    url='https://github.com/teurajarvi/website_monitor/',
    license='MIT',
    classifiers=[
      #   4 - Beta
      #   5 - Production/Stable
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Software Development :: Build Tools',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 2.7'],
    packages=['.controllers', '.models', '.logs'],
    install_requires=['requests','beautifulsoup4','lxml','configparser']
)
