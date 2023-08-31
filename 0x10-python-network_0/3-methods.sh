#!/bin/bash
#Script that displays all the methods accepted by the server
curl -sI ALLOW $1 -L | grep "Allow" | cut -d " " -f2-
