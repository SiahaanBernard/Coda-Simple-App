#! /bin/bash
FILE="/etc/systemd/system/simple-app.service"
if [ -f "$FILE" ]
then
        echo "File exist"
        systemctl stop simple-app
fi

exit 0