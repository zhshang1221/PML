from typing import List, Union
from decimal import Decimal as Dec
import numpy as NP
NP.random.seed(123)

import sys
sys.path.append('..')
from core import model_settings as MS

class Tick:
    '''tick in uniswap V3'''
    def __init__(self, ith):
        '''
        :param ith: location of the Tick
        '''
        self.ith: int = ith
        self.cal_price()

    def cal_price(self) -> None:
        '''
        calculate price under given tick_location: ith
        :return: no return, entitle directly
        '''
        self.tick_price = 1.0001 ** self.ith

class UniswapPosition:
    '''position in uniswap v3'''
    def __init__(self, tick_low: Tick, tick_high: Tick,
                 tokens_deposit: MS.TokenInfo):
        '''
        :param tick_low: low tick of the position
        :param tick_high: high tick of the position
        :param tokens_deposit: tokens deposit when creating such position
        '''
        self.tick_low = tick_low
        self.tick_high = tick_high
        self.tokens_deposit = tokens_deposit
        self.cal_virtual_liquidity()

    def cal_virtual_liquidity(self) -> MS.TokenInfo:
        '''calculate virtual liquidity under given parameters'''
        pass

class UniswapPositions(list):
    '''positions in uniswap v3, inherit from list, UniswapPosition inside'''
    def __init__(self, *args):
        list.__init__(*args)
        pass

class UniswapMarket:
    '''Uniswap market liquidity pool, reserves information and some trading related functions inside'''

    def __init__(self):
        self.fee_rate = Dec(0.003)
        self.gamma = Dec(1) - Dec(self.fee_rate)

        self.uniswap_positions = UniswapPositions([])
        self.uncollected_fees = Dec(0.)
        self.token_pairs = MS.TOKENS

    def swap_from(self, from_token: str, from_num: Dec) -> Dec:
        '''
        swap operation in the uniswap pool, return token num to get, simultaneously update the pool conditions
        :param from_token: from which token to swap, i.e. deposit token type
        :param from_num: token nums to deposit
        :return: token num of the other token in pool
        '''
        pass

    def swap_to(self, to_token: str, to_num: Dec) -> Dec:
        '''
        same with the above function but with which & how many tokens to get instead
        :param to_token: which type of token to get
        :param to_num: how many tokens to get
        :return: token need to deposit, Dec
        '''
        pass

    def mint(self, base_token: str, base_num: Dec, tick_low: Tick, tick_high: Tick) -> MS.TokenInfo:
        '''
        mint liquidity in the uniswap pool
        :param base_token: given one token type and UniswapPosition, then we can get all tokens we need to deposit
        :param base_num: together with base_token to calculate total deposits
        :param tick_low: tick_low to deposit
        :param tick_high: tick_high to deposit
        :return: total deposits info.
        '''
        pass

    def burn(self, base_token: str, base_num: Dec, tick_low: Tick, tick_high: Tick) -> MS.TokenInfo:
        '''same with the above one, but corresponding to burn liquidity'''
        pass


if __name__ == '__main__':
    pass