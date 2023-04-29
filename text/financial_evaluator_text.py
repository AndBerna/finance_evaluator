intro_text = """

In this page you can see the your financial analysis. It is organized as it follows:

- Status of the Finances : This section gives you an snapshot of your current financial situation
- Trends : This section gives you an overview on how your finances have evolved.

The whole idea is to provide some general indicators so you can track the health and status of your finances.

"""


to_drop_text = """

In the left sidebar, under the "Optional Settings" you can select if you want to remove any income or expenses concepts from the calculations. 
You can later save them as defaults by pressing the "Save as Default" button. This is useful if you want to remove concepts that **distort the analysis.**

- *You might want to remove an extraordinary expense, that is not representative of your monthly expenses.*
- *You might want to remove a shared apartment bill from your expenses and your subtenants payments from your income.*

"""


current_status_title = """### Status of the Finances"""
current_status_text = """
The results show the average  values of the last 3 months.  In order to reduce the influence of months with extraordinary events, the median is used instead of the mean.

Remember that the income and expenses calculations exclude the concepts indicated before. Saving calculations use the raw data
"""


trends_title = """### Trends"""
trends_extra = """
The results show the trends of your finances. The trend is calculated along the whole period provided in the csv file. 
i.e if your records are of one year is the last year trend. 
Results are calculated fitting a linear regression model to the data and using the 3-month rolling means.

Remember that the income and expenses calculations exclude the concepts indicated before. Saving calculations use the raw data
"""
