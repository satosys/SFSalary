#Assignment on SF Salary datset from Kaggle.

import pandas as pd
sal = pd.read_csv('/Users/SatsRocks9/Desktop/Salaries.csv')
#print (open('/Users/SatsRocks9/Desktop/Salaries.csv').read())

#print(sal.head())
#print(sal.info())
sal_mean_sum = sal['BasePay'].mean()
print(sal_mean_sum)
sal_max_pay = sal['OvertimePay'].max()
print(sal_max_pay)
job_title = sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle']
print(job_title)
Total_PayBenefits = sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['TotalPayBenefits']
print(Total_PayBenefits)
High_pay_emp = sal['TotalPayBenefits'].max()
print(High_pay_emp)
sal['title_len'] = sal['JobTitle'].apply(len)
sal[['title_len','TotalPayBenefits']].corr()