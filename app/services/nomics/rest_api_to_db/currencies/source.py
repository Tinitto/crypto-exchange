"""The currencies supported by Nomics resource got from the /currencies endpoint"""
from ..abstract.sources.bulk_source import NomicsBulkRestApiSource


class CurrenciesDataset(NomicsBulkRestApiSource):
    """
    Class for getting all supported currencies from Nomics
    """
    name: str = 'v1/currencies'
