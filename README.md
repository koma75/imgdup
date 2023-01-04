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


### Subcmd 1

Subcmd description

~~~shell
> imgdup hashfunc --hash-size SIZE -v PATH
~~~

* -o, --option1
    * description
* -a, --argopt1 ARG
    * description
* -v, --verbose
    * verbosity

Known Issues
------------------------------------------------------------------------

Need to be implemented.

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
