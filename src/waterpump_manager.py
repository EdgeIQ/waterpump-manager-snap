#!/usr/bin/env python3

import time
import os
import json
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
log = logging.getLogger('waterpump-manager')

def get_config():
    config_path = os.path.join(os.environ.get('SNAP_COMMON', '/var/snap/waterpump-manager-snap/common'), 'config.json')
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {"pump_status": "off"}

def main():
    while True:
        config = get_config()
        pump_status = config.get('pump_status', 'off')
        
        log.info(f"Water Pump Status: {pump_status}")
        log.info(f"Water Pressure: {120 if pump_status == 'on' else 0} PSI")
        log.info(f"Water Flow Rate: {10 if pump_status == 'on' else 0} GPM")
        
        time.sleep(60)  # Check status every minute

if __name__ == "__main__":
    main()