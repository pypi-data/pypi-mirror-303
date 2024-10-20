from dataclasses import dataclass, field, InitVar, asdict
from decimal import Decimal, ROUND_DOWN, ROUND_UP
from typing import List
from enum import Enum

def _to_decimal(value: float) -> Decimal:
    if isinstance(value, Decimal):
        return value
    return Decimal(str(value))


def round_decimal_values(d, precision=8) -> Decimal:
    for key, value in d.items():
        if isinstance(value, Decimal):
            d[key] = round(value, precision)
    return d


def truncate(number: Decimal, direction: Decimal, decimals: int=0) -> Decimal:
    if decimals < 0:
        raise ValueError('decimals must be >= 0')
    str_format = "{0:.%sf}" % decimals
    if direction == 1:
        return Decimal(str_format.format(number.quantize(Decimal('1e' + str(-decimals)), rounding=ROUND_DOWN)))
    else:
        return Decimal(str_format.format(number.quantize(Decimal('1e-' + str(decimals)), rounding=ROUND_UP)))


@dataclass
class DCAMartingaleOrder:
    order: int
    deviation: Decimal
    size: Decimal
    volume: Decimal
    price: Decimal
    average_price: Decimal
    required_price: Decimal
    required_change: Decimal
    total_size: Decimal
    total_volume: Decimal

    @classmethod
    def from_float(cls, order: int, deviation: float, size: float, volume: float, price: float, average_price: float, required_price: float, required_change: float, total_size: float, total_volume: float):
        return cls(
            order,
            _to_decimal(deviation), 
            _to_decimal(size), 
            _to_decimal(volume), 
            _to_decimal(price), 
            _to_decimal(average_price), 
            _to_decimal(required_price), 
            _to_decimal(required_change), 
            _to_decimal(total_size),
            _to_decimal(total_volume)
        )

    @property
    def deviation_float(self) -> float:
        return float(self.deviation)
    
    def set_float_deviation(self, value: float):
        self.deviation = Decimal(str(value))

    @property
    def size_float(self) -> float:
        return float(self.size)
    
    def set_float_size(self, value: float):
        self.size = Decimal(str(value))
    
    @property
    def volume_float(self) -> float:
        return float(self.volume)
    
    def set_float_volume(self, value: float):
        self.volume = Decimal(str(value))

    @property
    def price_float(self) -> float:
        return float(self.price)
    
    def set_float_price(self, value: float):
        self.price = Decimal(str(value))
    
    @property
    def average_price_float(self) -> float:
        return float(self.average_price)
    
    def set_float_average_price(self, value: float):
        self.average_price = Decimal(str(value))
    
    @property
    def required_price_float(self) -> float:
        return float(self.required_price)
    
    def set_float_required_price(self, value: float):
        self.required_price = Decimal(str(value))
    
    @property
    def required_change_float(self) -> float:
        return float(self.required_change)
    
    def set_float_required_change(self, value: float):
        self.required_change = Decimal(str(value))
    
    @property
    def total_size_float(self) -> float:
        return float(self.total_size)
    
    def set_float_total_size(self, value: float):
        self.total_size = Decimal(str(value))
    
    @property
    def total_volume_float(self) -> float:
        return float(self.total_volume)
    
    def set_float_total_volume(self, value: float):
        self.total_volume = Decimal(str(value))


def round_order_list(data: List[DCAMartingaleOrder], decimal_places: int=8) -> List[DCAMartingaleOrder]:
    rounded = [round_decimal_values(vars(row), decimal_places) for row in data]
    return [DCAMartingaleOrder(**row) for row in rounded]


def format_decimal_print(value: Decimal, column_width: int) -> str:
    if value == 0 or value == Decimal('0E-8'):
        value = Decimal('0.0')
    s = str(value)
    left, right = s.split('.') if '.' in s else (s, '0')
    right_length = column_width - len(left)
    right = right.ljust(right_length - 1, '0')
    return f"{left}.{right}"


def print_tabular(orders: List[DCAMartingaleOrder]):
    headers = ["Order", "Deviation", "Size", "Volume", "Price", "Average Price", "Required Price", "Required Change", "Total Size", "Total Volume"]
    rows = [list(asdict(order).values()) for order in orders]
    all_rows = [headers] + rows
    max_lengths = [max(len(str(row[i])) for row in all_rows) for i in range(len(headers))]
    formatted_data_rows = []
    for row in rows:
        formatted_row = []
        for i, item in enumerate(row):
            if i == 0:
                formatted_row.append(str(item).rjust(max_lengths[i]))
            else:
                formatted_row.append(format_decimal_print(item, max_lengths[i]))
        formatted_data_rows.append(formatted_row)

    formatted_headers = [header.center(max_lengths[i]) for i, header in enumerate(headers)]

    print('   '.join(formatted_headers))
    for row in formatted_data_rows:
        print('   '.join(row))


class Direction(Enum):
    long = 1
    short = -1


