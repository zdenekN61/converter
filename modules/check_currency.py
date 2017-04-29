"""Check currency"""

import os
import re
from modules.currency import CURRENCY_BYTECODE
from modules.currency import CURRENCY_CODE
from modules.currency import CURRENCY_NAME

__all__ = ["json_out"]

class CheckCurrency:
    def __init__(self):
        self.table_ok = self._check_currency_tables()

    # Main call.
    def _currency_codes(self, c_in, c_out):
        c_in_code = None
        c_out_code = None
        c_in_code = self._currency_in_check(c_in)
        # Checks if input is ok, otherwise do not continue.
        if c_in_code:
            c_out_code = self._currency_out_check(c_out, c_in_code)
        return c_in_code, c_out_code

    def _check_currency_tables(self):
        tables_ok = True
        c_table_count = []
        c_table_count.append(len(CURRENCY_CODE))
        c_table_count.append(len(CURRENCY_BYTECODE))
        c_table_count.append(len(CURRENCY_NAME))
        if c_table_count.count(c_table_count[0]) < 3:
            print (">>>Currency tables(currency.py) are not same(size-index). "
                   "Check them.\n")
            tables_ok = False
        return tables_ok

    # Checks input currency, return a proper code.
    def _currency_in_check(self, c_in):
        tmp_c_in = self._find_currency(c_in, 'input currency')
        ret_c_in_code = None
        if tmp_c_in:
            ret_c_in_code = CURRENCY_CODE[tmp_c_in]
        else:
            print ('\n>>>Unknown input currency, try again.\n')
        return ret_c_in_code

    # Checks output currency, return proper code(s).
    def _currency_out_check(self, c_out, c_in):
        ret_c_out_codes = []
        if not c_out:
            ret_c_out_codes = list(set(CURRENCY_CODE)-set([c_in]))
        else:
            tmp_c_out = self._find_currency(c_out, 'output currency')
            if tmp_c_out:
                ret_c_out_codes.append(CURRENCY_CODE[tmp_c_out])
        if not ret_c_out_codes:
            print ('\n>>>Unknown output currency, try again.\n')
        return ret_c_out_codes

    # Finds currency code in tables(from string, bytecode)
    def _find_currency(self, currency, spec_currency):
        county = 0
        c_index = None
        ret_currency = None
        # Checks encoded first.
        if currency[1] in CURRENCY_BYTECODE:
            county = CURRENCY_BYTECODE.count(currency[1])
            c_index = self._find_currency_index(currency[1], CURRENCY_BYTECODE)
        # Checks currency code table.
        elif currency[0] in CURRENCY_CODE:
            county = CURRENCY_BYTECODE.count(currency[0])
            c_index = self._find_currency_index(currency[0], CURRENCY_CODE)
        if c_index:
            if county > 1:
                ret_currency = self._more_variants(c_index, spec_currency)
            else:
                ret_currency = c_index[0]
        return ret_currency
    
    # Finds index in the table.
    def _find_currency_index(self, currency, table):
        table_index = []
        for pos, item in enumerate(table):
            if item == currency:
                table_index.append(pos)
        return table_index

    # More variants, gives user way to choose.
    def _more_variants(self, code_index, spec_currency):
        title = "Specifiy %s more precisely:" % spec_currency
        print (title)
        for item in range(0, len(code_index)):
            line = "[%s]: %s = %s" % (item, 
                    CURRENCY_CODE[code_index[item]],
                    CURRENCY_NAME[code_index[item]])
            print (line)
        print ('\nYour choose(Choose number in brackets):')
        choose = input()
        choosen_index = None
        if str.isdigit(choose):
            if int(choose) in range(0, len(code_index)):
                choosen_index = code_index[int(choose)]
        return choosen_index


