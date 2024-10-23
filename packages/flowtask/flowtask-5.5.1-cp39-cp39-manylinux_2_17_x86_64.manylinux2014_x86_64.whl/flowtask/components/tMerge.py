import asyncio
import pandas as pd
from typing import Any
from collections.abc import Callable
from querysource.exceptions import QueryException
from ..exceptions import ComponentError
from .abstract import FlowComponent


class tMerge(FlowComponent):
    """
    Merge DataFrame or named Series objects with a database-style join.
    """
    def __init__(
        self,
        loop: asyncio.AbstractEventLoop = None,
        job: Callable = None,
        stat: Callable = None,
        **kwargs,
    ):
        """Init Method."""
        self.df1: Any = None
        self.df2: Any = None
        self.type = kwargs.pop('type', 'cross')
        super(tMerge, self).__init__(loop=loop, job=job, stat=stat, **kwargs)

    async def start(self, **kwargs):
        if self.previous:
            self.data = self.input
        else:
            raise ComponentError("Data Not Found", code=404)
        try:
            self.df1 = self.previous[0].output()
        except IndexError as ex:
            name = self.depends[0]
            raise ComponentError(
                f"Missing LEFT Dataframe: {name}"
            ) from ex
        try:
            self.df2 = self.previous[1].output()
        except IndexError as ex:
            name = self.depends[1]
            raise ComponentError(
                "Missing RIGHT Dataframe"
            ) from ex
        return True

    async def close(self):
        pass

    async def run(self):
        try:
            if hasattr(self, "pd_args"):
                args = self.pd_args
            else:
                args = {}
            df = pd.merge(self.df1, self.df2, how=self.type, **args)
            self._result = df
            self.add_metric("NUM_ROWS", self._result.shape[0])
            self.add_metric("NUM_COLUMNS", self._result.shape[1])
            if self._debug:
                print("Debugging: tMerge ===")
                print(self._result)
                columns = list(self._result.columns)
                for column in columns:
                    t = self._result[column].dtype
                    print(
                        column, "->", t, "->", self._result[column].iloc[0]
                    )
            return self._result
        except (ValueError, KeyError) as err:
            raise ComponentError(f"tMerge Error: {err!s}") from err
        except Exception as err:
            raise ComponentError(f"tMerge error {err!s}") from err
