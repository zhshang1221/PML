import sys
sys.path.append('..')

from typing import List
from decimal import Decimal as Dec
import numpy as NP
NP.random.seed(123)

from core import model_settings as MS

class ReferenceMarket:
    '''reference market to trade, assume there is no price spread at first'''

    def __init__(self, drift: Dec, vol: Dec):
        '''
        :param drift: drift for price update
        :param vol: volatility for price update
        '''
        self.numeraire = 'USD' # define numeraire
        self.tokens = MS.TOKENS
        self.drift: MS.TokenInfo = MS.TokenInfo(*[drift for _ in MS.TOKENS])
        self.variance: MS.TokenInfo = MS.TokenInfo(*[vol for _ in MS.TOKENS])
        self.initialize_price()

    def initialize_price(self) -> None:
        '''generate initial price for the tokens, directly entitled without return'''
        self.cached_price: MS.TokenInfo = MS.TokenInfo(*[Dec(NP.random.uniform(10, 100)) for _ in MS.TOKENS])

    def generate_next_price(self) -> None:
        '''generate toekn prices for next time stamp'''
        result_list: List[Dec] = []
        for token_index in range(len(self.cached_price)):
            # price_new = price_old * exp(sigma * normal distributed x)
            new_price: Dec = self.cached_price[token_index] * Dec.exp(self.drift[token_index] + self.variance[token_index] * Dec(NP.random.normal()))
            result_list.append(Dec(new_price))

        self.cached_price = MS.TokenInfo(*result_list)

    @property
    def current_price(self) -> MS.TokenInfo:
        '''return current price of all available tokens'''
        return self.cached_price

if __name__ == '__main__':
    test_reference_market = ReferenceMarket(Dec(0), Dec(0.3))
    print('In the first time stamp:\n-----------------------------\n', test_reference_market.cached_price)
    test_reference_market.generate_next_price()
    print('\nIn the second time stamp:\n-----------------------------\n', test_reference_market.cached_price)
