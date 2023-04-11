#!/bin/bash
UPDATEURL="https://discord.com/api/download?platform=linux&format=tar.gz"
UPDATETAR="/tmp/discord.tar.gz"
UPDATEFOLDER="/tmp/Discord"
DISCORDPATH='/usr/lib64/discord'

echo "Getting discord udpate"

# get latest update
# wget "$UPDATEURL" -O /tmp/discord.tar.gz

# check if update exists
if compgen -G "${UPDATETAR}" > /dev/null; then
    echo "Extracting..."
	tar -xf $UPDATETAR -C /tmp

	# get latest update
	# manually move update fules
	echo "Updating..."
	mv $UPDATEFOLDER/* $DISCORDPATH/ 
	mv $UPDATEFOLDER/locales/* $DISCORDPATH/locales/ 
	mv $UPDATEFOLDER/resources/* $DISCORDPATH/resources/ 
	mv $UPDATEFOLDER/resources/bootstrap/* $DISCORDPATH/resources/bootstrap 
	mv $UPDATEFOLDER/swiftshader/* $DISCORDPATH/swiftshader/ 

	echo "Finished."
else
	echo "discord update could not found"
fi
