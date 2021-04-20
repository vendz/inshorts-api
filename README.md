# Inshorts API [Unofficial]
---
This API is capable of fetching news contents from various sources as gathered by Inshorts app.

---

## News Categories

This API supports category wise news. Here is a complete list of all categories.

1. all
2. national //Indian News only
3. business
4. sports
5. world
6. politics
7. technology
8. startup
9. entertainment
10. miscellaneous
11. hatke
12. science
13. automobile

---

## Usage

Make a request specifying the category of news you want
```
https://inshort.vandit.cf/shorts/technology
```
Example - https://inshort.vandit.cf/shorts/technology

---
see all the available categories
```
https://inshort.vandit.cf/shorts/categories
```
Example - https://inshort.vandit.cf/shorts/categories

---

## Response Format

The response JSON Object looks something like this - 

```JSON
{
  "category": "technology",
  "data": [
    {
      "author": "Pragya Swastik",
      "content": "A cybersecurity researcher has claimed that credit card details of nearly 10 lakh people who purchased from Domino's Pizza India are being sold on the dark web for $550,000 (over ₹4 crore). "Jubilant FoodWorks experienced an information security incident recently," a company statement said. However, it added that no data pertaining to the financial information of any person was accessed.",
      "date": "19 Apr",
      "img_url": "https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2021/04_apr/19_mon/img_1618830582251_240.jpg?",
      "read_more_url": "https://www.thenewsminute.com/article/dominos-pizza-india-hacked-data-10-lakh-indians-allegedly-sale-147423?amp=&utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
      "short_url": "https://inshorts.com/en/news/data-of-10-lakh-indian-customers-of-dominos-leaked-on-sale-for-₹4-cr-report-1618832250740",
      "time": "05:07 pm",
      "title": "Data of 10 lakh Indian customers of Domino's leaked, on sale for ₹4 cr: Report"
    },
    {
      "author": "Hiral Goyal",
      "content": "Community-oriented platform Ethernity Chain has announced that it will launch a collection of authenticated non-fungible tokens (NFTs) to "honour the legacy" of former Brazilian footballer Pelé. It will mark the first time for Pelé trading cards to be released digitally, Ethernity Chain said. It added, 90% of the proceeds from the sale of NFTs will go to The Pelé Foundation.",
      "date": "19 Apr",
      "img_url": "https://static.inshorts.com/inshorts/images/v1/variants/jpg/m/2021/04_apr/19_mon/img_1618822474861_599.jpg?",
      "read_more_url": "https://ethernitychain.medium.com/pele-locks-in-a-historical-anft-drop-with-ethernity-ef53afbe3f54?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts ",
      "short_url": "https://inshorts.com/en/news/former-footballer-pelés-trading-cards-to-be-launched-as-nfts-1618827073923",
      "time": "03:41 pm",
      "title": "Former footballer Pelé's trading cards to be launched as NFTs"
    }
    ],
  "success": true
}
```
---
## Setup

Install all dependencies listed in *requirements.txt* file. 

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python app.py
    ```
---

### You can fork the repo and deploy on VPS, Heroku or Vercel :)
[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/vendz/inshorts-api/tree/main)

---
#### :star: the Repo in case you liked it :)
#### Made with :heart: in India

# © [Vandit](https://github.com/vendz)
