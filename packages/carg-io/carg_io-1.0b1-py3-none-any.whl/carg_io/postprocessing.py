
# Bokeh imports
from bokeh.plotting import figure, output_file, save
from bokeh.models import CustomJS, Select, OpenURL, TapTool, Div, ColumnDataSource, Button
from bokeh.models.tools import HoverTool
from bokeh.transform import linear_cmap
from bokeh.palettes import Spectral6, Spectral11, Turbo256

from bokeh.layouts import row, column
from bokeh.models import DataTable, DateFormatter, TableColumn, ColorBar, Circle
from bokeh.io import show as show_in_bokeh
from .core import ParameterSet, Parameter, units
from typing import List, Type
import pandas as pd


class Analyze():
    """ParameterSets may be used to define input, but also the output from an certain analysis.
    If you have one or two such analyses, it may still be doable to go throught them numerically.
    Once we have more, it this might no longer be the case.

    
        ParameterSet1                                           ParameterSet4
        ParameterSet2   --input--> Calculation 1 --output-->    ParameterSet5
        ParameterSet3                                       


        ParameterSet1                                           ParameterSet4
        ParameterSet2   --input--> Calculation 2 --output-->    ParameterSet5
        ParameterSet3                                       

                                    ...etc




    
    """

    def __init__(self, sets:List[List[Type[ParameterSet]]]) -> None:
        self._check_sets(sets)
        self.sets = sets

    @staticmethod
    def _check_sets(sets:List[List[Type[ParameterSet]]]):
        """Check whether all input is correct"""
        for set in sets:
            for s in set:
                if not isinstance(s, ParameterSet):
                    raise TypeError('All items must be an instance of ParameterSet')

        aaa = []
        for set in sets:
            aaa.append({type(s) for s in set})
        
        for a in aaa[1:]:
            if not aaa[0] == a:
                raise TypeError('All sets of ParameterSets must be the same')
                
    
    def _sets_to_dataframe(self):
        """Convert all sets to 1 big dataframe"""
        sets = self.sets
        aa = []
        for ix, set in enumerate(sets):
            series = []
            for s in set:
                df = s.to_dataframe(name_include_unit=True) 
                df.set_index('name', inplace=True, drop=True)
                sr = df.value
                series.append(sr)
            ss = pd.concat(series)
            ss.name = str(ix)
            aa.append(ss)
        df = pd.concat(aa, axis=1).T
        return df

    def _get_single_scatter(self, source1:ColumnDataSource, source2:ColumnDataSource, show=False) -> column:
        """Return an interactive scatter for the current sets.
        
        Input:
            source1:ColumnDataSource


        Returns:
            A bokeh column[ row[Select, Select, Select]], figure]
        
        
        """
        ppp = figure(tools="pan,wheel_zoom,box_zoom,box_select,tap,undo,reset,save")
       
        ppp.toolbar.logo = None
        mapper = linear_cmap(field_name=f'ColorValues', palette=Turbo256 ,low=0 ,high=1)

        tags = source1.column_names
        tags.pop(tags.index('index'))
        tags.pop(tags.index('ColorValues'))
        x_start = tags[0]
        y_start = tags[1]

        scatter = ppp.circle(x=x_start, 
                             y=y_start,
                             color=mapper,
                             source=source1,
                             size=10,
                             fill_color=mapper, 
                             line_width=1)
        
        # The non-selected item should have constrasting color and a large alpha.
        scatter.nonselection_glyph = Circle(fill_color='pink', fill_alpha=0.75, line_color=None)

        ppp.xaxis.axis_label = x_start
        ppp.yaxis.axis_label = y_start
        
        
        ppp.toolbar.active_inspect = None
        
        # Sort of does want I want, but behaves erratic at times.
        js_link_selections = """ //link Cdf selection
        
        var s1 = source1
        var s2 = source2
        
        // impose the selected value to the other
        var ind1 = s1.selected.indices
        var ind2 = s2.selected.indices
        
        
        if (ind2.length == 0) {
            var ind = ind1
        } else {
            // intersection?
            var ind = ind1.filter(value => -1 !== ind2.indexOf(value))
        }
        
        //s1.selected.indices = ind
        s2.selected.indices = ind
        
        //source1.change.emit()
        source2.change.emit()
        
        """
        
        js = CustomJS(args=dict(source1=source1,
                                source2=source2,
                                ),
                      code=js_link_selections)
               
        source1.selected.js_on_change('indices', js)

        
        # url = "file://@PlatformID"
        # taptool = ppp.select(type=TapTool)
        # taptool.callback = OpenURL(url=url)
        
        hover = HoverTool()
        hover.tooltips = [(item,'@'+item) for item in tags]
        ppp.add_tools(hover)
        
        # Set what happens when you select item from the drop-down menu for X and Y axis data
        # NOTE: xaxis[0] has to be indexed, because there might be multiple axes
        xhandler = CustomJS(args=dict(axis=ppp.xaxis[0], 
                                      scatter=scatter),
                            code='''scatter.glyph.x = {field: cb_obj.value};
                                    axis.axis_label = cb_obj.value; 
                                 ''')
        
        
        xselect = Select(title="X-axis:", options=list(tags), value=x_start)
        xselect.js_on_change('value', xhandler)
        
        
        yhandler = CustomJS(args=dict(axis=ppp.yaxis[0], 
                                      scatter=scatter),
                            code='''scatter.glyph.y = {field: cb_obj.value};
                                    axis.axis_label = cb_obj.value; 
                                 ''')
        yselect = Select(title="Y-axis:", options=list(tags), value=y_start)
        yselect.js_on_change('value', yhandler)
        
        
        # Set what happens when you select item from the drop-down menu for color data
        # Color code # NOTE using fstring means using double brackets!  {{ }}
        codec = f"""
            
            var data = source1.data;
            var f = cb_obj.value;
            var x = data['ColorValues']
            
            //label.text = cb_obj.value.toString();
            
            var ind = source1.selected.indices
            
            
            // Update title
            ppp.title.text = 'Color: ' + cb_obj.value + ' - Selected: ' + ind.length
            
            if (cb_obj.value=="None") {{
                for (var i = 0; i < x.length; i++) {{
                    x[i] = 0
                }}
            }} else {{ 
            
                var y = data[f]
                var maxy = Math.max.apply(Math, y);
                var miny = Math.min.apply(Math, y);
                
                if (maxy==miny) {{
                    for (var i = 0; i < x.length; i++) {{
                       x[i] = 0
                    }}
                       
                }} else {{
                    for (var i = 0; i < x.length; i++) {{
                       x[i] = (y[i] - miny) / (maxy-miny)
                    }}
                }}
            }}
            
            source1.change.emit();
    
        """
        
        chandler = CustomJS(args=dict(source1=source1, ppp=ppp), code=codec)
        
        color_tags = ['None']
        color_tags.extend(list(tags))
        
        cselect = Select(title="Color:", options=color_tags, value='None')
        cselect.js_on_change('value', chandler)
        
        col = column(column(xselect, yselect, cselect), ppp)
        if show:
            show_in_bokeh(col)

        return col

    def get_double_scatter(self, show=False) -> row:
        """Return an interactive double scatter using Bokeh.
        A double scatter is a convenient way of navigating and filtering large parameteric
        data sets.
        """

        df = self._sets_to_dataframe()
        df = df.astype(float)
        df['ColorValues'] = 0.
        
        source1 = ColumnDataSource(df)
        source2 = ColumnDataSource(df)

        scat1 = self._get_single_scatter(source1, source2, show=False)
        scat2 = self._get_single_scatter(source2, source1, show=False)
        scatters = row(scat1, scat2)
        if show:
            show_in_bokeh(scatters)
        return scatters



        

