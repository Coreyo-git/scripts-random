#!/bin/bash

srcDIR="/home/coreyo/mnt/OneDrive/" # The source directory to sync from
syncDIR="/home/coreyo/Documents/OneDriveSync/" # The directory being synced too
bckDIR="/home/coreyo/Documents/ODSBakup" # Backup of the synced files
log="/tmp/OneDriveSync.txt"

if [ -d "$syncDIR" ]; # If the directory exists 
then
	if [ "(ls -A $syncDIR)" ]; then # if the directory is not empty
		echo "Works"
		rsync -av /home/coreyo/mnt/OneDrive/ /home/coreyo/Documents/OneDriveSync/
	else # if is empty
		echo "$syncDIR was empty" > $log 
	fi
else
	echo "Directory $srcDIR not found." > $log
fi 


# rsync -av --dry-run /home/coreyo/mnt/OneDrive/ /home/coreyo/Documents/OneDriveSync/
# rsync -rv /home/coreyo/mnt/OneDrive/ /home/coreyo/Documents/OneDriveSync/
