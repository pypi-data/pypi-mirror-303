from collections import defaultdict
import math
import numpy as np
from pydantic import Field as dataclass_field
from moapy.auto_convert import MBaseModel, auto_schema
from moapy.data_pre import OuterPolygon, InnerPolygon, Points, Point, Length, Stress, Temperature
from moapy.enum_pre import enUnitLength, enUnitStress, enUnitTemperature

# Eurocode 1 - Actions on structures - Part 1-5: General actions - Thermal actions
def data_group(group, sub_group=2):
        # 1a-Steel deck on steel girders
    data_type_1 = {
        "0" : {"T1_h": 30, "T2_h": 16, "T3_h": 6, "T4_h": 3, "T1_c": -8},
        "20": {"T1_h": 27, "T2_h": 15, "T3_h": 9, "T4_h": 5, "T1_c": -6},
        "40": {"T1_h": 24, "T2_h": 14, "T3_h": 8, "T4_h": 4, "T1_c": -6}
    }

    # 1b-Steel deck on steel truss or plate girders
    data_type_2 = {
        "0" : {"T1_h": 25, "T1_c": -6},
        "20": {"T1_h": 23, "T1_c": -5},
        "40": {"T1_h": 21, "T1_c": -5}
    }

    # 2-Composite decks
    data_type_31 = {
        "200": {"T1_h": 16.5, "T1_c": -5.9},
        "300": {"T1_h": 18.5, "T1_c": -9.0}
    }

    data_type_32 = {
        "200": {
            "0"  : {"T1_h": 23.0, "T1_c": -5.9},
            "50" : {"T1_h": 18.0, "T1_c": -4.4},
            "100": {"T1_h": 13.0, "T1_c": -3.5},
            "150": {"T1_h": 10.5, "T1_c": -2.3},
            "200": {"T1_h": 8.5 , "T1_c": -1.6}
        },
        "300":{
            "0"  : {"T1_h": 26.5, "T1_c": -9.0},
            "50" : {"T1_h": 20.5, "T1_c": -6.8},
            "100": {"T1_h": 16.0, "T1_c": -5.0},
            "150": {"T1_h": 12.5, "T1_c": -3.7},
            "200": {"T1_h": 10.0, "T1_c": -2.7}
        }
    }

    # 3-Concrete decks
    data_type_41 = {
        "200" : {"T1_h": 12.0, "T2_h": 5.0, "T3_h": 0.1, "T1_c": -4.7,  "T2_c": -1.7, "T3_c":  0.0, "T4_c": -0.7},
        "400" : {"T1_h": 15.2, "T2_h": 4.4, "T3_h": 1.2, "T1_c": -9.0,  "T2_c": -3.5, "T3_c": -0.4, "T4_c": -2.9},
        "600" : {"T1_h": 15.2, "T2_h": 4.0, "T3_h": 1.4, "T1_c": -11.8, "T2_c": -4.0, "T3_c": -0.9, "T4_c": -4.6},
        "800" : {"T1_h": 15.4, "T2_h": 4.0, "T3_h": 2.0, "T1_c": -12.8, "T2_c": -3.3, "T3_c": -0.9, "T4_c": -5.6},
        "1000": {"T1_h": 15.4, "T2_h": 4.0, "T3_h": 2.0, "T1_c": -13.4, "T2_c": -3.0, "T3_c": -0.9, "T4_c": -6.4},
        "1500": {"T1_h": 15.4, "T2_h": 4.5, "T3_h": 2.0, "T1_c": -13.7, "T2_c": -1.0, "T3_c": -0.6, "T4_c": -6.7}
    }

    data_type_42 = {
        "200": {
            "0"  : {"T1_h": 19.5, "T2_h": 8.5, "T3_h": 0.0, "T1_c": -4.7, "T2_c": -1.7, "T3_c":  0.0, "T4_c": -0.7},
            "50" : {"T1_h": 13.2, "T2_h": 4.9, "T3_h": 0.3, "T1_c": -3.1, "T2_c": -1.0, "T3_c": -0.2, "T4_c": -1.2},
            "100": {"T1_h": 8.5,  "T2_h": 3.5, "T3_h": 0.5, "T1_c": -2.0, "T2_c": -0.5, "T3_c": -0.5, "T4_c": -1.5},
            "150": {"T1_h": 5.6,  "T2_h": 2.5, "T3_h": 0.2, "T1_c": -1.1, "T2_c": -0.3, "T3_c": -0.7, "T4_c": -1.7},
            "200": {"T1_h": 3.7,  "T2_h": 2.0, "T3_h": 0.5, "T1_c": -0.5, "T2_c": -0.2, "T3_c": -1.0, "T4_c": -1.8}
        },
        "400": {
            "0"  : {"T1_h": 23.6, "T2_h": 6.5, "T3_h": 1.0, "T1_c": -9.0, "T2_c": -3.5, "T3_c": -0.4, "T4_c": -2.9},
            "50" : {"T1_h": 17.2, "T2_h": 4.6, "T3_h": 1.4, "T1_c": -6.4, "T2_c": -2.3, "T3_c": -0.6, "T4_c": -3.2},
            "100": {"T1_h": 12.0, "T2_h": 3.0, "T3_h": 1.5, "T1_c": -4.5, "T2_c": -1.4, "T3_c": -1.0, "T4_c": -3.5},
            "150": {"T1_h": 8.5,  "T2_h": 2.0, "T3_h": 1.2, "T1_c": -3.2, "T2_c": -0.9, "T3_c": -1.4, "T4_c": -3.8},
            "200": {"T1_h": 6.2,  "T2_h": 1.3, "T3_h": 1.0, "T1_c": -2.2, "T2_c": -0.5, "T3_c": -1.9, "T4_c": -4.0}
        },
        "600": {
            "0"  : {"T1_h": 23.6, "T2_h": 6.0, "T3_h": 1.4, "T1_c": -11.8, "T2_c": -4.0, "T3_c": -0.9, "T4_c": -4.6},
            "50" : {"T1_h": 17.6, "T2_h": 4.0, "T3_h": 1.8, "T1_c": -8.7,  "T2_c": -2.7, "T3_c": -1.2, "T4_c": -4.9},
            "100": {"T1_h": 13.0, "T2_h": 3.0, "T3_h": 2.0, "T1_c": -6.5,  "T2_c": -1.8, "T3_c": -1.5, "T4_c": -5.0},
            "150": {"T1_h": 9.7,  "T2_h": 2.2, "T3_h": 1.7, "T1_c": -4.9,  "T2_c": -1.1, "T3_c": -1.7, "T4_c": -5.1},
            "200": {"T1_h": 7.2,  "T2_h": 1.5, "T3_h": 1.5, "T1_c": -3.6,  "T2_c": -0.6, "T3_c": -1.9, "T4_c": -5.1}
        },
        "800": {
            "0"  : {"T1_h": 23.6, "T2_h": 5.0, "T3_h": 1.4, "T1_c": -12.8, "T2_c": -3.3, "T3_c": -0.9, "T4_c": -5.6},
            "50" : {"T1_h": 17.8, "T2_h": 4.0, "T3_h": 2.1, "T1_c": -9.8,  "T2_c": -2.4, "T3_c": -1.2, "T4_c": -5.8},
            "100": {"T1_h": 13.5, "T2_h": 3.0, "T3_h": 2.5, "T1_c": -7.6,  "T2_c": -1.7, "T3_c": -1.5, "T4_c": -6.0},
            "150": {"T1_h": 10.0, "T2_h": 2.5, "T3_h": 2.0, "T1_c": -5.8,  "T2_c": -1.3, "T3_c": -1.7, "T4_c": -6.2},
            "200": {"T1_h": 7.5,  "T2_h": 2.1, "T3_h": 1.5, "T1_c": -4.5,  "T2_c": -1.0, "T3_c": -1.9, "T4_c": -6.0}
        },
        "1000": {
            "0"  : {"T1_h": 23.6, "T2_h": 5.0, "T3_h": 1.4, "T1_c": -13.4, "T2_c": -3.0, "T3_c": -0.9, "T4_c": -6.4},
            "50" : {"T1_h": 17.8, "T2_h": 4.0, "T3_h": 2.1, "T1_c": -10.3, "T2_c": -2.1, "T3_c": -1.2, "T4_c": -6.3},
            "100": {"T1_h": 13.5, "T2_h": 3.0, "T3_h": 2.5, "T1_c": -8.0,  "T2_c": -1.5, "T3_c": -1.5, "T4_c": -6.3},
            "150": {"T1_h": 10.0, "T2_h": 2.5, "T3_h": 2.0, "T1_c": -6.2,  "T2_c": -1.1, "T3_c": -1.7, "T4_c": -6.2},
            "200": {"T1_h": 7.5,  "T2_h": 2.1, "T3_h": 1.5, "T1_c": -4.8,  "T2_c": -0.9, "T3_c": -1.9, "T4_c": -5.8}
        },
        "1500": {
            "0"  : {"T1_h": 23.6, "T2_h": 5.0, "T3_h": 1.4, "T1_c": -13.7, "T2_c": -1.0, "T3_c": -0.6, "T4_c": -6.7},
            "50" : {"T1_h": 17.8, "T2_h": 4.0, "T3_h": 2.1, "T1_c": -10.6, "T2_c": -0.7, "T3_c": -0.8, "T4_c": -6.6},
            "100": {"T1_h": 13.5, "T2_h": 3.0, "T3_h": 2.5, "T1_c": -8.4,  "T2_c": -0.5, "T3_c": -1.0, "T4_c": -6.5},
            "150": {"T1_h": 10.0, "T2_h": 2.5, "T3_h": 2.0, "T1_c": -6.5,  "T2_c": -0.4, "T3_c": -1.1, "T4_c": -6.2},
            "200": {"T1_h": 7.5,  "T2_h": 2.1, "T3_h": 1.5, "T1_c": -5.0,  "T2_c": -0.3, "T3_c": -1.2, "T4_c": -5.6}
        }
    }

    if group == 1:
        return data_type_1
    elif group == 2:
        return data_type_2
    elif group == 3:
        if sub_group == 1:
            return data_type_31
        elif sub_group == 2:
            return data_type_32
    elif group == 4:
        if sub_group == 1:
            return data_type_41
        elif sub_group == 2:
            return data_type_42
    else:
        return None

