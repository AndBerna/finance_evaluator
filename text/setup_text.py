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


headers_validation_text = """
Below you can a preview with the updated headers names. If you are happy with them, proceed.
"""

date_title = """##### Which is the date format of your file?
"""
date_text = """ In order to process the dates correctly, we need to know the format of your dates. 
We need to do it following the [Python datetime format](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes).
"""

date_text_extra = """

Your csv might look like this one:
```
date;concept;amount;currency
2021-01-31;Salary;1000.00;EUR
2021-01-31;Rent;-500.00;EUR
etc...
```
In this case the date format is `%Y-%m-%d` where `%Y` is the year, `%m` is the month and `%d` is the day. 
We also indicate the hyphens `-` to separate the date components.

    You can find a detailed list of the different date formats [here](https://strftime.org/).


Other common date formats are:

- `%d/%m/%Y`   : 31/01/2021
- `%m/%d/%Y`   : 01/31/2021
- `%d-%m-%Y`   : 31-01-2021
- `%d.%m.%y`   : 31.01.21
- `%B %d, %Y`  : January 31, 2021
- `%d %b %Y`   : 31 Jan 2021

"""
currency_title = """##### Which is your currency?"""
currency_text = """Please input the currency of your transactions. It should be the same for all of them."""


final_title = """

### 3. You are ready to go!"""
final_text = """ Click the Financial Evaluator tab in the top left corner to continue.
    Press the Save as Default button to save your settings for future use."""
