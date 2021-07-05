import sys
sys.path.append('..')

from decimal import Decimal as Dec

from agents import market_player as MP
from markets import uniswap_market as UM
from markets import reference_market as RM
from core import model_settings as MS

class Adviser(MP.MarketPlayer):
    '''
    our strategy, to optimize
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
        how to allocate liquidity
        :return: no return
        '''
        current_price = self.reference_market.cached_price
        # self.mint_to_uniswap()

    def step(self):
        self.allocate_liquidity()