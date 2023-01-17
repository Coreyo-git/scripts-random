#!/bin/bash
UPDATEURL="https://discord.com/api/download?platform=linux&format=tar.gz"
UPDATETAR="/tmp/discord.tar.gz"
UPDATEFOLDER="/tmp/Discord"
DISCORDPATH='/usr/lib64/discord/'

echo "Getting discord udpate"

# get latest update
wget "$UPDATEURL" -O /tmp/discord.tar.gz

# check if update exists
if compgen -G "${UPDATETAR}" > /dev/null; then
    echo "Extracting..."
	tar -xf $UPDATETAR -C /tmp

	# get latest update
	# manually move update fules
	echo "Updating..."
	mv $UPDATEFOLDER/* $DPATH/ >/dev/null 2>&1
	mv $UPDATEFOLDER/locales/* $DPATH/locales/ >/dev/null 2>&1
	mv $UPDATEFOLDER/resources/* $DPATH/resources/ >/dev/null 2>&1
	mv $UPDATEFOLDER/resources/bootstrap/* $DPATH/resources/bootstrap >/dev/null 2>&1
	mv $UPDATEFOLDER/swiftshader/* $DPATH/swiftshader/ >/dev/null 2>&1

	echo "Finished."
else
	echo "discord update could not found"
fi

	

