# TODO - Move to database/
# TODO - Also create database/types.py and define db schema types

from random import randint
from typing import Optional
from supabase import create_client, Client
from data import SUPABASE_KEY, SUPABASE_URL

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# TODO - Validate function output?
def getDbResponsibleNameByOrderNr(order: int) -> str | None:         
    """Returns a responsible from the database corresponding to the order given.

    Args:
        order (`int`): The order number of the responsible to fetch.
    Returns:
        :class:`str | None`
    """
    if not isinstance(order, int):
        raise TypeError("Input must be an integer.")
    # TODO - define 1 and 4 somewhere
    # TODO - hardcoding this doesn't seem like a good idea
    if order < 1 or order > 4:
        raise ValueError("Input must be between 1 and 4.")

    dbResponsibleDictsList = supabase.table("responsabili_curatenie").select("nume").filter("order_nr", "eq", order).execute().data
    if(len(dbResponsibleDictsList) > 0):
        return dbResponsibleDictsList[0]['nume']
    else: return None

def getDbRandomGreeting(type: Optional[str] = None) -> str | None:         
    """Returns a random greeting from the database of the specified type (or any type if omitted) if it finds one.

    Args:
        type (`str`): Optional parameter. The type name of the greeting to fetch. If left empty, a greeting of any type will be fetched.
    Returns:
        :class:`str | None`
    """
    if (type is not None) and (not isinstance(type, str)):
        raise TypeError("Input must be a string.")
    # TODO - Value error if not a supported type

    if (type == None):
        # Get the list of all greetings of any type
        dbGreetingsDictsList = supabase.table("greetings").select("greeting").execute().data
    else:
        # Only get the list of greetings of a specified type
        dbGreetingsDictsList = supabase.table("greetings").select("greeting").filter("type", "eq", type).execute().data
    if(len(dbGreetingsDictsList) > 0):
        randomIndex = randint(0, len(dbGreetingsDictsList) - 1)
        randomDataEntry = (dbGreetingsDictsList[randomIndex])
        return randomDataEntry['greeting'] 
    else: return None