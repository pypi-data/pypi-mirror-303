import requests
import json
import time
from threading import Lock

class HypixelBazaarWrapper:
    def __init__(self, cache_timeout=60):
        """
        Initialize the wrapper with a cache timeout.

        :param cache_timeout: Time in seconds to cache the Bazaar data.
        """
        self.endpoint = "https://api.hypixel.net/skyblock/bazaar"
        self.cache_timeout = cache_timeout
        self._cache = None
        self._last_updated = 0
        self._lock = Lock()

    def _fetch_data(self):
        """Fetch data from the Hypixel Bazaar API and cache it."""
        response = requests.get(self.endpoint)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        with self._lock:
            self._cache = data
            self._last_updated = time.time()

    def _get_data(self):
        """Retrieve Bazaar data, using cache if available and valid."""
        with self._lock:
            if self._cache and (time.time() - self._last_updated) < self.cache_timeout:
                return self._cache

        self._fetch_data()
        return self._cache

    def get_item(self, item_key):
        """
        Get data for a specific item.

        :param item_key: The key of the item (e.g., 'ENCHANTED_COBBLESTONE').
        :return: Dictionary containing item data.
        """
        data = self._get_data()
        products = data.get('products', {})
        if item_key in products:
            return products[item_key]
        else:
            raise KeyError(f"Item '{item_key}' not found in Bazaar data.")

    def list_items(self):
        """
        List all available item keys in the Bazaar.

        :return: List of item keys.
        """
        data = self._get_data()
        return list(data.get('products', {}).keys())

    def get_buy_price(self, item_key):
        """
        Get the current buy price for an item.

        :param item_key: The key of the item.
        :return: Float value of the buy price.
        """
        item_data = self.get_item(item_key)
        return item_data['quick_status']['buyPrice']

    def get_sell_price(self, item_key):
        """
        Get the current sell price for an item.

        :param item_key: The key of the item.
        :return: Float value of the sell price.
        """
        item_data = self.get_item(item_key)
        return item_data['quick_status']['sellPrice']

    def get_profit_margin(self, item_key):
        """
        Calculate the profit margin between buy and sell prices.

        :param item_key: The key of the item.
        :return: Float value representing the profit margin.
        """
        buy_price = self.get_buy_price(item_key)
        sell_price = self.get_sell_price(item_key)
        return sell_price - buy_price

    def get_top_profitable_items(self, top_n=10):
        """
        Get the top N items with the highest profit margins.

        :param top_n: Number of top items to return.
        :return: List of tuples containing item keys and profit margins.
        """
        items = self.list_items()
        profit_list = []

        for item in items:
            try:
                margin = self.get_profit_margin(item)
                profit_list.append((item, margin))
            except KeyError:
                continue  # Skip items that cause errors

        # Sort the items based on profit margin in descending order
        profit_list.sort(key=lambda x: x[1], reverse=True)
        return profit_list[:top_n]

    def refresh_data(self):
        """Force refresh the cached Bazaar data."""
        with self._lock:
            self._fetch_data()
