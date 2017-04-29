# Currency converter

## Author
	Zdenek Novotny

## Development environment:

	Windows 10 Home
	Vim 7.4
	Python 3.5.3


## Params
- --amount - amount of money to convert - float
- --input_currency - input currency - 3 letter name or symbol
- --output_currency - requested/output currency - 3 letters or symbol

## Output
```
{
    "input": { 
        "amount": <float>,
        "currency": <3 letter-currency_code>
    }
    "output": {
        <3 letter-currency_code>: <float>
    }
}
```

## Examples(tested inputs):

	./currency_converter.py --amount 100.0 --input_currency EUR --output_currency CZK
	./currency_converter.py --amount 0.9 --input_currency Y --output_currency AUD
	./currency_converter.py --amount 10.92 --input_currency L
	./currency_converter.py --amount 100.0 --input_currency Y --output_currency L
	./currency_converter.py --amount 100.0 --input_currency Y --output_currency
	./currency_converter.py --amount 100.0 --input_currency Y --output_currency t
	./currency_converter.py --amount 100.0 --input_currency t --output_currency L
	./currency_converter.py --amount nic --input_currency Y --output_currency L
	./currency_converter.py --supported_currency
