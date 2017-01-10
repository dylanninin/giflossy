#!/bin/env python

"""path2opt.
Convert a valid path of a URI to options of any command.

Usage:
    path2opt.py [-h | --path=<p>]

Options:
    -p --path=<p>   Input path.
    -h --help       Show this screen.

Example:
    path2opt.py -p /optimize/3/lossy/80/interlace
    path2opt.py -p /scale/1.5,1.5/optimize/3/lossy/80/interlace
    path2opt.py -p /resize/400x400/optimize/3/lossy/80/interlace
    path2opt.py -p /resize-fit/400x400/optimize/3/lossy/80/interlace
    path2opt.py -p /resize-colors/32/optimize/3/lossy/80/interlace
    path2opt.py -p /crop/400,400/optimize/3/lossy/80/interlace
    path2opt.py -p /rotate/90/optimize/3/lossy/80/interlace
    path2opt.py (-h | --help)
"""
import re
from docopt import docopt


def is_opt(name):
    """Return True if name if a valid option name, False otherwise.
    """
    return bool(re.search('[a-zA-Z\-]', name))


if __name__ == '__main__':
    opts = {}
    args = docopt(__doc__)
    path = args.get('--path') or '/optimize/3/lossy/80/interlace'
    path = path.strip('/').strip('/')
    parts = path.split('/')
    l = len(parts)
    for i, v in enumerate(parts):
        if is_opt(v):
            opts[v] = ''
            if i+1 < l and not is_opt(parts[i+1]):
                opts[v] = parts[i+1]
                continue
        else:
            continue
    for k, v in opts.items():
        print('--{0} {1}'.format(k, v), end=' ')
    print()
