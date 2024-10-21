"""Crawl wikipedia, wikimedia via cli

** Wiki Documentation **
https://www.mediawiki.org/wiki/API:Main_page

"""

# import shlex
import json
from subprocess import PIPE, Popen
from typing import Dict, Optional, Union

from pydantic import BaseModel, Field, field_validator


def exec_cli(command: str, is_dict: bool) -> Union[Dict, str]:
    """
    Run a shell command using subprocess and return the output.

    Args:
        command: The one-liner.
        is_dict (bool): If True, return a dictionary.
            Otherwise return the raw output as a string.
    """
    try:
        # print(f'GO CMND: {command}')
        process = Popen(command, stdout=PIPE, stderr=PIPE, shell=True)
        output, error = process.communicate()
        output = output.decode('utf-8').strip()
        error = error.decode('utf-8').strip()

        if is_dict:
            try:
                return json.loads(output)
            except json.JSONDecodeError:
                print("Error: not a valid dict (json)! Output=\n{output}")
                return None
        else:
            return output

    except Exception as e:
        print(f"Command failed with error: {e}")
        return None


def endpoint_baseitem(title: str) -> str:
    return f'https://en.wikipedia.org/w/api.php?action=query&prop=pageprops&ppprop=wikibase_item&format=json&redirects=1&titles={title}'


def endpoint_entity(item_id: str) -> str:
    return f"https://www.wikidata.org/wiki/Special:EntityData/{item_id}.json"


def cli_entity_profile(item_id: str) -> str:
    """Create the CLI command to get wiki entity profile

    Parameters
    ----------
    endpoint : str
        Such as
        https://www.wikidata.org/wiki/Special:EntityData/Q312.json

    Returns
    -------
    str
        The cli command such as

        curl -s "https://www.wikidata.org/wiki/Special:EntityData/Q312.json" | jq '
        {
          image_url: ("https://commons.wikimedia.org/wiki/Special:FilePath/" + .entities.Q312.claims.P18[0].mainsnak.datavalue.value),
          logo_url: ("https://commons.wikimedia.org/wiki/Special:FilePath/" + .entities.Q312.claims.P154[0].mainsnak.datavalue.value),
          description: .entities.Q312.descriptions.en.value
        } '
    """
    ep = endpoint_entity(item_id=item_id)
    return f'''curl -s -L "{ep}" | jq '{{image_url: ("https://commons.wikimedia.org/wiki/Special:FilePath/" + .entities.{item_id}.claims.P18[0].mainsnak.datavalue.value), logo_url: ("https://commons.wikimedia.org/wiki/Special:FilePath/" + .entities.{item_id}.claims.P154[0].mainsnak.datavalue.value), description: .entities.{item_id}.descriptions.en.value}}' '''


def get_item_id(endpoint: str) -> Optional[str]:
    """Get `wikidata` Item-ID from the endpoint

    Parameters
    ----------
    endpoint : str
        A wiki api endpoint

    Returns
    -------
    Optional[str]
        The item ID
    """

    cmd = f'''curl -s -L "{endpoint}" | jq -r '.query.pages[] | .pageprops.wikibase_item' '''
    item = exec_cli(cmd, is_dict=False)
    return item


def get_entity_profile(
    item_id: str
) -> Dict[str, str]:
    """Request the basic entity information given the api

    Example:

    For "https://www.wikidata.org/wiki/Special:EntityData/Q312.json"
    {
        "image_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Apple park cupertino 2019.jpg",
        "logo_url": "https://commons.wikimedia.org/wiki/Special:FilePath/Apple logo black.svg",
        "description": "American multinational technology company based in Cupertino, California"
    }

    Parameters
    ----------
    item_id: str

    Returns
    -------
    Dict[str, str]
        - image source
        - logo image source
        - description (english)
    """
    cmd = cli_entity_profile(item_id=item_id)
    resp = exec_cli(cmd, is_dict=True)
    return resp

def is_image(s:str):
    # Ignore the '.ico' cause its for microsoft
    imgformats = ('svg', 'jpeg', 'png', 'jpg', 'gif', 'webp', 'tif', 'tiff')
    suffix = s.lower().rsplit('.', 1)[-1]
    return suffix in imgformats
 
class WikiEntityProfile(BaseModel):
    image_url: str = Field(default='', description='Source of thumbnail')
    logo_url: str = Field(default='', description='Source image for logo')
    description: str = Field(default='', description='English description')

    @field_validator('image_url', mode='before')
    def validate_image(cls, v:str):
        if is_image(v):
           return v
        return ''

    @field_validator('logo_url', mode='before')
    def validate_logo(cls, v:str):
        if is_image(v):
           return v
        return ''

    @field_validator('description', mode='before')
    def validate_description(cls, v:str):
        return v.capitalize()


class WikiApiCrawler:

    @classmethod
    def get_profile(
        cls,
        entity_title: str
    ) -> WikiEntityProfile:
        api_base_entity = endpoint_baseitem(title=entity_title)
        item_id = get_item_id(endpoint=api_base_entity)
        profile = get_entity_profile(item_id=item_id)
        resp = WikiEntityProfile(**profile)
        return resp


if __name__ == '__main__':
    test = 'Apache_Superset'
    test = 'Steve_Jobs'
    prof = WikiApiCrawler.get_profile(entity_title=test)
    print(prof.model_dump_json(indent=4))
