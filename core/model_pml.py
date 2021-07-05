import sys
sys.path.append('..')
import warnings
warnings.filterwarnings('ignore')
from mesa import Model
from mesa.time import RandomActivation

import numpy as NP
from typing import Dict, Any
from decimal import Decimal as Dec

from core import statistics as SS
from core import model_settings as MS
from core import agent_settings as AS
from markets import reference_market, uniswap_market
from agents import adviser, random_traders, other_liquidity_providers

class ModelPML(Model):
    '''customized agent-based simulation platform'''

    def __init__(self, reference_market_settings: Dict[str, Any], agent_settings: Dict[str, Any]):
        '''
        :param reference_market_settings: settings when initializing reference market
            -- drift: drift when updating price in reference market
            -- vol: volatility when updating price in reference market
        :param agent_settings: settings for initializing agents, see agent_settings.py for more details
            -- AgentType, AgentNum, AgentScope: Adviser, RandomTrader, OtherLiquidityProviders
        '''
        Model.__init__(self)
        self.data_collector = SS.create_data_collector()
        self.reference_market = reference_market.ReferenceMarket(reference_market_settings['drift'], reference_market_settings['vol'])
        self.uniswap_market = uniswap_market.UniswapMarket()
        self.agent_settings = agent_settings
        self.schedule = RandomActivation(self)
        self.create_agents()

    def create_agents(self):
        '''create clients for simulation use, setting paras coming from self.agent_settings'''
        global_unique_id = 0
        agent_settings = self.agent_settings.copy()

        my_adviser = adviser.Adviser(global_unique_id, self, self.reference_market, self.uniswap_market)
        self.schedule.add(my_adviser)
        global_unique_id += 1

        # add other type of market players
        pass


    def step(self):
        self.data_collector.collect(self)
        self.schedule.step()
        self.reference_market.generate_next_price()

    def run_model(self):
        for step_index in range(400):
            print(f'\nProceeding step {step_index}')
            self.step()

if __name__ == '__main__':
    toy_model = ModelPML(reference_market_settings={'drift': Dec(0.0), 'vol': Dec(0.01)}, agent_settings=AS.get_defaults())
    toy_model.run_model()
    import os
    if not os.path.exists('model_info'):
        os.makedirs('model_info')
    if not os.path.exists('agent_info'):
        os.makedirs('agent_info')
    price_info = toy_model.data_collector.get_model_vars_dataframe()
    price_info.to_csv('./model_info/market_info.csv')
    agent_info = toy_model.data_collector.get_agent_vars_dataframe()

    # generate pnl information
    for agent_index in range(int(len(agent_info) / len(price_info))):
        test_single_agent_info = PA.generate_agent_info(price_info, agent_info, agent_index)
        file_name = str(agent_info['agent'].values[agent_index].__class__).split('.')[-1][: -2] + '_' + str(agent_index) + '.csv'
        test_single_agent_info.to_csv('./agent_info/' + file_name)

    import matplotlib.pyplot as plt