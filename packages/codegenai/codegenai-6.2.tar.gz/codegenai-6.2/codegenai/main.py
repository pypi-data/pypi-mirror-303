from codegenai.aids import *
from codegenai.cn import *
from codegenai.special import *
import os
import shutil
import subprocess


available = {'-1  ' : "AIDS CN (Folder)",
             '\nAIDS' : "",
             '0   ' : "All",
             '1   ' : "Breadth First Search",
             '2   ' : "Depth First Search",
             '3   ' : "Uniform Cost Search",
             '4   ' : "Depth Limited Search", 
             '5   ' : "Iterative Deepening Search(IDDFS)", 
             '6   ' : "A*", 
             '7   ' : "Iterative Deepening A*", 
             '8   ' : "Simplified Memory Bounded A*",
             '9   ' : "Genetic Algorithm", 
             '10  ' : "Simulated Annealing",
             '11  ' : "Solving Sudoku(Simulated Annealing)",
             '12  ' : "Alpha-Beta Pruning",
             '13  ' : "Map Coloring(Constraint Satisfaction Problem)",
             '14  ' : "House Allocation(Constraint Satisfaction Problem)",
             '15  ' : "Random Sampling",
             '16  ' : "Z Test",
             '17  ' : "T Test",
             '18  ' : "ANOVA",
             '19  ' : "Linear Regression",
             '20  ' : "Logistic Regression",
             '\nCN' : "",
             '21  ' : "Chat Application JAVA",
             '22  ' : "File Transfer JAVA",
             '23  ' : "RMI(Remote Method Invocation) JAVA",
             '24  ' : "wired.tcl     (Wired Network)",
             '25  ' : "wired.awk     (Wired Network)",
             '26  ' : "wireless.tcl  (Wireless Network)",
             '27  ' : "Wireless.awk  (Wireless Network)",
             '28  ' : "tahoe.tcl     (TCP Congestion Control)",
             '29  ' : "reno.tcl      (TCP Congestion Control)",
             '30  ' : "sack.tcl      (TCP Congestion Control)",
             '31  ' : "vegas.tcl     (TCP Congestion Control)",
             '32  ' : "flow.tcl      (TCP Flow Control)",
             '33  ' : "analysis.awk  (TCP Flow & Congestion Control)",
             '34  ' : "LS.tcl        (Link State & Distance Vector Routing)",
             '35  ' : "DV.tcl        (Link State & Distance Vector Routing)",
             '36  ' : "analysis.awk  (Link State & Distance Vector Routing)",
             '37  ' : "multicast.tcl (Multicast & Broadcast Routing)",
             '38  ' : "broadcast.tcl (Multicast & Broadcast Routing)",
             '39  ' : "analysis.awk  (Multicast & Broadcast Routing)",
             '40  ' : "DHCP JAVA",
             '41  ' : "LAN.tcl       (Ethernet LAN IEEE 802.3)",
             '42  ' : "analysis.awk  (Ethernet LAN IEEE 802.3)",
             '43  ' : "complexdcf.tcl(Wireless LAN IEEE 802.11)"}

file_path = { 'code'            : 'All.ipynb',
              'bfs'             : 'BFS.ipynb',
              'dfs'             : 'DFS.ipynb',
              'ucs'             : 'UCS.ipynb',
              'dls'             : 'DLS.ipynb',
              'ids'             : 'IDS.ipynb',
              'astar'           : 'Astar.ipynb',
              'idastar'         : 'IDAstar.ipynb',
              'smastar'         : 'SMAstar.ipynb',
              'genetic'         : 'Genetic.ipynb',
              'sa'              : 'Simulated Annealing.ipynb',
              'sudoku'          : 'Sudoku.ipynb',
              'alphabeta'       : 'AlphaBetaPruning.ipynb',
              'csp_map'         : 'CSP Map Coloring.ipynb',
              'csp_house'       : 'CSP House Allocation.ipynb',
              'random_sampling' : 'Random Sampling.ipynb',
              'z_test'          : 'Z Test.ipynb',
              't_test'          : 'T Test.ipynb',
              'bmi_data'        : 'height_weight_bmi.csv',
              'anova'           : 'ANOVA Test.ipynb',
              'sample_data'     : 'sample_data.csv',
              'linear'          : 'Linear Regression.ipynb',
              'logistic'        : 'Logistic Regression.ipynb',
              'house_scores'    : 'hours_scores_records.csv'}

