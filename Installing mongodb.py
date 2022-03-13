#Installing mongodb
#In anaconda prompt enviroment type pip install splinter, then pip install webdriver_manager, then pip install bs4 for beautiful soup, 
# then pip install pymongo, then cd c:\, then mkdir data\db. 
#Go to edit system environment and variables and add the downloaded mongo path bin to the path. (Should be C:\\Program Files\\MongoDB\\Server\\\\bin)
#In gitbash we did cd c:\, then mongod. Open new git bash and type mongo to test and launch. Keep both open
#To test if working, open anaconda environment terminal and type mongod

#To bridge Flask and Mongo, you'll also want to install the (Flask-PyMongo)[https://flask-pymongo.readthedocs.io/en/latest/] library.
#This library can be installed using pip and the following command from your terminal: pip install Flask-PyMongo.

#There are two final Python libraries required to run scraping code successfully: html5lib and lxml. Both packages are used to parse HTML in Python, which will be important as you traverse through different web pages to find and collect information.

#To install these libraries, first make sure your coding environment is active. Then, type the following commands in your terminal to install them:

#pip install html5lib
#pip install lxml