# Function to interpolate between two values
def linear_interpolation(lower_value, upper_value, lower_key, upper_key, input_value):
    interpolated_value = {}
    for param in lower_value:
        lower_param_value = lower_value[param]
        upper_param_value = upper_value[param]
        interpolated_value[param] = lower_param_value + (upper_param_value - lower_param_value) * (
            (input_value - lower_key) / (upper_key - lower_key)
        )
    return interpolated_value

# Function to Data Merge
def merge_and_interpolate(A1, A2, B1, B2):
    # Merge A1 and B1 arrays and sort them in descending order
    C = sorted(set(A1 + B1), reverse=True)
    
    # Create new arrays for A2 and B2
    A2_new = [np.nan] * len(C)
    B2_new = [np.nan] * len(C)

    # Interpolate values for A2 and B2 arrays
    for index, c_val in enumerate(C):
        if c_val in A1:
            A2_new[index] = A2[A1.index(c_val)]
        if c_val in B1:
            B2_new[index] = B2[B1.index(c_val)]

    for index, val in enumerate(A2_new):
        if np.isnan(val):
            for i in range(index-1, -1, -1):
                if not np.isnan(A2_new[i]):
                    y0 = A2_new[i]
                    x0 = C[i]
                    break
            for i in range(index, len(A2_new)):
                if not np.isnan(A2_new[i]):
                    y1 = A2_new[i]
                    x1 = C[i]
                    break
            A2_new[index] = y0 + (y1 - y0) * (C[index] - x0) / (x1 - x0)
    for index, val in enumerate(B2_new):
        if np.isnan(val):
            for i in range(index-1, -1, -1):
                if not np.isnan(B2_new[i]):
                    y0 = B2_new[i]
                    x0 = C[i]
                    break
            for i in range(index, len(B2_new)):
                if not np.isnan(B2_new[i]):
                    y1 = B2_new[i]
                    x1 = C[i]
                    break
            B2_new[index] = y0 + (y1 - y0) * (C[index] - x0) / (x1 - x0)

    return C, A2_new, B2_new

# Function to interpolate temperature
def interpolate_temperature(group, height, thickness, slabdepth=None):

    # Check if group is valid
    if group not in [1, 2, 3, 4]:
        raise ValueError("Group must be either 1, 2, 3 or 4")
    # Check if thickness is valid
    if isinstance(thickness, str):
        if thickness != "unsurfaced" and thickness != "waterproofed":
            raise ValueError("Thickness must be either unsurfaced or waterproofed")
    elif isinstance(thickness, (int, float)):
        if thickness < 0:
            raise ValueError("Thickness cannot be negative")
    else:
        raise ValueError("Thickness must be either string or number")

    # Temperature data for group 1 and 2
    if group == 1 or group == 2:
        # Get data for the group
        data = data_group(group)
        keys = [int(key) for key in data.keys()]
        max_thickness = max(keys)
        
        if thickness == "unsurfaced":
            data = data["0"]
        elif thickness >= max_thickness:
            data =  data[str(max_thickness)]
        else:
            for i  in range(len(keys) - 1):
                if keys[i] <= thickness < keys[i+1]:
                    lower_key, upper_key = keys[i], keys[i+1]
                    lower_value, upper_value = data[str(lower_key)], data[str(upper_key)]
                    data = linear_interpolation(lower_value, upper_value, lower_key, upper_key, thickness)

        # Create Return Value
        if height <= 500:
            raise ValueError("Slab depth must be greater than 500 for group 1")
        else:
            if group == 1:
                point_h = [0, -100, -300, -600, -height]
                temp_h = [data['T1_h'], data['T2_h'], data['T3_h'], data['T4_h'], 0]
                point_c = [0, -500, -height]
                temp_c = [data['T1_c'], 0, 0]
            else:
                point_h = [0, -500, -height]
                temp_h = [data['T1_h'], 0, 0]
                point_c = [0, -100, -height]
                temp_c = [data['T1_c'], 0, 0]
            
            inf_point, inf_temp_h, inf_temp_c = merge_and_interpolate(point_h, temp_h, point_c, temp_c)

    elif group == 3 or group == 4:
        # Slab depth must be provided
        if slabdepth is None or slabdepth < 0:
            raise ValueError("Slab depth must be provided as positive value for group 3 and 4")
        
        if thickness == "unsurfaced":
            data = data_group(group, 1)
            keys = sorted([int(key) for key in data.keys()])
            max_slab = max(keys)
            min_slab = min(keys)

            if slabdepth >= max_slab:
                return data[str(max_slab)]
            elif slabdepth <= min_slab:
                return data[str(min_slab)]
            else:
                for i  in range(len(keys) - 1):
                    if keys[i] <= slabdepth < keys[i+1]:
                        lower_key, upper_key = keys[i], keys[i+1]
                        lower_value, upper_value = data[str(lower_key)], data[str(upper_key)]
                        data = linear_interpolation(lower_value, upper_value, lower_key, upper_key, slabdepth)
                        break
        else:
            data = data_group(group, 2)
            keys = sorted([int(key) for key in data.keys()])
            max_slab = max(keys)
            min_slab = min(keys)

            if slabdepth >= max_slab:
                data = data[str(max_slab)]
            elif slabdepth <= min_slab:
                data = data[str(min_slab)]
            else:
                for i  in range(len(keys) - 1):
                    if keys[i] <= slabdepth < keys[i+1]:
                        lower_key, upper_key = keys[i], keys[i+1]
                        lower_value, upper_value = data[str(lower_key)], data[str(upper_key)]
                        data = {}
                        for param in lower_value.keys():
                            data[param] = {}
                            for sub_param in lower_value[param].keys():
                                lower_param_value = lower_value[param][sub_param]
                                upper_param_value = upper_value[param][sub_param]
                                data[param][sub_param] = lower_param_value + (upper_param_value - lower_param_value) * (
                                    (slabdepth - lower_key) / (upper_key - lower_key)
                                )
            
            keys = sorted([int(key) for key in data.keys()])
            max_thickness = max(keys)
            min_thickness = min(keys)
            
            if thickness >= max_thickness:
                return data[str(max_thickness)]
            elif thickness <= min_thickness:
                return data[str(min_thickness)]
            else:
                for i  in range(len(keys) - 1):
                    if keys[i] <= thickness < keys[i+1]:
                        lower_key, upper_key = keys[i], keys[i+1]
                        lower_value, upper_value = data[str(lower_key)], data[str(upper_key)]
                        data = linear_interpolation(lower_value, upper_value, lower_key, upper_key, thickness)
                        break
        
        if group == 3:
            if height - slabdepth < 400:
                raise ValueError("Height must be greater than slab depth + 400 for group 3")
            else:
                point_h = [0, -0.6*slabdepth, -slabdepth-400, -height]
                temp_h = [data['T1_h'], 4, 0, 0]
                point_c = [0, -0.6*slabdepth, -slabdepth, -slabdepth - 400, -height]
                temp_c = [data['T1_c'], 0, 0, -8, -8]

                inf_point, inf_temp_h, inf_temp_c = merge_and_interpolate(point_h, temp_h, point_c, temp_c)

        elif group == 4:
            ## For Heating
            # Basic Values
            h_temp = 0.3 * height

            # h1 and h2
            # h1 = 0.3h but <= 0.15m
            # h2 = 0.3h but >= 0.1m but <= 0.25m
            h1 = 0.3*height if 0.3*height <= 150 else 150
            h2 = 0.3*height if (0.3*height >= 100 and 0.3*height <= 250) else (250 if 0.3*height >= 250 else 100)
            
            # Valid height Check
            if height <= h1+h2:
                raise ValueError("Height must be greater than h1 + h2 for group 3 (heating)")

            # h3 defintions
            # h3 = 0.3h but <= (0.10m + surfacihng depth in metres) (for thin slabs, h3 is limited by h-h1-h2)
            slab = "Thick"
            if thickness == "unsurfaced" or thickness == "waterproofed":
                h3 = 0.3*height if 0.3*height <= 100 else 100
            else:
                h3 = 0.3*height if 0.3*height <= (100 + thickness) else (100 + thickness)
            
            if height - h1 - h2 <= h3:
                slab = "Thin"
                h3 = height - h1 - h2
            
            if slab == "Thick":
                point_h = [0, -h1, -h1-h2, -height + h3, -height]
                temp_h = [data['T1_h'], data['T2_h'], 0, 0, data['T3_h']]
            elif slab == "Thin":
                point_h = [0, -h1, -h1-h2, -height]
                temp_h = [data['T1_h'], data['T2_h'], 0, data['T3_h']]

            ## For Cooling
            #Basic Values
            h14 = 0.2*height if 0.2*height <= 250 else 250
            h23 = 0.25*height if 0.25*height <= 200 else 200

            point_c = [0, -h14, -h14-h23, -height+h14+h23, -height+h14, -height]
            temp_c = [data['T1_c'], data['T2_c'], 0, 0, data['T3_c'], data['T4_c']]
            
            inf_point, inf_temp_h, inf_temp_c = merge_and_interpolate(point_h, temp_h, point_c, temp_c)
    
    return inf_point, inf_temp_h, inf_temp_c, point_h, temp_h, point_c, temp_c



