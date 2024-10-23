# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

# -*- coding: utf-8 -*-
"""Python module used for calculating interfaces for CSP"""
from pathlib import Path
from powertrain_build.interface.service import get_service
from powertrain_build.lib import logger
from powertrain_build.interface import generation_utils

LOGGER = logger.create_logger("CSP service")


def parse_args():
    """Parse command line arguments

    Returns:
        Namespace: Arguments from command line
    """
    parser = generation_utils.base_parser()
    parser.add_argument(
        "--client-name",
        help="Name of the context object in CSP. Defaults to project name."
    )
    parser.add_argument(
        "output",
        help="Output directory for service models",
        type=Path
    )
    return parser.parse_args()


def main():
    """ Main function for stand alone execution.
    Mostly useful for testing and generation of dummy hal specifications
    """
    args = parse_args()
    app = generation_utils.process_app(args.config)
    client_name = generation_utils.get_client_name(args, app)
    service(args, app, client_name)


def service(args, app, client_name):
    """ Generate specifications for pt-scheduler wrappers.

    Args:
        args (Namespace): Arguments from command line
        app (Application): Application to generate specifications for
        client_name (str): Signal client name
    """
    model_internal = get_service(app, client_name, 'internal')
    model_external = get_service(app, client_name, 'external')
    model_observer = get_service(app, client_name, 'observer')
    generation_utils.write_to_file(model_internal, Path(args.output, 'model', 'internal.yaml'), is_yaml=True)
    generation_utils.write_to_file(model_external, Path(args.output, 'model', 'external.yaml'), is_yaml=True)
    generation_utils.write_to_file(model_observer, Path(args.output, 'model', 'observer.yaml'), is_yaml=True)


if __name__ == "__main__":
    main()
