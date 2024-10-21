
__version__ = '..'

import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import patches
import matplotlib.ticker as ticker
from matplotlib.ticker import MultipleLocator
import numpy as np
from . import H2ONaCl


def makeLogLinearAxes(ax,width_logaxis=0.4,xlim_log=(2E-3,1),xmax=100,xloc_major=20,xloc_minor=4,yloc='left',color_log=(127/255,0,1),xlabel='Bulk salinity (wt % NaCl)',bkcolor='None',ylim=None, yloc_major=None,yloc_minor=None,ylabel=None):
    # log segment
    ax_log=ax.inset_axes([0,0,width_logaxis,1],facecolor=bkcolor)
    ax_log.set_xscale('log')
    ax_log.set_xlim(xlim_log)
    #ax_log.xaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=(0.1,0.2,0.3,0.4, 0.5, 0.6, 0.7, 0.8, 0.9),numticks=10))
    ax_log.spines['right'].set_visible(False)
    ax_log.spines['bottom'].set_color(color_log)
    ax_log.spines['top'].set_color(color_log)
    ax_log.tick_params(axis='x', which='both', colors=color_log)
    ax_log.annotate("", xy=(0.03,-0.14), xycoords='axes fraction', xytext=(1,-0.14), textcoords='axes fraction', arrowprops=dict(arrowstyle="<->",connectionstyle="arc3",color=color_log),clip_on=False,zorder=0)
    ax_log.set_xlabel('Log-scale',color=color_log,bbox={'fc':'w','ec':'None'})

    # linear segment
    ax_linear=ax.inset_axes([width_logaxis,0, 1-width_logaxis, 1],facecolor=bkcolor)
    ax_linear.yaxis.set_label_position('right')
    ax_linear.yaxis.set_ticks_position('right')
    ax_linear.set_xlim(xlim_log[1], xmax)
    ax_linear.xaxis.set_major_locator(MultipleLocator(xloc_major))
    ax_linear.xaxis.set_minor_locator(MultipleLocator(xloc_minor))
    #ax_linear.spines['left'].set_visible(False)
    ax_linear.spines['left'].set_linewidth(0.5)
    ax_linear.spines['left'].set_linestyle('solid')
    ax_linear.spines['left'].set_color(color_log)
    ax_linear.spines['left'].set_capstyle("butt")
    ax_linear.annotate("", xy=(-0.03,-0.14), xycoords='axes fraction', xytext=(1,-0.14), textcoords='axes fraction', arrowprops=dict(arrowstyle="<->",connectionstyle="arc3"),clip_on=False,zorder=0)
    ax_linear.set_xlabel('Linear-scale',labelpad=10,bbox={'fc':'w','ec':'None'})
    # ytick location
    ax_linear.yaxis.set_ticklabels([]) if(yloc=='left') else ax_log.yaxis.set_ticklabels([])
    # share y axis
    ax_linear.get_shared_y_axes().join(ax_log, ax_linear)
    for axis in [ax_log,ax_linear]:
        if(ylim!=None): axis.set_ylim(ylim)
        if(yloc_major!=None): axis.yaxis.set_major_locator(MultipleLocator(yloc_major))
        if(yloc_minor!=None): axis.yaxis.set_minor_locator(MultipleLocator(yloc_minor))
    if(ylabel!=None): ax_log.set_ylabel(ylabel) if(yloc=='left') else ax_linear.set_ylabel(ylabel)
    # hide base axes
    for spine in ax.spines: ax.spines[spine].set_visible(False)
    ax.xaxis.set_ticks([])
    ax.yaxis.set_ticks([])
    if(xlabel!=None): ax.set_xlabel(xlabel,labelpad=40)

    return ax_log,ax_linear

def createWaterAxes(ax,fc='whitesmoke'):
    ax_water=ax.inset_axes([0.004,0,0.1,1],facecolor=fc)
    ax_water.spines['left'].set_visible(False)
    ax_water.spines['right'].set_visible(False)
    ax_water.set_xlim(-0.5,1)
    ax_water.xaxis.set_ticks([0])
    ax_water.yaxis.set_ticks([])
    ax_water.set_ylim(ax.get_ylim())
    mpl.rcParams['hatch.linewidth'] = 0.5
    mpl.rcParams['hatch.color'] = 'k'
    ax_water.axvspan(0.7,1,hatch='////',fc=fc)
    return ax_water

