from functools import cache
from typing import List, Optional, Tuple, Union

from metamart_schemas.base import Event, SourcedEdge, SourcedNode
from metamart_schemas.integrations.base import MetamartIntegrationImplementation
from metamart_schemas.v1.source import SourceV1

from metamart_source_bigquery.adapters import adapt_to_client
from metamart_source_bigquery.loader import BigqueryConnector, LoggingConnector


class BigQueryIntegration(MetamartIntegrationImplementation):
    """BigQuery integration.

    Attributes:
        connector: The BigQuery connector

    """

    def __init__(
        self,
        source: SourceV1,
        version: Optional[str] = None,
        namespace: Optional[str] = None,
        project: Optional[str] = None,
        dataset: Optional[Union[str, List[str]]] = None,
        credentials: Optional[str] = None,
        log_parsing: Optional[bool] = False,
        log_parsing_window: Optional[int] = 7,
    ):
        """Initializes the BigQuery integration.

        Args:
            source: The Metamart data source to associate with output from the integration. More information about source objects is available in the `metamart_schemas` library.
            version: The Metamart data version to associate with output from the integration
            namespace: The Metamart namespace to associate with output from the integration
            project: GCP project id
            dataset: BigQuery Dataset Id, or multiple datasets seperated by a comma (`,`)
            credentials: JSON credentials for service account
            log_parsing: The number of days to read logs

        """
        super().__init__(source, version)

        self.connector = (
            BigqueryConnector(
                project=project,
                namespace=namespace,
                dataset=dataset,
                credentials=credentials,
            )
            if not log_parsing
            else LoggingConnector(
                project=project,
                namespace=namespace,
                dataset=dataset,
                credentials=credentials,
                window=log_parsing_window,
            )
        )

    @cache
    def nodes(self) -> List[SourcedNode]:
        """Return nodes from the connector."""
        with self.connector.connect() as conn:
            connector_nodes = conn.nodes()
            metamart_nodes = adapt_to_client(connector_nodes, self.source, self.version)
        return metamart_nodes

    @cache
    def edges(self) -> List[SourcedEdge]:
        """Return edges from the connector."""
        with self.connector.connect() as conn:
            connector_edges = conn.edges()
            metamart_edges = adapt_to_client(connector_edges, self.source, self.version)
        return metamart_edges

    def get_nodes_and_edges(self) -> Tuple[List[SourcedNode], List[SourcedEdge]]:
        """Return nodes and edges from the connector."""

        return self.nodes(), self.edges()

    def ready(self) -> bool:
        """Check if the connector is ready to be used."""
        with self.connector.connect() as _:
            pass
        return True
