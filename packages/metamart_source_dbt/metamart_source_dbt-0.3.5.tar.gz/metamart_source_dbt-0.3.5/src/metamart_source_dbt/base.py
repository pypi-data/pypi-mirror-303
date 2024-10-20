from functools import cached_property
from typing import List, Optional, Tuple, Union

from metamart_schemas.base import SourcedEdge, SourcedNode
from metamart_schemas.integrations.base import MetamartIntegrationImplementation
from metamart_schemas.v1.source import SourceV1

from metamart_source_dbt.processor import ManifestProcessor


class DbtIntegration(MetamartIntegrationImplementation):
    """A class for extracting Metamart compliant metadata from a dbt manifest.json file.

    Attributes:
        manifest_data: A dictionary parsing of a manifest.json file
        namespace: The Metamart namespace to associate with output from the integration

    """

    def __init__(
        self,
        manifest_data: Union[str, dict],
        source: SourceV1,
        version: Optional[str] = None,
        namespace: Optional[str] = "default",
    ):
        """Initializes the dbt integration.

        Args:
            manifest_data: Either a string path to a manifest.json file, or a dictionary parsing of a manifest.json file
            source: The Metamart data source to associate with output from the integration. More information about source objects is available in the `metamart_schemas` library.
            version: The Metamart data version to associate with output from the integration
            namespace: The Metamart namespace to associate with output from the integration

        """
        super().__init__(source, version)

        self.manifest_data = manifest_data
        self.namespace = namespace

    @cached_property
    def manifest(self) -> ManifestProcessor:
        """Returns a ManifestProcessor object for the manifest.json file"""
        return ManifestProcessor.load(self.manifest_data, self.namespace, self.source)

    def nodes(self) -> List[SourcedNode]:
        """Returns a list of SourcedNode objects"""
        return self.manifest.adapted_nodes

    def edges(self) -> List[SourcedEdge]:
        """Returns a list of SourcedEdge objects"""
        return self.manifest.adapted_edges

    def get_nodes_and_edges(self) -> Tuple[List[SourcedNode], List[SourcedEdge]]:
        """Returns a tuple of lists of SourcedNode and SourcedEdge objects"""
        return self.nodes(), self.edges()

    def ready(self) -> bool:
        """Returns True if the integration is ready to run"""
        manifest = self.manifest
        return True