def steel_box(vSize, refSize):
    # Variable Initialization
    B1, B2, B3, B4, B5, B6, H, t1, t2, tw1, tw2 = vSize
    Top, Bot = refSize
    twx1 = tw1 * math.sqrt(H ** 2 + ((Bot + B4) - (Top + B1)) ** 2) / H
    twx2 = tw2 * math.sqrt(H ** 2 + ((Top + B1 + B2) - (Bot + B4 + B5)) ** 2) / H
    # Outer Cell - Left Side
    ycol = [0]
    zcol = [0]
    ycol.append(ycol[0] - B2 / 2 - B1)
    zcol.append(zcol[0])
    ycol.append(ycol[1])
    zcol.append(zcol[1] - t1)
    ycol.append(ycol[2] + B1 - twx1)
    zcol.append(zcol[2])
    ycol.append(-(Top + B1 + B2 / 2) + (Bot + B4 - twx1))
    zcol.append(zcol[3] - H)
    ycol.append(ycol[4] - B4 + twx1)
    zcol.append(zcol[4])
    ycol.append(ycol[5])
    zcol.append(zcol[5] - t2)
    ycol.append(ycol[6] + B4 + B5 / 2)
    zcol.append(zcol[6])
    # Outer Cell - Right Side
    ycor = [0]
    zcor = [0]
    ycor.append(ycor[0] + B2 / 2 + B3)
    zcor.append(zcor[0])
    ycor.append(ycor[1])
    zcor.append(zcor[1] - t1)
    ycor.append(ycor[2] - B3 + twx2)
    zcor.append(zcor[2])
    ycor.append(-(B2/2 + B1 + Top) + (Bot + B4 + B5 + twx2))
    zcor.append(zcor[3] - H)
    ycor.append(ycor[4] + B6 - twx2)
    zcor.append(zcor[4])
    ycor.append(ycor[5])
    zcor.append(zcor[5] - t2) 
    ycor.append(-(B2/2 + B1 + Top) + (Bot + B4 + B5/2))
    zcor.append(zcor[6])
    # Inner Cell - Left Side
    ycil = [0]
    zcil = [-t1]
    ycil.append(ycil[0] - B2 / 2)
    zcil.append(zcil[0])
    ycil.append(-(Top + B1 + B2 / 2) + (Bot + B4))
    zcil.append(zcil[1] - H)
    ycil.append(ycil[2] + B5 / 2)
    zcil.append(zcil[2])
    # Inner Cell - Right Side
    ycir = [0]
    zcir = [-t1]
    ycir.append(ycir[0] + B2 / 2)
    zcir.append(zcir[0])
    ycir.append(-(B2/2 + B1 + Top) + (Bot + B4 + B5))
    zcir.append(zcir[1] - H)
    ycir.append(ycir[2] - B5 / 2)
    zcir.append(zcir[2])
    # Reverse
    ycor.reverse()
    zcor.reverse()
    ycil.reverse()
    zcil.reverse()
    # Remove Origin
    ycor.pop(0)
    zcor.pop(0)
    ycil.pop(0)
    zcil.pop(0)
    # All Cell
    ycoAll = ycol + ycor
    zcoAll = zcol + zcor
    yciAll = ycir + ycil
    zciAll = zcir + zcil
    # Return
    outer = defaultdict(list)
    inner = defaultdict(list)
    comp = defaultdict(list)
    outer[0] = ycoAll
    outer[1] = zcoAll
    inner[0] = yciAll
    inner[1] = zciAll
    return outer, inner, comp

# Calculation of Section Geometry Properties
from collections import defaultdict

