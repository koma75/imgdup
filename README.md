imgdup
========================================================================

Image Duplicate finder using Image Hash.

This is a tool to find similar images in a set of images using imagehash
library.  If two or more similar images are found (same hash value), the
images are moved to a subfolder for each hash value.

Installation
------------------------------------------------------------------------

~~~shell
> pip install imgdup
~~~

Usage
------------------------------------------------------------------------

All subcommands will find duplicate images using the specified image hash
function.  Subcommands are used to specify the hash commands as follows:

* ahash  
    * Use Average hash to find duplicates in PATH
* color  
    * Use HSV color hash to find duplicates in PATH
* crop   
    * Use Crop resistant hash to find similar images in PATH
* db4       
    * Use Daubechies wavelet hash to find duplicates in PATH
* dhash  
    * Use Difference hash to find duplicates in PATH
* haar   
    * Use Haar wavelet hash to find duplicates in PATH
* phash  
    * Use Perceptual hash to find duplicates in PATH

~~~shell
> imgdup HASHFUNC --hash-size SIZE -v PATH
~~~

* HASHFUNC
    * hash function to use in sort images with.  See above for list of functions.
* PATH
    * PATH with the images to check for (will not be recursed)
* -s, --hash-size SIZE
    * specify the hash size to use. (Default: 8)
* -v, --verbose
    * specify verbosity.  specify twice to get debug message

If two or more images with the same hash is found, they are put into the 
same folder with tha hash value as the folder name.

Known Issues
------------------------------------------------------------------------

Not parallelized and is very slow on large data-sets

Development
------------------------------------------------------------------------

### Building an Executable

Install pyinstaller and package the project.
May want to use venv when executing the pyinstaller.

First, enter venv and install the local package and pyinstaller

~~~shell
>. .venv/Scripts/activate
(.venv) >pip install .
Processing /path/to/proj/imgdup
~snip~
Installing collected packages: imgdup
    Running setup.py install for imgdup ... done
Successfully installed imgdup-0.1.0

(.venv) >pip install pyinstaller
~snip~
Successfully installed pyinstaller-3.6
~~~

Use pyinstaller to build the exe file.

~~~shell
(.venv) >pyinstaller imgdup\cli.py --onefile --name imgdup
~snip~
13691 INFO: Building EXE from EXE-00.toc completed successfully.
~~~

Executable should be ready in dist/imgdup.exe

### Versioning

The project will follow the [semver2.0](http://semver.org/) versioning scheme.  
With initial development phase starting at 0.1.0 and increasing
minor/patch versions until we deploy the tool to production
(and reach 1.0.0).
The interface relevant to versioning is whatever defined in this
document's "Usage" section (includes all (sub)commands, and their cli arguments.

Version History
------------------------------------------------------------------------

Date        | Version   | Changes
:--         | --:       | :--
2023.01.03  | 0.1.0     | First Release
