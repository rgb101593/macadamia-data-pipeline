from pyspark.sql import functions as F

def calculate_cost_variance(cost_df):
    """Mirror your Macadamia cost analysis with PySpark"""
    return cost_df.withColumn(
        "Cost_Variance", 
        F.col("Actual_Cost") - F.col("Planned_Cost")
    ).groupBy("Project_ID", "Material").agg(
        F.avg("Cost_Variance").alias("Avg_Cost_Variance"),
        F.sum("Actual_Cost").alias("Total_Actual_Cost")
    )

def analyze_material_usage(material_df):
    """Replicate your material usage reports"""
    return material_df.groupBy("Project_ID", "Material").agg(
        F.sum("Quantity").alias("Total_Quantity"),
        F.count("Location").alias("Locations_Used")
    )