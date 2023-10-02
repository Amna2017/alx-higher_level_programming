#!/bin/bash
# displays status only code of the response.
curl -s -o  /dev/null -w "%{http_code}" "${1}"
