#!/usr/bin/env python3

import time
import os
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
log = logging.getLogger('waterpump-manager')

def get_config():
    config_path = os.path.join(os.environ.get('SNAP_COMMON', '/var/snap/waterpump-manager-snap/common'), 'config.json')
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"pump-status": "off"}

def main():
    while True:
        config = get_config()
        pump_status = config.get('pump-status', 'off')
        
        log.info(f"Water Pump Status: {pump_status.upper()}")
        log.info(f"Water Pressure: {120 if pump_status == 'on' else 0} psi")
        log.info(f"Water Flow Rate: {10 if pump_status == 'on' else 0} gpm")
        
        time.sleep(10)  # Check status every minute

if __name__ == "__main__":
    main()