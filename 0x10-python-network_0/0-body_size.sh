#!/bin/bash
# cUrl body
curl -sI "${1}" | grep "Content-Length" | cut -c 17-
