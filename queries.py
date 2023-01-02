# TODO - Move to database/
# TODO - Also create database/types.py and define db schema types

from random import randint
from typing import Optional
from supabase import create_client, Client
from data import SUPABASE_KEY, SUPABASE_URL

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# TODO - Validate order value? (1-4); or just return None?
def getDbResponsibleNameByOrderNr(order: int) -> str | None:         
    """Returns a responsible from the database corresponding to the order given.

    Args:
        order (`int`): The order number of the responsible to fetch.
    Returns:
        :class:`str | None`
    """
    dbResponsibleDictsList = supabase.table("responsabili_curatenie").select("nume").eq("order_nr", order).execute().data
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
    if (type == None):
        # Get the list of all greetings of any type
        dbGreetingsDictsList = supabase.table("greetings").select("greeting").execute().data
    else:
        # Only get the list of greetings of a specified type
        dbGreetingsDictsList = supabase.table("greetings").select("greeting").eq("type", type).execute().data
    if(len(dbGreetingsDictsList) > 0):
        randomIndex = randint(0, len(dbGreetingsDictsList) - 1)
        randomDataEntry = (dbGreetingsDictsList[randomIndex])
        return randomDataEntry['greeting'] 
    else: return None