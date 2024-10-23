# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

# -*- coding: utf-8 -*-
"""Python module used for calculating interfaces for CSP HI"""
from pathlib import Path
from powertrain_build.interface import generation_utils
from powertrain_build.interface.device_proxy import DPAL
from powertrain_build.lib.helper_functions import recursive_default_dict, to_normal_dict

OP_READ = 'read'
OP_WRITE = 'write'


def generate_hi_interface(args, hi_interface):
    """Generate HI YAML interface file.

    Args:
        args (Namespace): Arguments from command line.
        hi_interface (dict): HI interface dict based on HIApplication and generation_utils.get_interface.
    Returns:
        result (dict): Aggregated signal information as a dict.
    """

    io_translation = {
        'consumer': OP_READ,
        'producer': OP_WRITE
    }
    result = recursive_default_dict()
    for raster_data in hi_interface.values():
        for direction, signals in raster_data.items():
            hi_direction = io_translation[direction]
            for signal in signals:
                domain = signal['domain']
                group = signal['group']
                name = signal['variable']
                property_name = signal['property']
                if group is None:
                    port_name = signal['port_name'] or property_name
                    result[hi_direction]['signals'][domain][port_name]['data'][property_name] = name
                else:
                    port_name = signal['port_name'] or group
                    result[hi_direction]['signal_groups'][domain][port_name][group]['data'][property_name] = name
    generation_utils.write_to_file(to_normal_dict(result), args.output, is_yaml=True)


def parse_args():
    """Parse arguments.

    Returns:
        Namespace: the parsed arguments.
    """
    parser = generation_utils.base_parser()
    parser.add_argument(
        "output",
        help="Output file with interface specifications.",
        type=Path
    )
    return parser.parse_args()


def main():
    """ Main function for stand alone execution.
    Mostly useful for testing and generation of dummy hal specifications.
    """
    args = parse_args()
    app = generation_utils.process_app(args.config)
    hi_app = DPAL(app)
    interface = generation_utils.get_interface(app, hi_app)
    generate_hi_interface(args, interface)


if __name__ == "__main__":
    main()
