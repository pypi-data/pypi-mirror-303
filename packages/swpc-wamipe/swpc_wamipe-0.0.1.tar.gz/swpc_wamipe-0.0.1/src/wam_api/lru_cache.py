from collections import OrderedDict
import requests
import os
import json

class LRU_Cache():
    # Define Required Constants
    FILE_SIZE = 3  # size of each file in mb
    CACHE_PATH = 'wamapi_filecache'  # Move this to /tmp/wam_api/filecache, maybe?
    CACHE_METADATA = f'{CACHE_PATH}/metadata.json'

    def __init__(self, max_size=100, s3bucket='noaa-nws-wam-ipe-pds'):
        self.max_size = max_size  # allow the user to decide the max cache size, 100mb by default
        self.s3bucket = s3bucket

        if os.path.exists(self.CACHE_METADATA):
            with open(self.CACHE_METADATA, 'r') as metadata_file:
                self.file_map = json.load(metadata_file, object_pairs_hook=OrderedDict)
                self.current_size = len(self.file_map.keys())
        else:
            os.makedirs(self.CACHE_PATH, exist_ok=True)  # makes a directory if it doesn't already exist
            self.file_map = OrderedDict()   # maps file paths to their NetCDF dataset. ordered dict tracks the access order of the files 
            self.current_size = 0
    
    def get_file(self, file_path):
        if file_path not in self.file_map.keys():
            print(f'file NOT in cache... retrieving file from s3')
            if self.put_file(file_path) is True:
                self.file_map.move_to_end(file_path)    # mark file as recently used
            else:
                self.update_metadata()
                return None
        else:
            print(f'file IN cache')
            self.file_map.move_to_end(file_path)    # mark file as recently used

        self.update_metadata()
        return self.file_map[file_path]
    
    def put_file(self, file_path):  # downloads the NetCDF file from the s3 bucket, inserting the data into the file_map
        if self.current_size + self.FILE_SIZE > self.max_size:
            self.remove_lru_file()

        url = f"https://{self.s3bucket}.s3.amazonaws.com/{file_path}"
        response = requests.get(url)

        if response.status_code == 200:
            # create a valid output file path based on the input file path given
            output_path = os.path.join(self.CACHE_PATH, f'{file_path.replace(".", "_").replace("/", "_")}.nc')
            
            with open(output_path, 'wb') as file:  # saves the file into the designated local directory
                file.write(response.content)
            
            self.file_map[file_path] = output_path

            self.current_size += self.FILE_SIZE  # update cache size
            print(f'file added to cache with path {file_path}')
            return True
        else:
            print(f"failed to retrieve file with path {file_path} from s3")
            return False
    
    def remove_lru_file(self):
        # remove the least recently used file from the local directory
        _, output_lru = self.file_map.popitem(last=False) # removes the least recently used file from the cache
        if os.path.exists(output_lru):
            os.remove(output_lru) # removes least recently used file from local directory
        else:
            print('ERROR - attempted to remove NONEXISTENT file')

        self.current_size -= self.FILE_SIZE
        print('removed lru file')

    def print_cache(self):
        print(f'maxsize = {self.max_size}, currentsize = {self.current_size}')
        print(f'cache contains [{len(self.file_map.keys())}] total entries')
        for key, value in self.file_map.items():
            print(f'\t- file with path {key}')

    def update_metadata(self):    # call this function upon exiting the program 
        with open(self.CACHE_METADATA, 'w') as metadata_file:
            json.dump(self.file_map, metadata_file, indent=4)
