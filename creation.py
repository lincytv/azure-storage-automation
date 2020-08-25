import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.storage.models import StorageAccountCreateParameters

## Parameters 

RESOURCE_GROUP_NAME = ''
LOCATION = ''
STORAGE_ACCOUNT_NAME = ''

# account import account detials

subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID',
    '1111111-1111111' )
credentials = ServicePrincipalCredentials(
    client_id=os.environ['AZURE_CLIENT_ID'],
    secret=os.environ['AZURE_CLIENT_SECRET'],
    tenant=os.environ['AZURE_TENANT_ID']
  )
resurce_client = ResourceManagementClient(credentials, subscription_id)
storage_client = StorageManagementClient(credentials, subscription_id)

# check the storage name avaliable 

avali = storage_client.storage_accounts.check_name_availability(STORAGE_ACCOUNT_NAME)

print('The Account {} is available: {}'.format(STORAGE_ACCOUNT_NAME, avali.name_available))
print(avali.reason)
print(avali.message)

# creating an storage account

storage_async_operation = storage_client.storage_accounts.create(
    RESOURCE_GROUP_NAME,
    STORAGE_ACCOUNT_NAME,
    StorageAccountCreateParameters(
        sku=Sku(name=SkuName.standard_ragrs),
        kind=Kind.storage,
        location=LOCATION
    )
)
storage_account = storage_async_operation.result()

# getting 