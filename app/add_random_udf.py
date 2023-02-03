import pyspark.sql.types as T
import pyspark.sql.functions as F
import random


@F.udf(returnType=T.IntegerType())
def add_random(x):
   random_number = random.randint(1,99)
   return x + random_number
