# mpg_pure.ContextsApi

All URIs are relative to *https://pure.mpg.de/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_using_put**](ContextsApi.md#close_using_put) | **PUT** /contexts/{ctxId}/close | close
[**create_using_post**](ContextsApi.md#create_using_post) | **POST** /contexts | create
[**delete_using_delete**](ContextsApi.md#delete_using_delete) | **DELETE** /contexts/{ctxId} | delete
[**get_all_using_get**](ContextsApi.md#get_all_using_get) | **GET** /contexts | getAll
[**get_using_get**](ContextsApi.md#get_using_get) | **GET** /contexts/{ctxId} | get
[**open_using_put**](ContextsApi.md#open_using_put) | **PUT** /contexts/{ctxId}/open | open
[**update_using_put**](ContextsApi.md#update_using_put) | **PUT** /contexts/{ctxId} | update


# **close_using_put**
> ContextDbVO close_using_put(authorization, ctx_id, modificatio_date)

close

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ContextsApi()
authorization = 'authorization_example' # str | Authorization
ctx_id = 'ctx_id_example' # str | ctxId
modificatio_date = 'modificatio_date_example' # str | modificatioDate

try:
    # close
    api_response = api_instance.close_using_put(authorization, ctx_id, modificatio_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->close_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **ctx_id** | **str**| ctxId | 
 **modificatio_date** | **str**| modificatioDate | 

### Return type

[**ContextDbVO**](ContextDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_using_post**
> ContextDbVO create_using_post(authorization, ctx)

create

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ContextsApi()
authorization = 'authorization_example' # str | Authorization
ctx = mpg_pure.ContextDbVO() # ContextDbVO | ctx

try:
    # create
    api_response = api_instance.create_using_post(authorization, ctx)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->create_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **ctx** | [**ContextDbVO**](ContextDbVO.md)| ctx | 

### Return type

[**ContextDbVO**](ContextDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete**
> object delete_using_delete(authorization, ctx_id)

delete

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ContextsApi()
authorization = 'authorization_example' # str | Authorization
ctx_id = 'ctx_id_example' # str | ctxId

try:
    # delete
    api_response = api_instance.delete_using_delete(authorization, ctx_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **ctx_id** | **str**| ctxId | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get**
> SearchRetrieveResponseVOContextDbVO get_all_using_get(authorization=authorization, _from=_from, size=size)

getAll

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ContextsApi()
authorization = 'authorization_example' # str | Authorization (optional)
_from = 0 # int | from (optional) (default to 0)
size = 10 # int | size (optional) (default to 10)

try:
    # getAll
    api_response = api_instance.get_all_using_get(authorization=authorization, _from=_from, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->get_all_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | [optional] 
 **_from** | **int**| from | [optional] [default to 0]
 **size** | **int**| size | [optional] [default to 10]

### Return type

[**SearchRetrieveResponseVOContextDbVO**](SearchRetrieveResponseVOContextDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get**
> object get_using_get(ctx_id, authorization=authorization)

get

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ContextsApi()
ctx_id = 'ctx_id_example' # str | ctxId
authorization = 'authorization_example' # str | Authorization (optional)

try:
    # get
    api_response = api_instance.get_using_get(ctx_id, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ctx_id** | **str**| ctxId | 
 **authorization** | **str**| Authorization | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_using_put**
> ContextDbVO open_using_put(authorization, ctx_id, modificatio_date)

open

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ContextsApi()
authorization = 'authorization_example' # str | Authorization
ctx_id = 'ctx_id_example' # str | ctxId
modificatio_date = 'modificatio_date_example' # str | modificatioDate

try:
    # open
    api_response = api_instance.open_using_put(authorization, ctx_id, modificatio_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->open_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **ctx_id** | **str**| ctxId | 
 **modificatio_date** | **str**| modificatioDate | 

### Return type

[**ContextDbVO**](ContextDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put**
> ContextDbVO update_using_put(authorization, ctx, ctx_id)

update

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.ContextsApi()
authorization = 'authorization_example' # str | Authorization
ctx = mpg_pure.ContextDbVO() # ContextDbVO | ctx
ctx_id = 'ctx_id_example' # str | ctxId

try:
    # update
    api_response = api_instance.update_using_put(authorization, ctx, ctx_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContextsApi->update_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **ctx** | [**ContextDbVO**](ContextDbVO.md)| ctx | 
 **ctx_id** | **str**| ctxId | 

### Return type

[**ContextDbVO**](ContextDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

