# mpg_pure.YearbooksApi

All URIs are relative to *https://pure.mpg.de/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_using_post4**](YearbooksApi.md#create_using_post4) | **POST** /yearbooks | create
[**delete_using_delete4**](YearbooksApi.md#delete_using_delete4) | **DELETE** /yearbooks/{yearbookId} | delete
[**get_all_using_get3**](YearbooksApi.md#get_all_using_get3) | **GET** /yearbooks | getAll
[**get_items_using_get**](YearbooksApi.md#get_items_using_get) | **GET** /yearbooks/{yearbookId}/items | getItems
[**get_using_get4**](YearbooksApi.md#get_using_get4) | **GET** /yearbooks/{yearbookId} | get
[**query_using_post2**](YearbooksApi.md#query_using_post2) | **POST** /yearbooks/search | query
[**update_using_put4**](YearbooksApi.md#update_using_put4) | **PUT** /yearbooks/{yearbookId} | update


# **create_using_post4**
> YearbookDbVO create_using_post4(authorization, yearbook)

create

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.YearbooksApi()
authorization = 'authorization_example' # str | Authorization
yearbook = mpg_pure.YearbookDbVO() # YearbookDbVO | yearbook

try:
    # create
    api_response = api_instance.create_using_post4(authorization, yearbook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YearbooksApi->create_using_post4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **yearbook** | [**YearbookDbVO**](YearbookDbVO.md)| yearbook | 

### Return type

[**YearbookDbVO**](YearbookDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete4**
> object delete_using_delete4(authorization, yearbook_id)

delete

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.YearbooksApi()
authorization = 'authorization_example' # str | Authorization
yearbook_id = 'yearbook_id_example' # str | yearbookId

try:
    # delete
    api_response = api_instance.delete_using_delete4(authorization, yearbook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YearbooksApi->delete_using_delete4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **yearbook_id** | **str**| yearbookId | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get3**
> SearchRetrieveResponseVOYearbookDbVO get_all_using_get3(authorization=authorization, _from=_from, size=size)

getAll

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.YearbooksApi()
authorization = 'authorization_example' # str | Authorization (optional)
_from = 0 # int | from (optional) (default to 0)
size = 10 # int | size (optional) (default to 10)

try:
    # getAll
    api_response = api_instance.get_all_using_get3(authorization=authorization, _from=_from, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YearbooksApi->get_all_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | [optional] 
 **_from** | **int**| from | [optional] [default to 0]
 **size** | **int**| size | [optional] [default to 10]

### Return type

[**SearchRetrieveResponseVOYearbookDbVO**](SearchRetrieveResponseVOYearbookDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_items_using_get**
> SearchRetrieveResponseVOItemVersionVO get_items_using_get(yearbook_id, authorization=authorization, citation=citation, csl_cone_id=csl_cone_id, format=format)

getItems

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.YearbooksApi()
yearbook_id = 'yearbook_id_example' # str | yearbookId
authorization = 'authorization_example' # str | Authorization (optional)
citation = 'APA' # str | citation (optional) (default to APA)
csl_cone_id = 'csl_cone_id_example' # str | cslConeId (optional)
format = 'json' # str | format (optional) (default to json)

try:
    # getItems
    api_response = api_instance.get_items_using_get(yearbook_id, authorization=authorization, citation=citation, csl_cone_id=csl_cone_id, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YearbooksApi->get_items_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yearbook_id** | **str**| yearbookId | 
 **authorization** | **str**| Authorization | [optional] 
 **citation** | **str**| citation | [optional] [default to APA]
 **csl_cone_id** | **str**| cslConeId | [optional] 
 **format** | **str**| format | [optional] [default to json]

### Return type

[**SearchRetrieveResponseVOItemVersionVO**](SearchRetrieveResponseVOItemVersionVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get4**
> YearbookDbVO get_using_get4(yearbook_id, authorization=authorization)

get

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.YearbooksApi()
yearbook_id = 'yearbook_id_example' # str | yearbookId
authorization = 'authorization_example' # str | Authorization (optional)

try:
    # get
    api_response = api_instance.get_using_get4(yearbook_id, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YearbooksApi->get_using_get4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yearbook_id** | **str**| yearbookId | 
 **authorization** | **str**| Authorization | [optional] 

### Return type

[**YearbookDbVO**](YearbookDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_using_post2**
> SearchRetrieveResponseVOYearbookDbVO query_using_post2(query, authorization=authorization)

query

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.YearbooksApi()
query = mpg_pure.JsonNode() # JsonNode | query
authorization = 'authorization_example' # str | Authorization (optional)

try:
    # query
    api_response = api_instance.query_using_post2(query, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YearbooksApi->query_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**JsonNode**](JsonNode.md)| query | 
 **authorization** | **str**| Authorization | [optional] 

### Return type

[**SearchRetrieveResponseVOYearbookDbVO**](SearchRetrieveResponseVOYearbookDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put4**
> YearbookDbVO update_using_put4(authorization, yearbook, yearbook_id)

update

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.YearbooksApi()
authorization = 'authorization_example' # str | Authorization
yearbook = mpg_pure.YearbookDbVO() # YearbookDbVO | yearbook
yearbook_id = 'yearbook_id_example' # str | yearbookId

try:
    # update
    api_response = api_instance.update_using_put4(authorization, yearbook, yearbook_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling YearbooksApi->update_using_put4: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **yearbook** | [**YearbookDbVO**](YearbookDbVO.md)| yearbook | 
 **yearbook_id** | **str**| yearbookId | 

### Return type

[**YearbookDbVO**](YearbookDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

