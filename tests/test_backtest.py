import pytest
from pytech.backtest.backtest import Backtest
from pytech.algo.strategy import BuyAndHold, CrossOverStrategy
import datetime as dt


class TestBacktest(object):

    def test_backtest_constructor(self, ticker_list):

        initial_capital = 100000
        # start_date = '2016-03-10'
        start_date = dt.datetime(year=2016, month=3, day=10)
        backtest = Backtest(ticker_list=ticker_list,
                            initial_capital=initial_capital,
                            start_date=start_date,
                            strategy=CrossOverStrategy)

        assert isinstance(backtest, Backtest)
        backtest._run()


