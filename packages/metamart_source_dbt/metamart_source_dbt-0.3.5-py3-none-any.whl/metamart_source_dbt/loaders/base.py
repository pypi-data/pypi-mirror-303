from __future__ import annotations

import typing
from abc import ABC, abstractmethod

from pydantic import BaseModel

from metamart_source_dbt.loaders.utils import MetamartExtras
from metamart_source_dbt.utils import full_name

if typing.TYPE_CHECKING:
    from metamart_source_dbt.loaders import ManifestTypes


class BaseManifestLoader(ABC):
    """ """

    def __init__(self, manifest: ManifestTypes, namespace: str, *args, **kwargs):
        self.manifest = manifest
        self.namespace = namespace

        for node in self.manifest.nodes.values():
            node.metamart_ = MetamartExtras(full_name=full_name(node), namespace=self.namespace)
        for node in self.manifest.sources.values():
            node.metamart_ = MetamartExtras(full_name=full_name(node), namespace=self.namespace)

    @property
    @abstractmethod
    def nodes(self):
        """ """
        raise NotImplementedError

    @property
    @abstractmethod
    def edges(self):
        """ """
        raise NotImplementedError