def display(name = None, open = False):
    try:
        if name is not None:
            name = str(name)
        if   name in ['1']      :   print(bfs);             get_file(['bfs'], open)
        elif name in ['2']      :   print(dfs);             get_file(['dfs'], open)
        elif name in ['3']      :   print(ucs);             get_file(['ucs'], open)
        elif name in ['4']      :   print(dls);             get_file(['dls'], open)
        elif name in ['5']      :   print(ids);             get_file(['ids'], open)
        elif name in ['6']      :   print(astar);           get_file(['astar'], open)
        elif name in ['7']      :   print(idastar);         get_file(['idastar'], open)
        elif name in ['8']      :   print(smastar);         get_file(['smastar'], open)
        elif name in ['9']      :   print(genetic);         get_file(['genetic'], open)
        elif name in ['10']     :   print(sa);              get_file(['sa'], open)
        elif name in ['11']     :   print(sudoku);          get_file(['sudoku'], open)
        elif name in ['12']     :   print(alphabeta);       get_file(['alphabeta'], open)
        elif name in ['13']     :   print(csp_map);         get_file(['csp_map'], open)
        elif name in ['14']     :   print(csp_house);       get_file(['csp_house'], open)
        elif name in ['15']     :   print(random_sampling); get_file(['random_sampling'], open)
        elif name in ['16']     :   print(z_test);          get_file(['z_test', 'bmi_data'], open)
        elif name in ['17']     :   print(t_test);          get_file(['t_test', 'bmi_data'], open)
        elif name in ['18']     :   print(anova);           get_file(['anova', 'sample_data'], open)
        elif name in ['19']     :   print(linear);          get_file(['linear'], open)
        elif name in ['20']     :   print(logistic);        get_file(['logistic', 'house_scores'], open)
        elif name in ['21']     :   print(chat)
        elif name in ['22']     :   print(file_transfer)
        elif name in ['23']     :   print(rmi)
        elif name in ['24']     :   print(wired_tcl)
        elif name in ['25']     :   print(wired_awk)
        elif name in ['26']     :   print(wireless_tcl)
        elif name in ['27']     :   print(wireless_awk)
        elif name in ['28']     :   print(tahoe_tcl)
        elif name in ['29']     :   print(reno_tcl)
        elif name in ['30']     :   print(sack_tcl)
        elif name in ['31']     :   print(vegas_tcl)
        elif name in ['32']     :   print(flow_tcl)
        elif name in ['33']     :   print(tcp_flow_congestion_awk)
        elif name in ['34']     :   print(LS_tcl)
        elif name in ['35']     :   print(DV_tcl)
        elif name in ['36']     :   print(link_state_distance_vector_awk)
        elif name in ['37']     :   print(multicast_tcl)
        elif name in ['38']     :   print(broadcast_tcl)
        elif name in ['39']     :   print(multicast_broadcast_awk)
        elif name in ['40']     :   print(dhcp)
        elif name in ['41']     :   print(LAN_tcl)
        elif name in ['42']     :   print(ethernet_LAN_awk)
        elif name in ['43']     :   print(complexdcf_tcl)
        elif name in ['0']      :   print(code);        get_file(['code'], open)
        elif name in ['-1']     :   get_folder(loc = True)
        else:
            for k, v in available.items():
                sep = " : " if v else ""
                print(k,v,sep = sep)
    except:
        pass

def get_file(files = [], open = False):
    if files[0] == "*":
        files = file_path.keys()
    for file in files:
        src = os.path.realpath(__file__)[:-7]+"\\data\\"+file_path[file]
        src = src.replace("\\\\","\\")
        try:
            dest = os.getcwd()+"\\"+file_path[file]
            shutil.copy(src, dest)
            if open:
                subprocess.Popen(f"jupyter notebook {dest}")
        except:
            try:
                dest = os.path.expanduser('~')+"\\Downloads\\"+file_path[file]
                shutil.copy(src, dest)
            except:
                pass

def get_folder(loc = False, i = 0, j = 0):
    src = os.path.realpath(__file__)[:-7]+"\\data\\AIDS CN"
    src = src.replace("\\\\","\\")
    try:
        dest = os.getcwd()+"\\AIDS CN"+(f" ({i})" if i != 0 else "")
        shutil.copytree(src, dest, symlinks=False,
                        copy_function = shutil.copy2,
                        ignore=shutil.ignore_patterns('.ipynb_checkpoints', '__init__.py', '__pycache__'),
                        ignore_dangling_symlinks=False, 
                        dirs_exist_ok=False)
        if loc:
            print("Path:",dest.replace("\\\\","\\"))
    except FileExistsError:
        get_folder(loc, i + 1, j)
    except:
        try:
            dest = os.path.expanduser('~')+"\\Downloads\\AIDS CN"+(f" ({j})" if j != 0 else "")
            shutil.copytree(src, dest, symlinks=False,
                            copy_function = shutil.copy2,
                            ignore=shutil.ignore_patterns('.ipynb_checkpoints', '__init__.py', '__pycache__'),
                            ignore_dangling_symlinks=False, 
                            dirs_exist_ok=False)
            if loc:
                print("Path:",dest.replace("\\\\","\\"))
        except FileExistsError:
            get_folder(loc, i, j + 1)
        except:
            pass
                    
def ghost(key = None, what = ""):
    if key and isinstance(key,str) and key == pwd:
        available = {'101  or  sudoku   ' : "Solving Sudoku(Loading Bar)"}
        try:
            if isinstance(what,str):
                what =  what.lower()
            if what in ["sudoku", 101]   :   print(sudoku_lb)
            else:
                print("Invalid Value! Refer Below Table")
                for k, v in available.items():
                    print(k,v,sep = " : ")
        except:
            pass