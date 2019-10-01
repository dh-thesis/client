# mpg_pure.UploadFilesStagingApi

All URIs are relative to *https://pure.mpg.de/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_stage_component_using_post**](UploadFilesStagingApi.md#create_stage_component_using_post) | **POST** /staging/{componentName} | createStageComponent


# **create_stage_component_using_post**
> str create_stage_component_using_post(authorization, component_name)

createStageComponent

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UploadFilesStagingApi()
authorization = 'authorization_example' # str | Authorization
component_name = 'component_name_example' # str | componentName

try:
    # createStageComponent
    api_response = api_instance.create_stage_component_using_post(authorization, component_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UploadFilesStagingApi->create_stage_component_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **component_name** | **str**| componentName | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

