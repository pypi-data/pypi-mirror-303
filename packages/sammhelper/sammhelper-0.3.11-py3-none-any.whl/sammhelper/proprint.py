import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

def proprint(name):
    # Set the results directory
    rd = os.path.abspath(os.getcwd() + '\\Images')
    
    # Check if the Images folder exists, if not, create it
    if not os.path.exists(rd):
        os.makedirs(rd)
    
    # Set figure size
    plt.rcParams["figure.figsize"] = (6, 3)
    
    # Save the figure
    plt.savefig(os.path.join(rd, name + '.pdf'), bbox_inches='tight')