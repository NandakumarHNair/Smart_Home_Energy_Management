import schedule
import time
from device_manager import DeviceManager

class Scheduler:
    def __init__(self, device_manager):
        self.device_manager = device_manager

    def schedule_device(self, device_id, action, time_str):
        if action == 'ON':
            schedule.every().day.at(time_str).do(self.device_manager.update_device_status, device_id, 'ON')
        elif action == 'OFF':
            schedule.every().day.at(time_str).do(self.device_manager.update_device_status, device_id, 'OFF')

    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
