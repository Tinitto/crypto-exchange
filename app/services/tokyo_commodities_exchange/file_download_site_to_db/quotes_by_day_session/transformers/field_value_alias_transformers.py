"""Module containing transformer classes for exchanging field values with their aliases"""
from typing import Dict

from app.core.transformers.field_value_alias_transformer import FieldValueAliasTransformer


class QuotesTradeTypeValueTransformer(FieldValueAliasTransformer):
    """
    Transforms the trade_type field values to their aliases
    https://www.tocom.or.jp/historical/keishiki/souba_d.html#souba_daily
    """
    _field_name: str = 'trade_type'
    _alias_map: Dict[str, str] = {
        "11": "Physically Delivered Futures Transaction",
        "12": "Cash-settled Futures Transaction",
        "21": "Call Options Transaction",
        "22": "Put Options Transaction",
    }


class QuotesInstitutionsCodeValueTransformer(FieldValueAliasTransformer):
    """
    Transforms the institutions_code field values to their aliases
    https://www.tocom.or.jp/historical/keishiki/souba_d.html#souba_daily
    """
    _field_name: str = 'institutions_code'
    _alias_map: Dict[str, str] = {
        "77": "TOCOM",
    }


class QuotesProductCodeValueTransformer(FieldValueAliasTransformer):
    """
    Transforms the product_code field values to their aliases
    https://www.tocom.or.jp/historical/keishiki/souba_d.html#product_code
    """
    _field_name: str = 'product_code'
    _alias_map: Dict[str, str] = {
        "11": "GOLD",
        "12": "SILVER",
        "13": "PLATINUM",
        "14": "PALLADIUM",
        "16": "GOLD MINI",
        "17": "PLATINUM MINI",
        "18": "GOLD ROLLING SPOT",
        "19": "PLATINUM ROLLING SPOT",
        "31": "GASOLINE",
        "32": "KEROSENE",
        "33": "CRUDE OIL",
        "34": "GAS OIL",
        "37": "CHUKYO GASOLINE",
        "38": "CHUKYO KEROSENE",
        "41": "Cash-settled BARGE GASOLINE",
        "42": "Platts Cash-settled BARGE KEROSENE",
        "43": "Platts Cash-settled BARGE GAS OIL",
        "44": "Cash-settled LORRY GASOLINE",
        "45": "Platts Cash-settled LORRY KEROSENE",
        "46": "Platts Cash-settled LORRY GAS OIL",
        "61": "West Area Baseload Electricity",
        "62": "East Area Baseload Electricity",
        "63": "West Area Peakload Electricity",
        "64": "East Area Peakload Electricity",
        "81": "RSS3 RUBBER",
        "82": "TSR20 RUBBER",
        "100": "Nikkei-TOCOM Commodity Index",
        "101": "Nikkei-TOCOM Nearby Month Commodity Index",
        "103": "Nikkei-TOCOM Industrial Commodity Index",
        "110": "Nikkei-TOCOM Precious Metals Index",
        "111": "Nikkei-TOCOM Gold Index",
        "112": "Nikkei-TOCOM Silver Index",
        "113": "Nikkei-TOCOM Platinum Index",
        "114": "Nikkei-TOCOM Palladium Index",
        "130": "Nikkei-TOCOM Oil Index",
        "131": "Nikkei-TOCOM Gasoline Index",
        "132": "Nikkei-TOCOM Kerosene Index",
        "133": "Nikkei-TOCOM Crude Oil Index",
        "181": "Nikkei-TOCOM Rubber Index",
        "201": "Corn",
        "202": "Soybeans",
        "204": "Azuki Beans",
        "300": "Nikkei-TOCOM Agricultural Product & Sugar Index",
        "301": "Nikkei-TOCOM Corn Index",
        "302": "Nikkei-TOCOM Soybean Index",
        "304": "Nikkei-TOCOM Azuki Index",
        "501": "Nikkei-TOCOM Leveraged Commodity Index",
        "502": "Nikkei-TOCOM Leveraged Nearby Month Commodity Index",
        "503": "Nikkei-TOCOM Leveraged Industrial Commodity Index",
        "504": "Nikkei-TOCOM Leveraged Precious Metals Index",
        "505": "Nikkei-TOCOM Leveraged Oil Index",
        "506": "Nikkei-TOCOM Leveraged Agricultural Product & Sugar Index",
        "508": "Nikkei-TOCOM Leveraged Gold Index",
        "509": "Nikkei-TOCOM Leveraged Silver Index",
        "510": "Nikkei-TOCOM Leveraged Platinum Index",
        "511": "Nikkei-TOCOM Leveraged Palladium Index",
        "512": "Nikkei-TOCOM Leveraged Crude Oil Index",
        "513": "Nikkei-TOCOM Leveraged Gasoline Index",
        "514": "Nikkei-TOCOM Leveraged Kerosene Index",
        "515": "Nikkei-TOCOM Leveraged Corn Index",
        "516": "Nikkei-TOCOM Leveraged Soybean Index",
        "517": "Nikkei-TOCOM Leveraged Azuki Index",
        "518": "Nikkei-TOCOM Leveraged Rubber (RSS3) Index",
        "551": "Nikkei-TOCOM Inverse Commodity Index",
        "552": "Nikkei-TOCOM Inverse Nearby Month Commodity Index",
        "553": "Nikkei-TOCOM Inverse Industrial Commodity Index",
        "554": "Nikkei-TOCOM Inverse Precious Metals Index",
        "555": "Nikkei-TOCOM Inverse Oil Index",
        "556": "Nikkei-TOCOM Inverse Agricultural Product & Sugar Index",
        "558": "Nikkei-TOCOM Inverse Gold Index",
        "559": "Nikkei-TOCOM Inverse Silver Index",
        "560": "Nikkei-TOCOM Inverse Platinum Index",
        "561": "Nikkei-TOCOM Inverse Palladium Index",
        "562": "Nikkei-TOCOM Inverse Crude Oil Index",
        "563": "Nikkei-TOCOM Inverse Gasoline Index",
        "564": "Nikkei-TOCOM Inverse Kerosene Index",
        "565": "Nikkei-TOCOM Inverse Corn Index",
        "566": "Nikkei-TOCOM Inverse Soybean Index",
        "567": "Nikkei-TOCOM Inverse Azuki Index",
        "568": "Nikkei-TOCOM Inverse Rubber (RSS3) Index",
    }
