# pdf-decompiler

This is to decompile a given pdf to one just with selected pages.

## Prerequisites

This requires some steps to show GUI through X server.

1. Install X server, e.g. VcXsrv. 
<br>(For Win users: https://atmarkit.itmedia.co.jp/ait/articles/1812/06/news040.html)

1. Add command below to ~/.bashrc to configure an environment variable to connect a display running on Docker 
```
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0.0
```
2. Run command below to configure access to X server 
```
$ sudo apt-get install x11-xserver-utils
$ xhost +local:root
```
## Usage
1. Put a pdf you want to edit in ./data/
2. Run commands below to edit pdf so that the new file is generated on the same directory.
```
docker compose build
docker compose run app
```