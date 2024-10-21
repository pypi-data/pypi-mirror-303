"""
Stats subclient for the PulseChain API.

This module defines the StatsClient class, which handles API endpoints related to
retrieving various statistical data such as general stats, transaction charts, and market charts.
The client provides methods to query these statistics and return them in a structured response format.
"""

from pulsechain.models import BaseResponse
from pulsechain.req_handler import APIRequestHandler
from pulsechain.subclients.subpath_client import SubpathClient


class StatsClient(SubpathClient):
    """
    A client for accessing statistical endpoints in the PulseChain API.

    The StatsClient provides methods to retrieve general statistics, transaction data
    over a recent time period, and market-related data. These statistics can be used
    to analyze the state of the PulseChain network.
    """

    def __init__(self, request_handler: APIRequestHandler):
        """
        Initialize the StatsClient with the subpath 'stats'.
        """
        super().__init__(subpath="stats", request_handler=request_handler)

    def get_stats(self) -> BaseResponse:
        """
        Retrieve general statistical counters from the PulseChain network.

        This method fetches overall statistics from the PulseChain API, which
        may include transaction-related counters and other network statistics.

        :return: A BaseResponse object containing general statistics for the network.
        """
        response = self.get()
        return BaseResponse(items=[response])

    def get_transactions_chart(self) -> BaseResponse:
        """
        Retrieve transaction count data for the last 31 days.

        This method fetches a chart containing the transaction count (`tx_count`)
        for the past 31 days from the PulseChain network.

        :return: A BaseResponse object containing chart data with transaction counts for the last 31 days.
        """
        response = self.get("charts/transactions")
        return BaseResponse(items=[response["chart_data"]])

    def get_market_chart(self) -> BaseResponse:
        """
        Retrieve market chart data from the PulseChain API.

        This method fetches the available supply and chart data from the market-related
        endpoint. The data returned currently includes an empty supply and an empty chart.

        :return: A BaseResponse object containing market chart data, which may include
                 available supply and other market-related statistics.
        """
        return BaseResponse(items=[self.get("charts/market")])
