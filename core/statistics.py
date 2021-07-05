'''dynamic information from the simulation model.'''

from mesa.datacollection import DataCollector
def create_data_collector() -> DataCollector:
    model_reporters = {}
    reference_market_reporters = {
        'price_btc': lambda model: model.reference_market.cached_price.BTC,
        'price_eth': lambda model: model.reference_market.cached_price.ETH
    }
    uniswap_market_reporters = {
        'uniswap_positions': lambda model: model.uniswap_market.uniwap_positions,
    }
    model_reporters.update(reference_market_reporters)
    model_reporters.update(uniswap_market_reporters)

    agent_reporters = {
        'unique_id': lambda agent: agent.unique_id,
        'type': lambda agent: agent.__class__,
        'earnings': lambda agent: agent.earnings,
        'agent': lambda agent: agent
    }

    return DataCollector(
        model_reporters=model_reporters,
        agent_reporters=agent_reporters
    )