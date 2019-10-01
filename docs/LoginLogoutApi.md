# mpg_pure.LoginLogoutApi

All URIs are relative to *https://pure.mpg.de/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_using_get**](LoginLogoutApi.md#get_user_using_get) | **GET** /login/who | getUser
[**login_using_post**](LoginLogoutApi.md#login_using_post) | **POST** /login | login
[**logout_using_get**](LoginLogoutApi.md#logout_using_get) | **GET** /logout | logout


# **get_user_using_get**
> AccountUserDbVO get_user_using_get(authorization)

getUser

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.LoginLogoutApi()
authorization = 'authorization_example' # str | Authorization

try:
    # getUser
    api_response = api_instance.get_user_using_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginLogoutApi->get_user_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 

### Return type

[**AccountUserDbVO**](AccountUserDbVO.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_using_post**
> object login_using_post(credentials)

login

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.LoginLogoutApi()
credentials = 'credentials_example' # str | credentials

try:
    # login
    api_response = api_instance.login_using_post(credentials)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginLogoutApi->login_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | **str**| credentials | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_using_get**
> str logout_using_get(authorization)

logout

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.LoginLogoutApi()
authorization = 'authorization_example' # str | Authorization

try:
    # logout
    api_response = api_instance.logout_using_get(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginLogoutApi->logout_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

