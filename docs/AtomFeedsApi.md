# mpg_pure.AtomFeedsApi

All URIs are relative to *https://pure.mpg.de/rest*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_recent_oa_using_get**](AtomFeedsApi.md#get_recent_oa_using_get) | **GET** /feed/oa | getRecentOa
[**get_recent_releases_using_get**](AtomFeedsApi.md#get_recent_releases_using_get) | **GET** /feed/recent | getRecentReleases
[**get_recent_releasesfor_ou_using_get**](AtomFeedsApi.md#get_recent_releasesfor_ou_using_get) | **GET** /feed/organization/{ouId} | getRecentReleasesforOu
[**get_search_as_feed_using_get**](AtomFeedsApi.md#get_search_as_feed_using_get) | **GET** /feed/search | getSearchAsFeed


# **get_recent_oa_using_get**
> str get_recent_oa_using_get()

getRecentOa

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.AtomFeedsApi()

try:
    # getRecentOa
    api_response = api_instance.get_recent_oa_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AtomFeedsApi->get_recent_oa_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_releases_using_get**
> str get_recent_releases_using_get()

getRecentReleases

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.AtomFeedsApi()

try:
    # getRecentReleases
    api_response = api_instance.get_recent_releases_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AtomFeedsApi->get_recent_releases_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recent_releasesfor_ou_using_get**
> str get_recent_releasesfor_ou_using_get(ou_id)

getRecentReleasesforOu

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.AtomFeedsApi()
ou_id = 'ou_id_example' # str | ouId

try:
    # getRecentReleasesforOu
    api_response = api_instance.get_recent_releasesfor_ou_using_get(ou_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AtomFeedsApi->get_recent_releasesfor_ou_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ou_id** | **str**| ouId | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_as_feed_using_get**
> str get_search_as_feed_using_get(q)

getSearchAsFeed

### Example
```python
from __future__ import print_function
import time
import mpg_pure
from mpg_pure.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = mpg_pure.AtomFeedsApi()
q = 'q_example' # str | q

try:
    # getSearchAsFeed
    api_response = api_instance.get_search_as_feed_using_get(q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AtomFeedsApi->get_search_as_feed_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| q | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/atom+xml;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

