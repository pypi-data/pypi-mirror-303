from typing import Optional
from abc import ABC
import logging
import locale


class LocaleSupport(ABC):
    """LocaleSupport.

    Adding Support for Encoding and Locale to every Component in FlowTask.
    """

    encoding: str = "UTF-8"
    _locale: Optional[str] = None

    def __init__(self, *args, **kwargs):
        if not self.encoding:
            self.encoding = "UTF-8"
        if "l18n" in kwargs:
            self._locale = kwargs["l18n"]
        # Localization
        if self._locale is None:
            newloc = (locale.getlocale())[0]
            self._locale = f"{newloc}.{self.encoding}"
        else:
            if self.encoding not in self._locale:
                self._locale = f"{self._locale}.{self.encoding}"
        try:
            # avoid errors on unsupported locales
            locale.setlocale(locale.LC_TIME, self._locale)
        except (RuntimeError, NameError, locale.Error) as err:
            logging.warning(f"Error on Locale Support: {err}")
            newloc = (locale.getlocale())[0]
            self._locale = f"{newloc}.UTF-8"
            locale.setlocale(locale.LC_TIME, self._locale)
        super().__init__()
