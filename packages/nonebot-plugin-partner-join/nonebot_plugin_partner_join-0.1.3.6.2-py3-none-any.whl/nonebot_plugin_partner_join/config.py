from pydantic import BaseModel

class Config(BaseModel):
    params: dict[str, list[str]] = {
    "skip_gif": ["-s", "s", "stop"],
    }
    self_params: dict[str, list[str]] = {
    "self_join": ["自己", "me", "我"]
    }
    background_params: dict[str, list[str]] = {
    "background.gif": ["default"],   
    }
    join_commands: dict[str, list[str]] = {
    "加入": ["join", "旅行伙伴加入"]
    }
    gif_fps: int = 30
    total_duration: int = 2
    max_turns: int = 4
    rotation_direction: int = -1
