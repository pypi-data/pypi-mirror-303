# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Module to create an a2l file from a conversion table file."""

import argparse
import json
from pathlib import Path


def get_vtab_text(vtab):
    """Convert vtab dict to a2l text."""

    vtab_text = (
        '    /begin COMPU_VTAB\n'
        f'        CONV_TAB_{vtab["name"]}             /* Name */\n'
        '        "Conversion table"          /* LongIdentifier */\n'
        '        TAB_VERB            /* ConversionType */\n'
        f'        {len(vtab["disp_values"])}          /* NumberValuePairs */\n'
    )

    vtab_text += ''.join(
        f'        {vtab["start_value"]+i}          /* InVal */\n'
        f'        "{value}"          /* OutVal */\n'
        for i, value in enumerate(vtab['disp_values'])
    )

    vtab_text += '    /end COMPU_VTAB\n\n'

    return vtab_text


def create_conversion_table(input_json: Path, output_a2l: Path):
    """Create a2l conversion table for custom units."""
    with open(input_json.resolve(), encoding="utf-8") as f_h:
        conversion_table = json.load(f_h)

    with open(output_a2l.resolve(), 'w', encoding="utf-8") as f_h:
        for vtab in conversion_table:
            f_h.write(get_vtab_text(vtab))


def parse_args():
    """Parse args."""
    parser = argparse.ArgumentParser('Create a2l file from conversion_table.json file')
    parser.add_argument('input_file', type=Path)
    parser.add_argument('output_file', type=Path)
    args = parser.parse_args()
    return args


def main():
    """Main."""
    args = parse_args()
    conversion_table_json = args.input_file
    conversion_table_a2l = args.output_file
    create_conversion_table(conversion_table_json, conversion_table_a2l)


if __name__ == '__main__':
    main()
