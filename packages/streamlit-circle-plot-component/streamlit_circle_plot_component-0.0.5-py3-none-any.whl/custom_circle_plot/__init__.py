import os
import streamlit.components.v1 as components

_RELEASE = True 

if not _RELEASE:
    _custom_circle_plot = components.declare_component(
        
        "custom_circle_plot",
 
        url="http://localhost:3001",
    )
else:

    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _custom_circle_plot = components.declare_component("custom_circle_plot", path=build_dir)


def custom_circle_plot(plotData=None, styles=None, dmgType=None, dmgTypeMulti=None, colorGradient=None, singlePlot=True, chartLegend=None, default=None, key=None):

    component_value = _custom_circle_plot(plotData=plotData, styles=styles, dmgType=dmgType, dmgTypeMulti=dmgTypeMulti, singlePlot=singlePlot, chartLegend=chartLegend, colorGradient=colorGradient, default=default, key=key)

    return component_value
