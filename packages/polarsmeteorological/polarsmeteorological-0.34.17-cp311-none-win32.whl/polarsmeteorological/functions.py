from __future__ import annotations

import re
import sys
from datetime import date
from typing import TYPE_CHECKING, Literal, Sequence

import polars as pl
from polars.utils.udfs import _get_shared_lib_location

from polarsmeteorological.utils import parse_into_expr


if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

if TYPE_CHECKING:
    from polars.type_aliases import IntoExpr

lib = _get_shared_lib_location(__file__)

if TYPE_CHECKING:
    from polars import Expr

def celsius_to_fahrenheit(temperature: str | pl.Expr, ) -> pl.Expr:
    """
    Converts celsius to fahrenheit degrees
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="celsius_to_fahrenheit",
        args=[],
        is_elementwise=True,
    )

def celsius_to_kelvin(temperature: str | pl.Expr, ) -> pl.Expr:
    """
    Converts celsius to kelvin
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="celsius_to_kelvin",
        args=[],
        is_elementwise=True,
    )

def fahrenheit_to_kelvin(temperature: str | pl.Expr, ) -> pl.Expr:
    """
    Converts fahrenheit to kelvin
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="fahrenheit_to_kelvin",
        args=[],
        is_elementwise=True,
    )

def kelvin_to_celsius(temperature: str | pl.Expr, ) -> pl.Expr:
    """
    Converts from kelvin to celsius
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="kelvin_to_celsius",
        args=[],
        is_elementwise=True,
    )

def kelvin_to_fahrenheit(temperature: str | pl.Expr, ) -> pl.Expr:
    """
    Converts from kelvin to fahrenheit
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="kelvin_to_fahrenheit",
        args=[],
        is_elementwise=True,
    )

def fahrenheit_to_celsius(temperature: str | pl.Expr, ) -> pl.Expr:
    """
    Converts fahrenheit to degrees celsius
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="fahrenheit_to_celsius",
        args=[],
        is_elementwise=True,
    )

def celsius_dew_point(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr, 
                 atmospheric_pressure : str | IntoExpr) -> pl.Expr:
    """
    Calculates dew point using Magnus-Tetens formula using Celsius with given atmospheric pressure correction in hPa. Needs atmospheric pressure measurement in hPa in f64.

    Returns degrees of Celsius
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="celsius_dew_point",
        args=[relative_humidity, atmospheric_pressure],
        is_elementwise=True,
    )

def fahrenheit_humidex(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr, 
                 atmospheric_pressure : str | IntoExpr) -> pl.Expr:
    """
    Counts humidex for Fahrenheit from given values. Uses Fahrenheit with given atmospheric pressure correction in hPa.

    Returns degrees of Fahrenheit
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="fahrenheit_humidex",
        args=[relative_humidity, atmospheric_pressure],
        is_elementwise=True,
    )


def celsius_humidex(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr, 
                 atmospheric_pressure : str | IntoExpr) -> pl.Expr:
    """
    Counts humidex for Celsius from given values. Uses Celsius with given atmospheric pressure correction in hPa. Needs atmospheric pressure measurement in hPa in f64.

    Returns degrees of Celsius
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="celsius_humidex",
        args=[relative_humidity, atmospheric_pressure],
        is_elementwise=True,
    )

def celsius_mixing_ratio(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr, 
                 atmospheric_pressure : str | IntoExpr) -> pl.Expr:
    """
    Calculates mixing ratio using Magnus-Tetens formula using Celsius with precise atm. pressure given.

    Returns g/kg
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="celsius_mixing_ratio",
        args=[relative_humidity, atmospheric_pressure],
        is_elementwise=True,
    )

def fahrenheit_mixing_ratio(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr, 
                 atmospheric_pressure : str | IntoExpr) -> pl.Expr:
    """
    Calculates mixing ratio using Magnus-Tetens formula using Celsius with with precise atm. pressure given.

    Returns g/kg
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="fahrenheit_mixing_ratio",
        args=[relative_humidity, atmospheric_pressure],
        is_elementwise=True,
    )

def fahrenheit_dew_point(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr, 
                 atmospheric_pressure : str | IntoExpr) -> pl.Expr:
    """
    Calculates dew point using Magnus-Tetens formula using Fahrenheit with given atmospheric pressure correction in hPa. Needs atmospheric pressure measurement in hPa in f64.

    Returns degrees of Fahrenheit
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="fahrenheit_dew_point",
        args=[relative_humidity, atmospheric_pressure],
        is_elementwise=True,
    )

def common_celsius_dew_point(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculates dew point using Magnus-Tetens formula using Celsius with common atmospheric pressure using constant.

    Returns degrees of Celsius
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="common_celsius_dew_point",
        args=[relative_humidity],
        is_elementwise=True,
    )

def common_celsius_humidex(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculates humidex for Celsius from given values. Uses common dew point algorithm.

    Returns degrees of Celsius
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="common_celsius_humidex",
        args=[relative_humidity],
        is_elementwise=True,
    )

def common_celsius_mixing_ratio(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculates mixing ratio using Magnus-Tetens formula using Celsius with common atmospheric pressure using constant.

    Returns g/kg
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="common_celsius_mixing_ratio",
        args=[relative_humidity],
        is_elementwise=True,
    )

def common_fahrenheit_mixing_ratio(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculates mixing ratio using Magnus-Tetens formula using Celsius with common atmospheric pressure using constant.

    Returns g/kg
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="common_fahrenheit_mixing_ratio",
        args=[relative_humidity],
        is_elementwise=True,
    )


def  common_fahrenheit_dew_point(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculates common dew point using Magnus-Tetens formula using Fahrenheit with common atmospheric pressure using constant.

    Returns degrees of Fahrenheit
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="common_fahrenheit_dew_point",
        args=[relative_humidity],
        is_elementwise=True,
    )

def celsius_absolute_humidity(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculates absolute humidity using Magnus-Tetens formula using Celsius with common atmospheric pressure using constant.

    Returns g/m³
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="celsius_absolute_humidity",
        args=[relative_humidity],
        is_elementwise=True,
    )

def fahrenheit_absolute_humidity(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculates absolute humidity using Magnus-Tetens formula using Fahrenheit with common atmospheric pressure using constant.

    Returns g/m³
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="fahrenheit_absolute_humidity",
        args=[relative_humidity],
        is_elementwise=True,
    )

def celsius_heat_index(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculates heat index based on Rothfusz regression equation for Celsius.

    Returns degrees of Fahrenheit
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="celsius_heat_index",
        args=[relative_humidity],
        is_elementwise=True,
    )

def fahrenheit_heat_index(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculates heat index based on Rothfusz regression equation for Celsius.

    Returns degrees of Fahrenheit
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="fahrenheit_heat_index",
        args=[relative_humidity],
        is_elementwise=True,
    )

def common_fahrenheit_humidex(temperature: str | pl.Expr, 
                 relative_humidity: str | IntoExpr) -> pl.Expr:
    """
    Calculuates humidex for Fahrenheit from given values. Uses common dew point algorithm.

    Returns degrees of Fahrenheit
    """
    expr = parse_into_expr(temperature)
    return expr.register_plugin(
        lib=lib,
        symbol="common_fahrenheit_humidex",
        args=[relative_humidity],
        is_elementwise=True,
    )