import sys
sys.path.append('..')

import numpy as NP
import pandas as PD
from typing import Tuple, List
from decimal import Decimal as Dec

from agents import market_player as MP
from markets import uniswap_market as UM
from markets import reference_market as RM
from core import model_settings as MS

class OtherLiquidityProvider(MP.MarketPlayer):
    '''
    distribution of liquidity, apart from ours
    '''

    def __init__(self, unique_id, model, reference_market: RM.ReferenceMarket, uniswap_market: UM.UniswapMarket):
        '''
        :param unique_id: unique id to identify every specific agent
        :param model: simulation model the agent involved
        :param reference_market: reference market the agent involved
        :param uniswap_market: uniswap market the agent involved
        '''
        MP.MarketPlayer.__init__(self, unique_id, model, reference_market, uniswap_market)


    def allocate_liquidity(self) -> None:
        '''
        dynamically adjust liquidity in pool
        '''
        pass

    def step(self) -> None:
        self.allocate_liquidity()