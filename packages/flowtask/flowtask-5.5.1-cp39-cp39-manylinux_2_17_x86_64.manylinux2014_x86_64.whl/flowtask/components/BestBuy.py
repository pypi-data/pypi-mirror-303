"""
Scrapping a Web Page Using Selenium + ChromeDriver + BeautifulSoup.
"""
import asyncio
from collections.abc import Callable
import random
from bs4 import BeautifulSoup
import httpx
import pandas as pd
import backoff
import aiohttp
from navconfig.logging import logging
# Internals
from ..exceptions import (
    ComponentError,
    DataNotFound,
    NotSupported,
    ConfigError
)
from .abstract import FlowComponent
from ..interfaces import HTTPService, SeleniumService
from ..interfaces.http import ua


logging.getLogger(name='selenium.webdriver').setLevel(logging.WARNING)
logging.getLogger(name='WDM').setLevel(logging.WARNING)
logging.getLogger(name='hpack').setLevel(logging.WARNING)
logging.getLogger(name='seleniumwire').setLevel(logging.WARNING)


ProductPayload = {
    "locationId": None,
    "zipCode": None,
    "showOnShelf": True,
    "lookupInStoreQuantity": True,
    "xboxAllAccess": False,
    "consolidated": True,
    "showOnlyOnShelf": False,
    "showInStore": True,
    "pickupTypes": [
        "UPS_ACCESS_POINT",
        "FEDEX_HAL"
    ],
    "onlyBestBuyLocations": True,
    "items": [
        {
            "sku": None,
            "condition": None,
            "quantity": 1,
            "itemSeqNumber": "1",
            "reservationToken": None,
            "selectedServices": [],
            "requiredAccessories": [],
            "isTradeIn": False,
            "isLeased": False
        }
    ]
}

