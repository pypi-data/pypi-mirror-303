#!/usr/bin/env python3

# PE File Carver
# by Brian Baskin (@bbaskin)
# Updated by Corey Forman - github.com/digitalsleuth
#
# This program searches any large logical file for executable files, which are then
# carved out and stored onto the hard drive.
# It searches for the text 'This program' which is found in nearly all executables.
# It then attempts to read the EXE header, find the file size, and extract that number
# of bytes out to save.
#
# Version 1.0 - 18 Dec 12
#   Code I threw together because Foremost/Scalpel gave me so many false positives
# Version 1.1 - 27 Jun 16
#   OMG, 3.5 years later. Now it's a "legit" application that runs somewhat better
# Version 2.0 - 18 Oct 2024
#   Updated for Python 3, added the ability to choose file size limits, verbosity

import argparse
import bitstring  # Used to parse data. Download from: https://github.com/scott-griffiths/bitstring
import os
import pefile  # Used to parse PE header. Download from: https://github.com/erocarrera/pefile
import sys
from datetime import datetime

__version__ = "2.0"
__author__ = "Corey Forman - github.com/digitalsleuth"
__description__ = "Basic PE File carver for Python 3"
__tool__ = "pe-carver"

g_log = ""


def file_exists(fname):
    return os.path.exists(fname) and os.access(fname, os.R_OK)


def log(string, verbose=False):
    # This just tees output to a file and stdout
    if g_log:
        try:
            open(g_log, "a").write(string + "\n")
        except:
            pass
    if verbose:
        print(string)


def getSize_FromPE(PE_data):
    # Performs basic lookup to find the end of an EXE, based upon the
    # size of PE sections. Same algorithm is used to find EXE overlay
    # FYI: This will miss any overlay data, such as RAR SFX archives, etc
    try:
        pe = pefile.PE(data=PE_data)
        return pe.sections[-1].PointerToRawData + pe.sections[-1].SizeOfRawData
    except:
        return 0


def getArgs():
    global g_log

    parser = argparse.ArgumentParser(
        prog=__tool__,
        description=f"%(prog)s v" f"{str(__version__)}",
        formatter_class=argparse.HelpFormatter,
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="<input-file>",
        help="File to carve, full path",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="<output-folder>",
        help="Output folder, full path",
        required=True,
    )
    parser.add_argument(
        "-l",
        "--log",
        metavar="<logfile-name>",
        help="Log file name, full path",
        required=False,
    )
    parser.add_argument(
        "--min",
        metavar="#",
        help="Minimum EXE size in bytes, default 10000",
        required=False,
        default=10000,
        type=int,
    )
    parser.add_argument(
        "--max",
        metavar="#",
        help="Maximum EXE size in bytes, default 2000000",
        required=False,
        default=2000000,
        type=int,
    )
    parser.add_argument(
        "--verbose",
        help="Verbose - print status to stdout",
        required=False,
        action="store_true",
    )
    parser.add_argument("-v", action="version", version=parser.description)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    if args.file and not file_exists(args.file):
        print(f"[!] Source file not found: {args.file}")
        sys.exit(1)
    if args.log:
        g_log = args.log

    return args


def main():
    args = getArgs()
    if args.output:
        if not file_exists(args.output):
            print(f"[!] Output folder does not exist: {args.output}")
            sys.exit(1)
        output_folder = args.output

    start_time = datetime.now().strftime("[%d-%b-%Y %H:%M:%S]")
    log(f"Scan of {args.file} started at {start_time}", args.verbose)
    entries = []
    fstream = bitstring.ConstBitStream(filename=args.file)
    results = fstream.findall("0x546869732070726F6772616D")  # 'This program'
    log("Gathering search hits...", args.verbose)
    for i in results:
        # The result offsets are stored as binary values, so you have to divide by 8
        # -78 is the negative offset to the beginning of 'MZ' from 'This program'
        hit = int(i) / 8 - 78
        entries.append(hit)

    log("Parsing for EXEs...", args.verbose)
    ifile = open(args.file, "rb")
    for hit in entries:
        hit = int(hit)
        ifile.seek(hit)
        PE_header = ifile.read(1024)
        pesize = getSize_FromPE(PE_header)
        # These sizes are arbitrary. Had numerous junk PE headers (>30GB), so did base limiting
        if (args.min < pesize < args.max) and PE_header[0:2] == b"MZ":
            log(f"Found PE header at: 0x{hit:x} - ({pesize} bytes)", args.verbose)
            ifile.seek(hit)
            PE_data = ifile.read(pesize)
            outfile = os.path.join(
                output_folder, f"{os.path.basename(args.file)}_{hit}.livebin"
            )
            open(outfile, "wb").write(PE_data)
        else:
            log(f"Ignored PE header at: 0x{hit:x} - ({pesize} bytes)", args.verbose)

    end_time = datetime.now().strftime("[%d-%b-%Y %H:%M:%S]")
    log(f"Scan of {args.file} ended at {end_time}", args.verbose)


if __name__ == "__main__":
    main()
