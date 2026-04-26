import duckdb

df = duckdb.read_csv('DataAnalysis/UK_based_EDA/diabetes.csv')

df = duckdb.query("SELECT * FROM df").to_df()