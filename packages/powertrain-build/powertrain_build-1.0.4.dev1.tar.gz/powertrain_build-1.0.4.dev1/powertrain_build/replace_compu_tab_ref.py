# Copyright 2024 Volvo Car Corporation
# Licensed under Apache 2.0.

"""Module for replacing $CVC_* style references in a2l file."""

import re
import argparse

from pathlib import Path


def parse_args():
    """Parse args."""
    parser = argparse.ArgumentParser("Replace $CVC_* style references in a2l file")
    parser.add_argument("a2l_target_file")
    args = parser.parse_args()
    return args


def replace_tab_verb(file_path: Path):
    """Replace custom Units with conversion table."""
    with open(file_path, encoding='ISO-8859-1') as f_h:
        a2l_text = f_h.read()

    ##############################################################
    # Absolutely horrible multi-line regex                       #
    #                                                            #
    # Translates a fake COMPU_METHOD                             #
    # with custom $CVC_* Unit into using a conversion table      #
    #                                                            #
    ##############################################################
    # If a dollar is found make the following changes:           #
    # 'RAT_FUNC' => 'TAB_VERB'                                   #
    # 'LINEAR' => 'TAB_VERB'                                     #
    # New format => "%12.6"                                      #
    # Save the $-tag and remove it from the unit                 #
    # Change the line below the '/* Unit */'- line to            #
    # "['COMPU_TAB_REF CONV_TAB_' $-tag]                         #
    ##############################################################
    # ***************************BEFORE************************* #
    ##############################################################
    # /begin COMPU_METHOD                                        #
    #     VcDummy_spm_1_0_0_None__CVC_EmCoBaseMode   /* Name */  #
    #     ""    /* LongIdentifier */                             #
    #     RAT_FUNC    /* ConversionType */                       #
    #     "%11.3"   /* Format */                                 #
    #     "-,$CVC_EmCoBaseMode" /* Unit */                       #
    #     COEFFS 0 1 0.0 0 0 1                                   #
    # /end COMPU_METHOD                                          #
    ##############################################################
    # ***************************AFTER************************** #
    ##############################################################
    # /begin COMPU_METHOD                                        #
    #     VcDummy_spm_1_0_0_None__CVC_EmCoBaseMode   /* Name */  #
    #     ""    /* LongIdentifier */                             #
    #     TAB_VERB    /* ConversionType */                       #
    #     "%12.6"   /* Format */                                 #
    #     "-" /* Unit */                                         #
    #     COMPU_TAB_REF CONV_TAB_CVC_EmCoBaseMode               #
    # /end COMPU_METHOD                                          #
    ##############################################################

    COMPU_METHOD_EXPRESSION = (
        r"(RAT_FUNC|LINEAR)"  # Match conversion types RAT_FUNC or LINEAR
        r"(?P<conv_type_end>\s+/\* ConversionType \*/\n)"  # Capture end of conversion type line
        r'(?P<format_begin>\s+"%)'  # Capture beginning of format line
        r"[0-9]+[.][0-9]+"  # Capture formatting
        r'(?P<format_end>"\s+/\* Format \*/\n)'  # Capture end format line
        r'(?P<unit_begin>\s+"[\sA-Za-z0-9\-_/]+)'  # Capture beginning of unit line
        r",\$(?P<tab_verb>CVC_[A-Za-z0-9_]+)"  # Capture tab_verb 'CVC_*' of $CVC_EmCoBaseMode
        r'(?P<unit_end>"\s*/\* Unit \*/\n)'  # Capture end of unit line
        r"\s+COEFFS( \d+(.\d+)?)+"
    )  # Capture COEFFS line
    COMPU_METHOD_REGEX = re.compile(COMPU_METHOD_EXPRESSION)
    TAB_VERB_REPLACE = (
        r"TAB_VERB\g<conv_type_end>\g<format_begin>12.6\g<format_end>\g<unit_begin>\g<unit_end>"
        r"        COMPU_TAB_REF CONV_TAB_\g<tab_verb>"
    )

    a2l_patched = COMPU_METHOD_REGEX.sub(TAB_VERB_REPLACE, a2l_text)
    with open(file_path, "w") as f_h:
        f_h.write(a2l_patched)


def main():
    """Main."""
    args = parse_args()
    replace_tab_verb(args.a2l_target_file)


if __name__ == "__main__":
    main()
