#!/bin/bash

#pincushion user --user-id 120066 --archive-path archives/black-in-appalachia
#pincushion data --user-id 120066 --output archives/black-in-appalachia/data.json
pincushion regenerate --archive-path archives/black-in-appalachia

#pincushion user --user-id 52974 --archive-path archives/apiahip
#pincushion data --user-id 52974 --output archives/apiahip/data.json
pincushion regenerate --archive-path archives/apiahip

#pincushion user --user-id 120640 --archive-path archives/invisible-histories
#pincushion data --user-id 120640 --output archives/invisible-histories/data.json
pincushion regenerate --archive-path archives/invisible-histories

#pincushion user --user-id 120324 --archive-path archives/manila-town
#pincushion user --user-id 120324 --output archives/manila-town/data.json
pincushion regenerate --archive-path archives/manila-town

#pincushion user --user-id 120074 --archive-path archives/us-colored-troops-coalition
#pincushion data --user-id 120074 --output archives/us-colored-troops-coalition/data.json
pincushion regenerate --archive-path archives/us-colored-troops-coalition

#pincushion user --user-id 81351 --archive-path archives/mescalero-apache-nation
#pincushion data --user-id 81351 --output archives/mescalero-apache-nation/data.json
pincushion regenerate --archive-path archives/mescalero-apache-nation

pincushion regenerate --archive-path archives/jonvoss
