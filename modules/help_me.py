"""Help"""

import os
from modules.currency import *

__all__ = ["HelpMe"]

class HelpMe:
    def __init__(self):
        self.how_to = self._how_to()
        self.supported_currency = self._supported_currency()

    # Shows how to do it.
    def _how_to(self):
        how_to = (">>>HOW TO:<<<\n\n"
                  "File:\n"
                  "=====\n"
                  "currency_converter.py\n"
                  "Params:\n"
                  "=======\n"
                  "    --input_currency - requested - 3 letters name or\n"
                  "                                   currency symbol\n"
                  "    --output_currency - optional - 3 letters name or\n"
                  "                                   currency symbol\n"
                  "Example:\n"
                  "========\n"
                  " ./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK\n"
                  " python currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK\n"
                  "----------------------------------------------------------------------------------------\n"
                  "Do not know currency shortcut(code)?\n\n"
                  "./currency_converter.py --supported_currency\n"
                  "python currency_converter.py --supported_currency\n")
        return how_to

    # Supported currency.
    def _supported_currency(self):
        supp_c = (">>>Supported currency:<<<\n"
                 "===================:\n"
                 "CODE:   NAME:\n"
                 "=====   =====\n")
        for item in range(0, len(CURRENCY_BYTECODE)):
            supp_c += "%s  =  %s\n" % (CURRENCY_CODE[item], CURRENCY_NAME[item])
        return supp_c