@dataclass
class DCAMartingale():
    direction: InitVar[Direction]
    base_order_size: Decimal
    order_size: Decimal
    max_orders: int
    price_deviation: Decimal
    target_profit: Decimal
    order_scale: Decimal
    volume_scale: Decimal
    minimum_trade_decimals: int
    
    initial_price: Decimal = field(default=Decimal(1), init=False)
    _direction: Decimal = field(default=1, init=False)

    def __post_init__(self, direction: Direction):
        attributes = {
            'base_order_size': self.base_order_size,
            'order_size': self.order_size,
            'price_deviation': self.price_deviation,
            'target_profit': self.target_profit,
            'order_scale': self.order_scale,
            'volume_scale': self.volume_scale,
        }
    
        if not isinstance(direction, Direction):
            raise TypeError("direction must be an instance of Direction")
        if direction == Direction.long:
            self._direction = Decimal(1)
        elif direction == Direction.short:
            self._direction = Decimal(-1)
        else:
            raise ValueError("direction must be either long or short")

        for attr, value in attributes.items():
            if not isinstance(value, Decimal):
                raise TypeError(f"{attr} must be an instance of Decimal. If you want to use float, use the method from_float")
            if value <= 0:
                raise ValueError(f"{attr} must be greater than 0")
            
    @classmethod
    def from_float(cls, direction: Direction, base_order_size: float, order_size: float, max_orders: int, price_deviation: float, target_profit: float, order_scale: float, volume_scale: float, minimum_trade_decimals: int):
        return cls(
            direction, 
            _to_decimal(base_order_size), 
            _to_decimal(order_size), 
            max_orders,
            _to_decimal(price_deviation), 
            _to_decimal(target_profit), 
            _to_decimal(order_scale), 
            _to_decimal(volume_scale),
            minimum_trade_decimals
        )

    @property
    def base_order_size_float(self) -> float:
        return float(self.base_order_size)

    def set_float_base_order_size(self, value: float):
        self.base_order_size = Decimal(str(value))

    @property
    def order_size_float(self) -> float:
        return float(self.order_size)

    def set_float_order_size(self, value: float):
        self.order_size = Decimal(str(value))

    @property
    def price_deviation_float(self) -> float:
        return float(self.price_deviation)

    def set_float_price_deviation(self, value: float):
        self.price_deviation = Decimal(str(value))

    @property
    def target_profit_float(self) -> float:
        return self.target_profit

    def set_float_target_profit(self, value: float):
        self.target_profit = Decimal(str(value))

    @property
    def order_scale_float(self) -> float:
        return float(self.order_scale)

    def set_float_order_scale(self, value: float):
        self.order_scale = Decimal(str(value))

    @property
    def volume_scale_float(self) -> float:
        return self.volume_scale

    def set_float_volume_scale(self, value: float):
        self.volume_scale = Decimal(str(value))

    @property
    def initial_price_float(self) -> float:
        return float(self.initial_price)

    def set_float_initial_price(self, value: float):
        self.initial_price = Decimal(str(value))

    def _calculate_required_price(self, average_price: Decimal) -> Decimal:
        return average_price * (Decimal(1) + self._direction * self.target_profit / Decimal(100))
    
    def _calculate_required_change(self, price: Decimal, required_price: Decimal) -> Decimal:
        return  (required_price / price - Decimal(1)) * Decimal(100)
    
    def _calculate_price(self, deviation: Decimal) -> Decimal:
        return self.initial_price - self._direction * self.initial_price * (deviation * Decimal(0.01))

    def calculate_table(self, price: float) -> List[DCAMartingaleOrder]:
        self.set_float_initial_price(price)
        table = []
        order = 0
        deviation = Decimal(0)
        size = self.base_order_size / self.initial_price
        volume = self.initial_price * size
        price = self.initial_price
        average_price = price
        required_price = truncate(self._calculate_required_price(average_price), self._direction, self.minimum_trade_decimals)
        required_change = self._calculate_required_change(price, required_price)
        total_size = size
        total_volume = volume
        row = DCAMartingaleOrder(order, deviation, size, volume, price, average_price, required_price, required_change, total_size, total_volume)
        table.append(row)

        for i in range(1, self.max_orders + 1):
            order = i
            deviation = table[i - 1].deviation * self.order_scale + self.price_deviation
            price = self._calculate_price(deviation)
            volume_aux = self.order_size * self.volume_scale**Decimal((i - 1))
            size = volume_aux / price
            volume = size * price
            total_size = table[i - 1].total_size + size
            total_volume = table[i - 1].total_volume + volume
            average_price = total_volume / total_size
            required_price = truncate(self._calculate_required_price(average_price), self._direction, self.minimum_trade_decimals)
            required_change = self._calculate_required_change(price, required_price)
            row = DCAMartingaleOrder(order, deviation, size, volume, price, average_price, required_price, required_change, total_size, total_volume)
            table.append(row)

        return table
