from dataclasses import dataclass

from osbot_utils.base_classes.Type_Safe import Type_Safe
from osbot_utils.helpers.Random_Guid    import Random_Guid
from osbot_utils.utils.Misc             import random_text


@dataclass
class Model__User__Config_Data(Type_Safe):
    user_id    : Random_Guid
    user_name  : str

    @staticmethod
    def random_user():
        user_id   = Random_Guid()
        user_name = random_text("an-random-user", lowercase=True)
        return Model__User__Config_Data(user_id=user_id, user_name=user_name)