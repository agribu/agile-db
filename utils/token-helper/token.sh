#!/bin/bash
ALICE_POST="$(curl -s 'http://localhost:3000/oauth2/dialog/authorize/?response_type=token&redirect_uri=http://localhost:8000/&client_id=AGILE-OSJS' \
          -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' \
          -H 'Accept-Language: de,en-US;q=0.7,en;q=0.3' --compressed -H 'Referer: http://localhost:8000/' \
          -H 'Cookie: session=29660a10644a63826b0c7e49aa7c9a3e; connect.sid=s%3Aqid3jyh9oCXRRMbPmEw9bNwD_QPk96Wh.VarWHbf%2FKS7VHJTE79BtUOjZzT1Il0ZacXHiDB1Vn6E' \
          -H 'Connection: keep-alive' \
          -H 'Upgrade-Insecure-Requests: 1')"

ALICE_TOKEN="$(echo $ALICE_POST | cut -d '#' -f2 | cut -d '&' -f1 | cut -d '=' -f2)"

echo "Alice's token: ${ALICE_TOKEN}"
