#!/bin/bash

sd_device=/dev/mmcblk0
image=$( ls hivebox-image-*.xz | tail -1 )

device_id="$1"
token="$2"
color="$3"

echo -e "Writing image \033[1;36m${image}\033[0m to device \033[1;35m${sd_device}\033[0m"

mount | grep "^${sd_device}" | cut -d ' ' -f 3 | xargs -r umount
sleep 1
xzcat "$image" | dd of="$sd_device" bs=4M conv=fsync status=progress

sync
sleep 1
mount | grep "^${sd_device}" | cut -d ' ' -f 3 | xargs -r umount
sleep 1

rootfs=$( mktemp -d )
mkdir -p "$rootfs"

mount -t ext4 "${sd_device}p1" "$rootfs"

cat > "${rootfs}/home/hivemind/nfc-config.json" <<EOF
{
    "device": "$device_id",
    "token": "$token",
    "reader": "$color",
    "pin_config": [
        { "position": "stripes", "button": 74, "light": 233 },
        { "position": "abs",     "button": 71, "light": 78 },
        { "position": "queen",   "button": 69, "light": 70 },
        { "position": "skulls",  "button": 231, "light": 72 },
        { "position": "checks",  "button": 230, "light": 232 }
    ],
    "driver": "pn532_i2c",
    "i2c_channel": 2
}
EOF

sync
umount "$rootfs"
rm -rf "$tempdir"
