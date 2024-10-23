#!/bin/bash
# Writes the initial DietPi OS image to the card.

sd_device="$1"

while [ -z "$sd_device" ]; do
    read -p "SD card device [/dev/mmcblk0]: " sd_device

    if [ -z "$sd_device" ]; then
        sd_device="/dev/mmcblk0"
    fi

    set +e
    sd_model=$( fdisk -l /dev/mmcblk0 | head -1 )
    if [ $? -ne 0 ]; then
        echo "Cannot use ${sd_device}. Try one of the following:"
        lsblk -np -o TYPE,NAME,MODEL,SIZE | grep "^disk" | cut -d' ' -f 2-
        echo

        sd_device=""
    fi
    set -e
done


# Write to SD card
mount | grep "^${sd_device}" | cut -d ' ' -f 3 | xargs -r umount
if [ ! -e "$sd_device" ]; then
    echo "Cannot find ${sd_device}."
    exit 1
fi

if [ ! -e DietPi_OrangePiZero3-ARMv8-Bookworm.img.xz ]; then
    echo "Downloading."
    wget https://dietpi.com/downloads/images/DietPi_OrangePiZero3-ARMv8-Bookworm.img.xz
fi

echo "Copying."
xzcat DietPi_OrangePiZero3-ARMv8-Bookworm.img.xz | dd of="${sd_device}" bs=4M conv=fsync status=progress
sync

# Mount SD card
tempdir=$( mktemp -d )
rootfs="${tempdir}/rootfs"
boot="${tempdir}/boot"

mkdir -p "$boot" "$rootfs"

mount -t ext4 "${sd_device}p1" "$rootfs"
mount -t vfat "${sd_device}p2" "$boot"

# Copy config file and startup script
cp dietpi.txt "$boot/dietpi.txt"
cp Automation_Custom_Script.sh "$boot/Automation_Custom_Script.sh"
cp nfc-config.example.json "$rootfs/nfc-config.json"

# Cleanup
sync
umount "$rootfs"
umount "$boot"
rm -rf "$tempdir"