def section_calculator(outer, inner, slab, mat_girder=None, mat_slab=None) :

    # Find Centroid\
    girder_prop = girder_centroid(outer, inner)
    if mat_girder is None or mat_slab is None :
        compst_prop = composite_centroid(outer, inner, slab)
    else :
        compst_prop = composite_centroid(outer, inner, slab, mat_girder, mat_slab)
    # Grider moment of inertia
    girder_y_inertia = 0
    girder_z_inertia = 0
    girder_yz_inertia = 0
    for i in range(len(girder_prop["outer"])) :
        if i % 2 == 0 :
            girder_y_inertia += y_inertia_calc(girder_prop["outer"][i], girder_prop["outer"][i+1])
            girder_z_inertia += z_inertia_calc(girder_prop["outer"][i], girder_prop["outer"][i+1])
            girder_yz_inertia += yz_inertia_calc(girder_prop["outer"][i], girder_prop["outer"][i+1])
    for i in range(len(girder_prop["inner"])) :
        if i % 2 == 0 :
            girder_y_inertia += y_inertia_calc(girder_prop["inner"][i], girder_prop["inner"][i+1])
            girder_z_inertia += z_inertia_calc(girder_prop["inner"][i], girder_prop["inner"][i+1])
            girder_yz_inertia += yz_inertia_calc(girder_prop["inner"][i], girder_prop["inner"][i+1])
    # Composite moment of inertia
    compst_y_inertia = 0
    compst_z_inertia = 0
    compst_yz_inertia = 0
    for i in range(len(compst_prop["outer"])) :
        if i % 2 == 0 :
            compst_y_inertia += y_inertia_calc(compst_prop["outer"][i], compst_prop["outer"][i+1])
            compst_z_inertia += z_inertia_calc(compst_prop["outer"][i], compst_prop["outer"][i+1])
            compst_yz_inertia += yz_inertia_calc(compst_prop["outer"][i], compst_prop["outer"][i+1])
    for i in range(len(compst_prop["inner"])) :
        if i % 2 == 0 :
            compst_y_inertia += y_inertia_calc(compst_prop["inner"][i], compst_prop["inner"][i+1])
            compst_z_inertia += z_inertia_calc(compst_prop["inner"][i], compst_prop["inner"][i+1])
            compst_yz_inertia += yz_inertia_calc(compst_prop["inner"][i], compst_prop["inner"][i+1])
    for i in range(len(compst_prop["slab"])) :
        if i % 2 == 0 :
            compst_y_inertia += y_inertia_calc(compst_prop["slab"][i], compst_prop["slab"][i+1])*(mat_slab/mat_girder)
            compst_z_inertia += z_inertia_calc(compst_prop["slab"][i], compst_prop["slab"][i+1])*(mat_slab/mat_girder)
            compst_yz_inertia += yz_inertia_calc(compst_prop["slab"][i], compst_prop["slab"][i+1])*(mat_slab/mat_girder)
    section_properties = {
        "girder_area" : girder_prop["area"],
        "girder_y_cen" : girder_prop["y_cen"],
        "girder_z_cen" : girder_prop["z_cen"],
        "girder_y_inertia" : girder_y_inertia,
        "girder_z_inertia" : girder_z_inertia,
        "girder_yz_inertia" : girder_yz_inertia,
        "composite_area" : compst_prop["area"],
        "composite_y_cen" : compst_prop["y_cen"],
        "composite_z_cen" : compst_prop["z_cen"],
        "composite_y_inertia" : compst_y_inertia,
        "composite_z_inertia" : compst_z_inertia,
        "composite_yz_inertia" : compst_yz_inertia
    }
    return section_properties

def section_dimension(outer, inner, slab) :
    outer_y_max = None
    outer_y_min = None
    outer_z_max = None
    outer_z_min = None
    for key, value in outer.items() :
        if key % 2 != 0:
            if outer_z_max is None or max(value) > outer_z_max :
                outer_z_max = max(value)
            if outer_z_min is None or min(value) < outer_z_min :
                outer_z_min = min(value)
        else :
            if outer_y_max is None or max(value) > outer_y_max :
                outer_y_max = max(value)
            if outer_y_min is None or min(value) < outer_y_min :
                outer_y_min = min(value)
    slab_y_max = None
    slab_y_min = None
    slab_z_max = None
    slab_z_min = None
    for key, value in slab.items() :
        if key % 2 != 0:
            if slab_z_max is None or max(value) > slab_z_max :
                slab_z_max = max(value)
            if slab_z_min is None or min(value) < slab_z_min :
                slab_z_min = min(value)
        else :
            if slab_y_max is None or max(value) > slab_y_max :
                slab_y_max = max(value)
            if slab_y_min is None or min(value) < slab_y_min :
                slab_y_min = min(value)
    if slab == {}:
        total_height = outer_z_max - outer_z_min
        total_width = outer_y_max - outer_y_min
        slab_thick = 0
    else :
        total_height = max(outer_z_max, slab_z_max) - min(outer_z_min, slab_z_min)
        total_width = max(outer_y_max, slab_y_max) - min(outer_y_min, slab_y_min)
        slab_thick = slab_z_max - slab_z_min
    return {
        "height" : total_height,
        "width" : total_width,
        "slab_thick" : slab_thick
    }

def area_calc(yc, zc) :
    sum = 0
    if not yc or not zc:
        return 0.0
    else:
        for i in range(len(yc)-1):
            sum += yc[i] * zc[i+1] - yc[i+1] * zc[i]
        return sum/2

def y_cen_calc(yc, zc) :
    sum = 0
    if not yc or not zc:
        return 0.0
    else:
        for i in range(len(yc)-1):
            sum += (yc[i+1] + yc[i]) * (yc[i] * zc[i+1] - yc[i+1] * zc[i])
        area = area_calc(yc, zc)
        return sum/(6*area)

def z_cen_calc(yc, zc) :
    sum = 0
    if not yc or not zc:
        return 0.0
    else:
        for i in range(len(yc)-1):
            sum += (zc[i+1] + zc[i]) * (yc[i] * zc[i+1] - yc[i+1] * zc[i])
        area = area_calc(yc, zc)
        return sum/(6*area)

def z_inertia_calc(yc, zc) :
    sum = 0
    if not yc or not zc:
        return 0.0
    else:
        for i in range(len(yc)-1) :
            sum += (yc[i]**2 + yc[i] * yc[i+1] + yc[i+1]**2) * (yc[i] * zc[i+1] - yc[i+1] * zc[i])
        return sum/12

def y_inertia_calc(yc, zc) :
    sum = 0
    if not yc or not zc:
        return 0.0
    else:
        for i in range(len(yc)-1) :
            sum += (zc[i]**2 + zc[i] * zc[i+1] + zc[i+1]**2) * (yc[i] * zc[i+1] - yc[i+1] * zc[i])
        return sum/12

def yz_inertia_calc(yc, zc) :
    sum = 0
    if not yc or not zc:
        return 0.0
    else:
        for i in range(len(yc)-1) :
            sum += (yc[i] * zc[i+1] + 2 * yc[i] * zc[i] + 2 * yc[i+1] * zc[i+1] + yc[i+1] * zc[i]) * (yc[i] * zc[i+1] - yc[i+1] * zc[i])
        return sum/24

def girder_centroid(outer, inner) :
    area = []
    y_cen = []
    z_cen = []
    for i in range(int(len(outer)/2)) :
        area.append(area_calc(outer[i*2], outer[i*2+1]))
        y_cen.append(y_cen_calc(outer[i*2], outer[i*2+1]))
        z_cen.append(z_cen_calc(outer[i*2], outer[i*2+1]))
    for i in range(int(len(inner)/2)) :
        area.append(area_calc(inner[i*2], inner[i*2+1]))
        y_cen.append(y_cen_calc(inner[i*2], inner[i*2+1]))
        z_cen.append(z_cen_calc(inner[i*2], inner[i*2+1]))
    area_girder = sum(area)
    y_cen_girder = sum(y * area for y, area in zip(y_cen, area)) / area_girder
    z_cen_girder = sum(z * area for z, area in zip(z_cen, area)) / area_girder
    # Convert to centroid
    outer_converted = defaultdict(list)
    inner_converted = defaultdict(list)
    for i in range(len(outer)) :
        if i % 2 == 0 :
            outer_converted[i] = []
            for j in range(len(outer[i])) :
                outer_converted[i].append(outer[i][j] - y_cen_girder)
        else :
            outer_converted[i] = []
            for j in range(len(outer[i])) :
                outer_converted[i].append(outer[i][j] - z_cen_girder)
    for i in range(len(inner)) :
        if i % 2 == 0 :
            inner_converted[i] = []
            for j in range(len(inner[i])) :
                inner_converted[i].append(inner[i][j] - y_cen_girder)
        else :
            inner_converted[i] = []
            for j in range(len(inner[i])) :
                inner_converted[i].append(inner[i][j] - z_cen_girder)
    convert_properties = {
        "outer" : outer_converted,
        "inner" : inner_converted,
        "area" : area_girder,
        "y_cen" : y_cen_girder,
        "z_cen" : z_cen_girder
    }
    return convert_properties

