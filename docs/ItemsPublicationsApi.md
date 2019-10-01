# mpg_pure.ItemsPublicationsApi

All URIs are relative to *https://pure.mpg.de/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post1**](ItemsPublicationsApi.md#create_using_post1) | **POST** /items | create
[**delete_using_delete1**](ItemsPublicationsApi.md#delete_using_delete1) | **DELETE** /items/{itemId} | delete
[**get_component_content_using_get**](ItemsPublicationsApi.md#get_component_content_using_get) | **GET** /items/{itemId}/component/{componentId}/content | getComponentContent
[**get_technical_metadata_by_tika_using_get**](ItemsPublicationsApi.md#get_technical_metadata_by_tika_using_get) | **GET** /items/{itemId}/component/{componentId}/metadata | getTechnicalMetadataByTika
[**get_using_get1**](ItemsPublicationsApi.md#get_using_get1) | **GET** /items/{itemId} | get
[**get_version_history_using_get**](ItemsPublicationsApi.md#get_version_history_using_get) | **GET** /items/{itemId}/history | getVersionHistory
[**release_using_put**](ItemsPublicationsApi.md#release_using_put) | **PUT** /items/{itemId}/release | release
[**revise_using_put**](ItemsPublicationsApi.md#revise_using_put) | **PUT** /items/{itemId}/revise | revise
[**search_scroll_using_get**](ItemsPublicationsApi.md#search_scroll_using_get) | **GET** /items/search/scroll | searchScroll
[**search_using_post**](ItemsPublicationsApi.md#search_using_post) | **POST** /items/search | search
[**submit_using_put**](ItemsPublicationsApi.md#submit_using_put) | **PUT** /items/{itemId}/submit | submit
[**update_using_put1**](ItemsPublicationsApi.md#update_using_put1) | **PUT** /items/{itemId} | update
[**withdraw_using_put**](ItemsPublicationsApi.md#withdraw_using_put) | **PUT** /items/{itemId}/withdraw | withdraw


# **create_using_post1**
> ItemVersionVO create_using_post1(authorization, item)

create

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
authorization = 'authorization_example' # str | Authorization
item = mpg_pure.ItemVersionVO() # ItemVersionVO | item

try:
    # create
    api_response = api_instance.create_using_post1(authorization, item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->create_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **item** | [**ItemVersionVO**](ItemVersionVO.md)| item | 

### Return type

[**ItemVersionVO**](ItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete1**
> object delete_using_delete1(authorization, item_id, params)

delete

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
authorization = 'authorization_example' # str | Authorization
item_id = 'item_id_example' # str | itemId
params = mpg_pure.TaskParamVO() # TaskParamVO | params

try:
    # delete
    api_response = api_instance.delete_using_delete1(authorization, item_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->delete_using_delete1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **item_id** | **str**| itemId | 
 **params** | [**TaskParamVO**](TaskParamVO.md)| params | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_component_content_using_get**
> get_component_content_using_get(component_id, item_id, authorization=authorization, download=download)

getComponentContent

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
component_id = 'component_id_example' # str | componentId
item_id = 'item_id_example' # str | itemId
authorization = 'authorization_example' # str | Authorization (optional)
download = false # bool | download (optional) (default to false)

try:
    # getComponentContent
    api_instance.get_component_content_using_get(component_id, item_id, authorization=authorization, download=download)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->get_component_content_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| componentId | 
 **item_id** | **str**| itemId | 
 **authorization** | **str**| Authorization | [optional] 
 **download** | **bool**| download | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_technical_metadata_by_tika_using_get**
> str get_technical_metadata_by_tika_using_get(component_id, item_id, authorization=authorization)

getTechnicalMetadataByTika

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
component_id = 'component_id_example' # str | componentId
item_id = 'item_id_example' # str | itemId
authorization = 'authorization_example' # str | Authorization (optional)

try:
    # getTechnicalMetadataByTika
    api_response = api_instance.get_technical_metadata_by_tika_using_get(component_id, item_id, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->get_technical_metadata_by_tika_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **component_id** | **str**| componentId | 
 **item_id** | **str**| itemId | 
 **authorization** | **str**| Authorization | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get1**
> ItemVersionVO get_using_get1(item_id, authorization=authorization)

get

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
item_id = 'item_id_example' # str | itemId
authorization = 'authorization_example' # str | Authorization (optional)

try:
    # get
    api_response = api_instance.get_using_get1(item_id, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->get_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_id** | **str**| itemId | 
 **authorization** | **str**| Authorization | [optional] 

### Return type

[**ItemVersionVO**](ItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_history_using_get**
> list[AuditDbVO] get_version_history_using_get(authorization, item_id)

getVersionHistory

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
authorization = 'authorization_example' # str | Authorization
item_id = 'item_id_example' # str | itemId

try:
    # getVersionHistory
    api_response = api_instance.get_version_history_using_get(authorization, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->get_version_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **item_id** | **str**| itemId | 

### Return type

[**list[AuditDbVO]**](AuditDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **release_using_put**
> ItemVersionVO release_using_put(authorization, item_id, params)

release

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
authorization = 'authorization_example' # str | Authorization
item_id = 'item_id_example' # str | itemId
params = mpg_pure.TaskParamVO() # TaskParamVO | params

try:
    # release
    api_response = api_instance.release_using_put(authorization, item_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->release_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **item_id** | **str**| itemId | 
 **params** | [**TaskParamVO**](TaskParamVO.md)| params | 

### Return type

[**ItemVersionVO**](ItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revise_using_put**
> ItemVersionVO revise_using_put(authorization, item_id, params)

revise

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
authorization = 'authorization_example' # str | Authorization
item_id = 'item_id_example' # str | itemId
params = mpg_pure.TaskParamVO() # TaskParamVO | params

try:
    # revise
    api_response = api_instance.revise_using_put(authorization, item_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->revise_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **item_id** | **str**| itemId | 
 **params** | [**TaskParamVO**](TaskParamVO.md)| params | 

### Return type

[**ItemVersionVO**](ItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_scroll_using_get**
> SearchRetrieveResponseVOItemVersionVO search_scroll_using_get(scroll_id, authorization=authorization, citation=citation, csl_cone_id=csl_cone_id, format=format)

searchScroll

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
scroll_id = 'scroll_id_example' # str | scrollId
authorization = 'authorization_example' # str | Authorization (optional)
citation = 'citation_example' # str | citation (optional)
csl_cone_id = 'csl_cone_id_example' # str | cslConeId (optional)
format = 'format_example' # str | format (optional)

try:
    # searchScroll
    api_response = api_instance.search_scroll_using_get(scroll_id, authorization=authorization, citation=citation, csl_cone_id=csl_cone_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->search_scroll_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scroll_id** | **str**| scrollId | 
 **authorization** | **str**| Authorization | [optional] 
 **citation** | **str**| citation | [optional] 
 **csl_cone_id** | **str**| cslConeId | [optional] 
 **format** | **str**| format | [optional] 

### Return type

[**SearchRetrieveResponseVOItemVersionVO**](SearchRetrieveResponseVOItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_using_post**
> SearchRetrieveResponseVOItemVersionVO search_using_post(query, authorization=authorization, citation=citation, csl_cone_id=csl_cone_id, format=format, scroll=scroll)

search

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
query = mpg_pure.JsonNode() # JsonNode | query
authorization = 'authorization_example' # str | Authorization (optional)
citation = 'APA' # str | citation (optional) (default to APA)
csl_cone_id = 'csl_cone_id_example' # str | cslConeId (optional)
format = 'json' # str | format (optional) (default to json)
scroll = true # bool | scroll (optional)

try:
    # search
    api_response = api_instance.search_using_post(query, authorization=authorization, citation=citation, csl_cone_id=csl_cone_id, format=format, scroll=scroll)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->search_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**JsonNode**](JsonNode.md)| query | 
 **authorization** | **str**| Authorization | [optional] 
 **citation** | **str**| citation | [optional] [default to APA]
 **csl_cone_id** | **str**| cslConeId | [optional] 
 **format** | **str**| format | [optional] [default to json]
 **scroll** | **bool**| scroll | [optional] 

### Return type

[**SearchRetrieveResponseVOItemVersionVO**](SearchRetrieveResponseVOItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_using_put**
> ItemVersionVO submit_using_put(authorization, item_id, params)

submit

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
authorization = 'authorization_example' # str | Authorization
item_id = 'item_id_example' # str | itemId
params = mpg_pure.TaskParamVO() # TaskParamVO | params

try:
    # submit
    api_response = api_instance.submit_using_put(authorization, item_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->submit_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **item_id** | **str**| itemId | 
 **params** | [**TaskParamVO**](TaskParamVO.md)| params | 

### Return type

[**ItemVersionVO**](ItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put1**
> ItemVersionVO update_using_put1(authorization, item, item_id)

update

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
authorization = 'authorization_example' # str | Authorization
item = mpg_pure.ItemVersionVO() # ItemVersionVO | item
item_id = 'item_id_example' # str | itemId

try:
    # update
    api_response = api_instance.update_using_put1(authorization, item, item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->update_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **item** | [**ItemVersionVO**](ItemVersionVO.md)| item | 
 **item_id** | **str**| itemId | 

### Return type

[**ItemVersionVO**](ItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_using_put**
> ItemVersionVO withdraw_using_put(authorization, item_id, params)

withdraw

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ItemsPublicationsApi()
authorization = 'authorization_example' # str | Authorization
item_id = 'item_id_example' # str | itemId
params = mpg_pure.TaskParamVO() # TaskParamVO | params

try:
    # withdraw
    api_response = api_instance.withdraw_using_put(authorization, item_id, params)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemsPublicationsApi->withdraw_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **item_id** | **str**| itemId | 
 **params** | [**TaskParamVO**](TaskParamVO.md)| params | 

### Return type

[**ItemVersionVO**](ItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

