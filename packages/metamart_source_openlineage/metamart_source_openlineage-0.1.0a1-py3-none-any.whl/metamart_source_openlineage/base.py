from functools import cached_property
from typing import Dict, List, Optional, Tuple, Union

from metamart_schemas.base import SourcedEdge, SourcedNode
from metamart_schemas.integrations.base import MetamartIntegrationImplementation
from metamart_schemas.v1.source import SourceV1

from metamart_source_openlineage.processor import OpenLineageProcessor


class OpenLineageIntegration(MetamartIntegrationImplementation):
    """A class for extracting Metamart compliant metadata from an OpenLineage json string.

    Attributes:
        lineage_data: A dictionary parsing of a OpenLineage json file
        namespace: The Metamart namespace to associate with output from the integration
        namespaces: A dictionary of namespace aliases to use when parsing the lineage data

    """

    def __init__(
        self,
        lineage_data: Union[str, dict],
        source: SourceV1,
        version: Optional[str] = None,
        namespace: Optional[str] = "default",
        namespaces: Optional[Dict[str, str]] = None,
    ):
        """Initializes the dbt integration.

        Args:
            lineage_data: Either a string path to a manifest.json file, or a dictionary parsing of a manifest.json file
            source: The Metamart data source to associate with output from the integration. More information about source objects is available in the `metamart_schemas` library.
            version: The Metamart data version to associate with output from the integration
            namespace: The Metamart namespace to associate with output from the integration
            namespaces: A dictionary of namespace aliases to use when parsing the lineage data

        """
        super().__init__(source, version)

        self.lineage_data = lineage_data
        self.namespace = namespace
        self.namespaces = namespaces

    @cached_property
    def lineage(self) -> OpenLineageProcessor:
        """Returns a ManifestProcessor object for the lineage json file"""
        return OpenLineageProcessor.load(self.lineage_data, self.namespaces, self.namespace, self.source.spec)

    def nodes(self) -> List[SourcedNode]:
        """Returns a list of SourcedNode objects"""
        return self.lineage.adapted_nodes

    def edges(self) -> List[SourcedEdge]:
        """Returns a list of SourcedEdge objects"""
        return self.lineage.adapted_edges

    def get_nodes_and_edges(self) -> Tuple[List[SourcedNode], List[SourcedEdge]]:
        """Returns a tuple of lists of SourcedNode and SourcedEdge objects"""
        return self.nodes(), self.edges()

    def ready(self) -> bool:
        """Returns True if the integration is ready to run"""
        self.lineage
        return True
