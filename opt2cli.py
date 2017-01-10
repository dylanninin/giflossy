#!/bin/env python

"""opt2cli.
Convert options to a valid command with respective options.

Usage:
    opt2cli.py [ --info | --sinfo | --cinfo | --xinfo ]
    opt2cli.py [ --resize=<WxH> ] [ --lossy=<STRENGTH> ] [ --optimize=<LEVEL> ] [ --interlace ]
    opt2cli.py [ --resize-fit=<WxH> ] [ --lossy=<STRENGTH> ] [ --optimize=<LEVEL> ] [ --interlace ]
    opt2cli.py [ --resize-colors=<N> ] [ --lossy=<STRENGTH> ] [ --optimize=<LEVEL> ] [ --interlace ]
    opt2cli.py [ --optimize=<LEVEL>] [ --lossy=<STRENGTH> ] [ --interlace ]
    opt2cli.py [ --scale=<XFACTORxYFACTOR> ] [ --lossy=<STRENGTH> ] [ --optimize=<LEVEL> ] [ --interlace ]
    opt2cli.py [ --crop=<X,Y+WxH> ] [ --lossy=<STRENGTH> ] [ --optimize=<LEVEL> ] [ --interlace ]
    opt2cli.py [ --rotate=<DEGREE> ] [ --lossy=<STRENGTH> ] [ --optimize=<LEVEL> ] [ --interlace ]
    opt2cli.py (-h | --help)
    opt2cli.py --version

Options:
    -h --help                   Show this screen.
    --info                      Print info about input GIFs.
    --sinfo                     --info plus compression information.
    --cinfo                     --info plus colormap details.
    --xinfo                     --info plus extension details.
    --resize=<WxH>              Resize the output GIF to WxH.
    --resize-fit=<WxH>          Resize if necessary to fit within WxH.
    --resize-colors=<N>         Resize can add new colors up to N.
    --scale=<XFACTORxYFACTOR>   Scale the output GIF by XFACTORxYFACTOR.
    --lossy=<STRENGTH>          Order pixel patterns to create smaller
                                GIFs at cost of artifacts and noise.
    --optimize=<LEVEL>          Optimize output GIFs.
    --interlace                 Turn on interlacing.
    --crop=<X,Y+WxH>            or crop=<X,Y-X2,Y2>.
                                Crop the image.
    --rotate=<DEGREE>           Rotate the image: 90,180,270.
"""
from docopt import docopt


gifcile='/bin/gifsicle'
delimiters = {
    '--optimize': '=',
    '--lossy': '=',
    '--rotate': '-',
}


if __name__ == '__main__':
    cli = ''
    args = docopt(__doc__)
    for k in args.keys():
        v = args[k]
        d = delimiters.get(k) or ' '
        if v is True:
            cli += "{0} ".format(k)
        elif v is not None:
            cli += "{0}{1}{2} ".format(k, d, v) if v else ''
        else:
            pass
    print('{0} {1}'.format(gifcile, cli))
