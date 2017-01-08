A gif lossy compression service based on [gifsicle](https://github.com/kohler/gifsicle/pull/16).

Started
========

- pull: `docker pull dylanninin/giflossy`
- run: `docker run -p 9100:9100 dylanninin/giflossy`
- request:
  - source gif: `wget http://bit.ly/2iP176E -qO demo.gif`
  - lossy compressed: `wget http://localhost:9100/handler?url=http://bit.ly/2iP176E -qO lossy.gif`
  - diff

    ```shell
    ls -hl *.gif
    -rw-r--r--  1 dylanninin  staff    10M Jan  8 10:37 demo.gif
    -rw-r--r--  1 dylanninin  staff   1.9M Jan  8 11:04 lossy.gif
    ```

- handlers: a simple http wrapper on gifsicle executable binary, see [main.sh](main.sh)
  - info: `http://localhost:9100/info?url=http://bit.ly/2iP176E`
  - size, info: `http://localhost:9100/sinfo?url=http://bit.ly/2iP176E`
  - color, info: `http://localhost:9100/cinfo?url=http://bit.ly/2iP176E`
  - extension, info: `http://localhost:9100/xinfo?url=http://bit.ly/2iP176E`
  - default handler(optimize/lossy compressed): `http://localhost:9100/handler?url=http://bit.ly/2iP176E`
  - resize-fit: `http://localhost:9100/resizefit?url=http://bit.ly/2iP176E&m=600x600`
  - resize: `http://localhost:9100/resize?url=http://bit.ly/2iP176E&m=600x600`
  - scale: `http://localhost:9100/scale?url=http://bit.ly/2iP176E&m=XFACTOR[xYFACTOR]`
  - lossy: `http://localhost:9100/lossy?url=http://bit.ly/2iP176E&m=80`
  - optimize: `http://localhost:9100/optimze?url=http://bit.ly/2iP176E&m=3`
  - interlaced: `http://localhost:9100/interlace?url=http://bit.ly/2iP176E`
  - crop: `http://localhost:9100/crop?url=http://bit.ly/2iP176E&m=400,400`
  - rotate: `http://localhost:9100/rotate?url=http://bit.ly/2iP176E&m=90`
  - help: `http://localhost:9100/help`

Qiniu ufop
========

Refer [开发者自定义数据处理程序-快速入门](http://developer.qiniu.com/article/dora/ufop/v2/ufop-fast.html)

- register ufop

  ```shell
  qdoractl register giflossy -d "Gif Lossy Compression service based on gifsicle" -m protected
  ```

- push image

  ```shell
  qdoractl push dylanninin/giflossy:v1
  ```

- add release config

  ```shell
  qdoractl release --mkconfig .
  ```

- config release

  ```shell
  qdoractl release --config .
  ```

- add release

  ```shell
  qdoractl release giflossy -d
  ```

- deploy

  ```shell
  qdoractl deploy giflossy v1 --region z0 --expect 1
  ```

- test

  ```shell
  wget http://7xiqcg.com1.z0.glb.clouddn.com/demo.gif -qO origin.gif
  wget http://7xiqcg.com1.z0.glb.clouddn.com/demo.gif?giflossy -qO origin_lossy.gif

  ls -lh *.gif
  -rw-r--r--  1 dylanninin  staff    10M Jan  8 10:37 origin.gif
  -rw-r--r--  1 dylanninin  staff   1.9M Jan  8 10:37 origin_lossy.gif
  ```

Build from scratch
========

- build: `rocker build`

Reference
========

- https://github.com/msoap/shell2http
- https://github.com/pornel/giflossy
- https://github.com/kohler/gifsicle/pull/16
- https://github.com/dylanninin/gifsicle/tree/lossy
- https://github.com/grammarly/rocker
- http://developer.qiniu.com/article/dora/ufop/v2/ufop-fast.html
