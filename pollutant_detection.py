class PollutantDetector:
    def __init__(self):
        self.wavelength_ranges = {
            'nitrates': (400, 500),
            'CDOM': (300, 400),
            'aromatic_hydrocarbons': (250, 300),
            'chlorophyll': (650, 750),
            'phosphate': (200, 250),
            'iron': (350, 400),
            'copper': (300, 350),
        }

    def detect_pollutant(self, wavelength):
        for pollutant, (min_wl, max_wl) in self.wavelength_ranges.items():
            if min_wl <= wavelength <= max_wl:
                return pollutant
        return 'unknown'

    def turbidity_correction(self, raw_measurement, turbidity):
        # Placeholder for turbidity correction algorithm
        corrected_measurement = raw_measurement - (turbidity * 0.1)  # Example correction factor
        return max(corrected_measurement, 0)  # Ensure non-negative values
