import os

from blogofile.cache import bf

import blogofile_plugin_example as plugin

meta = {
    "name": "Example Controller",
    "author": "Ryan McGuire",
    "description": "Creates a dumb little photo gallery",
    "version": "0.1",
    }

def init():
    #Any setup you need to do before running goes here.
    pass

def run():
    #Run the controller
    import photos
    photos.copy_photos()
    photo_files = photos.get_photo_names()
    photos.write_pages(photo_files)
    photos.write_index(photo_files)
    
