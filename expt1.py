#Initialize Spark session
from pyspark.sql import SparkSession
spark=SparkSession.builder \
      .appName("Social Media Engagement Prediction")\
      .getOrCreate()

#Load and inspect the data
data_path="path/to/your/dataset.csv"
df=spark.read.csv(data_path,header=True,inferSchema=True)
df.printSchema()
df.show(5)

#Data Preprocessing
from pyspark.ml.feature import VectorAssembler,StandardScaler
assembler=VectorAssembler(inputcol="features",outputcols="feature_vector")
df=assembler.transform(df)
scaler=StandardScaler(inputcol="feature_vector",outputcol="scaled_features",withStd=True,WithMean=False)
scalerModel=scaler.fit(df)
df_scaled=scalerModel.transform(df)

#traintest split
(train_data,test_data)=df.randomSplit([0.8,0.2])

#ModelTraining
from pyspark.ml.regression import LinearRegression
lr=LinearRegression(featuresCol="scaled_features",labelcol="label")
lrModel=lr.fit(train_data)

#ModelEvaluation
predictions=lrModel.transform(test_data)
from pyspark.ml.evaluation import RegressionEvaluator
evaluator=RegressionEvaluator(labelCol="label",predictionCol="prediction",metricName="rmse")
rmse=evaluator.evaluate(predictions)
print("Root Mean Square Error(RMSE) on test_data = {rmse}")