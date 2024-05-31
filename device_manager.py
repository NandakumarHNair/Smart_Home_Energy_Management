import json

class DeviceManager:
    def __init__(self):
        self.devices = {}

    def add_device(self, device_id, name, power_rating):
        self.devices[device_id] = {
            'name': name,
            'power_rating': power_rating,
            'status': 'OFF'
        }

    def update_device_status(self, device_id, status):
        if device_id in self.devices:
            self.devices[device_id]['status'] = status

    def get_device_status(self, device_id):
        return self.devices.get(device_id, {}).get('status', 'UNKNOWN')

    def get_all_devices(self):
        return self.devices

    def calculate_energy_usage(self, device_id, hours):
        device = self.devices.get(device_id)
        if device and device['status'] == 'ON':
            return device['power_rating'] * hours
        return 0