def composite_centroid(outer, inner, slab, mat_girder=None, mat_slab=None) :
    area = []
    y_cen = []
    z_cen = []
    for i in range(int(len(outer)/2)) :
        area.append(area_calc(outer[i*2], outer[i*2+1]))
        y_cen.append(y_cen_calc(outer[i*2], outer[i*2+1]))
        z_cen.append(z_cen_calc(outer[i*2], outer[i*2+1]))
    outer_area = sum(area)
    outer_y_cen = sum(y * area for y, area in zip(y_cen, area)) / outer_area
    outer_z_cen = sum(z * area for z, area in zip(z_cen, area)) / outer_area
    area = []
    y_cen = []
    z_cen = []
    for i in range(int(len(inner)/2)) :
        area.append(area_calc(inner[i*2], inner[i*2+1]))
        y_cen.append(y_cen_calc(inner[i*2], inner[i*2+1]))
        z_cen.append(z_cen_calc(inner[i*2], inner[i*2+1]))
    inner_area = sum(area)
    if inner_area != 0:
        inner_y_cen = sum(y * area for y, area in zip(y_cen, area)) / inner_area
        inner_z_cen = sum(z * area for z, area in zip(z_cen, area)) / inner_area
    else:
        inner_y_cen = 0
        inner_z_cen = 0
    area = []
    y_cen = []
    z_cen = []
    for i in range(int(len(slab)/2)) :
        area.append(area_calc(slab[i*2], slab[i*2+1]))
        y_cen.append(y_cen_calc(slab[i*2], slab[i*2+1]))
        z_cen.append(z_cen_calc(slab[i*2], slab[i*2+1]))
    slab_area = sum(area)
    if slab_area != 0:
        slab_y_cen = sum(y * area for y, area in zip(y_cen, area)) / slab_area
        slab_z_cen = sum(z * area for z, area in zip(z_cen, area)) / slab_area
    else:
        slab_y_cen = 0
        slab_z_cen = 0

    if mat_girder is None or mat_slab is None :
        factor = 1
    else :
        factor = mat_slab / mat_girder
    Total_Area = outer_area + inner_area + slab_area * factor
    Total_y_cen = (outer_y_cen * outer_area + inner_y_cen * inner_area + slab_y_cen * slab_area * factor) / Total_Area
    Total_z_cen = (outer_z_cen * outer_area + inner_z_cen * inner_area + slab_z_cen * slab_area * factor) / Total_Area
    
    outer_converted = defaultdict(list)
    inner_converted = defaultdict(list)
    slab_converted = defaultdict(list)
    for i in range(len(outer)) :
        if i % 2 == 0 :
            outer_converted[i] = []
            for j in range(len(outer[i])) :
                outer_converted[i].append(outer[i][j] - Total_y_cen)
        else :
            outer_converted[i] = []
            for j in range(len(outer[i])) :
                outer_converted[i].append(outer[i][j] - Total_z_cen)
    for i in range(len(inner)) :
        if i % 2 == 0 :
            inner_converted[i] = []
            for j in range(len(inner[i])) :
                inner_converted[i].append(inner[i][j] - Total_y_cen)
        else :
            inner_converted[i] = []
            for j in range(len(inner[i])) :
                inner_converted[i].append(inner[i][j] - Total_z_cen)
    for i in range(len(slab)) :
        if i % 2 == 0 :
            slab_converted[i] = []
            for j in range(len(slab[i])) :
                slab_converted[i].append(slab[i][j] - Total_y_cen)
        else :
            slab_converted[i] = []
            for j in range(len(slab[i])) :
                slab_converted[i].append(slab[i][j] - Total_z_cen)
    convert_properties = {
        "outer" : outer_converted,
        "inner" : inner_converted,
        "slab" : slab_converted,
        "area" : Total_Area,
        "y_cen" : Total_y_cen,
        "z_cen" : Total_z_cen
    }
    return convert_properties

def section_calculator(outer, inner, slab, mat_girder=None, mat_slab=None) :
    # Find Centroid\
    girder_prop = girder_centroid(outer, inner)
    if mat_girder is None or mat_slab is None :
        compst_prop = composite_centroid(outer, inner, slab)
    else :
        compst_prop = composite_centroid(outer, inner, slab, mat_girder, mat_slab)
    # Grider moment of inertia
    girder_y_inertia = 0
    girder_z_inertia = 0
    girder_yz_inertia = 0
    for i in range(len(girder_prop["outer"])) :
        if i % 2 == 0 :
            girder_y_inertia += y_inertia_calc(girder_prop["outer"][i], girder_prop["outer"][i+1])
            girder_z_inertia += z_inertia_calc(girder_prop["outer"][i], girder_prop["outer"][i+1])
            girder_yz_inertia += yz_inertia_calc(girder_prop["outer"][i], girder_prop["outer"][i+1])
    for i in range(len(girder_prop["inner"])) :
        if i % 2 == 0 :
            girder_y_inertia += y_inertia_calc(girder_prop["inner"][i], girder_prop["inner"][i+1])
            girder_z_inertia += z_inertia_calc(girder_prop["inner"][i], girder_prop["inner"][i+1])
            girder_yz_inertia += yz_inertia_calc(girder_prop["inner"][i], girder_prop["inner"][i+1])
    # Composite moment of inertia
    compst_y_inertia = 0
    compst_z_inertia = 0
    compst_yz_inertia = 0
    for i in range(len(compst_prop["outer"])) :
        if i % 2 == 0 :
            compst_y_inertia += y_inertia_calc(compst_prop["outer"][i], compst_prop["outer"][i+1])
            compst_z_inertia += z_inertia_calc(compst_prop["outer"][i], compst_prop["outer"][i+1])
            compst_yz_inertia += yz_inertia_calc(compst_prop["outer"][i], compst_prop["outer"][i+1])
    for i in range(len(compst_prop["inner"])) :
        if i % 2 == 0 :
            compst_y_inertia += y_inertia_calc(compst_prop["inner"][i], compst_prop["inner"][i+1])
            compst_z_inertia += z_inertia_calc(compst_prop["inner"][i], compst_prop["inner"][i+1])
            compst_yz_inertia += yz_inertia_calc(compst_prop["inner"][i], compst_prop["inner"][i+1])
    for i in range(len(compst_prop["slab"])) :
        if i % 2 == 0 :
            compst_y_inertia += y_inertia_calc(compst_prop["slab"][i], compst_prop["slab"][i+1])*(mat_slab/mat_girder)
            compst_z_inertia += z_inertia_calc(compst_prop["slab"][i], compst_prop["slab"][i+1])*(mat_slab/mat_girder)
            compst_yz_inertia += yz_inertia_calc(compst_prop["slab"][i], compst_prop["slab"][i+1])*(mat_slab/mat_girder)
    section_properties = {
        "girder_area" : girder_prop["area"],
        "girder_y_cen" : girder_prop["y_cen"],
        "girder_z_cen" : girder_prop["z_cen"],
        "girder_y_inertia" : girder_y_inertia,
        "girder_z_inertia" : girder_z_inertia,
        "girder_yz_inertia" : girder_yz_inertia,
        "composite_area" : compst_prop["area"],
        "composite_y_cen" : compst_prop["y_cen"],
        "composite_z_cen" : compst_prop["z_cen"],
        "composite_y_inertia" : compst_y_inertia,
        "composite_z_inertia" : compst_z_inertia,
        "composite_yz_inertia" : compst_yz_inertia
    }
    return section_properties

