# web_scraping


Mission to Mars is a web application that scrapes various websites for data related to Mars and displays the information in a single HTML web page.

<p>The folder <a href="https://github.com/cspence001/web_scraping_challenge/tree/main/Missions_to_Mars">Missions_to_Mars</a> contains all of the files used to create the web page:</p>


<p>The jupyter notebook file <a href="https://github.com/cspence001/web_scraping_challenge/blob/main/Missions_to_Mars/mission_to_mars.ipynb">mission_to_mars.ipynb</a> is used to scrape the following URLs using BeautifulSoup, Pandas, and Requests/Splinter:</p>
<ul>
    <li>https://mars.nasa.gov/news/</li>
    <li>https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html</li>
    <li>https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars</li>
</u>
<p>The date is then stored as a dictionary and hosted in MongoDB.</p>

<p>The python script<a href="https://github.com/cspence001/web_scraping_challenge/blob/main/Missions_to_Mars/scrape_mars.py">scrape_mars.py</a> creates the scrape() function that executes the scraping code created in the jupyter notebook file. The scrape function is called in the app.py file.</p>

<p>The Flask app <a href="https://github.com/cspence001/web_scraping_challenge/blob/main/Missions_to_Mars/app.py">app.py</a> contains two routes one of which calls the scrape function from the previous code when executed via the "Scrape New Data" button on the home page. The root route queries the Mongo database and passes the executed Mars Data into an HTML page for rendering of the data dictionary for display.</p>

<p>The folder <a href="https://github.com/cspence001/web_scraping_challenge/tree/main/Missions_to_Mars/templates">templates</a> contains the <a href="https://github.com/cspence001/web_scraping_challenge/blob/main/Missions_to_Mars/templates/index.html">index.html</a> file that displays the data using Bootstrap page elements.</p>

<p>The folder <a href="https://github.com/cspence001/web_scraping_challenge/tree/main/Missions_to_Mars/Screenshots">Screenshots</a> contains two screenshots of the final webpage display. </p>



