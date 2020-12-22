"""Module having the entry point for the app"""
from typing import List, Optional, Type

import bonobo
from judah.controllers.base import BaseController

from app.services import ALL_SERVICE_CONTROLLERS


def get_graph_for_controllers(controllers: List[Type[BaseController]]):
    """
    This function builds the graph that needs to be executed.
    """
    graph = bonobo.Graph()

    for controller in controllers:
        graph.add_chain(
            controller.extract,
            controller.transform,
            controller.load,
        )

    return graph


def start(graph=get_graph_for_controllers(ALL_SERVICE_CONTROLLERS),
          strategy: Optional[str] = None, **kwargs):
    """Starts the ETL pipelines"""
    bonobo.run(graph, strategy=strategy, **kwargs)
