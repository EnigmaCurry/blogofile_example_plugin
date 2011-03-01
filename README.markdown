This is a [Blogofile](http://blogofile.com) plugin template.

You can use this as a base for creating your own plugins.

FYI: The stable Blogofile doesn't yet support plugins, you need the
[plugins
branch](https://github.com/enigmacurry/blogofile/tree/plugins) for
now.

To use this plugin:

* Install the plugin with pip:

    pip install -e git://github.com/EnigmaCurry/blogofile_plugin_example.git#egg=blogofile_plugin_example

* Configure your site's _config.py:

    plugins.example.enabled = True

  This will create a demo gallery at `/photos`. You can change this with:

    plugins.example.gallery.path = "/gallery"

  You can supply your own photos with:

    plugins.example.galelry.src = "/path/to/my/photos"

  Your photos will be copied to the gallery path you defined.


