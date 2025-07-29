import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/apidojo/api/tasty'

mcp = FastMCP('tasty')

@mcp.tool()
def recipes_auto_complete(prefix: Annotated[str, Field(description='Food name or ingredient')]) -> dict: 
    '''Get auto complete suggestions by name or ingredients'''
    url = 'https://tasty.p.rapidapi.com/recipes/auto-complete'
    headers = {'x-rapidapi-host': 'tasty.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'prefix': prefix,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recipes_list(_from: Annotated[Union[int, float], Field(description='The offset of items to be ignored in response for paging Default: 0')],
                 size: Annotated[Union[int, float], Field(description='Number of items returned per response Default: 20')],
                 tags: Annotated[Union[str, None], Field(description='Get suitable values from /tags/list API')] = None,
                 q: Annotated[Union[str, None], Field(description='Name of food or, ingredients to search by')] = None,
                 sort: Annotated[Union[str, None], Field(description='Leave empty to sort by popular as default OR one of the following : approved_at:desc|approved_at:asc')] = None) -> dict: 
    '''List recipes by option filters or name'''
    url = 'https://tasty.p.rapidapi.com/recipes/list'
    headers = {'x-rapidapi-host': 'tasty.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'from': _from,
        'size': size,
        'tags': tags,
        'q': q,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recipes_list_similarities(recipe_id: Annotated[Union[int, float], Field(description='The id value of any recipe returned in recipes/list API Default: 8138')]) -> dict: 
    '''List similar recipes by specific recipe id'''
    url = 'https://tasty.p.rapidapi.com/recipes/list-similarities'
    headers = {'x-rapidapi-host': 'tasty.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'recipe_id': recipe_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recipes_get_more_info(id: Annotated[Union[int, float], Field(description='The id value of any recipe returned in recipes/list API Default: 8138')]) -> dict: 
    '''Get more information of recipe if available, such as : ingredients, nutrition info, preparation, etc... This endpoint returns 404 status code, it means there is no more information to obtain. * .../recipes/list already returns ingredients, nutrition info, preparation, etc...'''
    url = 'https://tasty.p.rapidapi.com/recipes/get-more-info'
    headers = {'x-rapidapi-host': 'tasty.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tips_list(id: Annotated[Union[int, float], Field(description='The value of recipe id returned in .../recipes/list .../feeds/list .../recipes/list-similarities endpoints Default: 3562')],
              _from: Annotated[Union[int, float, None], Field(description='The offset of items to be ignored in response for paging Default: 0')] = None,
              size: Annotated[Union[int, float, None], Field(description='Number of items returned per response Default: 30')] = None) -> dict: 
    '''This endpoint is used to load tips (reviews)'''
    url = 'https://tasty.p.rapidapi.com/tips/list'
    headers = {'x-rapidapi-host': 'tasty.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
        'from': _from,
        'size': size,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tags_list() -> dict: 
    '''List supported tags name for filtering in recipes/list API'''
    url = 'https://tasty.p.rapidapi.com/tags/list'
    headers = {'x-rapidapi-host': 'tasty.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def feeds_list(size: Annotated[Union[int, float], Field(description='Number of items returned per response Default: 5')],
               timezone: Annotated[str, Field(description='The timezone of your location in format of +/- hhmm')],
               vegetarian: Annotated[bool, Field(description='List vegetarian food only')],
               _from: Annotated[Union[int, float], Field(description='The offset of items to be ignored in response for paging Default: 0')]) -> dict: 
    '''List latest feeds about new food, recipes,etc...'''
    url = 'https://tasty.p.rapidapi.com/feeds/list'
    headers = {'x-rapidapi-host': 'tasty.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'size': size,
        'timezone': timezone,
        'vegetarian': vegetarian,
        'from': _from,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def recipes_detail(id: Annotated[Union[int, float], Field(description='The id value of any recipe returned in recipes/list API Default: 5586')]) -> dict: 
    '''Get more information of recipe if available, such as : ingredients, nutrition info, preparation, etc...'''
    url = 'https://tasty.p.rapidapi.com/recipes/detail'
    headers = {'x-rapidapi-host': 'tasty.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'id': id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
