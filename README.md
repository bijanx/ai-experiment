# ai-money
[Backlog](https://trello.com/b/JIK5gFh8/tradesys)

#### Goals
- determine which strategies to trade and trade them

#### Glossary
- Backtest: A simulation of trades on historical market data
- Order: A decision emitted from Trading Strategies
- Signal: An action that is fired to enter/exit/modify a trade from a Trade Rule
- Trade Rule: A rule that defines the entry and exit of a trade. A trade rule creates entry/exit Signals.
- Trading Strategy: A system that receives market data and returns Orders

#### Tables
- accounts
- backtests
- broker_interaction
- data_source_interaction
- orders
- signals
- strategies
- trades

#### Subsystems
- backtesting
- broker API integration
- cronjobs
- deployment
- live trading
- portfolio optimization
- real-time market data collection
- testing and quality assurance

#### Setup
```sh
git clone git@github.com:bpourriahi/ai-money.git
cd ai-money/sys
vagrant up
vagrant ssh
```
