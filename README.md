# ai-money
**Phase 1**  
- [ ] Trading Agents
- [ ] Tradings Agents Updater (Collect mock broker interfaces to test system)

**Phase 2**  
- [ ] DataCollector
- [ ] Deployment
- [ ] Staging Environment
- [ ] Production Environment
- [ ] Broker Interaction

#### Setup
```sh
git clone git@github.com:bpourriahi/ai-money.git
cd ai-money/sys
vagrant up
vagrant ssh
```

#### Glossary
- *Backtest*: A simulation of trades on historical market data
- *ClassificationFilter*: A binary classification function that a TradingStrategy uses to filter its signals
- *Feature*: A data mining feature. A calculation meant to represent measure of some concept of interest
- *Order*: A decision emitted from a TradingStrategy
- *Signal*: An action that is emitted by a TradeRule to enter/exit/modify a trade
- *TradeRule*: A rule that defines the entry and exit of a trade. A TradeRule creates entry/exit Signals
- *TradingStrategy*: Utilizes a trade rule and the option to apply a ClassificationFilter

#### Data Entities
- accounts
- backtests
- broker_interaction
- classification_filters
- data_source_interaction
- orders
- signals
- trading_strategies
- trades
