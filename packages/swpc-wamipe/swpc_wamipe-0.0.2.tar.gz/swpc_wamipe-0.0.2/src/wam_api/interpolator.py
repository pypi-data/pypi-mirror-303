import numpy as np
from scipy.interpolate import interp1d, interpn

class Interpolator():
    def spatial(self, ds, lat, lon, alt):
        lats = ds.variables['lat'][:]
        lons = ds.variables['lon'][:]
        alts = ds.variables['hlevs'][:]
        density = ds.variables["den"][:]
        density = np.squeeze(density)

        # 2D interpolation using interpn for each altitude level
        interp_densities = []
        for i in range(len(alts)):
            density_slice = density[i, :, :]
            interp_density = interpn((lats, lons), density_slice, (lat, lon), method='linear', bounds_error=False, fill_value=np.nan)
            interp_densities.append(interp_density[0])

        # Logarithmic quadratic interpolation in the vertical
        log_alts = np.log(alts)
        log_alt = np.log(alt)
        log_interp = interp1d(log_alts, np.log(interp_densities), kind='quadratic', bounds_error=False, fill_value='extrapolate')
        
        density_interp = np.exp(log_interp(log_alt))

        return float(density_interp)
    
    def temporal(self, input_dt, surrounding_dts, densities):
        times = np.array([(tdt - surrounding_dts[0]).total_seconds() for tdt in surrounding_dts])
        dt_seconds = (input_dt - surrounding_dts[0]).total_seconds()
        return np.interp(dt_seconds, times, densities)