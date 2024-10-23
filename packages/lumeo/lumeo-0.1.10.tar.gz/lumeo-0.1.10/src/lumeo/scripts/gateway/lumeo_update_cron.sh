#!/bin/bash

set -eo pipefail

wget -q https://assets.lumeo.com/lumeod/lumeo_gateway_update.sh -O /dev/shm/lumeo_gateway_update.sh

sudo bash /dev/shm/lumeo_gateway_update.sh
rm /dev/shm/lumeo_gateway_update.sh
