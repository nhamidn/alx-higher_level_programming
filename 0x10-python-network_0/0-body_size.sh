#!/bin/bash
#Script that print the Content-Lenght of request
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
