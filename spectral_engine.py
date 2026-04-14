import numpy as np
import pandas as pd
import json

class SpectralEngine:
    def __init__(self):
        self.optical_paths = {'sample': [], 'reference': []}
        self.current_lamp = None
        self.last_scanned_wavelength = None
        
    def switch_lamp(self, wavelength):
        if 200 <= wavelength <= 300:
            self.current_lamp = 'Deuterium'
        elif 300 < wavelength <= 700:
            self.current_lamp = 'Tungsten'
        elif 700 < wavelength <= 800:
            self.current_lamp = 'Halogen'
        else:
            raise ValueError('Wavelength out of range')
        
    def scan_wavelength(self, start, end, step):
        wavelengths = np.arange(start, end, step)
        spectra = []
        for wavelength in wavelengths:
            self.switch_lamp(wavelength)
            spectrum = self.measure_spectrum(wavelength)
            spectra.append((wavelength, spectrum))
            self.last_scanned_wavelength = wavelength
        return spectra
        
    def measure_spectrum(self, wavelength):
        # Simulated spectrum measurement, include randomness for noise
        noise = np.random.normal(0, 0.1)  # Add stochastic noise 
        return (self.beer_lambert_law(wavelength) + noise)
        
    def beer_lambert_law(self, wavelength):
        # Placeholder for Beer-Lambert law implementation
        absorptivity = 0.1  # Example constant
        concentration = 1.0  # Example concentration
        path_length = 1.0  # Example path length
        return absorptivity * concentration * path_length
        
    def detect_lambda_max(self, spectra):
        max_value = max(spectra, key=lambda x: x[1])
        return max_value[0]

    def export_spectrum(self, spectra, format='csv'): 
        if format == 'csv':
            df = pd.DataFrame(spectra, columns=['Wavelength', 'Intensity'])
            df.to_csv('spectrum.csv', index=False)
        elif format == 'json':
            with open('spectrum.json', 'w') as json_file:
                json.dump(spectra, json_file)
        else:
            raise ValueError('Unsupported format')
