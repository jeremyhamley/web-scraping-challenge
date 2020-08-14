# web-scraping 
# MARS NEWS, WEATHER, and MORE
# BeautifulSoup and Splinter 

 - Web scraping using BeautifulSoup and Splinter
 - scraping function wrapped in a FLASK app.  
  - MongoDB used for data storage

![mars](Missions_to_Mars/images/app_screen_shot.PNG)

# PART I - BeautifulSoup and Splinter
### Uses: Python, Pandas, Jupyter Notebook
    - import pandas, time, BeautifulSoup and splinter

### This section of the project is saved in the Jupyter Notebook file: **mission_to_mars.ipynb**

Jupyter Notebook used to develope the Python script to scrape various websites for the Mars data used in this project. <br>
The scrape includes:  

 - MARS NEWS<br> 
    https://mars.nasa.gov/news/
 - MARS WEATHER<br> 
    https://twitter.com/marswxreport?lang=en
 - NASA JPL FEATURED IMAGE<br> 
    https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
 - MARS STATS<br> 
    https://space-facts.com/mars/
 - MARS HEMISPHERE IMAGES<br> 
 https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars
 <br><br>

# PART II - Flask, HTML, and MongoDB
### Uses: Python, Pandas, Flask, and MongoDB
    - import pandas, flask, Pymongo, BeautifulSoup, splinter

### This section of the project is saved in the Python files: **scrape_mars.py** , **app.py** , **index.html**

The Mars scrape script that was developed in Jupyter Notebook was dropped into the python file scrape_mars.py  <br>

## FLASK APP
The Mars scrape script (**scrape_mars.py**) was then imported into the **app.py** file and wrapped in Flask

### The Flask app does several things:

  - Scrapes the five websites for the relevent Mars data
  - Connects to a MongoDB to store the data<br>

## INDEX.html
###  The html file brings all of the pieces together
 - The **refresh Mars Data** button launches the scrape function, driven by Splinter and BeautifulSoup, and returns the scraped data to a MongoDB database.
 - The stored data is then called by and displayed by the index.html file

![mars](Missions_to_Mars/images/HW_12_1.PNG)
![mars](Missions_to_Mars/images/HW_12_2.PNG)

