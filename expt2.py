#Initialize Spark Session

from pyspark.sql import SparkSession
spark=SparkSession.builder\
  .appName("Statistical Measures and Probability Analysis") \
  .getOrCreate()

#Load Data

data_path = "path/to/your/dataset.csv"
df= spark.read.csv(data_path, header=True, inferSchema=True)
df.show(5)

#Descriptive Statistics

from pyspark.sql.functions import mean, stddev, col, max, min 

df.select(mean(col("your_column")).alias("Mean"),
         stddev(col("your_column")).alias("Standard Deviation"),
         max(col("your_column")).alias("Max"),
         min(col("your_column")).alias("Min")).show()

#Correlation and Covariance

from pyspark.sql.functions import corr

df.select(corr("column1", "column2").alias("Correlation")).show()
covariance = df.stat.cov("column1", "column2")
print (f"Covariance: {covariance}")

# Applying Probability theory
p_event = df.filter(df['event'] == 1).count() / df.count()
p_condition_given_event = df.filter((df['event'] == 1) & (df['condition'] == 1)).count()
p_condition = df.filter(df['condition'] == 1).count() / df.count()

# Apply Bayes' Theorem: P(Condition | Event) = (P(Event | Condition) * P(Condition)) / P(Event)
p_condition_given_event = (p_condition_given_event * p_condition) / p_event 
print(f"P(Condition | Event): {p_condition_given_event}")