def self_equilibrating_stress(outer, inner, slab, acg, acs, ecg, ecs, section_properties, section_dimension, inf_point, inf_temp_h, inf_temp_c):
    # print("girder thermal exapnsion coefficient =", acg)
    # print("girder elastic modulus =", ecg)
    # print("slab thermal exapnsion coefficient =", acs)
    # print("slab elastic modulus =", ecs)
    # print("section properties =", section_properties)
    # print("section dimension =", section_dimension)
    cog_z = section_properties["composite_z_cen"]
    cog_y = section_properties["composite_y_cen"]
    area = section_properties["composite_area"]
    iyy = section_properties["composite_y_inertia"]
    izz = section_properties["composite_z_inertia"]
    iyz = section_properties["composite_yz_inertia"]
    height_section = section_dimension["height"]
    e_ratio = ecs/ecg
    
    # y, z coordinates convert
    ymax, _, zmax, _ = maxmin_coordinates(outer, inner, slab)
    convert_z_cog = zmax - cog_z
    convert_y_cog = ymax - cog_y

    # Convert Y, Z
    outer_convert = defaultdict(list)
    inner_convert = defaultdict(list)
    slab_convert = defaultdict(list)

    if outer:
        for key, values in outer.items():
            if key % 2 == 0:
                outer_convert[key] = [i - ymax for i in values]
            else:
                outer_convert[key] = [i - zmax for i in values]
    if inner:
        for key, values in inner.items():
            if key % 2 == 0:
                inner_convert[key] = [i - ymax for i in values]
            else:
                inner_convert[key] = [i - zmax for i in values]
    if slab:
        for key, values in slab.items():
            if key % 2 == 0:
                slab_convert[key] = [i - ymax for i in values]
            else:
                slab_convert[key] = [i - zmax for i in values]

    # Add convert cog
    if outer :
        for i in range(int(len(outer)/2)):
            y_values = outer_convert[i*2]
            z_values = outer_convert[i*2+1]            
            new_y_values = []
            new_z_values = []

            for j in range(len(y_values)-1):
                if z_values[j] < -convert_z_cog < z_values[j + 1] or z_values[j] > -convert_z_cog > z_values[j + 1]:
                    y_value = (-convert_z_cog - z_values[j])*(y_values[j + 1] - y_values[j])/(z_values[j + 1]-z_values[j]) + y_values[j]
                    new_y_values.extend([y_values[j], y_value])
                    new_z_values.extend([z_values[j], -convert_z_cog])
                else:
                    new_y_values.append(y_values[j])
                    new_z_values.append(z_values[j])
            new_y_values.append(y_values[-1])
            new_z_values.append(z_values[-1])
            
            outer_convert[i*2] = new_y_values
            outer_convert[i*2+1] = new_z_values
    if inner :
        for i in range(int(len(inner)/2)):
            y_values = inner_convert[i*2]
            z_values = inner_convert[i*2+1]            
            new_y_values = []
            new_z_values = []

            for j in range(len(y_values)-1):
                if z_values[j] < -convert_z_cog < z_values[j + 1] or z_values[j] > -convert_z_cog > z_values[j + 1]:
                    y_value = (-convert_z_cog - z_values[j])*(y_values[j + 1] - y_values[j])/(z_values[j + 1]-z_values[j]) + y_values[j]
                    new_y_values.extend([y_values[j], y_value])
                    new_z_values.extend([z_values[j], -convert_z_cog])
                else:
                    new_y_values.append(y_values[j])
                    new_z_values.append(z_values[j])
            new_y_values.append(y_values[-1])
            new_z_values.append(z_values[-1])

            inner_convert[i*2] = new_y_values
            inner_convert[i*2+1] = new_z_values
    if slab :
        for i in range(int(len(slab)/2)):
            y_values = slab_convert[i*2]
            z_values = slab_convert[i*2+1]
            new_y_values = []
            new_z_values = []

            for j in range(len(y_values)-1):
                if z_values[j] < -convert_z_cog < z_values[j + 1] or z_values[j] > -convert_z_cog > z_values[j + 1]:
                    y_value = (-convert_z_cog - z_values[j])*(y_values[j + 1] - y_values[j])/(z_values[j + 1]-z_values[j]) + y_values[j]
                    new_y_values.extend([y_values[j], y_value])
                    new_z_values.extend([z_values[j], -convert_z_cog])
                else:
                    new_y_values.append(y_values[j])
                    new_z_values.append(z_values[j])
            new_y_values.append(y_values[-1])
            new_z_values.append(z_values[-1])

            slab_convert[i*2] = new_y_values
            slab_convert[i*2+1] = new_z_values

    # result.table_print(outer, outer_convert, tabletitle='Outer', pricision = 3)
    # result.table_print(inner, inner_convert, tabletitle='Inner', pricision = 3)
    # result.table_print(slab, slab_convert, tabletitle='Slab', pricision = 3)

    # Equivalent Force
    equ_force_H = []
    equ_force_C = []
    outer_heating = defaultdict(list)
    outer_cooling = defaultdict(list)
    inner_heating = defaultdict(list)
    inner_cooling = defaultdict(list)
    slab_heating = defaultdict(list)
    slab_cooling = defaultdict(list)

    if outer:
        for i in range(int(len(outer_convert)/2)):
            #Heating Cases
            merged_y = merge_yc(outer_convert[i*2], outer_convert[i*2+1], inf_point)
            merged_z = merge_zc(outer_convert[i*2+1], inf_point)
            merged_t = merge_tc(merged_z, inf_point, inf_temp_h)
            equ_force_H += equivalent_force(merged_y, merged_z, merged_t, acg, ecg, convert_z_cog)
            outer_heating[i] = [merged_y, merged_z, merged_t]
            #Cooling Cases
            merged_y = merge_yc(outer_convert[i*2], outer_convert[i*2+1], inf_point)
            merged_z = merge_zc(outer_convert[i*2+1], inf_point)
            merged_t = merge_tc(merged_z, inf_point, inf_temp_c)
            equ_force_C += equivalent_force(merged_y, merged_z, merged_t, acg, ecg, convert_z_cog)
            outer_cooling[i] = [merged_y, merged_z, merged_t]
    if inner:
        for i in range(int(len(inner_convert)/2)):
            #Heating Cases
            merged_y = merge_yc(inner_convert[i*2], inner_convert[i*2+1], inf_point)
            merged_z = merge_zc(inner_convert[i*2+1], inf_point)
            merged_t = merge_tc(merged_z, inf_point, inf_temp_h)
            equ_force_H += equivalent_force(merged_y, merged_z, merged_t, acg, ecg, convert_z_cog)
            inner_heating[i] = [merged_y, merged_z, merged_t]
            #Cooling Cases
            merged_y = merge_yc(inner_convert[i*2], inner_convert[i*2+1], inf_point)
            merged_z = merge_zc(inner_convert[i*2+1], inf_point)
            merged_t = merge_tc(merged_z, inf_point, inf_temp_c)
            equ_force_C += equivalent_force(merged_y, merged_z, merged_t, acg, ecg, convert_z_cog)
            inner_cooling[i] = [merged_y, merged_z, merged_t]
    if slab:
        for i in range(int(len(slab_convert)/2)):
            #Heating Cases
            merged_y = merge_yc(slab_convert[i*2], slab_convert[i*2+1], inf_point)
            merged_z = merge_zc(slab_convert[i*2+1], inf_point)
            merged_t = merge_tc(merged_z, inf_point, inf_temp_h)
            equ_force_H += equivalent_force(merged_y, merged_z, merged_t, acs, ecs, convert_z_cog)
            slab_heating[i] = [merged_y, merged_z, merged_t]
            #Cooling Cases
            merged_y = merge_yc(slab_convert[i*2], slab_convert[i*2+1], inf_point)
            merged_z = merge_zc(slab_convert[i*2+1], inf_point)
            merged_t = merge_tc(merged_z, inf_point, inf_temp_c)
            equ_force_C += equivalent_force(merged_y, merged_z, merged_t, acs, ecs, convert_z_cog)
            slab_cooling[i] = [merged_y, merged_z, merged_t]

    #Equivalent Forces
    sum_normal_h = 0
    sum_moment_h = 0
    for i in range(int(len(equ_force_H)/2)) :
        sum_normal_h += equ_force_H[i*2]
        sum_moment_h += equ_force_H[i*2+1]
    sum_normal_c = 0
    sum_moment_c = 0
    for i in range(int(len(equ_force_C)/2)) :
        sum_normal_c += equ_force_C[i*2]
        sum_moment_c += equ_force_C[i*2+1]

    # Equivalent Stress
    sigma_outer_heating = []
    sigma_outer_cooling = []
    sigma_inner_heating = []
    sigma_inner_cooling = []
    sigma_slab_heating = []
    sigma_slab_cooling = []

    for i in range(len(outer_heating)):
        eq_stress = equivalent_stress(
                sum_normal_h,
                sum_moment_h,
                outer_heating[i][1],
                outer_heating[i][2],
                acg,
                ecg,
                convert_z_cog,
                area,
                iyy
            )
        sigma_outer_heating.append({
            "y" : outer_heating[i][0],
            "z" : outer_heating[i][1],
            "t" : outer_heating[i][2],
            "s" : eq_stress
        })
    
    for i in range(len(outer_cooling)):
        eq_stress = equivalent_stress(
                sum_normal_c,
                sum_moment_c,
                outer_cooling[i][1],
                outer_cooling[i][2],
                acg,
                ecg,
                convert_z_cog,
                area,
                iyy
            )
        sigma_outer_cooling.append({
            "y" : outer_cooling[i][0],
            "z" : outer_cooling[i][1],
            "t" : outer_cooling[i][2],
            "s" : eq_stress
        })

    for i in range(len(inner_heating)):
        eq_stress = equivalent_stress(
                sum_normal_h,
                sum_moment_h,
                inner_heating[i][1],
                inner_heating[i][2],
                acg,
                ecg,
                convert_z_cog,
                area,
                iyy
            )
        sigma_inner_heating.append({
            "y" : inner_heating[i][0],
            "z" : inner_heating[i][1],
            "t" : inner_heating[i][2],
            "s" : eq_stress
        })

    for i in range(len(inner_cooling)):
        eq_stress = equivalent_stress(
                sum_normal_c,
                sum_moment_c,
                inner_cooling[i][1],
                inner_cooling[i][2],
                acg,
                ecg,
                convert_z_cog,
                area,
                iyy
            )
        sigma_inner_cooling.append({
            "y" : inner_cooling[i][0],
            "z" : inner_cooling[i][1],
            "t" : inner_cooling[i][2],
            "s" : eq_stress
        })

    for i in range(len(slab_heating)):
        eq_stress = equivalent_stress(
                sum_normal_h,
                sum_moment_h,
                slab_heating[i][1],
                slab_heating[i][2],
                acs,
                ecs,
                convert_z_cog,
                area,
                iyy,
                e_ratio
            )
        sigma_slab_heating.append({
            "y" : slab_heating[i][0],
            "z" : slab_heating[i][1],
            "t" : slab_heating[i][2],
            "s" : eq_stress
        })

    for i in range(len(slab_cooling)):
        eq_stress = equivalent_stress(
                sum_normal_c,
                sum_moment_c,
                slab_cooling[i][1],
                slab_cooling[i][2],
                acs,
                ecs,
                convert_z_cog,
                area,
                iyy,
                e_ratio
            )
        sigma_slab_cooling.append({
            "y" : slab_cooling[i][0],
            "z" : slab_cooling[i][1],
            "t" : slab_cooling[i][2],
            "s" : eq_stress
        })

    return sigma_outer_heating, sigma_outer_cooling, sigma_inner_heating, sigma_inner_cooling, sigma_slab_heating, sigma_slab_cooling

