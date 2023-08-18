import random


## alternative: as UDF, not really needed for now
#@F.udf(returnType=T.IntegerType())
def add_random(x):
   random_number = random.randint(1,99)
   return x + random_number

## alternative: as imported package (needs to be installed in the cluster)
# import importlib
#
# module = importlib.import_module("app.add_random_udf")
# add_random = getattr(module, "add_random")


def model(dbt, session):
   dbt.config(
      materialized="table",
      # # uncomment the following for submission under all-purpose cluster
      # submission_method="all_purpose_cluster",
      # cluster_id="0812-165614-tibia842"
   )

   # DataFrame representing an upstream model
   users_df = dbt.ref("stg_customers")

   df = users_df.withColumn("user_random_number", add_random(users_df["customer_id"]))
   return df
