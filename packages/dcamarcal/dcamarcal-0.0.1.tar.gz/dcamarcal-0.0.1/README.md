# dcamarcal

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

DCA Martingale strategy calculator.

## Overview

`dcamarcal` is a Python library designed to support the analysis of martingale-based DCA strategies in the cryptocurrency market by calculating order tables.

## Features

The library is developed with the following key features in mind:

- **No dependencies:** Does not use any external library.
- **High precision:** Uses `decimal` module enhance precision.
- **Bidirectional:** Support both long and short martingale-based DCA strategies.

## Examples

Basic usage:

```python
from dcamarcal.calculator import DCAMartingale, Direction, round_order_list, print_tabular

dca = DCAMartingale.from_float(
    direction=Direction.long, # or Direction.short
    base_order_size=20,       # initial order size 
    order_size=20,            # starting size for subsequent orders
    max_orders=8,             # max number of orders
    price_deviation=1.2,      # deviation required to trigger the next order
    target_profit=1.2,        # profit required to close the position
    order_scale=1.2,          # scaling factor for order deviation
    volume_scale=1.5,         # scaling factor for order size
    minimum_trade_decimals=5, # minimum number of decimals allowed in the market
)

result = dca.calculate_table(1) # starting price
result = round_order_list(result) # round to default 8 decimals
print_tabular(result) # display the table
```

> **Note:** The `minimum_trade_decimals` parameter should match the requirements of your chosen exchange.

That generates the following order table:

| Order | Deviation   | Size         | Volume       | Price      | Average Price | Required Price | Required Change | Total Size    | Total Volume  |
|-------|-------------|--------------|--------------|------------|---------------|----------------|-----------------|---------------|---------------|
| 0     | 0.000000000 | 20.000000000 | 20.000000000 | 1.00000000 | 1.00000000000 | 1.012000000000 | 1.2000000000000 | 20.0000000000 | 20.0000000000 |
| 1     | 1.200000000 | 20.242914980 | 20.000000000 | 0.98800000 | 0.99396378000 | 1.005800000000 | 1.8016194300000 | 40.2429149800 | 40.0000000000 |
| 2     | 2.640000000 | 30.813475760 | 30.000000000 | 0.97360000 | 0.98513307000 | 0.996900000000 | 2.3931799500000 | 71.0563907400 | 70.0000000000 |
| 3     | 4.368000000 | 47.055378950 | 45.000000000 | 0.95632000 | 0.97365403000 | 0.985300000000 | 3.0303664000000 | 118.111769690 | 115.000000000 |
| 4     | 6.441600000 | 72.147450150 | 67.500000000 | 0.93558400 | 0.95921764000 | 0.970700000000 | 3.7533775700000 | 190.259219840 | 182.500000000 |
| 5     | 8.929920000 | 111.17811690 | 101.25000000 | 0.91070080 | 0.94132334000 | 0.952600000000 | 4.6007646000000 | 301.437336740 | 283.750000000 |
| 6     | 11.91590400 | 172.42045602 | 151.87500000 | 0.88084096 | 0.91931589000 | 0.930300000000 | 5.6149795800000 | 473.857792750 | 435.625000000 |
| 7     | 15.49908480 | 269.59767177 | 227.81250000 | 0.84500915 | 0.89237020000 | 0.903000000000 | 6.8627479200000 | 743.455464520 | 663.437500000 |
| 8     | 19.79890176 | 426.07739482 | 341.71875000 | 0.80201098 | 0.85945106000 | 0.869700000000 | 8.4399115600000 | 1169.53285934 | 1005.15625000 |

## Current issues

- The `print_tabular` function currently pads numbers with additional zeroes to align table columns, which might lead to visual inconsistency in decimal places.