def equivalent_stress(Nx, My, zc, dt, ac, ec, cog, area, iyy, e_ratio=1) :
    sigma_t = []
    sigma_r = []
    sigma_s = []
    sigma_n = []
    sigma_m = []
    for i in range(len(zc)) :
        sigma_n.append(Nx/area*e_ratio)
        sigma_m.append(My*(cog-abs(zc[i]))/iyy*e_ratio)
        sigma_t.append(dt[i]*ac*ec*-1)
        sigma_r.append(Nx/area*e_ratio + My*(cog-abs(zc[i]))/iyy*e_ratio)
        sigma_s.append(sigma_t[i]+sigma_r[i])
    return sigma_s

def equivalent_stress_advanced(Nx, My, yc, zc, dt, ac, ec, cog_y, cog_z, area, iyy, izz, ixy, e_ratio=1) :
    sigma_t = []
    sigma_r = []
    sigma_s = []
    sigma_n = []
    sigma_mz = []
    sigma_my = []
    for i in range(len(zc)) :
        sigma_n.append(Nx/area*e_ratio)
        sigma_mz.append((My*ixy)*(cog_y-abs(yc[i]))/(iyy*izz-ixy**2))
        sigma_my.append((My*izz)*(cog_z-abs(zc[i]))/(iyy*izz-ixy**2))
        sigma_t.append(dt[i]*ac*ec*-1)
        sigma_r.append(Nx/area*e_ratio + ((My*ixy)*(cog_y-abs(yc[i]))+(My*izz)*(cog_z-abs(zc[i])))/(iyy*izz-ixy**2))
        sigma_s.append(sigma_t[i]+sigma_r[i])
    return sigma_t, sigma_r, sigma_s

def equivalent_force(yc, zc, dt, ac, ec, cog, e_ratio=1) :
    sum_normal = 0
    sum_moment = 0
    b1 = 0
    b2 = 0
    d1 = 0
    d2 = 0
    t1 = 0
    t2 = 0
    for i in range(len(yc)-1) :
        if zc[i+1] == zc[i] :
            b1 = 0
            b2 = 0
            d1 = 0
            d2 = 0
            t1 = 0
            t2 = 0
        else :
            b1 = abs(yc[i])
            b2 = abs(yc[i+1])
            d1 = abs(zc[i])
            d2 = abs(zc[i+1])
            t1 = dt[i]
            t2 = dt[i+1]
        sum_normal += ac*ec*-(d1-d2)*((2*b1+b2)*t1+(b1+2*b2)*t2)/6*e_ratio
        sum_moment += ac*ec*(d1**2*((3*b1+b2)*t1+(b1+b2)*t2)-2*d1*(d2*(b1*t1-b2*t2)+cog*((2*b1+b2)*t1+(b1+2*b2)*t2))-d2*(d2*((b1+b2)*t1+(b1+3*b2)*t2)-2*cog*((2*b1+b2)*t1+(b1+2*b2)*t2)))/12*e_ratio
    return sum_normal, sum_moment

def merge_yc(yc, zc, zt):
    added_vertex = 0
    db = 0.0
    merge_yc = yc.copy()

    for i in range(len(zc) - 1):
        if zc[i] > zc[i + 1]:
            for j in range(len(zt)):
                if max(zc[i], zc[i + 1]) > zt[j] and min(zc[i], zc[i + 1]) < zt[j]:
                    db = (zt[j] - zc[i]) * (yc[i + 1] - yc[i]) / (zc[i + 1] - zc[i]) + yc[i]
                    merge_yc.insert(i + 1 + added_vertex, db)
                    added_vertex += 1
        elif zc[i] < zc[i + 1]:
            for j in range(len(zt) - 1, -1, -1):
                if max(zc[i], zc[i + 1]) > zt[j] and min(zc[i], zc[i + 1]) < zt[j]:
                    db = (zt[j] - zc[i]) * (yc[i + 1] - yc[i]) / (zc[i + 1] - zc[i]) + yc[i]
                    merge_yc.insert(i + 1 + added_vertex, db)
                    added_vertex += 1

    return merge_yc

def merge_zc(zc, zt):
    added_vertex = 0
    merge_zc = zc.copy()

    for i in range(len(zc) - 1):
        if zc[i] > zc[i + 1]:
            for j in range(len(zt)):
                if max(zc[i], zc[i + 1]) > zt[j] and min(zc[i], zc[i + 1]) < zt[j]:
                    merge_zc.insert(i + 1 + added_vertex, zt[j])
                    added_vertex += 1
        elif zc[i] < zc[i + 1]:
            for j in range(len(zt) - 1, -1, -1):
                if max(zc[i], zc[i + 1]) > zt[j] and min(zc[i], zc[i + 1]) < zt[j]:
                    merge_zc.insert(i + 1 + added_vertex, zt[j])
                    added_vertex += 1

    return merge_zc

def merge_tc(zc, zt, dt):
    ycdt = np.zeros(len(zc), dtype=float)

    for i in range(len(zc)):
        for j in range(len(zt) - 1):
            if zt[j] >= zc[i] >= zt[j + 1]:
                if dt[j] == dt[j + 1]:
                    ycdt[i] = dt[j]
                else:
                    ycdt[i] = (dt[j + 1] - dt[j]) / (zt[j + 1] - zt[j]) * (zc[i] - zt[j]) + dt[j]

    return ycdt.tolist()

def maxmin_coordinates(outer, inner, slab) :
    # Find max and min y, z coordinates
    ymax = float('-inf')
    ymin = float('inf')
    zmax = float('-inf')
    zmin = float('inf')
    if outer:
        for key, values in outer.items():
            if key % 2 == 0:
                outer_ymax = max(values, default=float('-inf'))
                outer_ymin = min(values, default=float('inf'))
            else:
                outer_zmax = max(values, default=float('-inf'))
                outer_zmin = min(values, default=float('inf'))
        ymax = max(ymax, outer_ymax)
        ymin = min(ymin, outer_ymin)
        zmax = max(zmax, outer_zmax)
        zmin = min(zmin, outer_zmin)
    if inner:
        for key, values in inner.items():
            if key % 2 == 0:
                inner_ymax = max(values, default=float('-inf'))
                inner_ymin = min(values, default=float('inf'))
            else:
                inner_zmax = max(values, default=float('-inf'))
                inner_zmin = min(values, default=float('inf'))
        ymax = max(ymax, inner_ymax)
        ymin = min(ymin, inner_ymin)
        zmax = max(zmax, inner_zmax)
        zmin = min(zmin, inner_zmin)
    if slab:
        for key, values in slab.items():
            if key % 2 == 0:
                slab_ymax = max(values, default=float('-inf'))
                slab_ymin = min(values, default=float('inf'))
            else:
                slab_zmax = max(values, default=float('-inf'))
                slab_zmin = min(values, default=float('inf'))
        ymax = max(ymax, slab_ymax)
        ymin = min(ymin, slab_ymin)
        zmax = max(zmax, slab_zmax)
        zmin = min(zmin, slab_zmin)
    return ymax, ymin, zmax, zmin

