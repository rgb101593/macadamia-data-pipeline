from data_ingestion import load_data
from transformations import calculate_cost_variance, analyze_material_usage
from sql_operations import save_to_sql
from aws_utils import save_to_s3

def main():
  print("🚀 Starting Macadamia ETL Pipeline...")

  # Load data
  cost_df, material_df = load_data()
  print("📊 Data loaded successfully!")

  # Transform data
  cost_variance_df = calculate_cost_variance(cost_df)
  material_usage_df = analyze_material_usage(material_df)
  print("🔄 Data transformed successfully!")

  cost_variance_df.show()
  material_usage_df.show()

  # Save to SQLite
  save_to_sql(cost_variance_df, "cost_variance_analysis")
  save_to_sql(material_usage_df, "material_usage_summary")
  print("💾 Data saved to SQLite database!")

  # Save to S3
  try:
    save_to_s3(cost_variance_df, "macadamia-data-bucket", "cost_analysis")
    save_to_s3(material_usage_df, "macadamia-data-bucket", "material_usage")
  except Exception as e:
    print(f"❌ Error saving to S3: {str(e)} (Continuing without S3 upload)")

  print("pipeline completed successfully!")

if __name__ == "__main__":
  main()