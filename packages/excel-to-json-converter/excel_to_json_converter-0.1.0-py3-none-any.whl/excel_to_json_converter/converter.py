# excel_to_json_converter/converter.py

import pandas as pd
import json

class ExcelToJsonConverter:
    def __init__(self, file_path, sheet_name=None):
        self.file_path = file_path
        self.sheet_name = sheet_name
        self.input_data = self.read_excel_to_input_data()

    def read_excel_to_input_data(self):
        if self.sheet_name is not None:
            df = pd.read_excel(self.file_path, sheet_name=self.sheet_name)
        else:
            df = pd.read_excel(self.file_path)

        input_data = {}
        
        for col in df.columns:
            key = col
            values = []
            for value in df[col]:
                if pd.isna(value):
                    values.append(None)
                else:
                    values.append(value)

            input_data[key] = values

        return input_data

    def generate_json(self, indent=None):
        result = []
        for i in range(len(self.input_data["name"])):
            obj = {key: value[i] for key, value in self.input_data.items()}
            result.append(obj)

        if isinstance(indent, int):
            return json.dumps(result, indent=indent)
        if indent == "unspaced":
            return json.dumps(result, separators=(',', ':'))
        return json.dumps(result)
