# Sync _Drive Project
# ------------------------------------------------------------------------------------------------
# This is the Main Launch file for _drive
# The Idea of this project is to create a Highly available open source version of drop box
# This will leverage Amazon Web Services and is maent to solitify the knowledge required for
# Amazon Solutions Architect Certification - Associate
# ------------------------------------------------------------------------------------------------

# Imports For Main Function ----------------------------------------------------------------------
from cloud_launcher.launch import Launcher
from exit_clean_up.exit import Exit
# ------------------------------------------------------------------------------------------------

# Main File Project Flow -------------------------------------------------------------------------
# 1. Kick off Cloud Formation Script in Sub Thread
# 2. Wait for completion of Stack Creation and then provide details of Stack
# 3. on Exit of Main Delete Stavk from AWS to Solidify Stack only exists durring life of process
# ------------------------------------------------------------------------------------------------

launcher = Launcher()

# life of function -------------------------------------------------------------------------------
# As we only want this function to run only durring the life of the function and have the aws resources removed after the process is killed. This cxode will perform action. Probably should be looked at before production
if __name__ == "__main__":
    try:
        while True:
            pass
    except KeyboardInterrupt:
        clean_up_stack = Exit()
# ------------------------------------------------------------------------------------------------