class BestBuy(FlowComponent, HTTPService, SeleniumService):
    """BestBuy.

    Combining API Key and Web Scrapping, this component will be able to extract
    Best Buy Information (stores, products, Product Availability, etc).
    """
    def __init__(
        self,
        loop: asyncio.AbstractEventLoop = None,
        job: Callable = None,
        stat: Callable = None,
        **kwargs,
    ):
        self._fn = kwargs.pop('type', None)
        self.chunk_size: int = kwargs.get('chunk_size', 100)
        if not self._fn:
            raise ConfigError(
                "BestBuy: require a `type` Function to be called, ex: availability"
            )
        super(BestBuy, self).__init__(
            loop=loop,
            job=job,
            stat=stat,
            **kwargs
        )
        # Always use proxies:
        self.use_proxy: bool = True
        self._free_proxy: bool = False
        self.cookies = {
            "CTT": "f3dbf688e45146555bb2b8604a993601",
            "SID": "d4fa1142-2998-4b68-af78-46d821bb3e1f",
            "bby_rdp": "l",
            "bm_sz": "9F5ED0110AF18594E2347A89BB4AB998~YAAQxm1lX6EqYHGSAQAAw+apmhkhXIeGYEc4KnzUMsjeac3xEoQmTNz5+of62i3RXQL6fUI+0FvCb/jgSjiVQOcfaSF+LdLkOXP1F4urgeIcqp/dBAhu5MvZXaCQsT06bwr7j21ozhFfTTWhjz1HmZN8wecsE6WGbK6wXp/33ODKlLaGWkTutqHbkzvMiiHXBCs9hT8jVny0REfita4AfqTK85Y6/M6Uq4IaDLPBLnTtJ0cTlPHk1HmkG5EsnI46llghcx1KZnCGnvZfHdb2ME9YZJ2GmC2b7dNmAgyL/gSVpoNdCJOj5Jk6z/MCVhZ81OZfX4S01E2F1mBGq4uV5/1oK2KR4YgZP4dsTN8izEEPybUKGY3CyM1gOUc=~3556420~4277810",  # noqa
            "bby_cbc_lb": "p-browse-e",
            "intl_splash": "false"
        }
        self.headers: dict = {
            "Host": "www.bestbuy.com",
            "Referer": "https://www.bestbuy.com/",
            "X-Requested-With": "XMLHttpRequest",
            "TE": "trailers",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",  # noqa
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": random.choice(ua),
            **self.headers
        }
        self.semaphore = asyncio.Semaphore(10)

    async def close(self, **kwargs) -> bool:
        self.close_driver()
        return True

    async def start(self, **kwargs) -> bool:
        await super(BestBuy, self).start(**kwargs)
        if self.previous:
            self.data = self.input
        else:
            raise DataNotFound(
                "Data Not Found",
                code=404
            )
        if not isinstance(self.data, pd.DataFrame):
            raise ComponentError(
                "Incompatible Pandas Dataframe",
                code=404
            )
        if self._fn == 'availability':
            if not hasattr(self, 'brand'):
                raise ConfigError(
                    "BestBuy: A Brand is required for using Product Availability"
                )
            if not hasattr(self, 'sku'):
                raise ConfigError(
                    "BestBuy: Product SKU is required for using Product Availability"
                )
        if not hasattr(self, self._fn):
            raise ConfigError(
                f"BestBuy: Unable to found Function {self._fn} in BBY Component."
            )

    def _search_product(self, brand: str, sku: str) -> str:
        front_url = "https://www.bestbuy.com/site/searchpage.jsp?cp="
        middle_url = "&searchType=search&st="
        page_count = 1
        # TODO: Get the Brand and Model from the Component.
        search_term = f'{brand}%20{sku}'
        end_url = "&_dyncharset=UTF-8&id=pcat17071&type=page&sc=Global&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All%20Categories&ks=960&keys=keys"  # noqa
        url = front_url + str(page_count) + middle_url + search_term + end_url
        print('SEARCH URL: ', url)
        return url

    async def _extract_product_list(self, content: str) -> dict:
        soup = BeautifulSoup(content, 'html.parser')
        # Find all elements with class "sku-item"
        product_items = soup.find_all('li', {'class': ['sku-item']})
        # Iterate over each product item
        result = {}
        for item in product_items:
            # Get the "data-sku-id" attribute
            sku_id = item.get("data-sku-id")
            # Check if the SKU ID matches your target SKU ID
            if sku_id == self.sku:
                print(f"Found matching SKU ID: {sku_id}")
                # Now look for the child with class "sku-title"
                pd = item.find('h4', {'class': ['sku-title']})
                anchor = pd.a
                title = anchor.text
                price = item.find(
                    'div', {'class': ['priceView-customer-price']}
                ).select_one(
                    'span:nth-child(1)'
                ).text
                # Image:
                image = item.find('img', {"class": ['product-image']})['src']
                # Product Model
                model = item.select_one(
                    'div.sku-attribute-title:nth-child(1) span.sku-value'
                ).text
                url = "https://www.bestbuy.com{url}".format(
                    url=anchor['href']
                )
                self._logger.notice(
                    f':: Product URL: {url}'
                )
                result = {
                    "sku": sku_id,
                    "brand": self.brand,
                    "model": model,
                    "product_name": title,
                    "image_url": image,
                    "price": price,
                    "url": url
                }
                # if product found, break
                return result
        return result

    def chunkify(self, lst, n):
        """Split list lst into chunks of size n."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    async def api_post(self, url: str, cookies: httpx.Cookies, payload: dict):
        proxies = await self.get_proxies()
        proxy = proxies[0]
        proxies = {
            "http://": httpx.AsyncHTTPTransport(
                proxy=f"http://{proxy}"
            ),
            "https://": httpx.AsyncHTTPTransport(
                proxy=f"http://{proxy}"
            ),
        }
        async with httpx.AsyncClient(cookies=cookies, verify=False) as client:
            try:
                response = await client.post(
                    url,
                    json=payload,
                    headers=self.headers
                )
                response.raise_for_status()
                if response.status_code == 200:
                    return response.json()
                return {}
            except (httpx.HTTPError) as ex:
                print('ERR > ', ex)
                raise
            except Exception as exc:
                print('EXC > ', exc)
                raise ComponentError(
                    f"An error occurred: {exc}"
                )

    @backoff.on_exception(
        backoff.expo,
        (httpx.ConnectTimeout, asyncio.TimeoutError),
        max_tries=2
    )
    async def _check_store_availability(
        self,
        sku,
        row,
        cookies
    ):
        async with self.semaphore:
            # extract zipcode, sku and location_code from row:
            zipcode = row['zipcode']
            location_code = row['location_code']
            payload = ProductPayload.copy()
            payload["locationId"] = location_code
            payload["zipCode"] = zipcode
            # Useful for looking several products at time
            for item in payload["items"]:
                item["sku"] = sku
            try:
                result = await self.api_post(
                    url="https://www.bestbuy.com/productfulfillment/c/api/2.0/storeAvailability",
                    cookies=cookies,
                    payload=payload
                )
            except httpx.HTTPError as ex:
                self._logger.error(ex)
                return row
            except Exception as ex:
                self._logger.error(ex)
                return row
            if not result:
                return row
            # working with result:
            # TODO: can work with several products at the same time:
            items = result.get('ispu', {}).get('items', [])
            # for every item, extract the SKU and locations:
            for item in items:
                # product_sku = item.get('sku')
                locations = item.get('locations')
                for location in locations:
                    lid = location.get('locationId')
                    matching_store = self.data[self.data['location_code'] == lid]
                    # If we found a matching store (location_code == locationId)
                    if not matching_store.empty:
                        # Get the index of the matched row
                        idx = matching_store.index[0]
                        self.data.at[idx, 'location_data'] = location
                        # Update the row with the location data
                        # by converting location dict to columns
                        for key, val in location.items():
                            self.data.at[idx, key] = val
                            if key == 'inStoreAvailability':
                                try:
                                    self.data.at[idx, 'availableInStoreQuantity'] = val.get('availableInStoreQuantity')
                                except KeyError:
                                    pass
                        # Mark the row as checked
                        self.data.at[idx, 'checked'] = True
                        print(
                            f"Updated Store with LocationId {lid} at index {idx}"
                        )

            # Return the Row
            return row

    def column_exists(self, column: str):
        if column not in self.data.columns:
            self._logger.warning(
                f"Column {column} does not exist in the dataframe"
            )
            self.data[column] = None
            return False
        return True

    async def availability(self):
        """availability.

        Best Buy Product Availability.
        """
        # 1. Get the Product List URL
        url = self._search_product(self.brand, self.sku)
        await self.get_page(url, self.cookies)
        content = self.driver().page_source
        product_info = await self._extract_product_list(content)
        if not product_info:
            raise DataNotFound(
                f"BestBuy: Cannot found product information for {self.brand}-{self.sku}"
            )
        # With Product info, extract the cookies from Selenium:
        # Get the cookies from Selenium WebDriver
        selenium_cookies = self.driver().get_cookies()
        # Convert Selenium cookies to httpx format
        httpx_cookies = httpx.Cookies()
        cookies_avail = ["CTT", "SID", '_abck', 'bby_rdp', 'bm_sz']
        for cookie in selenium_cookies:
            if cookie['name'] in cookies_avail:
                httpx_cookies.set(
                    cookie['name'], cookie['value'],
                    domain=cookie['domain'],
                    path=cookie['path']
                )
        # make a join between current df and product info:
        new_df = pd.DataFrame([product_info] * len(self.data))
        # Concatenate the DataFrames horizontally
        self.data = pd.concat([self.data, new_df], axis=1)
        # With available cookies, iterate over dataframe for stores:
        self.data['checked'] = False  # Add 'checked' flag column

        # define the columns returned:
        self.column_exists('location_data')
        self.column_exists('locationId')
        self.column_exists('availability')
        self.column_exists('inStoreAvailability')
        self.column_exists('onShelfDisplay')
        self.column_exists('availableInStoreQuantity')

        for _, row in self.data.iterrows():
            if not row['checked']:
                await self._check_store_availability(
                    self.sku, row, httpx_cookies
                )

        # Remove the 'checked' column after completion
        # self.data.drop(columns=['checked'], inplace=True)
        # return existing data
        return self.data

    async def run(self):
        # we need to call the "function" for Best Buy Services.
        fn = getattr(self, self._fn)
        result = None
        try:
            result = await fn()
        except (ComponentError, TimeoutError, NotSupported):
            raise
        except Exception as exc:
            raise ComponentError(
                f"BestBuy: Unknown Error: {exc}"
            ) from exc
        # Print results
        print(result)
        print("::: Printing Column Information === ")
        for column, t in result.dtypes.items():
            print(column, "->", t, "->", result[column].iloc[0])
        self._result = result
        return self._result
