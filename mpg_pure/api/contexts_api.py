# coding: utf-8

"""
    PubMan REST API

    This is an automatically generated REST API client for PubMan.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from mpg_pure.api_client import ApiClient


class ContextsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def close_using_put(self, authorization, ctx_id, modificatio_date, **kwargs):  # noqa: E501
        """close  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.close_using_put(authorization, ctx_id, modificatio_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str ctx_id: ctxId (required)
        :param str modificatio_date: modificatioDate (required)
        :return: ContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.close_using_put_with_http_info(authorization, ctx_id, modificatio_date, **kwargs)  # noqa: E501
        else:
            (data) = self.close_using_put_with_http_info(authorization, ctx_id, modificatio_date, **kwargs)  # noqa: E501
            return data

    def close_using_put_with_http_info(self, authorization, ctx_id, modificatio_date, **kwargs):  # noqa: E501
        """close  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.close_using_put_with_http_info(authorization, ctx_id, modificatio_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str ctx_id: ctxId (required)
        :param str modificatio_date: modificatioDate (required)
        :return: ContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'ctx_id', 'modificatio_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method close_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `close_using_put`")  # noqa: E501
        # verify the required parameter 'ctx_id' is set
        if ('ctx_id' not in params or
                params['ctx_id'] is None):
            raise ValueError("Missing the required parameter `ctx_id` when calling `close_using_put`")  # noqa: E501
        # verify the required parameter 'modificatio_date' is set
        if ('modificatio_date' not in params or
                params['modificatio_date'] is None):
            raise ValueError("Missing the required parameter `modificatio_date` when calling `close_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ctx_id' in params:
            path_params['ctxId'] = params['ctx_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'modificatio_date' in params:
            body_params = params['modificatio_date']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/contexts/{ctxId}/close', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContextDbVO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_using_post(self, authorization, ctx, **kwargs):  # noqa: E501
        """create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_using_post(authorization, ctx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param ContextDbVO ctx: ctx (required)
        :return: ContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_using_post_with_http_info(authorization, ctx, **kwargs)  # noqa: E501
        else:
            (data) = self.create_using_post_with_http_info(authorization, ctx, **kwargs)  # noqa: E501
            return data

    def create_using_post_with_http_info(self, authorization, ctx, **kwargs):  # noqa: E501
        """create  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_using_post_with_http_info(authorization, ctx, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param ContextDbVO ctx: ctx (required)
        :return: ContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'ctx']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `create_using_post`")  # noqa: E501
        # verify the required parameter 'ctx' is set
        if ('ctx' not in params or
                params['ctx'] is None):
            raise ValueError("Missing the required parameter `ctx` when calling `create_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ctx' in params:
            body_params = params['ctx']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/contexts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContextDbVO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_using_delete(self, authorization, ctx_id, **kwargs):  # noqa: E501
        """delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_using_delete(authorization, ctx_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str ctx_id: ctxId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_using_delete_with_http_info(authorization, ctx_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_using_delete_with_http_info(authorization, ctx_id, **kwargs)  # noqa: E501
            return data

    def delete_using_delete_with_http_info(self, authorization, ctx_id, **kwargs):  # noqa: E501
        """delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_using_delete_with_http_info(authorization, ctx_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str ctx_id: ctxId (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'ctx_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `delete_using_delete`")  # noqa: E501
        # verify the required parameter 'ctx_id' is set
        if ('ctx_id' not in params or
                params['ctx_id'] is None):
            raise ValueError("Missing the required parameter `ctx_id` when calling `delete_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ctx_id' in params:
            path_params['ctxId'] = params['ctx_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/contexts/{ctxId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all_using_get(self, **kwargs):  # noqa: E501
        """getAll  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization
        :param int _from: from
        :param int size: size
        :return: SearchRetrieveResponseVOContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """getAll  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization
        :param int _from: from
        :param int size: size
        :return: SearchRetrieveResponseVOContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', '_from', 'size']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'size' in params:
            query_params.append(('size', params['size']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/contexts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SearchRetrieveResponseVOContextDbVO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_using_get(self, ctx_id, **kwargs):  # noqa: E501
        """get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_using_get(ctx_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ctx_id: ctxId (required)
        :param str authorization: Authorization
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_using_get_with_http_info(ctx_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_using_get_with_http_info(ctx_id, **kwargs)  # noqa: E501
            return data

    def get_using_get_with_http_info(self, ctx_id, **kwargs):  # noqa: E501
        """get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_using_get_with_http_info(ctx_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str ctx_id: ctxId (required)
        :param str authorization: Authorization
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ctx_id', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'ctx_id' is set
        if ('ctx_id' not in params or
                params['ctx_id'] is None):
            raise ValueError("Missing the required parameter `ctx_id` when calling `get_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ctx_id' in params:
            path_params['ctxId'] = params['ctx_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/contexts/{ctxId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def open_using_put(self, authorization, ctx_id, modificatio_date, **kwargs):  # noqa: E501
        """open  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_using_put(authorization, ctx_id, modificatio_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str ctx_id: ctxId (required)
        :param str modificatio_date: modificatioDate (required)
        :return: ContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.open_using_put_with_http_info(authorization, ctx_id, modificatio_date, **kwargs)  # noqa: E501
        else:
            (data) = self.open_using_put_with_http_info(authorization, ctx_id, modificatio_date, **kwargs)  # noqa: E501
            return data

    def open_using_put_with_http_info(self, authorization, ctx_id, modificatio_date, **kwargs):  # noqa: E501
        """open  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.open_using_put_with_http_info(authorization, ctx_id, modificatio_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param str ctx_id: ctxId (required)
        :param str modificatio_date: modificatioDate (required)
        :return: ContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'ctx_id', 'modificatio_date']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method open_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `open_using_put`")  # noqa: E501
        # verify the required parameter 'ctx_id' is set
        if ('ctx_id' not in params or
                params['ctx_id'] is None):
            raise ValueError("Missing the required parameter `ctx_id` when calling `open_using_put`")  # noqa: E501
        # verify the required parameter 'modificatio_date' is set
        if ('modificatio_date' not in params or
                params['modificatio_date'] is None):
            raise ValueError("Missing the required parameter `modificatio_date` when calling `open_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ctx_id' in params:
            path_params['ctxId'] = params['ctx_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'modificatio_date' in params:
            body_params = params['modificatio_date']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/contexts/{ctxId}/open', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContextDbVO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_using_put(self, authorization, ctx, ctx_id, **kwargs):  # noqa: E501
        """update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_using_put(authorization, ctx, ctx_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param ContextDbVO ctx: ctx (required)
        :param str ctx_id: ctxId (required)
        :return: ContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_using_put_with_http_info(authorization, ctx, ctx_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_using_put_with_http_info(authorization, ctx, ctx_id, **kwargs)  # noqa: E501
            return data

    def update_using_put_with_http_info(self, authorization, ctx, ctx_id, **kwargs):  # noqa: E501
        """update  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_using_put_with_http_info(authorization, ctx, ctx_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization: Authorization (required)
        :param ContextDbVO ctx: ctx (required)
        :param str ctx_id: ctxId (required)
        :return: ContextDbVO
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization', 'ctx', 'ctx_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'authorization' is set
        if ('authorization' not in params or
                params['authorization'] is None):
            raise ValueError("Missing the required parameter `authorization` when calling `update_using_put`")  # noqa: E501
        # verify the required parameter 'ctx' is set
        if ('ctx' not in params or
                params['ctx'] is None):
            raise ValueError("Missing the required parameter `ctx` when calling `update_using_put`")  # noqa: E501
        # verify the required parameter 'ctx_id' is set
        if ('ctx_id' not in params or
                params['ctx_id'] is None):
            raise ValueError("Missing the required parameter `ctx_id` when calling `update_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'ctx_id' in params:
            path_params['ctxId'] = params['ctx_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'ctx' in params:
            body_params = params['ctx']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/contexts/{ctxId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ContextDbVO',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
