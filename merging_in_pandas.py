import pandas as pd
orders = pd.DataFrame({
    "Order_ID": [101,102,103,101,104,102],
    "Customer": ["Ali","Sara","Ahmed","Ali","Ayesha","Sara"],
    "Product": ["Laptop","Phone","Tablet","Laptop","Laptop","Phone"],
    "Quantity": [1,2,1,1,3,2]
})

payments = pd.DataFrame({
    "Payment_ID": ["P001","P002","P003","P004","P005"],
    "Order_ID": [101,102,103,101,104],
    "Amount": [1200,800,500,1200,3600]
})
df1=pd.read_csv(r"C:\Users\hp\Downloads\order-id-customer-6.csv")
df2=pd.read_csv(r"C:\Users\hp\Downloads\payment-id-order-id-5.csv")
print(df1)
print(df2)