from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient("AstraCS:RsAusBQQCCsueKCjsgfDOHFE:ecdc7555f977f744173936adc107b1074b715e4037969b145c364aaa77416614")
db = client.get_database_by_api_endpoint(
  "https://13593b98-d1e3-46ae-86ed-caa9a0448374-us-east-2.apps.astra.datastax.com"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")
