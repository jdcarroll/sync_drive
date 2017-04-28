# Sync _Drive Project
# ------------------------------------------------------------------------------------------------
# This is the Main Launch file for _drive
# The Idea of this project is to create a Highly available open source version of drop box
# This will leverage Amazon Web Services and is maent to solitify the knowledge required for
# Amazon Solutions Architect Certification - Associate
# ------------------------------------------------------------------------------------------------

# Imports For Main Function ----------------------------------------------------------------------
from cloud_launcher.launch import Launcher
# ------------------------------------------------------------------------------------------------

# Main File Project Flow -------------------------------------------------------------------------
# 1. Kick off Cloud Formation Script in Sub Thread
# 2. Wait for completion of Stack Creation and then provide details of Stack
# 3. on Exit of Main Delete Stavk from AWS to Solidify Stack only exists durring life of process
# ------------------------------------------------------------------------------------------------

launcher = Launcher()
