# Phone Spider

### Diogo Coutinho Coelho

#### Instructions for install the project
Install  [Python 3.7+](https://www.python.org/downloads/)

````
sudo apt-get python3.7
 ````   

[Clone the project](https://github.com/diogocoutinhocoelho/rgr_dnb.git)

    
Through __TERMINAL__ access the project folder
````
cd project_path
````

Active the virtualenv:

````
source venv/bin/activate
````
Write the list of sites in the sites.txt file:

```
EXEMPLES:
https://www.cmsenergy.com/contact-us/
https://www.illion.com.au
https://www.phosagro.com/contacts/
https://www.powerlinx.com/contact
https://www.cialdnb.com/
https://www.illion.com.au/contact-us/
```
Run the spider:

```
scrapy runspider crawler/dnb_crwaler/spiders/page_info_spider.py 
```

retrun.json file will be created on the desktop
