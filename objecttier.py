import datatier
import csv
import re

class Statement:
    def __init__(self, D, PD, Desc, Amt, Tp, Bal, CorS):
        self._details = D
        self._posting_date = PD
        self._description = Desc
        self._amount = Amt
        self._type = Tp
        self._balance = Bal
        self._check_or_slip = CorS
        