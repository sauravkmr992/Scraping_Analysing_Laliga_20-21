# Laliga 20/21
Laliga is a top tier *spanish* league. Data has been collected match wise and insights have been drawn from them using various python data manipulation and data visualisation libraries.

## Scraping

Data has been scraped out from [Sofascore](https://www.sofascore.com/) which uses [Cloudfare](https://www.cloudflare.com/) protection to sheild the data from bots or spiders.
*downloader_middleware* is used to bypass the cloudfare network. 

* You can find the script that is used for scraping in the directory as follows:

  * Laliga
    * Laliga
      * Spiders
        * laligarounds

Request is sent to [this link](https://api.sofascore.com/api/v1/unique-tournament/8/season/32501/events/round) using `start_requests` func which returns the response to `parse`
func then *parse* func loops through and send request using each extracted *match id* to [this link](https://api.sofascore.com/api/v1/event/8966364/lineups) returning a json object to `parseid` func which then analyses and yeilds the data. Please go through the scripts to understand the flow of request.


### Running the Script

1. Conda/pip install scrapy version listed in the `requirements.txt` and all the other dependencies
2. Now, move folder laliga to your local machine.
3. Activate the environment then move into `laliga` folder from your terminal/cmd.
4. Type `scrapy crawl laligarounds.py -o laliga.csv` in your terminal
5. This will generate a csv file named  ***laliga*** in your main folder.


#### Note:  
 * Scraping is done using *Web API* not the normal url as you can see in the link above.
 * Scraped csv file is present inside main `laliga` folder by name **laliga.csv**
 * `Players.json` is the response that is returned by `parse` func for a single matchid.
 * `Players.json` structure is used to write the extraction code for scraping.


## Generating Insights

Using Pandas, seaborn and scipy I have attempted to answer few interesting questions that surrounds this dataset. This `laliga.ipynb` is a well documented notebook which answers *what* and  *why* of the scraped dataset. Pdf and cdf has also been used to understand important features of the dataset for eg. Goals. Scatter and line plots have been used mainly to gather the hidden insight. All the other answering tasks have been acheived using Pandas which makes manipulating data easier with its available function. Please head over to `laliga.ipynb` for a better understanding of the analysis done.
