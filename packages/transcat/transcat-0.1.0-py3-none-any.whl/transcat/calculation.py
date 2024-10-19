import pandas as pd

def landgroup(input,output):

    df = pd.read_csv(input)
    a = df.groupby('category')['amount'].sum()
    with open(output, 'w') as f:
        f.write(f"Доход: {a['Доход']}\nРасход: {a['Расход']}")