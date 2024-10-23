from .constants import POSITION_BY_TEAM

def get_position_id(pin_setting, team):
    return pin_setting.get(
        "player_id",
        POSITION_BY_TEAM.get(team, {}).get(pin_setting.get("position"), None),
    )
