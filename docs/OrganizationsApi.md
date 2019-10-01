# mpg_pure.OrganizationsApi

All URIs are relative to *https://pure.mpg.de/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**child_organizations_using_get**](OrganizationsApi.md#child_organizations_using_get) | **GET** /ous/{ouId}/children | childOrganizations
[**close_using_put1**](OrganizationsApi.md#close_using_put1) | **PUT** /ous/{ouId}/close | close
[**create_using_post2**](OrganizationsApi.md#create_using_post2) | **POST** /ous | create
[**delete_using_delete2**](OrganizationsApi.md#delete_using_delete2) | **DELETE** /ous/{ouId} | delete
[**get_all_using_get1**](OrganizationsApi.md#get_all_using_get1) | **GET** /ous | getAll
[**get_using_get2**](OrganizationsApi.md#get_using_get2) | **GET** /ous/{ouId} | get
[**open_using_put1**](OrganizationsApi.md#open_using_put1) | **PUT** /ous/{ouId}/open | open
[**query_using_post**](OrganizationsApi.md#query_using_post) | **POST** /ous/search | query
[**top_level_using_get**](OrganizationsApi.md#top_level_using_get) | **GET** /ous/toplevel | topLevel
[**update_using_put2**](OrganizationsApi.md#update_using_put2) | **PUT** /ous/{ouId} | update


# **child_organizations_using_get**
> list[AffiliationDbVO] child_organizations_using_get(ou_id)

childOrganizations

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()
ou_id = 'ou_id_example' # str | ouId

try:
    # childOrganizations
    api_response = api_instance.child_organizations_using_get(ou_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->child_organizations_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ou_id** | **str**| ouId | 

### Return type

[**list[AffiliationDbVO]**](AffiliationDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_using_put1**
> AffiliationDbVO close_using_put1(authorization, modification_date, ou_id)

close

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()
authorization = 'authorization_example' # str | Authorization
modification_date = 'modification_date_example' # str | modificationDate
ou_id = 'ou_id_example' # str | ouId

try:
    # close
    api_response = api_instance.close_using_put1(authorization, modification_date, ou_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->close_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **modification_date** | **str**| modificationDate | 
 **ou_id** | **str**| ouId | 

### Return type

[**AffiliationDbVO**](AffiliationDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_using_post2**
> AffiliationDbVO create_using_post2(authorization, ou)

create

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()
authorization = 'authorization_example' # str | Authorization
ou = mpg_pure.AffiliationDbVO() # AffiliationDbVO | ou

try:
    # create
    api_response = api_instance.create_using_post2(authorization, ou)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->create_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **ou** | [**AffiliationDbVO**](AffiliationDbVO.md)| ou | 

### Return type

[**AffiliationDbVO**](AffiliationDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete2**
> object delete_using_delete2(authorization, ou_id)

delete

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()
authorization = 'authorization_example' # str | Authorization
ou_id = 'ou_id_example' # str | ouId

try:
    # delete
    api_response = api_instance.delete_using_delete2(authorization, ou_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->delete_using_delete2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **ou_id** | **str**| ouId | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get1**
> SearchRetrieveResponseVOAffiliationDbVO get_all_using_get1(authorization=authorization, _from=_from, size=size)

getAll

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()
authorization = 'authorization_example' # str | Authorization (optional)
_from = 0 # int | from (optional) (default to 0)
size = 10 # int | size (optional) (default to 10)

try:
    # getAll
    api_response = api_instance.get_all_using_get1(authorization=authorization, _from=_from, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_all_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | [optional] 
 **_from** | **int**| from | [optional] [default to 0]
 **size** | **int**| size | [optional] [default to 10]

### Return type

[**SearchRetrieveResponseVOAffiliationDbVO**](SearchRetrieveResponseVOAffiliationDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get2**
> AffiliationDbVO get_using_get2(ou_id, authorization=authorization)

get

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()
ou_id = 'ou_id_example' # str | ouId
authorization = 'authorization_example' # str | Authorization (optional)

try:
    # get
    api_response = api_instance.get_using_get2(ou_id, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->get_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ou_id** | **str**| ouId | 
 **authorization** | **str**| Authorization | [optional] 

### Return type

[**AffiliationDbVO**](AffiliationDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_using_put1**
> AffiliationDbVO open_using_put1(authorization, modification_date, ou_id)

open

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()
authorization = 'authorization_example' # str | Authorization
modification_date = 'modification_date_example' # str | modificationDate
ou_id = 'ou_id_example' # str | ouId

try:
    # open
    api_response = api_instance.open_using_put1(authorization, modification_date, ou_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->open_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **modification_date** | **str**| modificationDate | 
 **ou_id** | **str**| ouId | 

### Return type

[**AffiliationDbVO**](AffiliationDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_using_post**
> SearchRetrieveResponseVOAffiliationDbVO query_using_post(query, authorization=authorization)

query

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()
query = mpg_pure.JsonNode() # JsonNode | query
authorization = 'authorization_example' # str | Authorization (optional)

try:
    # query
    api_response = api_instance.query_using_post(query, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->query_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**JsonNode**](JsonNode.md)| query | 
 **authorization** | **str**| Authorization | [optional] 

### Return type

[**SearchRetrieveResponseVOAffiliationDbVO**](SearchRetrieveResponseVOAffiliationDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **top_level_using_get**
> list[AffiliationDbVO] top_level_using_get()

topLevel

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()

try:
    # topLevel
    api_response = api_instance.top_level_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->top_level_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AffiliationDbVO]**](AffiliationDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put2**
> AffiliationDbVO update_using_put2(authorization, ou, ou_id)

update

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.OrganizationsApi()
authorization = 'authorization_example' # str | Authorization
ou = mpg_pure.AffiliationDbVO() # AffiliationDbVO | ou
ou_id = 'ou_id_example' # str | ouId

try:
    # update
    api_response = api_instance.update_using_put2(authorization, ou, ou_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizationsApi->update_using_put2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **ou** | [**AffiliationDbVO**](AffiliationDbVO.md)| ou | 
 **ou_id** | **str**| ouId | 

### Return type

[**AffiliationDbVO**](AffiliationDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