def plot_Pslice(P0, x0_log_linear=0.01, sw=H2ONaCl.cH2ONaCl("IAPS84")):
    # x0_log_linear=0.01 # mass fraction of NaCl: kg/kg
    slice_constP = sw.Slice_constP(P0)
    lines = slice_constP.lines
    key_lines=np.array(lines)
    regions=slice_constP.regions
    lines=slice_constP.lines
    points=slice_constP.points
    # plot
    fig,axes=plt.subplots(1,2,figsize=(12,4),gridspec_kw={'wspace':0.05})
    xlim_log=(2E-4,x0_log_linear*100) # wt.% NaCl
    # TPX
    ax=axes[0]
    # make log-linear hybrid axes for isobaric slice
    ax_log_TPX,ax_linear_TPX=makeLogLinearAxes(axes[0],xlim_log=xlim_log,ylabel='Temperature ($^{\circ}$C)',ylim=(1,1000),yloc_major=200,yloc_minor=40)
    ax_log_HPX,ax_linear_HPX=makeLogLinearAxes(axes[1],xlim_log=xlim_log,yloc='right',ylabel='Specific enthalpy (MJ/kg)',ylim=(0,4.6),yloc_major=1, yloc_minor=0.2)
    ax_water_TPX=createWaterAxes(ax_log_TPX)
    ax_water_HPX=createWaterAxes(ax_log_HPX)
    for ax_log in [ax_log_TPX, ax_log_HPX]:
        ax_log.xaxis.set_major_locator(mpl.ticker.LogLocator(base=10.0, subs=(1.0,),numticks=10))
        ax_log.xaxis.set_minor_locator(mpl.ticker.LogLocator(base=10.0, subs=(0.1,0.2,0.3,0.4, 0.5, 0.6, 0.7, 0.8, 0.9),numticks=10))
    # plot
    for name in np.array(regions):
        ec = 'None'
        label=name
        for region in np.array(regions[name]):
            T, P, X, H = np.array(region.T)-273.15, np.array(region.P), np.array(region.X)*100,np.array(region.H)/1E6
            if('V+L+H' in name): ec=region.ec
            for ax_T, ax_H in zip([ax_log_TPX,ax_linear_TPX], [ax_log_HPX,ax_linear_HPX]):
                ax_T.fill(X, T, fc=region.fc, ec=ec,lw=0.5)
                ax_H.fill(X, H, fc=region.fc, ec=ec, label=label,lw=0.5)
            label=None
    for name in np.array(lines):
        for line in np.array(lines[name]):
            T, P, X, H = np.array(line.T)-273.15, np.array(line.P), np.array(line.X)*100,np.array(line.H)/1E6
            for ax_T, ax_H in zip([ax_log_TPX,ax_linear_TPX], [ax_log_HPX,ax_linear_HPX]):
                ax_T.plot(X, T, color=line.color, ls=line.ls, lw=line.lw)
                if("V+L+H" not in name): ax_H.plot(X, H, color=line.color, ls=line.ls, lw=line.lw)
            if('water' in name):
                ax_water_HPX.axhspan(H[0],H[1], 0.1, 0.6, fc='gold', ec='None')
                ax_water_HPX.text(0,(H[0]+H[1])/2, 'V+L', ha='center', va='center', rotation=90)
                ax_water_HPX.axhspan(0,H[0], 0.1, 0.6, fc='lightgreen', ec='None')
                ax_water_HPX.text(0,H[0]/2, 'Liquid', ha='center', va='center', rotation=90)
                ax_water_HPX.axhspan(H[1], 5, 0.1, 0.6, fc='lightcyan', ec='None')
                ax_water_HPX.text(0,(4.5+H[1])/2, 'Vapor', ha='center', va='center', rotation=90)
    handles_points_log=[]
    for name in np.array(points):
        label=name
        for point in np.array(points[name]):
            ax_T, ax_H = ax_linear_TPX, ax_linear_HPX
            if(point.X<x0_log_linear):
                ax_T = ax_log_TPX
                ax_H = ax_log_HPX
            if('water' in name):
                ax_T = ax_water_TPX
                ax_H = ax_water_HPX
            ax_T.scatter(point.X*100, point.T-273.15, marker=point.marker, fc=np.array(point.mfc), ec=np.array(point.mec),lw=0.5,zorder=4)
            s=ax_H.scatter(point.X*100, point.H/1E6, marker=point.marker, fc=np.array(point.mfc), ec=np.array(point.mec),lw=0.5,label=label,zorder=4)
            if((point.X<x0_log_linear) & ('water' not in name)): handles_points_log.append(s)
            label=None
    # legend
    leg=ax_linear_HPX.legend(loc='lower left', bbox_to_anchor=[-2.45, 1.02], ncol=15)
    ax_linear_HPX.legend(handles=leg.legendHandles + handles_points_log,loc='lower left', bbox_to_anchor=[-2.45, 1.02], ncol=15, columnspacing=0.8, handletextpad=0.2,markerscale=1,handlelength=1.1)
    # customized text
    ax_linear_HPX.text(60, 3, 'T > 1000 $^{\circ}$C', rotation=-42)
    for ax_log, ax_linear in zip([ax_log_TPX, ax_log_HPX], [ax_linear_TPX, ax_linear_HPX]):
        ax_log.text(0.2,0.02,'P = %.0f bar'%(P0/1E5), transform=ax_log.transAxes, fontsize=12, fontweight='normal',va='bottom',ha='left')
    for ax_water in [ax_water_TPX, ax_water_HPX]:
        if(P0>sw.get_pWater().p_critical()):  ax_water.text(0.5, 0.5, 'Critical water', transform=ax_water.transAxes, ha='center',va='center',rotation=90)

    ax_log_TPX.text(0.03,0.98,'(a)', transform=ax_log_TPX.transAxes, fontsize=12, fontweight='bold',va='top',ha='left',bbox={'fc':'w','ec':'None','alpha':0.9}, zorder=9)
    ax_log_HPX.text(0.03,0.98,'(b)', transform=ax_log_HPX.transAxes, fontsize=12, fontweight='bold',va='top',ha='left',bbox={'fc':'w','ec':'None','alpha':0.9}, zorder=9)

    return {'data':slice_constP, 'ax_T': [ax_log_TPX, ax_linear_TPX], 'ax_H':[ax_log_HPX, ax_linear_HPX], 'ax_water': [ax_water_TPX, ax_water_HPX]}


