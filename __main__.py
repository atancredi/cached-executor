import sys
from importlib import reload

# module to reload keeping the variable in cache
import ext_module

data = None
if __name__ == "__main__":
    while True:
        
        if not data:
            data = ext_module.very_intensive_data_collction()
        try:
            ext_module.computations_that_uses_data(data)
        except Exception as ex:
            print(ex)
            
        print("Press enter to re-run the script, CTRL-C to exit")
        sys.stdin.readline()
        reload(ext_module)