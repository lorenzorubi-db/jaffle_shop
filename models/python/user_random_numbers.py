# # import pyspark.sql.types as T
# # import pyspark.sql.functions as F
# import random


# # @F.udf(returnType=T.IntegerType())
# def add_random(x):
#    random_number = random.randint(1,99)
#    return x + random_number

import importlib

module = importlib.import_module("app.add_random_udf")
add_random = getattr(module, "add_random")


def model(dbt, session):
   dbt.config(materialized="table")

   # DataFrame representing an upstream model
   users_df = dbt.ref("stg_customers")

   df = users_df.withColumn("user_random_number", add_random(users_df["customer_id"]))
   return df
