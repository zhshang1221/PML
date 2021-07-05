import sys
sys.path.append('..')

import numpy as NP
from typing import List
from decimal import Decimal as Dec

from agents import market_player as MP
from markets import uniswap_market as UM
from markets import reference_market as RM

class RandomTrader(MP.MarketPlayer):
    '''
    random traders enters uniswap market randomly, proceeding swaps
    '''

    def __init__(self, unique_id, model, reference_market: RM.ReferenceMarket, uniswap_market: UM.UniswapMarket):
        '''
        :param unique_id: unique id to identify every specific agent
        :param model: simulation model the agent involved
        :param reference_market: reference market the agent involved
        :param uniswap_market: uniswap market the agent involved
        '''
        MP.MarketPlayer.__init__(self, unique_id, model, reference_market, uniswap_market)


    def random_trade(self) -> None:
        '''
        swap in uniswap market
        :return: no return
        '''
        pass

    def step(self) -> None:
        '''
        randomly pick an trade according to random_trade
        :return: no return, dynamically adjust parameters
        '''
        self.random_trade()