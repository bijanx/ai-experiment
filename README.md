# ai-money

#### Goals:
- determine which strategies to trade and trade them

#### Glossary:
- Trade Rule: A rule that defines the entry and exit of a trade. A trade rule creates entry/exit Signals.
- Backtest: A simulation of trades on historical market data
- Signal: An action that is fired to enter/exit/modify a trade from a Trade Rule
- Trading Strategy: A system that receives market data and returns Orders
- Order: A decision emitted from Trading Strategies

#### Tables:
- accounts
- backtests
- orders
- strategies
- trades

#### Setup
```sh
git clone git@github.com:bpourriahi/ai-money.git
cd ai-money/sys
vagrant up
vagrant ssh
```
