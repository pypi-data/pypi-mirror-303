from chainalysis.orm import Orm
from chainalysis.sql import Sql
from chainalysis.utils import Utils


class DataSolutionsClient:
    """
    This class provides SDK functions for users to query
    Data Solutions databases.
    """

    def __init__(
        self,
        api_key: str,
    ):
        """
        Initialize the DataSolutionsClient class.

        :param api_key: The API key for the Data Solutions API
        :type api_key: str
        """
        self.api_key = api_key

        self._sql = Sql(self.api_key)

        self._orm = Orm(self.api_key)

        self._utils = Utils()

    @property
    def sql(self) -> Sql:
        """
        Call the sql property to access the Sql class.
        """
        return self._sql

    @property
    def orm(self) -> Orm:
        """
        Call the orm property to access the Orm class.
        """
        return self._orm

    @property
    def utils(self) -> Utils:
        """
        Call the utils property to access the Utils class.
        """
        return self._utils
