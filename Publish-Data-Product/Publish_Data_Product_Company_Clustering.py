# Databricks notebook source
# MAGIC %md
# MAGIC **Install SDK**
# MAGIC
# MAGIC With this SDK you can perform Business Data Cloud Connect operations such as:
# MAGIC
# MAGIC - Create or update shares
# MAGIC - Create or update shares CSN
# MAGIC - Publish or unpublish Data Products

# COMMAND ----------

# MAGIC %pip install --upgrade pydantic

# COMMAND ----------

# Code 1
%pip install sap-bdc-connect-sdk
%pip install --upgrade pydantic
%restart_python
#%pip uninstall -y pydantic typing-extensions
#%pip install --force-reinstall pydantic==2.10.6 typing-extensions==4.12.0 --no-deps --no-cache-dir


#%restart_python

# COMMAND ----------

# MAGIC %restart_python

# COMMAND ----------

# MAGIC %md
# MAGIC **Create or update share**
# MAGIC
# MAGIC A share is a mechanism for distributing and accessing data across different systems. Creating or updating a share involves including specific attributes, such as @openResourceDiscoveryV1, in the request body, aligning with the Open Resource Discovery protocol. This procedure ensures that the share is properly structured and described according to specified standards, facilitating effective data sharing and management.

# COMMAND ----------

# Code 2
from bdc_connect_sdk.auth import BdcConnectClient
from bdc_connect_sdk.auth import DatabricksClient

databricks_client = DatabricksClient(dbutils)
bdc_connect_client = BdcConnectClient(databricks_client)

# COMMAND ----------

dir(databricks_client)

# COMMAND ----------

databricks_client.get_bdc_connect_endpoint()

# COMMAND ----------

# MAGIC %md
# MAGIC **Create a client**
# MAGIC
# MAGIC -   DatabricksClient receives dbutils as a parameter, which is a Databricks utility that can be used inside the Databricks notebooks
# MAGIC -   BdcConnectClient receives the DatabricksClient as a parameter to get information from the Databricks environment (e.g. secrets, api_token, workspace_url_base)

# COMMAND ----------

# Code 3
from bdc_connect_sdk.auth import BdcConnectClient
from bdc_connect_sdk.auth import DatabricksClient
import json

with BdcConnectClient(DatabricksClient(dbutils)) as bdc_connect_client:
    share_name = "company_code_clustering_share_ac234645u08"
    try:
        share_body = {
            "type": "REMOTE_SHARE",
            "provider": {
                "type": "FEDERATION",
                "name": "databricks"
            },
            "@openResourceDiscoveryV1": {
                "title": "Company Code Clustering Data Product From ac234645u08",
                "shortDescription": "Data asset for company code clustering",
                "description": "This data product contains the data used for the company clustering prediction model. A hyperparameter optimization is performed on the cleased data with the help of the Bayesian Search optimization. For the clustering we use the Affinity Propagation algorithm.After the hyperparameter optimization is performed, the model with the highest silhouette score is applied as the best model to the prepared clustering dataset. The resulting clustering labels are stored and merged together with a T-SNE based representation of the input dataset."
            }
        }
        share_request_body = json.dumps(share_body)
        catalog_response = bdc_connect_client.create_or_update_share(
            share_name,
            share_request_body
        )
        print(f"[SUCCESS] Share '{share_name}' created or updated. Response: {catalog_response}")
    except Exception as ex:
        print(f"[ERROR] Exception when creating and updating share name {share_name}: {ex}\n")

# COMMAND ----------

# MAGIC %md
# MAGIC **Create or update share CSN**
# MAGIC
# MAGIC The CSN serves as a standardized format for configuring and describing shares within a network. To create or update the CSN for a share, it's advised to prepare the CSN content in a separate file and include this content in the request body. This approach ensures accuracy and compliance with the CSN interoperability specifications, facilitating consistent and effective share configuration across systems.

# COMMAND ----------

# Code 4
from bdc_connect_sdk.auth import BdcConnectClient
from bdc_connect_sdk.auth import DatabricksClient
from bdc_connect_sdk.utils import csn_generator
import json

with BdcConnectClient(DatabricksClient(dbutils)) as bdc_connect_client:
    share_name = "company_code_clustering_share_ac234645u08"

try:
    csn_schema = csn_generator.generate_csn_template(share_name)
    csn_schema_string = json.dumps(csn_schema)
    
    csn_response = bdc_connect_client.create_or_update_share_csn(
        share_name,
        csn_schema_string
    )
except Exception as ex:
    print(f"Exception when creating or updating CSN for share(name={share_name}): {ex}\n")

# COMMAND ----------

print(csn_schema_string)


# COMMAND ----------

# MAGIC %md
# MAGIC **Publish a Data Product**
# MAGIC
# MAGIC A Data Product is an abstraction that represents a type of data or data set within a system, facilitating easier management and sharing across different platforms. It bundles resources or API endpoints to enable efficient data access and utilization by integrated systems. Publishing a Data Product allows these systems to access and consume the data, ensuring seamless communication and resource sharing.

# COMMAND ----------

# Code 5
from bdc_connect_sdk.auth import BdcConnectClient
from bdc_connect_sdk.auth import DatabricksClient

bdc_connect_client = BdcConnectClient(DatabricksClient(dbutils))
share_name ="company_code_clustering_share_ac234645u08"

try:
    publish_response = bdc_connect_client.publish_data_product(
      share_name,
    )
    print(f"[SUCCESS] Data Product for share '{share_name}' published. Response: {publish_response}")
except Exception as ex:
    print(f"[ERROR] Publish Data Product for share name=(:{share_name}):{ex}")

# COMMAND ----------

try:
    csn = bdc_connect_client.get_share_csn(share_name)
    print(f"CSN for share '{share_name}': {csn}")
except Exception as ex:
    print(f"Share '{share_name}' does not exist or CSN not found: {ex}")

# COMMAND ----------

x=bdc_connect_client.publish_data_product(share_name)

print(x)