from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment

# Create endpoint
endpoint = ManagedOnlineEndpoint(
    name="cataract-endpoint",
    auth_mode="key",
    description="Endpoint to serve MLflow cataract model"
)
ml_client.begin_create_or_update(endpoint).result()

# Create deployment (no scoring script needed for MLflow model)
deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name=endpoint.name,
    model=ml_client.models.get(name="cataract-model", version="1"),
    environment="mlflow-env@latest",
    instance_type="Standard_DS2_v2",
    instance_count=1
)
ml_client.begin_create_or_update(deployment).result()

# Set traffic
endpoint.traffic = {"blue": 100}
ml_client.begin_create_or_update(endpoint).result()
