from datetime import datetime, timedelta
from interpolator import Interpolator
from netCDF4 import Dataset
from lru_cache import LRU_Cache


class WAMInterpolator:
    # Define Class Constants
    BUCKET = 'noaa-nws-wam-ipe-pds'  # AWS S3 Bucket Definition
    FORECAST_SYS_FALLBACK = ['wrs', 'wfs']  # Order of preference for system types

    METADATA_DICT = [
        {'v1.1': {
            'start_datetime': datetime(2023, 3, 20, 21, 10, 0),
            'end_datetime': datetime(2023, 6, 30, 21, 0, 0)
        }},
        {'v1.2': {
            'start_datetime': datetime(2023, 6, 30, 21, 10, 0),
            'end_datetime': datetime.utcnow()
        }}
    ]

    def __init__(self, cache_size=100, forecast_sys_prefer='wrs'):
        self.forecast_sys_prefer = forecast_sys_prefer
        self.cache = LRU_Cache(cache_size)

    def get_density(self, input_dt, lat, lon, alt):
        """
        Get the interpolated density at the given datetime, latitude, longitude, and altitude.

        Parameters:
            input_dt (datetime): The target datetime in UTC.
            lat (float): Latitude in degrees north (-90 to 90).
            lon (float): Longitude in degrees east (0 to 360).
            alt (float): Altitude in kilometers.

        Returns:
            float: The interpolated density value.
        """

        if not (-90 <= lat <= 90):
            raise ValueError("Latitude must be between -90 and 90 degrees.")

        if not (0 <= lon <= 360):
            lon = lon % 360

        if alt < 0:
            raise ValueError("Altitude must be a positive number")

        datasets = self.get_datasets(input_dt)
        if len(datasets) < 1:
            raise FileNotFoundError("No Datasets Exist for the specified Date/Time")

        # Create an Instance of the Interpolator
        interpolate = Interpolator()
        densities = []

        # Spatial Interpolation
        for ds in datasets:
            density = interpolate.spatial(ds, lat, lon, alt)
            densities.append(density)
            ds.close()

        # Temporal interpolation
        surrounding_dts = self.get_surrounding_datetimes(input_dt)
        return interpolate.temporal(input_dt, surrounding_dts, densities)

    def get_version_number(self, dt):
        for version_info in self.METADATA_DICT:
            for version, time_range in version_info.items():
                if time_range['start_datetime'] <= dt <= time_range['end_datetime']:
                    return version

        raise ValueError("No data available for the specified datetime.")

    def get_wrs_archive(self, dt):
        # Determine the appropriate WRS archive time
        if dt.hour < 3 or (dt.hour == 3 and dt.minute == 0):
            archive_dt = dt.replace(hour=18, minute=0, second=0, microsecond=0) - timedelta(days=1)
        elif dt.hour < 9 or (dt.hour == 9 and dt.minute == 0):
            archive_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        elif dt.hour < 15 or (dt.hour == 15 and dt.minute == 0):
            archive_dt = dt.replace(hour=6, minute=0, second=0, microsecond=0)
        elif dt.hour < 21 or (dt.hour == 21 and dt.minute == 0):
            archive_dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
        else:
            archive_dt = dt.replace(hour=18, minute=0, second=0, microsecond=0)

        return archive_dt

    def get_wfs_archive(self, dt):
        # Determine the appropriate WFS archive time
        if dt.hour < 3 or (dt.hour == 3 and dt.minute == 0):
            archive_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        elif dt.hour < 9 or (dt.hour == 9 and dt.minute == 0):
            archive_dt = dt.replace(hour=6, minute=0, second=0, microsecond=0)
        elif dt.hour < 15 or (dt.hour == 15 and dt.minute == 0):
            archive_dt = dt.replace(hour=12, minute=0, second=0, microsecond=0)
        elif dt.hour < 21 or (dt.hour == 21 and dt.minute == 0):
            archive_dt = dt.replace(hour=18, minute=0, second=0, microsecond=0)
        else:
            archive_dt = (dt + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)

        return archive_dt

    def get_surrounding_datetimes(self, dt):
        floor_dt = self.datetime_floor(dt)
        ceil_dt = floor_dt + timedelta(minutes=10)
        return [floor_dt, ceil_dt]

    @staticmethod
    def datetime_floor(dt):
        minute = (dt.minute // 10) * 10
        return dt.replace(minute=minute, second=0, microsecond=0)

    def construct_s3_key(self, dt, forecast_sys, wfs_start_dt=None):
        # Determine the archive time
        if forecast_sys == 'wrs':
            archive_dt = self.get_wrs_archive(dt)
        elif forecast_sys == 'wfs':
            archive_dt = self.get_wfs_archive(dt)
        else:
            raise ValueError("Forecast System Type Invalid!")

        # Use user-provided forecast start date if available (WHY??)
        if forecast_sys == 'wfs' and wfs_start_dt is not None:
            ymd = wfs_start_dt.strftime('%Y%m%d')
        else:
            ymd = archive_dt.strftime('%Y%m%d')

        # Construct and return the S3 key
        version = self.get_version_number(dt)
        model_type = "wam10" if version == "v1.2" else "gsm10"
        return (
            f"{version}/{forecast_sys}.{ymd}/"
            f"{archive_dt.strftime('%H')}/wam_fixed_height.{forecast_sys}.t"
            f"{archive_dt.strftime('%H')}z.{model_type}.{dt.strftime('%Y%m%d_%H%M%S')}.nc"
        )

    def get_files(self, input_dt):
        target_dts = self.get_surrounding_datetimes(input_dt)
        files = []

        for target_dt in target_dts:
            # Construct S3 Key and Fetch Files from Preferred Forecast System
            preferred_sys_key = self.construct_s3_key(target_dt, self.forecast_sys_prefer)
            file = self.cache.get_file(preferred_sys_key)

            # See if Preferred Forecast Fetch was Successful
            if file is not None:
                files.append(file)

            # Consume Available Fallback Data Systems
            else:
                fallback_systems_failed = True
                for fallback_system in self.FORECAST_SYS_FALLBACK:
                    if fallback_system == self.forecast_sys_prefer:
                        continue

                    else:
                        fallback_sys_key = self.construct_s3_key(target_dt, fallback_system)
                        file = self.cache.get_file(fallback_sys_key)
                        if file is not None:
                            files.append(file)
                            fallback_systems_failed = False
                            break

                if fallback_systems_failed:
                    raise FileNotFoundError(f"Fetch for '{target_dt}' Failed: All Preffered and Fallback Systems Do "
                                            f"Not Exist")

        # Return List of Cached File Paths
        return files

    def get_datasets(self, input_dt):
        # Return NetCDF Parser Instances for each file in date range
        return [Dataset(f) for f in self.get_files(input_dt)]
