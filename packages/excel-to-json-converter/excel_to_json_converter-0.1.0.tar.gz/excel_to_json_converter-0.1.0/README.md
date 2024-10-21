# Excel to JSON Converter

A simple library to convert Excel sheets to JSON format by Ksr小熙.

## Installation

```
from excel_to_json_converter import ExcelToJsonConverter
```

### Usage

To use the library, follow these steps:

```
Import the library:

from excel_to_json_converter import ExcelToJsonConverter  # 导入库
Create a converter instance:

converter = ExcelToJsonConverter('data.xlsx', sheet_name='Sheet1')  # 创建转换器实例
Generate JSON output:

json_output = converter.generate_json(indent=2)  # 生成 JSON 输出
Print the result:

print(json_output)  # 打印结果
Parameters
file_path: The path to the Excel file to be converted.
sheet_name: The name of the Excel sheet to read (optional).
indent: The level of indentation for the JSON output. This can be:
None: For compact format.
An integer: Specifies the number of spaces for indentation.
"unspaced": For output without spaces.
```

#### Example

Here is a complete example:

```
from excel_to_json_converter import ExcelToJsonConverter

# Create a converter instance
converter = ExcelToJsonConverter('data.xlsx', sheet_name='Sheet1')

# Generate JSON output
json_output = converter.generate_json(indent=2)

# Print the result
print(json_output)
```