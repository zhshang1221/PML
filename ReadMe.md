## !! firstly
```
pip install -r requirement.txt
```

## `core`: core files for modelling
- `model_settings`: model parameters(constants mainly) inside
- `agent_settings`: settings for initializing agents
- `model_pml`: simulation model, tackle all other parts of this simulation framework
- `statistics`: dynamic information(agent info collector and model info collector) from the simulation model

## `agents`: agent behaviors inside, different agent written in different file
- `market_player`: super class for all agents, define common things(e.g. reservers, trading behaviors) inside
- `adviser`: our proactive liquidity management strategy, to optimize
- `other_liquidity_providers`: distribution of the total liquidity, apart from our contributions
- `random_trader`: Random traders enters uniswap market randomly, asking for tokens and carrying out swaps

## `markets`: market behaviors
- `reference_market`: price series generation
- `uniswap_market`: information & activities in Uniswap market

## `analysis`: data structure, analysis and visualization

