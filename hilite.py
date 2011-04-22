#!/usr/bin/python

from __future__ import print_function
import fileinput
from termcolor import colored
from os.path import isdir, isfile

execolor = 'red'
urlcolor = 'blue'
filecolor = 'green'
dircolor = 'cyan'

def looksLikeAFile(f):
    
    if  ('/' in f or f.startswith('.')) \
        and '.' in f[1:]                \
        and not f.endswith('.'):
        return True
    return False

def color(f,testPath=False):
    color = None
    attrs = []
    
    f=f.strip(' \r\n\t\'\"`')
    
    if testPath and which(f):
        color = execolor
    elif 'http' in f:
        color = urlcolor
        attrs += ['underline']
    elif isfile(f) or looksLikeAFile(f):
        color = filecolor
    elif isdir(f):
        color = dircolor
    else:
        attrs += ['dark']
    
    return colored(f,color,attrs=attrs)

# -- Borrowed from http://goo.gl/XVeDx
def which(program):
    import os
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


if __name__ == '__main__':

    # -- Read in on stdin
    for line in fileinput.input():
        tokens = line.split()
    
        if len(tokens):
            exe = which(tokens[0])
            if exe:
                tokens[0] = color(tokens[0],True)
    
            tokens[1:] = [ color(f) for f in tokens[1:] ]
    
            for token in tokens: print(token,end=' ')
            print()
