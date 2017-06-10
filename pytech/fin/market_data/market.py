import datetime as dt

import pytech.data.reader as reader
import pytech.utils.dt_utils as dt_utils


class Market(object):
    _shared_state = None

    def __init__(self, ticker: str = 'SPY',
                 source: str = 'google',
                 start_date: dt.datetime = None,
                 end_date: dt.datetime = None):
        if self._shared_state is None:
            self._shared_state = self.__dict__
            start_date, end_date = dt_utils.sanitize_dates(start_date,
                                                           end_date)
            self.ticker = ticker
            self.start_date = start_date
            self.end_date = end_date
            self.data = reader.get_data(self.ticker, source,
                                        self.start_date, self.end_date)[ticker]
        else:
            self.__dict__ = self._shared_state