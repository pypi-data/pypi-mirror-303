from .constants import WCI_BASE_URL, BASE_HEADERS
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import json


class CryptocoinEngine:
    """
    Wrapper for the WorldCoinIndex API.
    """

    def __init__(self, api_key):
        self.__api_key = api_key
        self.__base_url = WCI_BASE_URL
        self.__base_headers = BASE_HEADERS

    def _make_request(
        self, query_params: dict = {}, path_params: str = [], extra_headers: dict = {}
    ) -> dict:
        """
        Makes a GET request to the WorldCoinIndex API.
        """
        query_params["key"] = self.__api_key
        params_str = urlencode({k: v for k, v in query_params.items() if v})
        path_params = "/".join(path_params)
        request = Request(
            url=f"{self.__base_url}/{path_params}?{params_str}",
            headers={**self.__base_headers},
            method="GET",
        )
        try:
            with urlopen(request) as response:
                response: dict = json.loads(response.read().decode())
                return response
        except Exception as e:
            raise e

    def get_tickers(self, labels: list = [], fiat: str = "USD") -> dict:
        """
        Fetches ticker data for specified labels.

        Parameters:
            labels (list): List of pairs for which the latest price ticker is needed.
            fiat (str): The currency used to get the Volume_24h value in the response.

        Returns:
            dict: Latest tickers for the specified labels
        """
        labels = [label.lower() for label in labels]
        labels_param = "-".join(labels)
        query_params = {"label": labels_param, "fiat": fiat}
        path_params = ["ticker"]
        response = self._make_request(
            query_params=query_params, path_params=path_params
        )
        return response

    def get_markets(self, use_v2: bool = True, fiat: str = "USD") -> dict:
        """
        Fetches market data for all currencies.

        Parameters:
            fiat (str): The currecncy with respect to which the tickers are returned.
            use_v2 (bool): Choose the latest v2 version of the API or the depricated v1 version

        Returns:
            dict: Tickers of the entire market with respect to the fiat currency.
        """
        path_params = [("getmarkets" if not use_v2 else "v2getmarkets")]
        query_params = {"fiat": fiat}
        response = self._make_request(
            query_params=query_params, path_params=path_params
        )
        return response

    def get_all(self) -> dict:
        """
        Fetches the data for each coin with respect to usd, btc, cny, eur, gbp, rur.

        Note:
            This is a depricated feature in the API.
        """
        path_params = ["json"]
        response = self._make_request(path_params=path_params)
        return response
