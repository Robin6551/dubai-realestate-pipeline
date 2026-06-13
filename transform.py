import pandas as pd

def clean_data(df):
    arabic_cols = [col for col in df.columns if col.endswith('_ar')]
    df =df.drop(columns= arabic_cols)
    print(f'dropped {len(arabic_cols)} arabic colmns')

    df['instance_date'] = pd.to_datetime(df['instance_date'], errors='coerce')

    before = len(df)
    df = df.dropna(subset= ['instance_date', 'actual_worth'])
    print(f'removed {before - len(df):,} rows with missing date or value')

    df['year'] = df['instance_date'].dt.year
    df['month'] = df['instance_date'].dt.month
    df['quarter'] = df['instance_date'].dt.quarter
    df['day'] = df['instance_date'].dt.day

    df = df[df['trans_group_en'] == 'Sales']
    print(f'Sales transation remaining {len(df):,}')

    df = df[df['actual_worth'] > 0]
    df = df[df['procedure_area']> 0]

    print('cleaning done')
    return df



def build_star_schema(df):

    dim_date = df[['instance_date','year', 'month', 'quarter', 'day']].drop_duplicates().reset_index(drop= True)
    dim_date['date_id'] = dim_date.index + 1


    dim_area = df[['area_id','area_name_en','nearest_landmark_en', 'nearest_metro_en',
                   'nearest_mall_en']].drop_duplicates(subset= 'area_id').reset_index(drop= True)
    
    dim_property = df[['property_type_en', 'property_sub_type_en','property_usage_en',
                    'rooms_en', 'has_parking']].drop_duplicates().reset_index(drop= True)

    dim_property['property_id'] = dim_property.index+1

    dim_procedure = df[['procedure_id','procedure_name_en','trans_group_en',
                        'reg_type_en']].drop_duplicates(subset= 'procedure_id').reset_index(drop= True)
    

    df = df.merge(dim_date[['instance_date', 'date_id']], on= 'instance_date', how= 'left')
    df = df.merge(dim_property[['property_type_en', 'property_sub_type_en',
                                'property_usage_en', 'rooms_en', 'has_parking', 'property_id']],
                  on=['property_type_en', 'property_sub_type_en',
                      'property_usage_en', 'rooms_en', 'has_parking'], how='left')
    
    fact_transactions = df[[
        'transaction_id', 'date_id', 'area_id', 'property_id', 'procedure_id',
        'actual_worth', 'meter_sale_price', 'procedure_area'
    ]].copy()

    print(f"fact_transactions: {len(fact_transactions):,} rows")
    print(f"dim_date: {len(dim_date):,} rows")
    print(f"dim_area: {len(dim_area):,} rows")
    print(f"dim_property: {len(dim_property):,} rows")
    print(f"dim_procedure: {len(dim_procedure):,} rows")
    print("Star schema built.")

    return fact_transactions, dim_date, dim_area, dim_property, dim_procedure

if __name__ == "__main__":
    from extract import extract
    df = extract()
    df_clean = clean_data(df)
    tables = build_star_schema(df_clean)
    print("All tables ready.")

