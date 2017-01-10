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
    -rw-r- r-   1 dylanninin  staff    10M Jan  8 10:37 demo.gif
    -rw-r- r-   1 dylanninin  staff   1.9M Jan  8 11:04 lossy.gif
    ```

- handler: a simple http wrapper on gifsicle executable binary, see [main.sh](main.sh)
  - syntax: `http://localhost:9100/handler?url={gif_url}&opt={options}`
  - `gif_url`: the url of a gif
  - `options`: like `/opt_1/val_1/opt_2/opt_3/val_3`. available options:
    - info                    Print info about input GIFs.
    - sinfo                   info plus compression information.
    - cinfo                   info plus colormap details.
    - xinfo                   info plus extension details.
    - resize/WxH              Resize the output GIF to WxH.
    - resize-fit/WxH          Resize if necessary to fit within WxH.
    - resize-colors/N         Resize can add new colors up to N.
    - scale/XFACTORxYFACTOR   Scale the output GIF by XFACTORxYFACTOR.
    - lossy/STRENGTH          Order pixel patterns to create smaller
                                GIFs at cost of artifacts and noise.
    - optimize/LEVEL          Optimize output GIFs.
    - interlace               Turn on interlacing.
    - crop/X,Y+WxH            or crop/X,Y-X2,Y2.
                                Crop the image.
    - rotate/DEGREE           Rotate the image: 90,180,270.
    - `examples`
      - lossy/80
      - /optimize/3/lossy/80/interlace
      - /resize/400x400/optimize/3/lossy/80/interlace
      - /resize-fit/400x400/optimize/3/lossy/80/interlace
      - /resize-colors/32/optimize/3/lossy/80/interlace
      - /scale/1.5,1.5/optimize/3/lossy/80/interlace
      - /crop/400,400/optimize/3/lossy/80/interlace
      - /rotate/90/optimize/3/lossy/80/interlace


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
  -rw-r- r-   1 dylanninin  staff    10M Jan  8 10:37 origin.gif
  -rw-r- r-   1 dylanninin  staff   1.9M Jan  8 10:37 origin_lossy.gif
  ```

- Usage

  - `http://{resource_url}?giflossy`: default with `/optimize/3/lossy/80/interlace`
  - `http://{resource_url}?giflossy&opt={options}`: see handler options above.

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
