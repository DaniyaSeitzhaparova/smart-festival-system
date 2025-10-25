import random
import time

class SmartLightingSystem:
    def __init__(self):
        self.energy_usage = 0.0
        self.lights_on = True

    def measure_energy(self):
        """Simulate real-time energy measurement."""
        self.energy_usage = round(random.uniform(2.5, 4.0), 2)
        print(f"[Lighting] Current energy usage: {self.energy_usage} kWh")

    def optimize(self):
        """Simulate automated optimization based on sensor data."""
        if self.energy_usage > 3.5:
            self.lights_on = False
            print("[Lighting] Lights turned off to save energy.")
        else:
            self.lights_on = True
            print("[Lighting] Energy usage optimal, lights remain on.")

if __name__ == "__main__":
    system = SmartLightingSystem()
    for _ in range(3):
        system.measure_energy()
        system.optimize()
        time.sleep(1)
