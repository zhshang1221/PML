import copy
from typing import Dict
from decimal import Decimal as Dec
from core import model_settings as MS

def get_defaults() -> Dict:
    '''generates setting parameters for agents'''
    settings = {
        'AgentType': {
            # these are normalised to total 1 later
            'Adviser': 3, # different parameters for the same kind of agent
            'RandomTrader': 5, # different type of random traders differ from their trading preferences
            'OtherLiquidityProviders': 1, # other liquidity providers share the same account
        },
        'AgentNum': {
            # num of agents in specific kind and specific type
            'Adviser': 1,
            'RandomTrader': 3,
            'OtherLiquidityProviders': 1
        },
        'AgentScope': { # parameter options for agent variety
            'Adviser': [],
            'RandomTrader': [],
            'OtherLiquidityProviders': []
        },
        'AgentDescriptions': {
            "Adviser": "Our adviser for proactive liquidity management",
            "RandomTrader": "Random traders enters uniswap market randomly, asking for tokens and carrying out swaps",
            "OtherLiquidityProviders": "",
        }
    }
    return copy.deepcopy(settings)