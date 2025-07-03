import pandas as pd
from pyspark.sql import SparkSession

def load_data():
    """Load sample datasets"""
    spark = SparkSession.builder \
        .appName("MacadamiaETL") \
        .getOrCreate()
    
    # Load CSV data
    cost_df = spark.read.csv("/app/data/cost_reports.csv", header=True, inferSchema=True)
    material_df = spark.read.csv("/app/data/material_usage.csv", header=True, inferSchema=True)
    
    return cost_df, material_df