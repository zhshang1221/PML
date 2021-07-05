from decimal import Decimal as Dec
from namedlist import namedlist

COIN_PRICE_VOLATILITY = Dec(0.01)
TOKENS = ['BTC', 'ETH']
TOKEN_NUM = len(TOKENS)
TokenInfo = namedlist('TokenInfo', TOKENS)