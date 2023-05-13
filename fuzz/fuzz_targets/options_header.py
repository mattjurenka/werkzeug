#!/usr/bin/env python3

import atheris
import sys
import os

with atheris.instrument_imports():
    from werkzeug.http import parse_options_header

def TestOneInput(input):
    fdp = atheris.FuzzedDataProvider(input)
    parse_options_header(fdp.ConsumeUnicodeNoSurrogates(fdp.ConsumeIntInRange(1, 4096)))

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()
