#!/bin/sh

/bin/shell2http \
  -port=9100 \
  -form \
  /handler 'wget $v_url -qO- | `python3 /app/path2opt.py --path $v_opt | xargs python3 /app/opt2cli.py`' \
  /health 'echo ok'
