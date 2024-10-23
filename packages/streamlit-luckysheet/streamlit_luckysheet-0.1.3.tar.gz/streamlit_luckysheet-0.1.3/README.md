# streamlit-luckysheet

2024 Aug 18 First Ever Streamlit luckysheet. Credit To TAN YIHAO

## Installation instructions

```sh
pip install streamlit-luckysheet
```

## Usage instructions

```python
import streamlit as st
from streamlit_luckysheet import streamlit_luckysheet
import base64
import os

st.set_page_config(layout="wide")
st.subheader("Component with constant args")

name = "Streamlit_Excelsheet"
key = "Streamlit_Excelsheet"
height = 1000
excel_path = r".\excel\Employee Sample Data.xlsx"
output_path = r".\excel\testing.xlsx"

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

encodedFile = excel_to_file(excel_path)

return_result = streamlit_luckysheet(name=name, height=height, encodedFile=encodedFile, key=key, default=[])
if isinstance(return_result, dict) and "incoming_save" in return_result:
    if return_result["incoming_save"]:
        base64_string = return_result["incoming_save"]
        base64_to_excel(base64_string, output_path)




```
