import matplotlib.pyplot as mlt
from matplotlib.ticker import MultipleLocator
from IPython import get_ipython
from pathlib import Path

def customize_graf(axes, title, xlabel, ylabel, xmajor_locator=1, ymajor_locator=1, xmax=50, ymax=50, color='#004494', facecolor='#ffffff', gridcolor='#e6e6fa', act_gridcolor=True, tickcolor='#580F41',tick_style=True, frontsize=13, legend=True):
    #Titulos
    axes.set_xlabel(xlabel,labelpad=10, color=color)
    axes.set_ylabel(ylabel,labelpad=10, color=color)
    axes.set_title(title, color=color, pad=20)
    #Ejes
    axes.set_xlim(xmin=0, xmax=xmax)
    axes.set_ylim(ymin=0, ymax=ymax)
    axes.xaxis.set_major_locator(MultipleLocator(xmajor_locator))
    axes.yaxis.set_major_locator(MultipleLocator(ymajor_locator))
    #Ticks
    axes.tick_params(axis='both',labelsize=frontsize, colors=tickcolor)
    if tick_style==True:
        axes.spines['right'].set_visible(False)
        axes.spines['top'].set_visible(False)
    else:
        axes.spines['right'].set_color(tickcolor)
        axes.spines['top'].set_color(tickcolor)
    axes.spines['left'].set_color(tickcolor)
    axes.spines['bottom'].set_color(tickcolor)
    #Color de fondo
    axes.set_facecolor(facecolor)

    #Cuadrícula
    if act_gridcolor==True:
        axes.grid(visible=True, which='major', axis='both',color=gridcolor,linewidth=1)
        axes.set_axisbelow(True)
    #Leyenda
    if legend==True:
        frontsize_legend=frontsize/2 +1
        axes.legend(fontsize=frontsize_legend,facecolor='#f0ffff',labelcolor="#000000")


def save_figure(figure,filename):
    #Guarda una figura a disco en carpeta figures
    absolute_filename=Path.cwd()/'figures'/filename
    #facecolor-background
    #bbox_inches-permite especificar que porción de la figura ha de ser guardada
        #tight-se extiende o reduce el área de la figura guardada para incluir a todos los componentes de ella, eliminado también los espacios blancos sobrantes en los bordes
    figure.savefig(absolute_filename,facecolor='#fff',bbox_inches='tight')


