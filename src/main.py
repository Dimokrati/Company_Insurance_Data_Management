from pipelines.raw.api_pipeline import ApiPipeline

api_pipeline = ApiPipeline()

df_data = api_pipeline.run_pipeline()

print(df_data)