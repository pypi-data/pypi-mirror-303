import itertools
from functools import cached_property
from typing import Dict, List, Optional

from metamart_source_cube.api import CubeAPI, CubeSchema
from metamart_source_cube.settings import CubeApiConfig
from metamart_source_cube.types import (
    CubeEdgeTypes,
    CubeNode,
    CubeNodeTypes,
    DimensionNode,
    MetamartID,
    MeasureNode,
    SourceTableNode,
)
from pydantic import BaseModel


class NamespaceMap(BaseModel):
    map: Dict[str, str] = {}


class CubeConnector(CubeAPI):
    """ """

    def __init__(
        self,
        namespace: str,
        config: Optional[CubeApiConfig] = None,
        namespace_map: Dict[str, str] = {},
        *args,
        **kwargs
    ):
        """

        Args:
            namespace:
            config:
            namespace_map: An optional mapping between cube data sources and Metamart namespaces
            *args:
            **kwargs:
        """
        self.namespace = namespace
        self.namespace_map = NamespaceMap(map=namespace_map).map
        super().__init__(config=config)

    def get_cube_source_table(self, cube: CubeSchema) -> Optional[SourceTableNode]:
        if cube.meta.metamart is None:
            return None

        if cube.meta.metamart.table_name is None:
            # TODO: We should extract this from the sql
            return None
        else:
            table_name = cube.meta.metamart.table_name

        if cube.meta.metamart.source_namespace is not None:
            namespace = cube.meta.metamart.source_namespace
        elif table_name in self.namespace_map:
            namespace = self.namespace_map[table_name]
        else:
            return None

        cube_id = MetamartID(name=table_name, namespace=namespace)
        cube_source = SourceTableNode(node_id=cube_id)
        return cube_source

    @cached_property
    def cubes(self) -> List[CubeSchema]:
        cubes = self.meta().cubes
        return cubes

    @cached_property
    def nodes(self) -> List[CubeNodeTypes]:
        # Need to identify the source table, and columns from sql
        # Nodes will include, source table, source column, cube measures, and cube dimensions
        nodes = []
        for cube in self.cubes:
            source_table = self.get_cube_source_table(cube)
            cube_node = CubeNode.from_schema(cube, self.namespace, source_table)

            initial_nodes = [cube_node] if source_table is None else [cube_node, source_table]
            source_columns = []  # TODO: Extract source columns from sql
            measures = (MeasureNode.from_schema(measure, cube_node) for measure in cube.measures)
            dimensions = (DimensionNode.from_schema(dimension, cube_node) for dimension in cube.dimensions)
            nodes.extend(itertools.chain(initial_nodes, source_columns, measures, dimensions))
        return nodes

    @cached_property
    def edges(self) -> List[CubeEdgeTypes]:
        # Edges between source columns and cube measures / dimensions
        edge_iters = (node.edges() for node in self.nodes)
        edges = list(itertools.chain(*edge_iters))
        return edges
