import streamlit as st
from streamlit_luckysheet import streamlit_luckysheet
import base64
import os
import time

st.set_page_config(layout="wide")
st.subheader("Component with constant args")

name = "Streamlit_Excelsheet"
key = "Streamlit_Excelsheet"
height = 1000
# excel_path = r".\excel\Employee Sample Data_Rev2.xlsx"
excel_path = r".\excel\SampleDocs-SampleXLSFile_6800kb.xlsx" 
output_path = r".\excel\Config_Test_Output.xlsx"

# template_working
# Unuse empty row will affect the performance.    | Result
# Speed 400kRow9Column.xlsx 25,430 KB             | Time out
# Speed 400kRow9Column_Reduce.xlsx 20,129 KB      | Time out @ 2 minutes
# Speed 200kRow9Column.xlsx 15,680 kB             | 1min 04:68
# Speed 100kRow9Column.xlsx 10,806 kB             | 31.72 second
# Speed 50kRow9Column.xlsx 3,192 kB               | 16.33 second

# Luckyexcel Simulation
# Unuse empty row will affect the performance.    | Result
# Speed 400kRow9Column.xlsx 25,430 KB             | Time out
# Speed 400kRow9Column_Reduce.xlsx 20,129 KB      | Time out @ 1:53.94
# Speed 200kRow9Column.xlsx 15,680 kB             | 1min 03.30
# Speed 100kRow9Column.xlsx 10,806 kB             | 30.67
# Speed 50kRow9Column.xlsx 3,192 kB               | 16.12 


showtoolbarConfig = {
        "save": True,
        "download": False,
        "undoRedo": True,
        "paintFormat": True,
        "currencyFormat": False,
        "percentageFormat": False,
        "numberDecrease": False,
        "numberIncrease": False,
        "moreFormats": False,
        "font": True,
        "fontSize": True,
        "bold": True,
        "italic": True,
        "strikethrough": True,
        "underline": True,
        "textColor": True,
        "fillColor": True,
        "border": True,
        "mergeCell": True,
        "horizontalAlignMode": True,
        "verticalAlignMode": True,
        "textWrapMode": True,
        "textRotateMode": True,
        "image": False,
        "link": False,
        "chart": False,
        "postil": False,
        "pivotTable": False,
        "function": False,
        "frozenMode": False,
        "sortAndFilter": False,
        "conditionalFormat": False,
        "dataVerification": False,
        "splitColumn": False,
        "screenshot": False,
        "findAndReplace": False,
        "protection": False,
        "print": False,
        "exportXlsx": False,
      }

def excel_to_file(path):
    try:
        if not os.path.exists(path):
            return ""
        with open(path, 'rb') as file:
            file_data = file.read() 
            if file_data:
                return base64.b64encode(file_data).decode('utf-8')
            else:
                st.warning("File is empty or could not be read.")
                return ""
    except Exception as e:
        st.warning(f"An error occurred while processing the file: {e}")
        return ""

def excel_file(path):
    try:
        if not os.path.exists(path):
            return ""
        with open(path, 'rb') as file:
            file_data = file.read()     
            if file_data:
                return file_data
            else:
                st.warning("File is empty or could not be read.")
                return 
            
    except Exception as e:
        st.warning(f"An error occurred while processing the file: {e}")
        return ""

    
def base64_to_excel(base64_string, output_path):
    try:
        output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        file_data = base64.b64decode(base64_string)
        with open(output_path, 'wb') as file:
            file.write(file_data)
        st.success(f"Excel file successfully created at: {output_path}")

    except Exception as e:
        st.warning(f"An error occurred while converting to Excel file: {e}")

with st.spinner():
    #encodedFile = excel_to_file(excel_path)
    file = excel_file(excel_path)
    time.sleep(1)
    #st.warning(encodedFile)

return_result = streamlit_luckysheet(name=name, height=height, file=file, showtoolbarConfig=showtoolbarConfig, key=key, default=[])
if isinstance(return_result, dict) and "incoming_save" in return_result:
    if return_result["incoming_save"]:
        base64_string = return_result["incoming_save"]  
        base64_to_excel(base64_string, output_path)  


