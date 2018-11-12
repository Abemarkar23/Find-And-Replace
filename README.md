# Find-And-Replace

simple python command line tool to find and replace the first occurence of a string in a given file. This tool should work for linux and MacOS. It most likely will work for Windows, but you will have to make your own installation script because the current installation script uses ```/usr/bin```. 

#### Requirements 

  - Python
  - Optional:
    - Argparse
    - Pathlib

Note: Optional libraries will be installed during installation

#### Installation

to install simply run: 
1. ```git clone https://github.com/Abemarkar23/Find-And-Replace```
1. ```cd Find-And-Replace ```
1. ```sudo python setup.py``` 
1. Then you may keep or delete the repository

#### Usage
```
  far <filename> <text to be replaced> <new text>
  far hello.txt  Lorem                 Ipsum 
```
Note: multiple spaces are not required, they are just in the example for demonstration


##### MIT License

Copyright (c) 2018 Arjun Bemarkar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
