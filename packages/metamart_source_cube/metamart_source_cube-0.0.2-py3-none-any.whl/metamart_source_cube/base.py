import json
from typing import Dict, List, Optional, Tuple, Union
from warnings import warn

from metamart_schemas.base import SourcedEdge, SourcedNode
from metamart_schemas.integrations.base import MetamartIntegrationImplementation
from metamart_schemas.v1.source import SourceSpec, SourceV1
from metamart_source_cube.adapters import adapt_to_client
from metamart_source_cube.connector import CubeConnector, NamespaceMap
from metamart_source_cube.settings import CubeApiConfig
from requests import HTTPError


def process_namespace_map(namespace_map: Optional[Union[NamespaceMap, Dict, str]]) -> NamespaceMap:
    if namespace_map is None:
        result = NamespaceMap()
    elif isinstance(namespace_map, dict):
        try:
            result = NamespaceMap(map=namespace_map)
        except Exception as e:
            raise ValueError(f"Could not parse the `namespace_map` from the provided dictionary: {e}")
    elif isinstance(namespace_map, str):
        try:
            result = NamespaceMap(map=json.loads(namespace_map))
        except Exception as e:
            raise ValueError(f"Could not parse the `namespace_map` from the provided string: {e}")
    elif not isinstance(namespace_map, NamespaceMap):
        raise ValueError("The `namespace_map` must be a `CubeSourceMap`, dictionary, or json string.")
    else:
        raise ValueError("The `namespace_map` must be a `CubeSourceMap`, dictionary, or json string.")
    return result


class CubeIntegration(MetamartIntegrationImplementation):
    """A class for extracting Metamart compliant metadata from the Cube.dev REST API"""

    def __init__(
        self,
        source: Union[SourceV1, SourceSpec],
        namespace: str,
        config: Optional[CubeApiConfig] = None,
        namespace_map: Optional[Union[NamespaceMap, Dict, str]] = None,
        version: str = "v1",
    ):
        """Initializes the Cube.js integration.

        Args:
            source: The Metamart data source to associate with output from the integration.
            namespace: The Metamart namespace to associate with output from the integration
            config: The connection configuration for your cube API. If not provided, an effort will be made to load
                these from the environment.
            namespace_map: An optional mapping between cube data sources and Metamart namespaces
            version: The version of the Metamart API to use for the integration
        """
        namespace_map = process_namespace_map(namespace_map)
        source: SourceV1 = source if isinstance(source, SourceV1) else SourceV1.from_spec(source)
        super().__init__(source, version)

        self.connector = CubeConnector(namespace=namespace, namespace_map=namespace_map.map, config=config)

    def nodes(self) -> List[SourcedNode]:
        """Returns a list of SourcedNode objects"""
        # adapted nodes
        return adapt_to_client(self.connector.nodes, self.source, self.version)

    def edges(self) -> List[SourcedEdge]:
        """Returns a list of SourcedEdge objects"""
        # adapted edges
        return adapt_to_client(self.connector.edges, self.source, self.version)

    def get_nodes_and_edges(self) -> Tuple[List[SourcedNode], List[SourcedEdge]]:
        """Returns a tuple of lists of SourcedNode and SourcedEdge objects"""
        return self.nodes(), self.edges()

    def ready(self) -> bool:
        """Returns True if the integration is ready to run"""
        response = self.connector.ready()
        try:
            response.raise_for_status()
            return True
        except HTTPError:
            return False
        except Exception:
            warn("An unexpected error occurred while checking the readiness of the cube API.")
            return False
