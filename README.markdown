This is a [Blogofile](http://blogofile.com) plugin template.

You can use this as a base for creating your own plugins.

FYI: The stable Blogofile doesn't yet support plugins, you need the
[plugins
branch](https://github.com/enigmacurry/blogofile/tree/plugins) for
now.

To use this plugin:

* Install the plugin with pip:

        pip install -e git://github.com/EnigmaCurry/blogofile_plugin_example.git#egg=blogofile_plugin_example

* Check that blogofile recognizes the plugin:

        blogofile plugin list

        example (0.1) - A minimal photo gallery as an example plugin - Ryan McGuire

        
* Configure your site's `_config.py`:

        plugins.example.enabled = True

  This will create a demo gallery at `/photos`. You can change this with:

        plugins.example.gallery.path = "/gallery"

  You can supply your own photos with:

        plugins.example.galelry.src = "/path/to/my/photos"

  Your photos will be copied to the gallery path you defined.


  Also notice the command line entry points that got installed (they don't really *do* anything, just showing you what's possible):

       ryan@Sovereign:~$ bfdev help example
       example - Plugin: A minimal photo gallery as an example plugin
       usage: -c example [-h] [-s DIR] [--version] [-v] [-vv]
       {command1,command2       } ...
       
       positional arguments:
         {command1,command2}
           command1            Example Command 1
           command2            Example Command 2
       
  You can add your own in commands.py.
