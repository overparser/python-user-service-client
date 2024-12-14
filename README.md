# openapi-client
User Management Service

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.03
- Package version: 1.0.0
- Generator version: 7.10.0
- Build package: org.openapitools.codegen.languages.PythonPydanticV1ClientCodegen
For more information, please visit [https://t.me/overparser](https://t.me/overparser)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8001
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8001"
)



# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.HealthApi(api_client)

    try:
        # Health Check
        api_response = await api_instance.get_health()
        print("The response of HealthApi->get_health:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HealthApi->get_health: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8001*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*HealthApi* | [**get_health**](docs/HealthApi.md#get_health) | **GET** /health | Health Check
*UsersApi* | [**delete_users_user_id**](docs/UsersApi.md#delete_users_user_id) | **DELETE** /users/{userId} | Delete User
*UsersApi* | [**get_users_user_id**](docs/UsersApi.md#get_users_user_id) | **GET** /users/{userId} | Get User Info by User ID
*UsersApi* | [**patch_users_user_id**](docs/UsersApi.md#patch_users_user_id) | **PATCH** /users/{userId} | Update User Information
*UsersApi* | [**post_user**](docs/UsersApi.md#post_user) | **POST** /user | Create New User


## Documentation For Models

 - [Error](docs/Error.md)
 - [GetHealth200Response](docs/GetHealth200Response.md)
 - [GetUsersUserId404Response](docs/GetUsersUserId404Response.md)
 - [GetUsersUserId404ResponseError](docs/GetUsersUserId404ResponseError.md)
 - [PatchUsersUserIdRequest](docs/PatchUsersUserIdRequest.md)
 - [PostUserRequest](docs/PostUserRequest.md)
 - [User](docs/User.md)
 - [UserPreferences](docs/UserPreferences.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

derror.dd@gmail.com

