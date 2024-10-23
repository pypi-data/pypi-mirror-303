import asyncio
from typing import Union
from collections.abc import Callable
import pandas as pd
from ..exceptions import ComponentError, ConfigError
from .abstract import FlowComponent
import warnings

class tOrder(FlowComponent):
    """
        tOrder

        Overview

        The `tOrder` class is a component designed to order a Pandas DataFrame by a specified column. It allows sorting the DataFrame either in ascending or descending order based on the specified column.

        Properties

        .. table:: Properties
        :widths: auto

        +------------------+----------+-----------+-----------------------------------------------------------------------------------+
        | Name             | Required | Type      | Description                                                                       |
        +------------------+----------+-----------+-----------------------------------------------------------------------------------+
        | columns          | Yes      | str       | The name of the column to sort the DataFrame by.                                  |
        +------------------+----------+-----------+-----------------------------------------------------------------------------------+
        | ascending        | No       | bool      | Specifies whether to sort the DataFrame in ascending order. Defaults to True.     |
        +------------------+----------+-----------+-----------------------------------------------------------------------------------+

        Return
           The dataframe ordinated by the column give it in the order_by either ascending or descending.

    """

    condition = ""

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop = None,
        job: Callable = None,
        stat: Callable = None,
        **kwargs,
    ):
        """Init Method."""
        self._column: Union[str,list] = kwargs.pop("columns", None)
        if isinstance(self._column, list):
            ascending = [True for x in self._column]
        elif isinstance(self._column, str):
            ascending = [True]
            self._column = [self._column]
        self._ascending: Union[bool,list] = kwargs.pop("ascending", ascending)
        if not self._column:
            raise ConfigError(
                "tOrder requires a column for ordering => **columns**"
            )
        self.pd_args = kwargs.pop("pd_args",{})
        super(tOrder, self).__init__(loop=loop, job=job, stat=stat, **kwargs)

    async def start(self, **kwargs):
        # If what arrives is not a Pandas DataFrame, the task is cancelled
        if self.previous:
            self.data = self.input
        else:
            raise ComponentError("Data Not Found", code=404)
        if not isinstance(self.data, pd.DataFrame):
            raise ComponentError("Incompatible Pandas Dataframe", code=404)
        return True

    async def close(self):
        pass

    async def run(self):
        self._result = None
        try:
            # Check if the specified column exists in the DataFrame
            columns = self.data.columns
            for col in self._column:
                if col not in columns:
                    self._logger.warning(f"The column '{self._column}' does not exist in the DataFrame.")
                    self._result = self.data # Return the unsorted DataFrame
                    # Check if the specified column is empty
                    if self.data[self._column].empty:
                        self._logger.warning(f"The column '{self._column}' is empty.")
            # Sort the DataFrame by the specified column
            df = self.data.sort_values(by=self._column, ascending=self._ascending,**self.pd_args).reset_index(drop=True)
            self._result = df
        except Exception as err:
            raise ComponentError(f"Generic Error on Data: error: {err}") from err
        if self._debug is True:
            print("::: Printing Ordered Data === ")
            print("Ordered: ", self._result)
        return True
