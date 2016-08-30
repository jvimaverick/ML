#!/bin/bash
/bin/sed "s/NEW_RELIC_APP_NAME/${NEW_RELIC_APP_NAME}/g" nginx-nr-agent.template > nginx-nr-agent.ini
/usr/bin/nginx-nr-agent.py -c nginx-nr-agent.ini start &
/bin/bash -c "echo \"Aloha! im nginx ${APP_NAME}\" > /tmp/index.html && nginx -g 'daemon off;'"
