intro_text = """Welcome to the Financial Evaluator app. This app will provide you an overview of your finances.
In order to make it run we need to set up some things first. Please follow the instructions below
"""

load_file_title = """### 1. Load your CSV file """


format_file_title = """### 2. Define the format of your file"""
format_file_text = """ In order to be able to read and process your data we need to know how it is structured. Please answer the
following questions"""

csv_separator_extra_text = """
CSV files are text files that contain data. This data is organized in columns and rows. 
The columns are differentiated by a separator. Your file might probably look like this:
```
2021-01-01;Salary;10;EUR
2021-01-01;Rent;-5;EUR
etc...
```
In this case the separator is `;`

You can open the file with any text editor or Excel to check it.
Once you have done it, please input it in the box below.
"""

csv_separator_text = """##### What is the separator between columns?."""

thousands_decimals_separator_title = (
    """##### What is the separator between thousands and decimals?"""
)

thousands_decimals_separator_extra_text = """
Your csv might look like this one:
```
2021-01-01;Salary;1,000.00;EUR
2021-01-01;Rent;-500.00;EUR
etc...
```
In this case the thousand separator is `,` and the decimal separator is `.`

You can open the file with any text editor or Excel to check it.
Once you have done it, please input it in the boxes below.
"""


headers_title = """##### Which are the headers of your file?"""


headers_extra_text = """
Your csv might look like this one:
```
date;concept;amount;currency
2021-01-01;Salary;1000.00;EUR
2021-01-01;Rent;-500.00;EUR
etc...
```
In this case your file  has predefined headers are `date`, `concept`, `amount` and `currency`

But in might also have no headers at all:

```
2021-01-01;Salary;1000.00;EUR
2021-01-01;Rent;-500.00;EUR
etc...
```
In both cases you need to input the headers in the boxes below.

"""

headers_text = """
We need to identify the following headers: 

`date` : The date of the transaction

`concept` : The concept of the transaction

`amount` : The amount of the transaction

`account` : The balance in your savings account

Below you can see a preview of your file. You can see which index each column has.

"""
