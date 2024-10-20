from functools import cache
from typing import List, Optional, Tuple

from metamart_schemas.base import SourcedEdge, SourcedNode
from metamart_schemas.integrations.base import MetamartIntegrationImplementation
from metamart_schemas.v1.source import SourceV1

from metamart_source_snowflake.adapters import adapt_to_client
from metamart_source_snowflake.loader import SnowflakeConnector


class SnowflakeIntegration(MetamartIntegrationImplementation):
    """A class for extracting Metamart compliant metadata from Snowflake

    Attributes:
        connector: The connector responsible for communicating with Snowflake.

    """

    def __init__(
        self,
        source: SourceV1,
        version: Optional[str] = None,
        account: Optional[str] = None,
        user: Optional[str] = None,
        password: Optional[str] = None,
        warehouse: Optional[str] = None,
        role: Optional[str] = None,
        database: Optional[str] = None,
        namespace: Optional[str] = None,
        **kwargs,
    ):
        """Initializes the Snowflake integration.

        Args:
           source: The Metamart data source to associate with output from the integration. More information about source objects is available in the `metamart_schemas` library.
           version: The Metamart data version to associate with output from the integration
           namespace: The Metamart namespace to associate with output from the integration
           account: Snowflake account, the characters in front of `.snowflakecomputing.com`
           user: The database user
           role: The Snowflake role to use.
           warehouse: The Snowflake warehouse to use.
           database: The Snowflake database to connect to.
           password: The password to use when connecting to Snowflake.

        """
        super().__init__(source, version)

        self.connector = SnowflakeConnector(
            account=account,
            user=user,
            password=password,
            warehouse=warehouse,
            role=role,
            database=database,
            namespace=namespace,
            **kwargs,
        )

    @cache
    def get_nodes_and_edges(self) -> Tuple[List[SourcedNode], List[SourcedEdge]]:
        """Returns a tuple of lists of SourcedNode and SourcedEdge objects"""
        with self.connector.connect() as conn:
            nodes, edges = conn.get_nodes_and_edges()

        nodes = adapt_to_client(nodes, self.source, self.version)
        edges = adapt_to_client(edges, self.source, self.version)
        return nodes, edges

    def ready(self) -> bool:
        """Returns True if the integration is ready to run"""
        with self.connector.connect() as _:
            pass
        return True

    def nodes(self) -> List[SourcedNode]:
        """Returns a list of SourcedNode objects"""
        return self.get_nodes_and_edges()[0]

    def edges(self) -> List[SourcedEdge]:
        """Returns a list of SourcedEdge objects"""
        return self.get_nodes_and_edges()[1]
