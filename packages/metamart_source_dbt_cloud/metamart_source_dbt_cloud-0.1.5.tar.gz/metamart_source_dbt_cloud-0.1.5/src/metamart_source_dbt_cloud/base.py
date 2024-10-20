from functools import cache
from typing import List, Optional, Tuple

from metamart_client.integrations.base import EventMixin
from metamart_schemas.base import Event, SourcedEdge, SourcedNode
from metamart_schemas.integrations.base import MetamartIntegrationImplementation
from metamart_schemas.v1.source import SourceV1
from metamart_source_dbt_cloud.loader import DbtCloudConnector


class DbtCloudIntegration(EventMixin, MetamartIntegrationImplementation):
    """A class for extracting Metamart compliant metadata from the dbt cloud API.

    Attributes:
        connector: The dbt cloud connector responsible for communicating with the dbt cloud api.

    """

    def __init__(
        self,
        api_key: str,
        source: SourceV1,
        version: Optional[str] = None,
        namespace: Optional[str] = "default",
    ):
        """Initializes the dbt cloud integration.

        Args:
            api_key: A dbt cloud api key
            source: The Metamart data source to associate with output from the integration. More information about source objects is available in the `metamart_schemas` library.
            version: The Metamart data version to associate with output from the integration
            namespace: The Metamart namespace to associate with output from the integration

        """
        super().__init__(source, version)

        self.connector = DbtCloudConnector(
            namespace=namespace,
            api_key=api_key,
            source=source,
        )

    @cache
    def get_nodes_and_edges(self) -> Tuple[List[SourcedNode], List[SourcedEdge]]:
        """Returns a tuple of lists of SourcedNode and SourcedEdge objects"""
        nodes, edges = self.connector.get_nodes_and_edges()
        return nodes, edges

    def nodes(self) -> List[SourcedNode]:
        """Returns a list of SourcedNode objects"""
        return self.get_nodes_and_edges()[0]

    def edges(self) -> List[SourcedEdge]:
        """Returns a list of SourcedEdge objects"""
        return self.get_nodes_and_edges()[1]

    def events(self, last_event_date: Optional[str]) -> List[Event]:
        """Returns a list of Event objects"""
        events = self.connector.get_events(last_event_date=last_event_date)
        return events

    def ready(self) -> bool:
        """Returns True if the integration is ready to run"""
        _ = self.connector.default_account
        return True
