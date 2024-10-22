############################################################################
#               Create database

# Created by:   Huy Pham
#               University of California, Berkeley

# Date created: January 2024

# Description:  Main workfile for TFP-MF database, reworked in new framework

# Open issues:  

############################################################################

import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, '../')

from db import Database

main_obj = Database(400, n_buffer=8, seed=130, 
                    struct_sys_list=['MF'], isol_wts=[1, 0])

main_obj.design_bearings(filter_designs=True)
main_obj.design_structure(filter_designs=True)