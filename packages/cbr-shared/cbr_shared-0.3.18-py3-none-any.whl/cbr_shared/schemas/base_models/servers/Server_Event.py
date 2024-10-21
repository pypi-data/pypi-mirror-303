from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.helpers.Random_Guid    import Random_Guid


class Server_Event(Type_Safe):
    event_data : dict
    event_id   : Random_Guid
    event_type : str
    level      : str            = 'INFO'                # todo: see if need to use the normal level numbers 10, 20, 30, 40, 50, etc..
    message    : str
    server_id  : Random_Guid
    timestamp  : int