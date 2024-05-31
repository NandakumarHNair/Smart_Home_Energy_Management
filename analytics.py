import pandas as pd

class Analytics:
    def __init__(self):
        self.data = []

    def log_energy_usage(self, device_id, energy_usage):
        self.data.append({
            'device_id': device_id,
            'energy_usage': energy_usage
        })

    def get_energy_usage_report(self):
        df = pd.DataFrame(self.data)
        return df.groupby('device_id').sum().reset_index()
