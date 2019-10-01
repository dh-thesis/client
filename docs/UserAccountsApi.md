# mpg_pure.UserAccountsApi

All URIs are relative to *https://pure.mpg.de/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_using_put**](UserAccountsApi.md#activate_using_put) | **PUT** /users/{userId}/activate | activate
[**add_grant_using_put**](UserAccountsApi.md#add_grant_using_put) | **PUT** /users/{userId}/add | addGrant
[**create_using_post3**](UserAccountsApi.md#create_using_post3) | **POST** /users | create
[**deactivate_using_put**](UserAccountsApi.md#deactivate_using_put) | **PUT** /users/{userId}/deactivate | deactivate
[**delete_using_delete3**](UserAccountsApi.md#delete_using_delete3) | **DELETE** /users/{userId} | delete
[**get_all_using_get2**](UserAccountsApi.md#get_all_using_get2) | **GET** /users | getAll
[**get_using_get3**](UserAccountsApi.md#get_using_get3) | **GET** /users/{userId} | get
[**query_using_post1**](UserAccountsApi.md#query_using_post1) | **POST** /users/search | query
[**remove_grant_using_put**](UserAccountsApi.md#remove_grant_using_put) | **PUT** /users/{userId}/remove | removeGrant
[**update_using_put3**](UserAccountsApi.md#update_using_put3) | **PUT** /users/{userId} | update


# **activate_using_put**
> AccountUserDbVO activate_using_put(authorization, modification_date, user_id)

activate

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
authorization = 'authorization_example' # str | Authorization
modification_date = 'modification_date_example' # str | modificationDate
user_id = 'user_id_example' # str | userId

try:
    # activate
    api_response = api_instance.activate_using_put(authorization, modification_date, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->activate_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **modification_date** | **str**| modificationDate | 
 **user_id** | **str**| userId | 

### Return type

[**AccountUserDbVO**](AccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_grant_using_put**
> AccountUserDbVO add_grant_using_put(authorization, grants, user_id)

addGrant

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
authorization = 'authorization_example' # str | Authorization
grants = [mpg_pure.GrantVO()] # list[GrantVO] | grants
user_id = 'user_id_example' # str | userId

try:
    # addGrant
    api_response = api_instance.add_grant_using_put(authorization, grants, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->add_grant_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **grants** | [**list[GrantVO]**](GrantVO.md)| grants | 
 **user_id** | **str**| userId | 

### Return type

[**AccountUserDbVO**](AccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_using_post3**
> AccountUserDbVO create_using_post3(authorization, user)

create

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
authorization = 'authorization_example' # str | Authorization
user = mpg_pure.AccountUserDbVO() # AccountUserDbVO | user

try:
    # create
    api_response = api_instance.create_using_post3(authorization, user)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->create_using_post3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **user** | [**AccountUserDbVO**](AccountUserDbVO.md)| user | 

### Return type

[**AccountUserDbVO**](AccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_using_put**
> AccountUserDbVO deactivate_using_put(authorization, modification_date, user_id)

deactivate

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
authorization = 'authorization_example' # str | Authorization
modification_date = 'modification_date_example' # str | modificationDate
user_id = 'user_id_example' # str | userId

try:
    # deactivate
    api_response = api_instance.deactivate_using_put(authorization, modification_date, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->deactivate_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **modification_date** | **str**| modificationDate | 
 **user_id** | **str**| userId | 

### Return type

[**AccountUserDbVO**](AccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete3**
> object delete_using_delete3(authorization, user_id)

delete

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
authorization = 'authorization_example' # str | Authorization
user_id = 'user_id_example' # str | userId

try:
    # delete
    api_response = api_instance.delete_using_delete3(authorization, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->delete_using_delete3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **user_id** | **str**| userId | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_using_get2**
> SearchRetrieveResponseVOAccountUserDbVO get_all_using_get2(authorization=authorization, _from=_from, size=size)

getAll

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
authorization = 'authorization_example' # str | Authorization (optional)
_from = 0 # int | from (optional) (default to 0)
size = 10 # int | size (optional) (default to 10)

try:
    # getAll
    api_response = api_instance.get_all_using_get2(authorization=authorization, _from=_from, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->get_all_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | [optional] 
 **_from** | **int**| from | [optional] [default to 0]
 **size** | **int**| size | [optional] [default to 10]

### Return type

[**SearchRetrieveResponseVOAccountUserDbVO**](SearchRetrieveResponseVOAccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get3**
> AccountUserDbVO get_using_get3(user_id, authorization=authorization)

get

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
user_id = 'user_id_example' # str | userId
authorization = 'authorization_example' # str | Authorization (optional)

try:
    # get
    api_response = api_instance.get_using_get3(user_id, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->get_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId | 
 **authorization** | **str**| Authorization | [optional] 

### Return type

[**AccountUserDbVO**](AccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_using_post1**
> SearchRetrieveResponseVOAccountUserDbVO query_using_post1(query, authorization=authorization)

query

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
query = mpg_pure.JsonNode() # JsonNode | query
authorization = 'authorization_example' # str | Authorization (optional)

try:
    # query
    api_response = api_instance.query_using_post1(query, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->query_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | [**JsonNode**](JsonNode.md)| query | 
 **authorization** | **str**| Authorization | [optional] 

### Return type

[**SearchRetrieveResponseVOAccountUserDbVO**](SearchRetrieveResponseVOAccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_grant_using_put**
> AccountUserDbVO remove_grant_using_put(authorization, grants, user_id)

removeGrant

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
authorization = 'authorization_example' # str | Authorization
grants = [mpg_pure.GrantVO()] # list[GrantVO] | grants
user_id = 'user_id_example' # str | userId

try:
    # removeGrant
    api_response = api_instance.remove_grant_using_put(authorization, grants, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->remove_grant_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **grants** | [**list[GrantVO]**](GrantVO.md)| grants | 
 **user_id** | **str**| userId | 

### Return type

[**AccountUserDbVO**](AccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put3**
> AccountUserDbVO update_using_put3(authorization, user, user_id)

update

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.UserAccountsApi()
authorization = 'authorization_example' # str | Authorization
user = mpg_pure.AccountUserDbVO() # AccountUserDbVO | user
user_id = 'user_id_example' # str | userId

try:
    # update
    api_response = api_instance.update_using_put3(authorization, user, user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserAccountsApi->update_using_put3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 
 **user** | [**AccountUserDbVO**](AccountUserDbVO.md)| user | 
 **user_id** | **str**| userId | 

### Return type

[**AccountUserDbVO**](AccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

