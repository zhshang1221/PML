import sys
sys.path.append('..')

import pandas as PD
import numpy as NP
from typing import Any
from mesa import Agent
from decimal import Decimal as Dec

from core import model_settings as MS
from markets import reference_market as RM
from markets import uniswap_market as UM

class MarketPlayer(Agent):
    '''super class for all different kinds of agents to inherit, note that reserves are all initialized with 0, and should be entitled with other values when adding into schedule(if not zero)'''
    def __init__(self, unique_id, model: Any, reference_market: RM.ReferenceMarket, uniswap_market: UM.UniswapMarket):
        '''
        initial market player, super class to be inherit by other specified agents
        :param unique_id: unique id to identify every agent
        :param model: simulation model
        :param reference_market: reference market the agent involved
        :param uniswap_market: uniswap pool the agent involved
        '''
        Agent.__init__(self, unique_id, model)
        self.unique_id = unique_id
        self.model = model
        self.fiat: Dec = Dec(NP.infty)
        self.tokens: MS.TokenInfo = MS.TokenInfo(*[Dec(1000.) for _ in MS.TOKENS])
        self.tokens_in_pool = MS.TokenInfo(*[Dec(0.0) for _ in MS.TOKENS])

        self.reference_market = reference_market
        self.uniswap_market = uniswap_market

        self.uniswap_positions = UM.UniswapPositions([])
        self.earnings = Dec(0.)
        self.gas_cost = Dec(0.)


    def ask_from_uniswap(self, ask_token: str, ask_num: Dec) -> None:
        '''
        ask tokens from uniswap pool
        :param ask_token: token type to buy
        :param ask_num: token num to buy
        :return: no return, update agent & uniswap conditions
        '''
        # after judging whether current agent could proceed this trading
        token_need = self.uniswap_market.swap_from(ask_token, ask_num)


    def mint_to_uniswap(self, base_token: str, base_num: Dec, tick_low: UM.Tick, tick_high: UM.Tick):
        '''
        mint liquidity to the uniswap pool
        :param base_token: given one token type and UniswapPosition, then we can get all tokens we need to deposit
        :param base_num: together with base_token to calculate total deposits
        :param tick_low: tick_low to deposit
        :param tick_high: tick_high to deposit
        :return: no return, update agent & uniswap conditions
        '''
        # after judging whether current agent could proceed this trading
        self.uniswap_market.mint(base_token, base_num, tick_low, tick_high)
        pass

    def burn_to_uniswap(self, base_token: str, base_num: Dec, tick_low: UM.Tick, tick_high: UM.Tick):
        '''same with the above one, but corresponding to burn liquidity'''
        pass