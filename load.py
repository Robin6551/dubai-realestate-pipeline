from sqlalchemy import create_engine

def get_engine():
    return create_engine("postgresql://postgres:Hulksmashearth52@localhost:5432/dubai_realestate")

def load(fact_transactions, dim_date, dim_area, dim_property, dim_procedure):
    engine = get_engine()
    tables = {"dim_date": dim_date,
        "dim_area": dim_area,
        "dim_property": dim_property,
        "dim_procedure": dim_procedure,
        "fact_transactions": fact_transactions}
    
    for name, df in tables.items():
        print(f'loading{name}...({len(df):,})rows')
        df.to_sql(name, engine, if_exists="replace", index=False, chunksize=10000)
        print("Done.")


if __name__ == "__main__":
    from extract import extract
    from transform import clean_data, build_star_schema

    df = extract()
    df_clean = clean_data(df)
    fact_transactions, dim_date, dim_area, dim_property, dim_procedure = build_star_schema(df_clean)
    load(fact_transactions, dim_date, dim_area, dim_property, dim_procedure)