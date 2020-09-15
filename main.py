import bonobo

from dotenv import load_dotenv

load_dotenv()

from app.services.nomics.rest_api_to_db import NOMICS_REST_API_TO_DB_CONTROLLERS
from app.services.nomics.file_download_site_to_db import NOMICS_FILE_DOWNLOAD_SITE_TO_DB_CONTROLLERS


def get_graph(**options):
    """
    This function builds the graph that needs to be executed.
    :return: bonobo.Graph
    """
    graph = bonobo.Graph()

    for controller in NOMICS_REST_API_TO_DB_CONTROLLERS:
        graph.add_chain(
            controller.extract,
            controller.transform,
            controller.load,
        )

    for controller in NOMICS_FILE_DOWNLOAD_SITE_TO_DB_CONTROLLERS:
        graph.add_chain(
            controller.extract,
            controller.transform,
            controller.load,
        )

    return graph


def get_services(**options):
    """Service Dependency injector"""
    return {}


if __name__ == '__main__':
    parser = bonobo.get_argument_parser()
    with bonobo.parse_args(parser) as options:
        bonobo.run(
            get_graph(**options),
            services=get_services(**options)
        )
