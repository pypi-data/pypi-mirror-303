# HiveBox for Orange Pi Zero3

## Connecting to WiFi

If the system is not connected to a WiFi network for more than one minute, it will start up a hotspot named "HiveMind Config". Connect to this hotspot and select the network you wish to connect to.

## Installing from Image

to do

## Advanced: Installing from Scratch

- On your PC, get the DietPi image: https://dietpi.com/downloads/images/DietPi_OrangePiZero3-ARMv8-Bookworm.img.xz
- Write this image to an SD card using a tool such as [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
- After writing the image, copy the following files from this repository to the card's setup partition:
  - `dietpi.txt`
  - `Automation_Custom_Script.sh`
  - `nfc-config.example.json` (rename to `nfc-config.json`)
- Edit the `nfc-config.json` file to set the device ID and token.
- Take the card out of your PC and put it into the Pi.
- Connect the Pi to the internet using an ethernet cable.
- Start up the Pi and wait for initial setup to complete. When complete, the Pi will shut down.

## Building and Uploading the Image

Write the initial settings to the card:
```
sudo ./setup_card.sh
```

Start up the Pi with this card. Make sure its ethernet cable is connected. Wait for initial boot and setup to complete.

When the script finishes, the Pi will shut down. Take out the card and put it back in your PC.

```
export VERSION=1.00
export IMAGE="hivebox-image-${VERSION}.img"
sudo dd if=/dev/mmcblk0 of="${IMAGE}" bs=4M conv=fsync status=progress
sudo chown "${USER}" "${IMAGE}"
sudo ./pishrink.sh "${IMAGE}"  # https://raw.githubusercontent.com/Drewsif/PiShrink/master/pishrink.sh
xz -vzT0 "${IMAGE}"
s3cmd put "${IMAGE}.xz" s3://kqhivemind/pi-images/ --acl-public
```

