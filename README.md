# FileHasher
[![LICENSE](https://img.shields.io/badge/LICENSE-GPL--3.0-green)](https://github.com/DarjaGFX/FileHasher/blob/master/LICENSE)


## How to Run:
Ex. hash all jpg files in current directory: `python filehasher.py *.jpg`

switches:
>-p or -P    to get prefix name. (ex. hash `mypic.jpg` directory and output would be `hashed_mypic.jpg` instead of       overwriting on existing file. `python filehasher.py -p hashed_ mypic.jpg`)


after running script you have to input a SALT.

#### <span style="color:red">To recover your File you have to run script again with same SALT. So if you dont have a Good memory, save your salt in a safe place!</span>

> You Can do this unlimited times with different SALTs. but remember your SALTs sequence cause you need to use them reversely to recover your files.
