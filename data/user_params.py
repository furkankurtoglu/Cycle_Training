 
# This file is auto-generated from a Python script that parses a PhysiCell configuration (.xml) file.
#
# Edit at your own risk.
#
import os
from ipywidgets import Label,Text,Checkbox,Button,HBox,VBox,FloatText,IntText,BoundedIntText,BoundedFloatText,Layout,Box
    
class UserTab(object):

    def __init__(self):
        
        micron_units = Label('micron')   # use "option m" (Mac, for micro symbol)

        constWidth = '180px'
        tab_height = '500px'
        stepsize = 10

        #style = {'description_width': '250px'}
        style = {'description_width': '25%'}
        layout = {'width': '400px'}

        name_button_layout={'width':'25%'}
        widget_layout = {'width': '15%'}
        widget2_layout = {'width': '10%'}
        units_button_layout ={'width':'15%'}
        desc_button_layout={'width':'45%'}
        divider_button_layout={'width':'40%'}

        param_name1 = Button(description='initial_tumor_radius', disabled=True, layout=name_button_layout)
        param_name1.style.button_color = 'tan'

        self.initial_tumor_radius = FloatText(
          value=150,
          step=10,
          style=style, layout=widget_layout)

        div_row1 = Button(description='---Phase link between G0/G1 and S---', disabled=True, layout=divider_button_layout)

        param_name2 = Button(description='r01', disabled=True, layout=name_button_layout)
        param_name2.style.button_color = 'lightgreen'

        self.r01 = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name3 = Button(description='r01_arrest', disabled=True, layout=name_button_layout)
        param_name3.style.button_color = 'tan'

        self.r01_arrest = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name4 = Button(description='oxygen_threshold', disabled=True, layout=name_button_layout)
        param_name4.style.button_color = 'lightgreen'

        self.oxygen_threshold = FloatText(
          value=40,
          step=1,
          style=style, layout=widget_layout)

        div_row2 = Button(description='---Phase link between S and G2---', disabled=True, layout=divider_button_layout)

        param_name5 = Button(description='r12', disabled=True, layout=name_button_layout)
        param_name5.style.button_color = 'tan'

        self.r12 = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name6 = Button(description='r12_arrest', disabled=True, layout=name_button_layout)
        param_name6.style.button_color = 'lightgreen'

        self.r12_arrest = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name7 = Button(description='lactate_threshold', disabled=True, layout=name_button_layout)
        param_name7.style.button_color = 'tan'

        self.lactate_threshold = FloatText(
          value=10.0,
          step=1,
          style=style, layout=widget_layout)

        div_row3 = Button(description='---Phase link between G2 an M---', disabled=True, layout=divider_button_layout)

        param_name8 = Button(description='r23', disabled=True, layout=name_button_layout)
        param_name8.style.button_color = 'lightgreen'

        self.r23 = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name9 = Button(description='r23_arrest', disabled=True, layout=name_button_layout)
        param_name9.style.button_color = 'tan'

        self.r23_arrest = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name10 = Button(description='pressure_threshold', disabled=True, layout=name_button_layout)
        param_name10.style.button_color = 'lightgreen'

        self.pressure_threshold = FloatText(
          value=1.0,
          step=0.1,
          style=style, layout=widget_layout)

        div_row4 = Button(description='---Phase link between M an G0/G1 (division)---', disabled=True, layout=divider_button_layout)

        param_name11 = Button(description='r30', disabled=True, layout=name_button_layout)
        param_name11.style.button_color = 'tan'

        self.r30 = FloatText(
          value=0.001,
          step=0.0001,
          style=style, layout=widget_layout)

        param_name12 = Button(description='r30_arrest', disabled=True, layout=name_button_layout)
        param_name12.style.button_color = 'lightgreen'

        self.r30_arrest = Checkbox(
          value=False,
          style=style, layout=widget_layout)

        param_name13 = Button(description='volume_threshold', disabled=True, layout=name_button_layout)
        param_name13.style.button_color = 'tan'

        self.volume_threshold = FloatText(
          value=2490.0,
          step=100,
          style=style, layout=widget_layout)

        units_button1 = Button(description='micrometer', disabled=True, layout=units_button_layout) 
        units_button1.style.button_color = 'tan'
        units_button2 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button2.style.button_color = 'tan'
        units_button3 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button3.style.button_color = 'lightgreen'
        units_button4 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button4.style.button_color = 'tan'
        units_button5 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button5.style.button_color = 'lightgreen'
        units_button6 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button6.style.button_color = 'lightgreen'
        units_button7 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button7.style.button_color = 'tan'
        units_button8 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button8.style.button_color = 'lightgreen'
        units_button9 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button9.style.button_color = 'tan'
        units_button10 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button10.style.button_color = 'tan'
        units_button11 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button11.style.button_color = 'lightgreen'
        units_button12 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button12.style.button_color = 'tan'
        units_button13 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button13.style.button_color = 'lightgreen'
        units_button14 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button14.style.button_color = 'lightgreen'
        units_button15 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button15.style.button_color = 'tan'
        units_button16 = Button(description='', disabled=True, layout=units_button_layout) 
        units_button16.style.button_color = 'lightgreen'
        units_button17 = Button(description='1/min', disabled=True, layout=units_button_layout) 
        units_button17.style.button_color = 'tan'

        desc_button2 = Button(description='initial tumor radius' , tooltip='initial tumor radius', disabled=True, layout=desc_button_layout) 
        desc_button2.style.button_color = 'tan'
        desc_button3 = Button(description='transition rate between G0/G1 and S' , tooltip='transition rate between G0/G1 and S', disabled=True, layout=desc_button_layout) 
        desc_button3.style.button_color = 'lightgreen'
        desc_button4 = Button(description='arrest function according to oxygen' , tooltip='arrest function according to oxygen', disabled=True, layout=desc_button_layout) 
        desc_button4.style.button_color = 'tan'
        desc_button5 = Button(description='environmental oxygen threshold to pass this phase transition' , tooltip='environmental oxygen threshold to pass this phase transition', disabled=True, layout=desc_button_layout) 
        desc_button5.style.button_color = 'lightgreen'
        desc_button6 = Button(description='transition rate between S and G2' , tooltip='transition rate between S and G2', disabled=True, layout=desc_button_layout) 
        desc_button6.style.button_color = 'tan'
        desc_button7 = Button(description='arrest function according to cell volume' , tooltip='arrest function according to cell volume', disabled=True, layout=desc_button_layout) 
        desc_button7.style.button_color = 'lightgreen'
        desc_button8 = Button(description='environmental lactate threshold to stall this phase transition' , tooltip='environmental lactate threshold to stall this phase transition', disabled=True, layout=desc_button_layout) 
        desc_button8.style.button_color = 'tan'
        desc_button9 = Button(description='transition rate between G2 and M' , tooltip='transition rate between G2 and M', disabled=True, layout=desc_button_layout) 
        desc_button9.style.button_color = 'lightgreen'
        desc_button10 = Button(description='arrest function according to nuclear volume' , tooltip='arrest function according to nuclear volume', disabled=True, layout=desc_button_layout) 
        desc_button10.style.button_color = 'tan'
        desc_button11 = Button(description='cell pressure threshold to stall this phase transition' , tooltip='cell pressure threshold to stall this phase transition', disabled=True, layout=desc_button_layout) 
        desc_button11.style.button_color = 'lightgreen'
        desc_button12 = Button(description='transition rate between M and G0/G1' , tooltip='transition rate between M and G0/G1', disabled=True, layout=desc_button_layout) 
        desc_button12.style.button_color = 'tan'
        desc_button13 = Button(description='arrest function according to pressure level' , tooltip='arrest function according to pressure level', disabled=True, layout=desc_button_layout) 
        desc_button13.style.button_color = 'lightgreen'
        desc_button14 = Button(description='cell pressure threshold to stall this phase transition' , tooltip='cell pressure threshold to stall this phase transition', disabled=True, layout=desc_button_layout) 
        desc_button14.style.button_color = 'tan'

        row2 = [param_name1, self.initial_tumor_radius, units_button1, desc_button2] 
        row3 = [param_name2, self.r01, units_button3, desc_button3] 
        row4 = [param_name3, self.r01_arrest, units_button4, desc_button4] 
        row5 = [param_name4, self.oxygen_threshold, units_button5, desc_button5] 
        row6 = [param_name5, self.r12, units_button7, desc_button6] 
        row7 = [param_name6, self.r12_arrest, units_button8, desc_button7] 
        row8 = [param_name7, self.lactate_threshold, units_button9, desc_button8] 
        row9 = [param_name8, self.r23, units_button11, desc_button9] 
        row10 = [param_name9, self.r23_arrest, units_button12, desc_button10] 
        row11 = [param_name10, self.pressure_threshold, units_button13, desc_button11] 
        row12 = [param_name11, self.r30, units_button15, desc_button12] 
        row13 = [param_name12, self.r30_arrest, units_button16, desc_button13] 
        row14 = [param_name13, self.volume_threshold, units_button17, desc_button14] 

        box_layout = Layout(display='flex', flex_flow='row', align_items='stretch', width='100%')
        box2 = Box(children=row2, layout=box_layout)
        box3 = Box(children=row3, layout=box_layout)
        box4 = Box(children=row4, layout=box_layout)
        box5 = Box(children=row5, layout=box_layout)
        box6 = Box(children=row6, layout=box_layout)
        box7 = Box(children=row7, layout=box_layout)
        box8 = Box(children=row8, layout=box_layout)
        box9 = Box(children=row9, layout=box_layout)
        box10 = Box(children=row10, layout=box_layout)
        box11 = Box(children=row11, layout=box_layout)
        box12 = Box(children=row12, layout=box_layout)
        box13 = Box(children=row13, layout=box_layout)
        box14 = Box(children=row14, layout=box_layout)

        self.tab = VBox([
          box2,
          div_row1,
          box3,
          box4,
          box5,
          div_row2,
          box6,
          box7,
          box8,
          div_row3,
          box9,
          box10,
          box11,
          div_row4,
          box12,
          box13,
          box14,
        ])

    # Populate the GUI widgets with values from the XML
    def fill_gui(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        self.initial_tumor_radius.value = float(uep.find('.//initial_tumor_radius').text)
        self.r01.value = float(uep.find('.//r01').text)
        self.r01_arrest.value = ('true' == (uep.find('.//r01_arrest').text.lower()) )
        self.oxygen_threshold.value = float(uep.find('.//oxygen_threshold').text)
        self.r12.value = float(uep.find('.//r12').text)
        self.r12_arrest.value = ('true' == (uep.find('.//r12_arrest').text.lower()) )
        self.lactate_threshold.value = float(uep.find('.//lactate_threshold').text)
        self.r23.value = float(uep.find('.//r23').text)
        self.r23_arrest.value = ('true' == (uep.find('.//r23_arrest').text.lower()) )
        self.pressure_threshold.value = float(uep.find('.//pressure_threshold').text)
        self.r30.value = float(uep.find('.//r30').text)
        self.r30_arrest.value = ('true' == (uep.find('.//r30_arrest').text.lower()) )
        self.volume_threshold.value = float(uep.find('.//volume_threshold').text)


    # Read values from the GUI widgets to enable editing XML
    def fill_xml(self, xml_root):
        uep = xml_root.find('.//microenvironment_setup')  # find unique entry point
        vp = []   # pointers to <variable> nodes
        if uep:
            for var in uep.findall('variable'):
                vp.append(var)

        uep = xml_root.find('.//user_parameters')  # find unique entry point
        uep.find('.//initial_tumor_radius').text = str(self.initial_tumor_radius.value)
        uep.find('.//r01').text = str(self.r01.value)
        uep.find('.//r01_arrest').text = str(self.r01_arrest.value)
        uep.find('.//oxygen_threshold').text = str(self.oxygen_threshold.value)
        uep.find('.//r12').text = str(self.r12.value)
        uep.find('.//r12_arrest').text = str(self.r12_arrest.value)
        uep.find('.//lactate_threshold').text = str(self.lactate_threshold.value)
        uep.find('.//r23').text = str(self.r23.value)
        uep.find('.//r23_arrest').text = str(self.r23_arrest.value)
        uep.find('.//pressure_threshold').text = str(self.pressure_threshold.value)
        uep.find('.//r30').text = str(self.r30.value)
        uep.find('.//r30_arrest').text = str(self.r30_arrest.value)
        uep.find('.//volume_threshold').text = str(self.volume_threshold.value)
