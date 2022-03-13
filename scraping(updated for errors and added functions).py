
# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

# Run all scraping functions and store results in dictionary
data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now()
}

# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


#n our case, we want our code to be reused, and often, to pull the most recent data. That's what web scraping is all about, right? Pulling in the live data at the click of a button. Functions enable this capability by bundling our code into something that is easy for us (and once it's deployed, whoever else we share the web app with) to use and reuse as needed.

#Also, because the intention is to reuse this code often, we need to update our scraping.py script to use functions. Each major scrape, such as the news title and paragraph or featured image, will be divided into a self-contained, reusable function. Let's take a look at our code.
#When we add the word "browser" to our function, we're telling Python that we'll be using the browser variable we defined outside the function. All of our scraping code utilizes an automated browser, and without this section, our function wouldn't work.
#Adding function with browser argument
def mars_news(browser):

# Visit the Mars news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

# Add try/except for error handling
try:
     slide_elem = news_soup.select_one('div.list_text')
     # Use the parent element to find the first 'a' tag and save it as 'news_title'
     news_title = slide_elem.find('div', class_='content_title').get_text()
     # Use the parent element to find the paragraph text
     news_p = slide_elem.find('div', class_='article_teaser_body').get_text()


except AttributeError:
    return None, None
#Instead of having our title and paragraph printed within the function, we want to return them from the function so they can be used outside of it. We'll adjust our code to do so by deleting news_title and news_p and include them in the return statement instead, as shown below.
#Returning our function to tell function it is complete

return news_title, news_p



# ## JPL Space Images Featured Image

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

# ## Mars Facts

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

   # Stop webdriver and return data
   browser.quit()
   return data

   if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
