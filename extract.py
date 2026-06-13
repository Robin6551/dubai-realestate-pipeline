import pandas as pd

def extract():
    df = pd.read_csv(r'C:\Users\ALL AtoZ\Downloads\dubai-realestate-pipeline\data\Transactions.csv', low_memory= False)
    print(f'loaded{len(df)}:, rows and{len(df.columns)} columns')

    return df

if __name__ == "__main__":
    df = extract()
    print(df.head())


