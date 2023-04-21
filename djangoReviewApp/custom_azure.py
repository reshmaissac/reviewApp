from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'reviewappstorage001' # Must be replaced by your <storage_account_name>
    account_key = 'N1HVJib7A2Bv29unqW8zzh6WFNDeEIkPsGBg5sHw0zvhfjOPmYsrlrIFS++FVdVtelAlUxRqsx63+AStw7gAFA==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'reviewappstorage001' # Must be replaced by your storage_account_name
    account_key = 'N1HVJib7A2Bv29unqW8zzh6WFNDeEIkPsGBg5sHw0zvhfjOPmYsrlrIFS++FVdVtelAlUxRqsx63+AStw7gAFA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None
