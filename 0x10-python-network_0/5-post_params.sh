#!/bin/bash
# URL as argument , sends GET request to the URL
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST ${1}
