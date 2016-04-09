# ai-money

- Trade Rule: A rule that defines the entry and exit of a trade. A trade rule creates entry/exit Signals.
- Backtest: A simulation of trades on historical market data
- Signal: An action that is fired to enter/exit/modify a trade from a Trade Rule
- Trading Strategy: A system that receives market data and returns Orders
- Order: A decision emitted from Trading Strategies

Tables:
- accounts
- backtests

- orders
- strategies
- trades

Business Operations:
- backtest a trading strategy and store the results of the backtest
- create a trading strategy with just a trade rule
