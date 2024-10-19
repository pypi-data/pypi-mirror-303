import sys
from commands import hexagonal_template_genrator

def cli():
    argv = sys.argv
    if len(argv) < 2:
        return None
    cmd = hexagonal_template_genrator(argv=argv)
    if cmd is None:
        return None
    cmd.generate()
    
if __name__=="__main__":
    cli()