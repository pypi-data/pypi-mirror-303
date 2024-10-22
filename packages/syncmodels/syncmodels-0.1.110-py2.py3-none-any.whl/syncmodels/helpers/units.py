import sys

from pydantic import BaseModel

from syncmodels.crawler import iPlugin, iAsyncCrawler
from syncmodels.mapper import Mapper
from syncmodels.model import Enum
from syncmodels.session import iSession
from syncmodels.registry import iRegistry


class UnitInventory(dict):
    """Helper class to build inventory of classes from a `unit` module"""

    def build_all(self, name, **kw):
        """Build the whole inventory"""
        self.build_inventory(name, **kw)
        self.bootstrap(**kw)

    def build_inventory(
        self, name, local=True, final=True, categories=None, **_
    ):
        """Build an inventory of some categories classes"""
        mod = sys.modules[name]
        inventory = self
        categories = (
            [
                BaseModel,
                Enum,
                iSession,
                Mapper,
                iPlugin,
                iAsyncCrawler,
                iRegistry,
            ]
            if categories is None
            else categories
        )
        for key, item in mod.__dict__.items():
            # print(f"{key}: {item}")
            for klass in categories:
                try:
                    if item == klass:
                        # skip category classes
                        continue
                    if local and item.__module__ != name:
                        # skip outside definitions
                        break
                    if issubclass(item, klass):
                        inventory.setdefault(klass.__name__, {})[key] = item
                except AttributeError:
                    pass
                except TypeError:
                    pass
                # except Exception as why:
                #     pass

        if final:
            # try to remove any intermediate class
            for options in inventory.values():
                for parent_name, parent_klass in list(options.items()):
                    for child_name, child_klass in options.items():
                        if child_name != parent_name and issubclass(
                            child_klass, parent_klass
                        ):
                            options.pop(parent_name)
                            break

        return inventory

    def bootstrap(self, **_):
        """Get all bootstrap initial setup"""
        bootstrap = {}
        for name, klass in self[iAsyncCrawler.__name__].items():
            crawler = klass()
            bootstrap[name] = list(crawler.default_bootstrap())

        return bootstrap
