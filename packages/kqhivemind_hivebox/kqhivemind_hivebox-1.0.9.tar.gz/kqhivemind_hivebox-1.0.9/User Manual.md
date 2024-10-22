# 1. Initial Setup

- Plug in your device using a USB Type-C power cable.
- Connect to the Internet: see section 2
- Select which cabinet the device will sign in to: see section 3.
- (Recommended) Follow the **Command Line Access** instructions in section 4.
  - **This is not required, but it is important to change your device's password.**

# 2. Connecting to Internet

## Wired

- If a wired network is available, plugging in an Ethernet cable to the device should connect it to the internet with no further steps.

## Wireless

- Start up the HiveBox.
- On your phone or PC, wait for the "HiveMind Config" network to be available, then connect to it.
- The configuration page should appear automatically.
  - If it does not, try loading any website.
- On the configuration page, select your wireless network. If necessary, enter your password.
- The HiveBox should connect to your wireless network.

# 3. Cabinet Selection

- Go to [https://kqhivemind.com/devices] or click "Manage Client Devices" in the HiveMind menu.
- Your device should be visible in the list. If it is not, click "Add New Device" to create one.
- Click the "Edit" button.
- Click the "Assigned Cabinet" box.
- Select the scene and cabinet that this device should sign in users for.
- Click the "Save" button.

# 4. Command Line Access

- Find the HiveBox's IP address. This should be shown on the LCD screen at boot. You can also find it on your router's configuration page.
- Open a command prompt:
  - **Windows**: search for and run the "Command Prompt" program
  - **Mac OS or Linux**: launch the "Terminal" application
  - **Android or iOS**: install [Termius](https://termius.com/) (or any other SSH client of your choice)
- In the command prompt, type `ssh <address>`, replacing `<address>` with the HiveBox's IP address.
- The initial password is `HiveMind123`. You will be prompted to change it.

## Editing the Configuration File

- Type `nano nfc-config.json`.
- Make any required edits to the configuration.
- Press `Ctrl+X`, `Y`, and `Enter` to save the edited file and exit the editor.

## Example Configuration File

- See [nfc-config.example.json] for an example config file.

# 5. Troubleshooting

## No Internet Connection

## Invalid Device ID or Token

- Connect to the device via SSH (see section 4).
- Get the correct device ID and token from [https://kqhivemind.com/devices]
- Edit the configuration file with the correct device ID and token.

## Factory Resetting the Software
