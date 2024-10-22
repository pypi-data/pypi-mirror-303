'''
title_font_size = "60px"
logo_height = "100px"
margin = "30px"
text_font_size = "25px"
border_line = "1px solid #000"
border_radius = "10px"
area_height = "550px"
dropdown_select_width = "300px"
editor_window_height = "1300px"
popup_font_size = "30px"
error_plot_width = "500px"
error_plot_height = "500px"
default_input_width = "100px"
model_input_width = "1500px"
model_add_width = "500px"
stop_training_width = "150px"
shap_height = "350px"
lime_expl_width = "850px"
'''
'''
# both
title_font_size = "60px"
text_font_size = "25px"
popup_font_size = "30px"
border_line = "1px solid #000"
border_radius = "10px"

# height
logo_height = "100px"
shap_height = "350px"
area_height = "550px"
editor_window_height = "1300px"
error_plot_height = "500px"

# width
dropdown_select_width = "300px"
error_plot_width = "500px"
default_input_width = "100px"
model_input_width = "1500px"
model_add_width = "500px"
stop_training_width = "150px"
lime_expl_width = "850px"
margin = "30px"
'''

# Resolution: ca. 50%

# both
title_font_size = "25px"
text_font_size = "12px"
popup_font_size = "15px"
border_line = "0.5px solid #000"
border_radius = "10px" #
padding = "7px"

# height
logo_height = "50px"
shap_height = "175px"
area_height = "275px"
editor_window_height = "650px"
error_plot_height = "250px"

# width
dropdown_select_width = "150px"
error_plot_width = "250px"
default_input_width = "50px"
model_input_width = "750px"
model_add_width = "250px"
stop_training_width = "75px"
lime_expl_width = "425px"
margin = "15px"





'''
# height 100 / 768 * N       0.130208333 * N
logo_height = "50px" # = "6.5%"
shap_height = "175px" # = "22.8%"
area_height = "275px" # = "35.8%"
editor_window_height = "650px" # = "84.635%"
error_plot_height = "250px" # = "32.55%"

# width 100 / 1386 * N       0.072150072 * N
dropdown_select_width = "150px" # = "10.8225%"
error_plot_width = "250px" # = "18.0375%"
default_input_width = "50px" # = "3.6075%"
model_input_width = "750px" # = "54.11256%"
model_add_width = "250px" # = "18.0375%"
stop_training_width = "75px" # = "5.41126%"
lime_expl_width = "425px" # = "30.66378%"
margin = "15px" # = "1.0823%"
padding = "7px" # = "0.50505%"
tab_gap = "20px" # = "1.443%"
'''

#pip uninstall SAInTool -y && python setup.py sdist bdist_wheel && pip install dist/*.whl && python -m SAInT




size_table = {
    "title_font_size": ("width", 1.985, "px"),
    "feature_popup_width": ("width", 30, "px"),
    "error_plot_width": ("width", 50, "px"),
    "figure_width": ("width", 93, "-"),
    "marker_size": ("width", 0.8, "-"),
    "area_height": ("height", 25, "px"),
    "editor_window_height": ("height", 70, "px"),
    "lime_height": ("height", 32, "px"),
    "shap_height": ("height", 22, "px"),
    "error_plot_height": ("height", 15, "px"),
    "default_figure_height": ("height", 62, "-"),
}

# Function factory that creates the required functions
def create_function(name, ref_value, percentage, unit):
    def func():
        return calc_rel_size(ref_value, percentage, unit)
    func.__name__ = name
    return func

# Dynamically create functions based on the size_table
for name, (dimension, percentage, unit) in size_table.items():
    ref_value = width if dimension == "width" else height
    globals()[name] = create_function(name, ref_value, percentage, unit)