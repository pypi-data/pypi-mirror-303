"""
Exposes an easy API to get prices from coingecko
"""

from typing import List

import pandas as pd
import requests

from strideutils import stride_config, stride_requests
from strideutils.stride_config import config

COINGECKO_ENDPOINT = "https://pro-api.coingecko.com/"
COINGECKO_PRICE_QUERY = "api/v3/simple/price?ids={ticker_id}&vs_currencies=usd"
COINGECKO_TVL_QUERY = "api/v3/coins/{ticker_id}"


def get_coingecko_name(chain_config: stride_config.ChainConfig) -> str:
    """
    Returns the coingecko name for a given chain
    """
    try:
        return chain_config.coingecko_name
    except AttributeError:
        return chain_config.name


def get_token_price(
    ticker: str,
    api_token: str = config.COINGECKO_API_TOKEN,
    cache_response: bool = False,
):
    """
    Reads token price from coingecko
    """
    # TODO: Consider using the coingecko ID for stTokens instead of the redemption rate
    # Get redemption rate for calculating st token prices
    redemption_rate = float(1)
    if ticker.startswith('st') and ticker[3].isupper():
        redemption_rate = stride_requests.get_redemption_rate(ticker[2:])
        ticker = ticker[2:]
    # get coingecko_name
    try:
        coingecko_name = get_coingecko_name(config.get_chain(ticker=ticker))
    except KeyError:
        coingecko_name = ticker
    # query endopint
    endpoint = COINGECKO_ENDPOINT + COINGECKO_PRICE_QUERY.format(ticker_id=coingecko_name)
    headers = {'x-cg-pro-api-key': api_token}
    response = stride_requests.request(endpoint, headers=headers, cache_response=cache_response)
    price = response[coingecko_name]["usd"] * redemption_rate

    return price


def get_tvl(
    chain_config: stride_config.ChainConfig,
    api_token: str = config.COINGECKO_API_TOKEN,
    cache_response: bool = False,
) -> float:
    """
    Fetch TVL from coingecko in USD
    """
    coingecko_name = get_coingecko_name(chain_config)
    endpoint = COINGECKO_ENDPOINT + COINGECKO_TVL_QUERY.format(ticker_id=coingecko_name)
    headers = {'x-cg-pro-api-key': api_token}

    # The data structure is huge https://docs.coingecko.com/reference/coins-id
    response = stride_requests.request(endpoint, headers=headers, cache_response=cache_response)
    return float(response['market_data']['market_cap']['usd'])


def get_token_price_history(token: str, num_days: int = 90, use_key: bool = True, memo={}) -> pd.Series:
    """
    returns a Pandas Series with token price data going back num_days
    e.g. get_token_price_history('uatom', 30) returns a Series with 30 days of ATOM price data
    TODO: Figure out why API key is throwing an error when used.
    """
    price_key = (token, num_days)
    if price_key not in memo:
        tstr = get_coingecko_name(config.get_chain(ticker=token))
        rurl = f"{COINGECKO_ENDPOINT}api/v3/coins/{tstr}/market_chart?vs_currency=usd&days={num_days}"  # noqa:E231
        rel_headers = {"x-cg-pro-api-key": config.COINGECKO_API_TOKEN} if use_key else None
        r = requests.get(
            rurl,
            headers=rel_headers,
        )
        assert r.status_code == 200
        out_df = pd.DataFrame(r.json()["prices"])
        out_df.columns = pd.Index(["time", "price"])
        out_df["time"] = pd.to_datetime(out_df["time"], unit="ms")
        out_df["price"] = out_df["price"].astype(float)
        out_df.set_index("time", inplace=True)
        memo[token] = out_df
    return memo[token]


def get_token_volume_history(token: str, num_days=90, use_key=True, memo={}) -> pd.Series:
    """
    returns a Pandas Series with token volume data going back num_days
    e.g. get_token_volume_history('uatom', 30) returns a Series with 30 days of ATOM volume data
    TODO: Figure out why API key is throwing an error when used.
    """
    volume_key = (token, num_days)
    if volume_key not in memo:
        tstr = get_coingecko_name(config.get_chain(ticker=token))
        rurl = f"{COINGECKO_ENDPOINT}api/v3/coins/{tstr}/market_chart?vs_currency=usd&days={num_days}"  # noqa:E231
        rel_headers = {"x-cg-pro-api-key": config.COINGECKO_API_TOKEN} if use_key else None
        r = requests.get(
            rurl,
            headers=rel_headers,
        )
        assert r.status_code == 200
        out_df = pd.DataFrame(r.json()["total_volumes"])
        out_df.columns = pd.Index(["time", "volume"])
        out_df["time"] = pd.to_datetime(out_df["time"], unit="ms")
        out_df["volume"] = out_df["volume"].astype(float)
        out_df.set_index("time", inplace=True)
        memo[token] = out_df
    return memo[token]


def get_dataframe_of_prices(token_list: List[str], num_days: int = 90, use_key: bool = True) -> pd.DataFrame:
    """
    returns a Pandas DataFrame with token price data going back num_days, for the given tokens
    e.g. get_dataframe_of_prices(["ATOM", "OSMO", "STRD"], 30) returns a DataFrame of 30 days of price data
    """
    # gather the dataframe
    df = {}
    for token in token_list:
        df[token] = get_token_price_history(token, num_days, use_key=use_key)["price"]
    df = pd.DataFrame(df)
    # resample based on how much data we're gathering
    if num_days > 90:
        df = df.resample("1D").last()
    elif num_days >= 2:
        df = df.resample("1H").last()
    else:
        df = df.resample("5min").last()
    return df


def get_dataframe_of_volumes(token_list: List[str], num_days: int = 90) -> pd.DataFrame:
    """
    returns a Pandas DataFrame with token volume data going back num_days, for the given tokens
    e.g. get_dataframe_of_volumes(["ATOM", "OSMO", "STRD"], 30) returns a DataFrame of 30 days of volume data
    """
    # gather the dataframe
    df = {}
    for token in token_list:
        df[token] = get_token_volume_history(token, num_days)["volume"]
    df = pd.DataFrame(df)
    # resample based on how much data we're gathering
    if num_days > 90:
        df = df.resample("1D").last()
    elif num_days >= 2:
        df = df.resample("1H").last()
    else:
        df = df.resample("5min").last()
    return df
