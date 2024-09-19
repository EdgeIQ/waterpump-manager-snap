# waterpump-manager-snap

A demo snap application that simulates a water pump manager daemon.

## Installation

To install the snap, use the following command:

``` bash
sudo snap install waterpump-manager-snap --devmode --dangerous
```

This updated README.md file now includes all the necessary information about the project, including installation instructions, usage guidelines, configuration details, development setup, and contribution information. It provides a comprehensive overview of the waterpump-manager-snap project.

Note: The `--devmode` flag is used because this is a development version. For production, you would use `--stable` instead.

## Usage

### Controlling the Water Pump

You can control the water pump status using the following command:


### Viewing Logs

To view the daemon logs, which include the current status of the

```bash
sudo journalctl -u snap.waterpump-manager-snap.daemon.service
```

## Configuration

The configuration is stored in `/var/snap/waterpump-manager-snap/common/config.json`. This file is automatically created and updated when you use the `snap set` command.

```bash
sudo snap set waterpump-manager-snap pump_status=<on|off>
```


## Development

### Project Structure

- `src/waterpump_manager.py`: The main Python script for the water pump manager daemon.
- `snap/snapcraft.yaml`: The snapcraft configuration file that defines how the snap is built.
- `snap/hooks/configure`: A hook script that handles configuration changes.

### Building the Snap

To build the snap package:

1. Ensure you have `snapcraft` installed:
   ```bash
   sudo snap install snapcraft --classic
   ```

2. Navigate to the project directory and run:
   ```bash
   snapcraft
   ```

3. This will create a `.snap` file in the current directory.

### Testing

To test the snap locally:

1. Install the newly created snap:
   ```bash
   sudo snap install --devmode waterpump-manager-snap_*.snap
   ```

2. Use the `snap set` commands as described in the Usage section to control the pump.

3. Check the logs to verify the daemon is working as expected.

## Contributing

Contributions to improve the waterpump-manager-snap are welcome. Please feel free to submit pull requests or open issues to discuss potential changes or improvements.
