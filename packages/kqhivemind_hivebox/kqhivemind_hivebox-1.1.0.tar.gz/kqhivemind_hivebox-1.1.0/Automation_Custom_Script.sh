#!/bin/bash
# Generates HiveMind image starting from DietPi OS base.
set -e

# Install packages
apt-get update
apt-get -o Dpkg::Options::='--force-confold' -y install libnfc-dev libnfc-bin libnfc-examples \
        gpiod libgpiod-dev i2c-tools libi2c-dev network-manager dnsmasq cmake rsync python3-smbus

# Add HiveMind user
gpioset /dev/gpiochip0 233=1
useradd -m -U -G sudo,plugdev,i2c hivemind
usermod -L dietpi
chsh -s /bin/bash hivemind
echo 'hivemind:HiveMind123' | chpasswd
passwd -e hivemind

cat /etc/sudoers | sed 's/^\%sudo.*$/%sudo  ALL=(ALL) NOPASSWD:ALL/' > /tmp/sudoers
chown root:root /tmp/sudoers
chmod 600 /tmp/sudoers
mv /tmp/sudoers /etc/sudoers

cd /home/hivemind

# Enable I2C
gpioset /dev/gpiochip0 233=0 78=1
sed -i 's/^overlays\=.*$/overlays=i2c3-ph/' /boot/dietpiEnv.txt

# Create gpio group
groupadd -U hivemind gpio
cat > /etc/udev/rules.d/90-gpio.rules <<EOF
KERNEL=="gpio*", MODE:="0660", GROUP:="gpio"
SUBSYSTEM=="gpio*", PROGRAM="/bin/sh -c 'find -L /sys/class/gpio/ -maxdepth 2 -exec chown root:gpio {} \; -exec chmod 770 {} \; || true'"
EOF

# Install NFC client and scripts
gpioset /dev/gpiochip0 78=0 70=1
mv /nfc-config.json /home/hivemind/
chown hivemind:hivemind /home/hivemind/nfc-config.json
sudo -u hivemind pip3 install kqhivemind_hivebox
cat > /home/hivemind/hivebox.sh <<EOF
#!/bin/bash
/home/hivemind/.local/bin/hivebox /home/hivemind/nfc-config.json >> /home/hivemind/hivebox.log 2>&1
EOF

chmod +x /home/hivemind/hivebox.sh

cat > /root/crontab <<EOF
35 * * * * /usr/local/bin/pip3 install --upgrade kqhivemind_hivebox
EOF
crontab -u hivemind /root/crontab
rm /root/crontab

cat > /lib/systemd/system/hivebox.service <<EOF
[Unit]
Description=HiveMind NFC Reader Service
After=network-online.target nss-lookup.target
Wants=network-online.target nss-lookup.target

[Service]
ExecStart=/home/hivemind/hivebox.sh
User=hivemind

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable hivebox

# Install NetworkManager and wifi-connect
gpioset /dev/gpiochip0 70=0 72=1
systemctl enable NetworkManager
systemctl disable dnsmasq

echo "sprdwl_ng" > /etc/modules-load.d/dietpi-enable_wifi.conf
rm /etc/modprobe.d/dietpi-disable_wifi.conf

cat > /etc/network/interfaces <<EOF
# Location: /etc/network/interfaces

source interfaces.d/*

allow-hotplug eth0
iface eth0 inet dhcp
EOF

wget https://github.com/balena-os/wifi-connect/releases/download/v4.11.59/wifi-connect-aarch64-unknown-linux-gnu.tar.gz
tar xfvz wifi-connect-aarch64-unknown-linux-gnu.tar.gz
mv wifi-connect /usr/local/bin/
chmod +x /usr/local/bin/wifi-connect

wget https://github.com/balena-os/wifi-connect/releases/download/v4.4.6/wifi-connect-v4.4.6-linux-aarch64.tar.gz
tar xfvz wifi-connect-v4.4.6-linux-aarch64.tar.gz
rm wifi-connect
mkdir -p /usr/share/wifi-connect
mv ui /usr/share/wifi-connect/

rm -f wifi-connect-aarch64-unknown-linux-gnu.tar.gz wifi-connect-v4.4.6-linux-aarch64.tar.gz

cat > /usr/local/bin/auto-wifi-connect.sh <<'EOF'
#!/bin/bash

fails=0
while true; do
    active=$( nmcli -t conn show --active | grep wlan0 )
    if [ -z "$active" ]; then
        fails=$(($fails + 1))
    else
        fails=0
    fi

    if [[ $fails > 2 ]]; then
        echo $active
        /usr/local/bin/wifi-connect -s "HiveMind Config" -u /usr/share/wifi-connect/ui
    fi

    sleep 30
done
EOF
chmod +x /usr/local/bin/auto-wifi-connect.sh

cat > /lib/systemd/system/auto-wifi-connect.service <<EOF
[Unit]
Description=Auto WiFi-Connect
After=network-online.target nss-lookup.target
Wants=network-online.target nss-lookup.target

[Service]
ExecStart=/usr/local/bin/auto-wifi-connect.sh

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable auto-wifi-connect

# Cleanup
cat > /lib/systemd/system/regenerate-ssh-host-keys.service <<EOF
[Unit]
Description=Regenerate SSH host keys
Before=ssh.service
ConditionFileIsExecutable=/usr/bin/ssh-keygen

[Service]
Type=oneshot
ExecStartPre=-sh -c "rm -f -v /etc/ssh/ssh_host_*_key*"
ExecStart=ssh-keygen -A -v
ExecStartPost=-sh -c "echo ssh-keygen: Complete"
ExecStartPost=systemctl disable regenerate-ssh-host-keys.service
StandardOutput=journal+console

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable regenerate-ssh-host-keys.service

chown -R hivemind:hivemind /home/hivemind
rm /etc/ssh/ssh_host_*
gpioset /dev/gpiochip0 72=0 232=1
shutdown now
