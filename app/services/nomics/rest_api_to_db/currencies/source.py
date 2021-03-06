"""
The currencies supported by Nomics resource got from the /currencies endpoint
https://nomics.com/docs/#operation/getCurrencies
"""
from ..abstract.sources.bulk import NomicsBulkRestApiSource


class CurrenciesDataset(NomicsBulkRestApiSource):
    """
    Class for getting all supported currencies from Nomics
    """
    name: str = 'v1/currencies'
