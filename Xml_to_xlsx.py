import xml.etree.ElementTree as ET#importing module for xml processing
import pandas as pd#importing module for conversion into excel

element_tree = ET.parse('Input.xml')#parsing through the input xml
root = element_tree.getroot()#viewing the root element
all_vouchers = root.findall(".//VOUCHER")#finding all the voucher tags

res=[]
elements=('DATE','VOUCHERNUMBER','PARTYLEDGERNAME')#elements to be taken

for v in all_vouchers:#loop through the voucher tags
    d={}
    for e in elements:#loop for taking suitable entries within voucher tag
        if v.find('VOUCHERTYPENAME').text=='Receipt':#check whether name of voucher is receipt
            d[e]=v.find(e).text#actual content
            if not(bool(d)):#if dictionary empty
                continue
            else:
                if len(d)==len(elements):#if all the required values are present
                    res.append(d)

df=pd.DataFrame(res)#converting the list having dictionary values into a dataframe
df.columns=['Date','Vch No','Debtor']#renaming the columns
print(df)#output
df.to_excel("Tally_Receipt.xlsx",index=False)#excel sheet containing voucher numbers of Receipt type voucher