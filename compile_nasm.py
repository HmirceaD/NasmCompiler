#!/usr/bin/env python

import sys
import subprocess

def compile_asm():
    asm_prog = sys.argv[1]
    subprocess.call(["nasm", "-f", "elf64", asm_prog])

    compiled_asm = asm_prog[:-3]
    compiled_asm += "o"

    subprocess.call(["ld", "-s", "-o", compiled_asm[:-2] , compiled_asm])

compile_asm()


