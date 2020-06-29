#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convert rst to html."""

import docutils.core
from pathlib import Path
import sys

def rst2html(source_path, destination_path=None, css=None):
    if destination_path is None:
        destination_path = str(Path(source_path).parent/(Path(source_path).name.split('.')[0] + '.html'))

    if css is not None:
        settings_overrides = {'stylesheet_path' : css}
        docutils.core.publish_file(source_path      = source_path,
                                   destination_path = destination_path,
                                   writer_name ="html",
                                   settings_overrides = settings_overrides)
    else:
        docutils.core.publish_file(source_path      = source_path,
                                   destination_path = destination_path,
                                   writer_name ="html")

if __name__ == '__main__':

    if len(sys.argv) == 3:
        rst2html(source_path=sys.argv[1], destination_path=None, css=sys.argv[2])
    else:
        rst2html(source_path=sys.argv[1])
