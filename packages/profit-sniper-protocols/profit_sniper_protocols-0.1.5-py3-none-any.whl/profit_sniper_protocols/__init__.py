# Copyright 2024 Takin Profit. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
from typing import Literal, Protocol
from uuid import UUID
from pydantic import BaseModel, Field

type OrderType = Literal["market", "limit", "stop", "stop_limit", "trailing_stop"]
"""
    The type of order to submit.
"""

type OrderSide = Literal["buy", "sell"]
"""
    The side of the market to place the trade on.
"""
type TimeInForce = Literal["day", "gtc", "opg", "cls", "ioc", "fok"]
"""
    Represents the various time in force options for an Order.

    - day: A day order is eligible for execution only on the day it is live.
    - gtc: The order is good until canceled.
    - opg: Use this TIF with a market/limit order type to submit "market on open" (MOO) and "limit on open" (LOO) orders. This order is eligible to execute only in the market opening auction. Any unfilled orders after the open will be cancelled.
    - cls: Use this TIF with a market/limit order type to submit "market on close" (MOC) and "limit on close" (LOC) orders. This order is eligible to execute only in the market closing auction. Any unfilled orders after the close will be cancelled.
    - ioc: An Immediate Or Cancel (IOC) order requires all or part of the order to be executed immediately. Any unfilled portion of the order is canceled.
    - fok: A Fill or Kill (FOK) order is only executed if the entire order quantity can be filled, otherwise the order is canceled.
    
"""

type OrderClass = Literal["simple", "bracket", "oco", "oto"]
"""
    Represents what class of order this is.
"""

type PositionIntent = Literal[
    "buy_to_open", "buy_to_close", "sell_to_open", "sell_to_close"
]
"""
    Represents what side this order was executed on.
    Used for alpaca.
    """


class TakeProfitRequest(BaseModel):
    """
    Used for providing take profit details for a bracket order.
    """

    limit_price: float = Field(
        ..., description="The execution price for exiting a profitable trade."
    )


class StopLossRequest(BaseModel):
    """
    Used for providing stop loss details for a bracket order.
    """

    stop_price: float = Field(
        ..., description="The price at which the stop loss is triggered."
    )
    limit_price: float | None = Field(
        default=None,
        description="The execution price for exiting a losing trade. If not provided, the stop loss will execute as a market order.",
    )


class OrderRequest(BaseModel):
    """A class for creating an order."""

    symbol: str = Field(
        ..., description="The symbol identifier for the asset being traded"
    )
    qty: float | None = Field(
        default=None,
        description="The number of shares to trade. Fractional qty for stocks only with market orders.",
    )
    notional: float | None = Field(
        default=None,
        description="The base currency value of the shares to trade. For stocks, only works with MarketOrders. Does not work with qty.",
    )
    side: OrderSide = Field(
        ..., description="Whether the order will buy or sell the asset."
    )

    limit_price: float | None = Field(
        default=None, description="The price at which the limit order will execute"
    )

    stop_price: float | None = Field(
        default=None,
        description="""stop_price (float): The price at which the stop order is converted to a market order
        or a stop limit order is converted to a limit order.""",
    )

    type: OrderType = Field(
        ..., description="The execution logic type of the order (market, limit, etc)."
    )
    time_in_force: TimeInForce = Field(
        ..., description="The expiration logic of the order."
    )
    order_class: OrderClass | None = Field(
        default=None,
        description="The class of the order. Simple orders have no other legs.",
    )
    extended_hours: bool | None = Field(
        default=None,
        description="Whether the order can be executed during regular market hours.",
    )
    client_order_id: str | None = Field(
        default=None,
        description="A string to identify which client submitted the order.",
    )
    take_profit: TakeProfitRequest | None = Field(
        default=None,
        description="For orders with multiple legs, an order to exit a profitable trade.",
    )
    stop_loss: StopLossRequest | None = Field(
        default=None,
        description="For orders with multiple legs, an order to exit a losing trade.",
    )
    position_intent: PositionIntent | None = Field(
        default=None,
        description="An enum to indicate the desired position strategy: BTO, BTC, STO, STC.",
    )

    trail_price: float | None = Field(
        default=None,
        description="The absolute price difference by which the trailing stop will trail.",
    )

    trail_percent: float | None = Field(
        default=None,
        description="The percent price difference by which the trailing stop will trail.",
    )


class ClosePositionRequest(BaseModel):
    """
    Attributes:
        qty (str): The number of shares to liquidate.
        percentage (str): The percentage of shares to liquidate.
    """

    symbol_or_asset_id: str | UUID = Field(
        ..., description="The symbol name of asset id of the position to close"
    )

    qty: str | None = Field(
        default=None, description="The number of shares to liquidate"
    )
    percentage: str | None = Field(
        default=None, description="The percentage of shares to liquidate"
    )


type Broker = Literal["pineconnector", "profitview", "alpaca", "phemex", "oanda"]


class ExecutionDefinition(BaseModel):
    """
    An ExecutionDefinition contains all of the data needed
    for a Broker plugin to execution actions on the said broker platform.
    """

    broker: Broker = Field(..., description="the broker used for execution.")

    trade_syntax: str | None = Field(
        default=None,
        description="""
        The trade syntax that is used for submitting the trade.
        This is only used if the broker is "pineconnector" or "profitview".
        Other brokers which use trade_syntax may be added in the future.
    """,
    )

    order_request: OrderRequest | None = Field(
        default=None, description="The order request, used to submit the order."
    )

    close_position_request: ClosePositionRequest | None = Field(
        default=None, description="The data used to close a position."
    )


class BrokerPlugin(Protocol):
    """
    A broker plugin is a class that is responsible for execution trades
    with a specific broker.
    """

    @property
    def broker(self) -> Broker:
        """
        The broker that the plugin uses for submitting trades.
        """
        ...
