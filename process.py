from snowflake.snowpark.functions import col, udf
from snowflake.snowpark.types import StringType
from connections import SnowflakeConnection

conn = SnowflakeConnection()
session = conn.get_session()


@udf(name="convert_fullname", replace=True)
def convert_fullname(s: str) -> str:
  return s.strip().lower().replace(" ", "_")

df = session.table("USERS")
print("Show table USERS")
df.show(n=100)

df_filtered = df.filter(col("STATUS") == "ACTIVE")
print("Show active users")
df_filtered.show()

df_with_udf = df_filtered.select(convert_fullname(col("FULL_NAME")))
print("Format fullname to username")
df_with_udf.show()