# Draw Example Section of Steel Box

# define the dimension -> from G2 and S5, S10, S11
# group : Number (1, 2, 3, 4) -> from G1
#   1a - Steel Decks -> 1
#   1b - Steel Decks -> 2
#   2 - Composite Decks -> 3
#   3 - Concrete Decks -> 4
# surf_thick : String (unsurfaced, waterproofed(for group 3 and 4)) or Number(mm) -> from G3
# slab_depth : Number(mm) (for group 3 and 4, sec_dim['slab_thick']) -> by Calcualtions
# sect_height : Number(mm) (sec_dim['height']) -> by Calculations and print to G4
# Material Properties
#   g_thermal : Number (/°C)   -> from S9
#   s_thermal : Number (/°C)     -> from S7
#   g_elastic : Number (MPa)   -> from S8
#   s_elastic : Number (MPa)     -> from S6
class SteelBoxSection(MBaseModel):
    """
    SteelBoxSection
    """
    top: Length = dataclass_field(default=Length(value=0.0, unit=enUnitLength.MM), description="Top")
    bot: Length = dataclass_field(default=Length(value=100.0, unit=enUnitLength.MM), description="Bot")
    b1: Length = dataclass_field(default=Length(value=150.0, unit=enUnitLength.MM), description="B1")
    b2: Length = dataclass_field(default=Length(value=900.0, unit=enUnitLength.MM), description="B2")
    b3: Length = dataclass_field(default=Length(value=150.0, unit=enUnitLength.MM), description="B3")
    b4: Length = dataclass_field(default=Length(value=150.0, unit=enUnitLength.MM), description="B4")
    b5: Length = dataclass_field(default=Length(value=700.0, unit=enUnitLength.MM), description="B5")
    b6: Length = dataclass_field(default=Length(value=150.0, unit=enUnitLength.MM), description="B6")
    h: Length = dataclass_field(default=Length(value=1000.0, unit=enUnitLength.MM), description="H")
    t1: Length = dataclass_field(default=Length(value=25.0, unit=enUnitLength.MM), description="T1")
    t2: Length = dataclass_field(default=Length(value=25.0, unit=enUnitLength.MM), description="T2")
    tw1: Length = dataclass_field(default=Length(value=30.0, unit=enUnitLength.MM), description="Tw1")
    tw2: Length = dataclass_field(default=Length(value=30.0, unit=enUnitLength.MM), description="Tw2")

    class Config(MBaseModel.Config):
        title = "SteelBoxSection"

class GirderMaterials(MBaseModel):
    """
    GirderMaterials
    """
    E: Stress = dataclass_field(default=Stress(value=210000.0, unit=enUnitStress.MPa), description="Elastic Modulus")
    thermal: Temperature = dataclass_field(default=Temperature(value=12E-6, unit=enUnitTemperature.Celsius), description="Thermal Expansion")

class ResultThermal(MBaseModel):
    """
    Result Thermal
    """
    y: list[Length] = dataclass_field(default_factory=list, description="Y")
    z: list[Length] = dataclass_field(default_factory=list, description="Z")
    temp: list[Temperature] = dataclass_field(default_factory=list, description="Temperature")
    stress: list[Stress] = dataclass_field(default_factory=list, description="Stress")

class ResultNonlinearTemperatureEffect(MBaseModel):
    """
    Result Nonlinear Temperature Effect
    """
    heating: ResultThermal = dataclass_field(default_factory=ResultThermal, description="Heating")
    cooling: ResultThermal = dataclass_field(default_factory=ResultThermal, description="Cooling")
    outer: list[Point] = dataclass_field(default_factory=list[Point], description="Outer polygon")
    inner: list[list[Point]] = dataclass_field(default_factory=list[Point], description="Inner polygon")
    temp_heating: list[Point] = dataclass_field(default_factory=list[Point], description="Temperature Heating")
    temp_cooling: list[Point] = dataclass_field(default_factory=list[Point], description="Temperature Cooling")


@auto_schema(title="Steel Box Section Calculation", description="Calculate the temperature effect on steel box section")
def calc_steel_box(sect: SteelBoxSection, matl: GirderMaterials) -> ResultNonlinearTemperatureEffect:
    # Dimension
    refSize = [sect.top.value, sect.bot.value]
    vSize = [sect.b1.value, sect.b2.value, sect.b3.value, sect.b4.value, sect.b5.value, sect.b6.value, sect.h.value, sect.t1.value, sect.t2.value, sect.tw1.value, sect.tw2.value]
    # refSize = [0, 100]
    # vSize = [150, 900, 150, 150, 700, 150, 1000, 25, 25, 30, 30]

    # Calculate the section cooridnates
    outer, inner, slab = steel_box(vSize, refSize)

    # Group
    group = 1

    # Material Properties (if slab properties are not provided, take the girder properties)
    g_thermal = matl.thermal.value
    s_thermal = g_thermal
    g_elastic = matl.E.value
    s_elastic = g_elastic

    # Calculate the section properties
    sec_prop = section_calculator(outer, inner, slab, g_elastic, s_elastic)
    sec_dim = section_dimension(outer, inner, slab)

    surf_thick = 30
    slab_depth = sec_dim["slab_thick"]
    sect_height = sec_dim["height"]

    # print section calculation results
    # preprocess_result_print(outer, inner, slab, sec_prop, sec_dim)

    # Calculate the temperature distribution
    inf_point, inf_temp_h, inf_temp_c, point_h, temp_h, point_c, temp_c = interpolate_temperature(group, sect_height, surf_thick, slab_depth)

    # print temperature distribution results
    # plot_graphs("Steel Box", outer, inner, slab, point_h, temp_h, point_c, temp_c)

    # Calculate the self equilibrating stress
    self_eq_stress = self_equilibrating_stress(outer, inner, slab, g_thermal, s_thermal, g_elastic, s_elastic, sec_prop, sec_dim, inf_point, inf_temp_h, inf_temp_c)
    out_points = [Point(x=Length(value=xv, unit=enUnitLength.MM), y=Length(value=yv, unit=enUnitLength.MM)) for xv, yv in zip(outer[0], outer[1])]
    inner_points = [[Point(x=Length(value=xv, unit=enUnitLength.MM), y=Length(value=yv, unit=enUnitLength.MM)) for xv, yv in zip(inner[0], inner[1])]]
    heating = ResultThermal(y=list(Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[0][0]['y']), z=list(Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[0][0]['z']),
                            temp=list(Temperature(value=xv, unit=enUnitTemperature.Celsius) for xv in self_eq_stress[0][0]['t']), stress=list(Stress(value=xv, unit=enUnitStress.MPa) for xv in self_eq_stress[0][0]['s']))
    cooling = ResultThermal(y=list(Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[1][0]['y']), z=list(Length(value=xv, unit=enUnitLength.MM) for xv in self_eq_stress[1][0]['z']),
                            temp=list(Temperature(value=xv, unit=enUnitTemperature.Celsius) for xv in self_eq_stress[1][0]['t']), stress=list(Stress(value=xv, unit=enUnitStress.MPa) for xv in self_eq_stress[1][0]['s']))
    return ResultNonlinearTemperatureEffect(heating=heating, cooling=cooling, outer=out_points, inner=inner_points,
                                            temp_heating=[Point(x=Length(value=xv, unit=enUnitLength.MM), y=Length(value=yv, unit=enUnitLength.MM)) for xv, yv in zip(temp_h, point_h)], temp_cooling=[Point(x=Length(value=xv, unit=enUnitLength.MM), y=Length(value=yv, unit=enUnitLength.MM)) for xv, yv in zip(temp_c, point_c)])

# res = calc_steel_box(SteelBoxSection(), GirderMaterials())
# print(res)