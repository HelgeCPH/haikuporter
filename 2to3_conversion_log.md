# Steps taken

  * Automatic conversion of sources:
    
    ```bash
    $ 2to3 -n -w -W -f all -f idioms -j4 -v . > 2to3_conversion.log 2>&1
    ```
  * Autopep8 the sources, i.e., automatted version of the PEP8 styleguide, see https://www.python.org/dev/peps/pep-0008/
  
    ```bash
    $ autopep8 --in-place --aggressive --aggressive haikuporter
    $ autopep8 --in-place --aggressive --aggressive HaikuPorter/*.py
    ```
    

## Manual conversions

### `string_escape` from `encodings`

```
Traceback (most recent call last):
  File "/boot/home/haikuporter_port/haikuporter", line 16, in <module>
    from HaikuPorter.Main import Main
  File "/boot/home/haikuporter_port/HaikuPorter/Main.py", line 23, in <module>
    from .Repository import Repository
  File "/boot/home/haikuporter_port/HaikuPorter/Repository.py", line 11, in <module>
    from .Port import Port
  File "/boot/home/haikuporter_port/HaikuPorter/Port.py", line 64, in <module>
    from encodings import string_escape
ImportError: cannot import name 'string_escape' from 'encodings' (/packages/python3-3.7.3-2/.self/lib/python3.7/encodings/__init__.py)
```






# How to check if the conversion is working?

For the conversion run for example:

$ cd ../haikuports/dev-lang/python/
$ python3 ~/haikuporter_port/haikuporter python3
$ python3 ~/haikuporter_port/haikuporter python3-3.7.3 
