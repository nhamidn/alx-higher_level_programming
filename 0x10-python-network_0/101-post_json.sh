#!/bin/bash
#Script that sends POST request with json datae
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L
