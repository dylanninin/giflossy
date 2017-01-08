#!/bin/sh

/bin/shell2http \
  -port=9100 \
  -form \
  /info 'wget $v_url -qO- | /bin/gifsicle -I' \
  /sinfo 'wget $v_url -qO- | /bin/gifsicle --sinfo' \
  /cinfo 'wget $v_url -qO- | /bin/gifsicle --cinfo' \
  /xinfo 'wget $v_url -qO- | /bin/gifsicle --xinfo' \
  /verbose 'wget $v_url -qO- | /bin/gifsicle -V' \
  /handler 'wget $v_url -qO- | /bin/gifsicle -O3 --lossy=80' \
  /resizefit 'wget $v_url -qO- | /bin/gifsicle -O3 --lossy=80 --resize-fit $v_m' \
  /resize 'wget $v_url -qO- | /bin/gifsicle -O3 --lossy=80 --resize $v_m' \
  /scale 'wget $v_url -qO- | /bin/gifsicle -O3 --scale $v_m' \
  /lossy 'wget $v_url -qO- | /bin/gifsicle -O3 --lossy=$v_m' \
  /optimize 'wget $v_url -qO- | /bin/gifsicle -O$v_m' \
  /interlace 'wget $v_url -qO- | /bin/gifsicle -i' \
  /crop 'wget $v_url -qO- | /bin/gifsicle --crop $v_m' \
  /rotate 'wget $v_url -qO- | /bin/gifsicle --rotate-$v_m' \
  /health 'echo ok' \
  /help '/bin/gifsicle -h'
