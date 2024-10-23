#!/usr/bin/env python3

from fire import Fire
from cmd_ai import config # , key_enter, topbar, unitname
import os
from console import fg,bg,fx
import json
import sys

def get_filename_my_context():
    ff = config.CONFIG['current_messages']  # with path but no ext
    nn = config.CONFIG['current_name']
    res = os.path.expanduser( f"{ff}_{nn}.txt" )
    #print("D ..................", res)
    return res

def get_filename_my_last_resp():
    ff = config.CONFIG['last_response']  # with path but no ext
    nn = config.CONFIG['current_name']
    res = os.path.expanduser( f"{ff}_{nn}.txt" )
    #print("D ..................", res)
    return res

def get_filename_my_sourcecode():
    """
    volatile ext
    """
    ff = config.CONFIG['sourcecode']  # with path but no ext
    nn = config.CONFIG['current_name']
    ex = config.CONFIG['sourcecodeext']
    OUTFILE = f"{ff}_{nn}.{ex}"
    res = os.path.expanduser( OUTFILE )
    #print("D ..................", res)
    return res

def get_filename_my_pyscript():
    ff = config.CONFIG['pyscript']  # with path but no ext
    nn = config.CONFIG['current_name']
    ex = "py"
    OUTFILE = f"{ff}_{nn}.{ex}"
    res = os.path.expanduser( OUTFILE )
    #print("D ..................", res)
    return res

def get_filename_my_shscript():
    ff = config.CONFIG['shscript']  # with path but no ext
    nn = config.CONFIG['current_name']
    ex = "sh"
    OUTFILE = f"{ff}_{nn}.{ex}"
    res = os.path.expanduser( OUTFILE )
    #print("D ..................", res)
    return res


def get_filename_my_png():
    ff = "/tmp/cmd_ai_image"  # with path but no ext
    nn = config.CONFIG['current_name']
    ex = "png"
    OUTFILE = f"{ff}_{nn}.{ex}"
    res = os.path.expanduser( OUTFILE )
    #print("D ..................", res)
    return res




def load_all_config_messages( silent = False):
    """
    retuns number of bytes
    """
    curmessages = get_filename_my_context()
    #mmm = config.CONFIG["current_messages"]
    print(f"i... {fg.cyan} .. I try to catch up with  {curmessages} ... {fg.default}", file=sys.stderr)
    CONT = []
    totsize = 0
    totlines = 0
    if os.path.exists(curmessages):
        with open(curmessages) as f:
            CONT = json.loads( f.read() )
        #print( fx.italic,CONT, fx.default)
        #print( len(CONT) , " - items is conversation" )
        for i in CONT:
            #if i['role'] == 'system': continue
            PROM = "- "
            if i['role'] == 'system': PROM = ":# "+fg.lightred
            if i['role'] == 'user': PROM = ":> "+fx.bold+fg.lightslategray
            if i['role'] == 'assistant': PROM = "<: "+fx.italic+fg.pink
            totlines+=len(i['content'].split("\n"))
            totsize+=len( i['content'] )

            if not config.silent and not silent:
                print(  PROM,i['content'] , fx.default, fg.default, file=sys.stderr)
        print("  ~~~ ~~~ ~~~ ~~~ ~~~ ~~~ ~~~  ")
    else:
        print(f"X... conversation {curmessages} doesnot exist... :(", file=sys.stderr)
    # ========== THIS IS CRUTIAL =====
    config.messages = CONT
    return totsize,totlines


def save_all_config_messages():
    curmessages = get_filename_my_context()
    # this I want to be json
    with open( os.path.expanduser( curmessages  ), "w" )  as f:
        try:
            f.write( json.dumps( config.messages, indent=2, separators=(',', ': ')) )
        except:
            print(fg.red,f"X... I cannot write {len(config.messages)} messages to json {curmessages}. Is it web content? ")
            #f.write( str(config.messages) )
    return


def save_last_response( resiw ):
    ff = get_filename_my_last_resp()
    with open( os.path.expanduser( ff ),"w"  ) as f:
        f.write( resiw )
    return

def save_source_code( resco ):
    """
    not pyscript nor shscript
    """
    OUTFILE = get_filename_my_sourcecode() #f"{config.CONFIG['sourcecode']}.{config.CONFIG['sourcecodeext']}"
    print( " ... written to ... ",OUTFILE )
    with open( OUTFILE , "w" ) as f:
        #f.write("#!/bin/bash\n\n")
        f.write(resco)
    return




def main():
    print()

if __name__=="__main__":
    Fire(main)
