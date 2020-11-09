import numpy as np
import xarray as xr

# first  - download netCDF files from cds.climate.copernicus.eu
# second - read netCDF file into the xarray
# third  - extract the necessary data from the xarray using this module

def get_longitude(xarray_dset, name_coord):
    # getting longitude values from xarray
    longitude = np.asarray(xarray_dset[name_coord])
    return longitude


def get_latitude(xarray_dset, name_coord):
    # getting latitude values from xarray
    latitude = np.asarray(xarray_dset[name_coord])
    return latitude


def get_times(xarray_dset, name_coord):
    # getting time values from xarray
    times = np.asarray(xarray_dset[name_coord])
    return times


def get_data_cube(xarray_dset, name_data_var):
    # getting data values from xarray
    data_cube = xarray_dset[name_data_var]
    return data_cube


def form_times_file(start_year, end_year, months, times, file_name):
	# formation of a times list of the form "yyyy.mm.dd hh:00:00"
    n_times = 0
    my_file = open(file_name, "w")
    for year in range(start_year, end_year + 1):
        str_year = str(year)
    
        for month in months:
            if month < 10:
                srt_month = '0' + str(month)
            else:
                srt_month = str(month)

            if month in np.asarray([1, 3, 5, 7, 8, 10, 12]):
                days = range(1, 32) #[1,2,...,30,31]
            elif month in np.asarray([4, 6, 9, 11]):
                days = range(1, 31) #[1,2,...,29,30]
            elif (month == 2) and (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)): # високосный год
                days = range(1, 30) #[1,2,...,28,29]
            else:
                days = range(1, 29) #[1,2,...,27,28]
            
            for day in days:
                if day < 10:
                    str_day = '0' + str(day)
                else:
                    str_day = str(day)

                for time in times:
                    my_file.write(str_year + '.' + srt_month + '.' + str_day + ' ' + time + '\n')
                    n_times += 1
    my_file.close()
    return n_times
 
 
def form_resulting_data_cube_from_parts_by_time(*parts):
    # concatenate of xarray by time
	# (since a large data set has to be uploaded as multiple netCDF files)
	# resulting_cube - 3D np.ndarray (time, lat, lon)
    resulting_cube = parts[0]
    for k in range(1, len(parts)):
        resulting_cube = np.concatenate((resulting_cube, parts[k]), axis = 0)
    return resulting_cube