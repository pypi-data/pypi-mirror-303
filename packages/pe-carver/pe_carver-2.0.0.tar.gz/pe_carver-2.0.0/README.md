## pe-carver

Carves EXEs from given data files, using intelligent carving based upon PE headers.

Updated for Python 3 by digitalsleuth

## Usage

```
usage: pe-carver [-h] -f <input-file> -o <output-folder> [-l <logfile-name>] [--min #] [--max #] [--verbose] [-v]

pe-carver v2.0

optional arguments:
  -h, --help            show this help message and exit
  -f <input-file>, --file <input-file>
                        File to carve, full path
  -o <output-folder>, --output <output-folder>
                        Output folder, full path
  -l <logfile-name>, --log <logfile-name>
                        Log file name, full path
  --min #               Minimum EXE size in bytes, default 10000
  --max #               Maximum EXE size in bytes, default 2000000
  --verbose             Verbose - print status to stdout
  -v                    show program's version number and exit
  ```
