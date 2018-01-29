#!/usr/bin/env python
from __future__ import absolute_import
from __future__ import print_function
import sys

__all__ = [
    # object
    'psp',
    # no newlines
    'nrm', 'udl', 'whtb', 'wht', 'aqu', 'pur', 'blu', 'ylw', 'grn', 'red',
    # with newlines
    'nrmln', 'udlln', 'whtbln', 'whtln', 'aquln', 'purln', 'bluln', 'ylwln', 'grnln', 'redln'
]

class PSP(object):
    bldwht=1; nrm=0;
    red=31; grn=32; ylw=33; blu=34; pur=35; aqu=36; wht=37; udl=4;
    _sb = None # before
    _sa = None # after

    @property
    def sb(self):
        if self._sb is not None: return self._sb
        else: self._sb = '\033[01;%dm'; self._sa = '\033[0;0m';
        return self._sb

    @property
    def sa(self):
        if self._sa is not None: return self._sa
        else: self._sa = '\033[0m';
        return self._sa

    @property
    def write(self): return sys.stdout.write

    @property
    def flush(self): return sys.stdout.flush

    @property
    def write2(self): return sys.__stderr__.write

    @property
    def flush2(self): return sys.__stderr__.flush

    def __init__(self, base=0, mode=0, debug=False):
        self.base = base
        self.mode = mode
        self.debug = debug
        if (self.debug):
            self.PutsCln(PSP.bldwht, '\n\t>>>> psp init <<<<<\n')

    def PutsCln(self, cl, data):
        cl += self.base
        try:
            self.write2(self.sb % cl); self.write2(data); self.write2(self.sa); self.write2('\n');
            self.flush2();
        except Exception as e: pass

    def PutsC(self, cl, data):
        cl += self.base
        try:
            self.write2(self.sb % cl); self.write2(data); self.write2(self.sa);
            self.flush2();
        except Exception as e: pass


psp = PSP(base=0, mode=0, debug=True)

nrm = lambda m: psp.PutsC(PSP.nrm, m);
red = lambda m: psp.PutsC(PSP.red, m);
grn = lambda m: psp.PutsC(PSP.grn, m);
ylw = lambda m: psp.PutsC(PSP.ylw, m);
blu = lambda m: psp.PutsC(PSP.blu, m);
pur = lambda m: psp.PutsC(PSP.pur, m);
aqu = lambda m: psp.PutsC(PSP.aqu, m);
udl = lambda m: psp.PutsC(PSP.udl, m);
wht = lambda m: psp.PutsC(PSP.wht, m);
whtb = lambda m: psp.PutsC(PSP.bldwht, m);

nrmln = lambda m: psp.PutsCln(PSP.nrm, m);
redln = lambda m: psp.PutsCln(PSP.red, m);
grnln = lambda m: psp.PutsCln(PSP.grn, m);
ylwln = lambda m: psp.PutsCln(PSP.ylw, m);
bluln = lambda m: psp.PutsCln(PSP.blu, m);
purln = lambda m: psp.PutsCln(PSP.pur, m);
aquln = lambda m: psp.PutsCln(PSP.aqu, m);
udlln = lambda m: psp.PutsCln(PSP.udl, m);
whtln = lambda m: psp.PutsCln(PSP.wht, m);
whtbln = lambda m: psp.PutsCln(PSP.bldwht, m);


__version__ = '0.0.6'
