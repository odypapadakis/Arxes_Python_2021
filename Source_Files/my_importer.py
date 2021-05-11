def importer (module_name):
    import subprocess
    import sys

    try:
        print("Importing 1st time ")
        __import__( module_name )
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
    finally:
        print("Importing 2nd time ")
        __import__( module_name )

    # print("aa-->",module_name)
