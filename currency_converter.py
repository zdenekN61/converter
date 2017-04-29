"""Currency converter"""

import codecs
import json
import numbers as num
import os
import re
import sys
from modules.check_currency import CheckCurrency
from modules.json_out import json_out
from modules.help_me import HelpMe
from modules.url_reader import URLReader

__all__=["CurrencyConverter"]

class CurrencyConverter:
    def __init__(self, argv):
        self.currency = CheckCurrency()
        if not self.currency.table_ok:
            self._exit()
        self.help_me = HelpMe()
        self.output_json = json_out()
        self._params_processing(argv)

    # Params processing(what params, encode, check).
    def _params_processing(self, argv):
        if argv and len(argv) in range(5,8):
            _amount = -1
            _input_c = []
            _output_c = []
            for argv_item in range(0, len(argv)):
                if argv[argv_item] == "--amount":
                    _amount = argv[argv_item+1]
                elif argv[argv_item] == "--input_currency":
                    # [0] - original, [1] - encoded
                    _input_c.append(argv[argv_item+1])
                    _input_c.append(argv[argv_item+1].encode('UTF-8'))
                elif argv[argv_item] == "--output_currency":
                    if (argv_item+1) < len(argv):
                        # [0] - original, [1] - encoded
                        _output_c.append(argv[argv_item+1])
                        _output_c.append(argv[argv_item+1].encode('UTF-8'))
            # Processed params -> show them.
            p_amout, p_input, p_output = self._processed_params(_amount,
                                                                _input_c,
                                                                _output_c)
            # Converts amount.
            self._convert(p_amout, p_input, p_output)
            # Shows result.
            self._show()
        else:
            for argv_item in range(0, len(argv)):
                if argv[argv_item] == "--supported_currency":
                    print (self.help_me.supported_currency)
                    self._exit()

    # Check each valid param.
    def _processed_params(self, amount, input_c, output_c):
        _v_amount = -1
        _v_input_c = None
        _v_output_c = []
        finished_ok = False
        # Checks if amount is usable number.
        if str.isdigit(amount) or self._is_float(amount):
            _v_amount = float(amount)
        else:
            print (""">>>Wrong param 'amount', its not processable.\n""")
            self._help_tail()
        # Gets currency codes involved in the conversion.
        _v_input_c, _v_output_c = self.currency._currency_codes(input_c,
                                                                output_c)
        if _v_amount != -1 and _v_input_c and _v_output_c:
            finished_ok = True
        else:
            print ('>>>Wrong params, check them.\n')
            self._help_tail()
        return _v_amount, _v_input_c, _v_output_c

    # Converts the amount to output currency.
    def _convert(self, amount, c_in, c_out):
        url_reader = URLReader()
        # Sets the amount, input currency code.
        self.output_json['input']['amount'] = amount
        self.output_json['input']['currency'] = c_in
        # Sets output currency + converted amount.
        for item in c_out:
            ex_site = "http://www.x-rates.com/calculator/"
            url_l = "%s?from=%s&to=%s&amount=%.2f" % (ex_site, c_in, item,
                                                      amount)
            value_out = url_reader.get_url_response(url_l)
            if value_out['status'] == 200 and value_out['body']:
                new_amount = self._get_new_amount(value_out['body'])
                if  new_amount:
                    self.output_json['output'][item] = new_amount

    # Parses a new amount from a url response.
    def _get_new_amount(self, raw_text):
        ret_amount = None
        founded = re.findall(r'<span class="ccOutputRslt">(.*?)<span', raw_text)
        if founded:
            ret_amount = founded[0]
        return ret_amount

    # Shows the output.
    def _show(self):
        _json_out = json.dumps(self.output_json)
        print (_json_out)
    
    # Help globall tail.
    def _help_tail(self):
        print (self.help_me.how_to)
        self._exit()

    # Its float number?
    def _is_float(self, input_str):
        ret_status = True
        try:
            float(input_str)
        except:
            ret_status = False
        return ret_status

    def _exit(self):
        sys.exit()

if __name__=='__main__':
    converter = CurrencyConverter(sys.argv)


