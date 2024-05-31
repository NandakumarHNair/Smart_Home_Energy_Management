from mqtt_client import init_mqtt_client
from device_manager import DeviceManager
from scheduler.py import Scheduler
from analytics import Analytics

def main():
    device_manager = DeviceManager()
    analytics = Analytics()
    scheduler = Scheduler(device_manager)

    # Initialize MQTT client
    mqtt_client = init_mqtt_client()
    mqtt_client.loop_start()

    # Example device management
    device_manager.add_device('device1', 'Air Conditioner', 1.5)
    device_manager.add_device('device2', 'Heater', 2.0)

    # Schedule devices
    scheduler.schedule_device('device1', 'ON', '08:00')
    scheduler.schedule_device('device1', 'OFF', '20:00')
    scheduler.schedule_device('device2', 'ON', '18:00')
    scheduler.schedule_device('device2', 'OFF', '22:00')

    # Run scheduler
    scheduler.run()

    # Example analytics logging
    energy_usage = device_manager.calculate_energy_usage('device1', 12)
    analytics.log_energy_usage('device1', energy_usage)
    print(analytics.get_energy_usage_report())

if __name__ == "__main__":
    main()
