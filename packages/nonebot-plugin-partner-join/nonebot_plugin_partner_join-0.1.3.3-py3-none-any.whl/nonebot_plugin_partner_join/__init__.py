import os
import time
import io
import re
import datetime
from PIL import Image, ImageDraw, ImageSequence
import imageio
import httpx
from nonebot.plugin import PluginMetadata
from nonebot import on_command, get_driver
from nonebot.adapters import Bot, Event, Message
from nonebot.adapters.onebot.v11 import Message, MessageSegment, Bot, Event
from nonebot.params import Arg, CommandArg
from nonebot.typing import T_State
from nonebot import require
require("nonebot_plugin_alconna")
from nonebot_plugin_alconna.uniseg.tools import reply_fetch
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler
from tarina import LRU
from dotenv import load_dotenv
from typing import Optional
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="nonebot_plugin_partner_join",
    description="NoneBot2 插件 用于生成舞萌DX(maimaiDX)旅行伙伴加入图片(旋转gif) 也可用于类似嵌入相应圆形框架图片生成(如将图片嵌入校徽)",
    usage="",
    type="application",
    homepage="https://github.com/YuuzukiRin/nonebot_plugin_partner_join",
    supported_adapters={"~onebot.v11"},
)

join_DIR = os.path.join(os.getcwd(), 'data', 'join')

@scheduler.scheduled_job('cron', hour=0, minute=0)
async def clear_join_daily():
    today = datetime.datetime.now().strftime('%Y-%m-%d')

    if os.path.exists(join_DIR):
        for filename in os.listdir(join_DIR):
            file_path = os.path.join(join_DIR, filename)
            try:
                if os.path.isfile(file_path):
                    os.remove(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception:
                pass
                
class ReplyMergeExtension:
    def __init__(self, add_left: bool = False, sep: str = " "):
        self.add_left = add_left
        self.sep = sep

    async def message_provider(self, event, state, bot, use_origin: bool = True):
        if event.get_type() != "message":
            return
        try:
            msg = event.get_message()
        except (NotImplementedError, ValueError):
            return

        original_message = msg.get_plain_text() if hasattr(msg, 'get_plain_text') else str(msg)
        
        if not (reply := await reply_fetch(event, bot)):
            return original_message
        if not reply.msg:
            return original_message
        
        reply_msg = reply.msg
        reply_message = reply_msg if not isinstance(reply_msg, str) else str(reply_msg)
        
        if self.add_left:
            combined_message = f"{reply_message}{self.sep}{original_message}"
        else:
            combined_message = f"{original_message}{self.sep}{reply_message}"
        
        return combined_message

reply_merge = ReplyMergeExtension(add_left=True, sep="\n")

driver = get_driver()
PARAMS = driver.config.params
BACKGROUND_PARAMS = driver.config.background_params
JOIN_COMMANDS = driver.config.commands

for main_command, aliases in JOIN_COMMANDS.items():
    join = on_command(main_command, aliases=set(aliases), priority=5, block=True)

@join.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State, args: Message = CommandArg()):
    full_message = await reply_merge.message_provider(event, state, bot)
    
    for key in PARAMS.keys():
        state[key] = False
    
    for key, aliases in PARAMS.items():
        for alias in aliases:
            if full_message.endswith(alias):
                state[key] = True
                break
            
    selected_background = "background.gif"
    for bg_file, aliases in BACKGROUND_PARAMS.items():
        for alias in aliases:
            if alias in full_message:
                selected_background = bg_file
                break
    state["selected_background"] = selected_background       
            
    message_str = str(full_message)
    
    user_id = event.get_user_id()
    at_pattern = re.compile(r'\[CQ:at,qq=(\d+)\]')
    at_segments = at_pattern.findall(full_message)
    at_id = None
    if at_segments:
        at_id = at_segments[0]
    image_pattern = re.compile(r'\[CQ:image,[^\]]*\]')
    image_segments = image_pattern.findall(message_str)
    
    if image_segments:
        image_info = image_segments[0]
        state["image"] = image_info
        await join.send("旅行伙伴加入中...")
        state["image_processed"] = True
    elif at_id:
        state["image"] = "url=https://q4.qlogo.cn/headimg_dl?dst_uin={}&spec=640,".format(at_id)
        await join.send("旅行伙伴加入中...")
        state["image_processed"] = True
        state["image_at"] = True
    elif state.get("self_join", False):
        state["image"] = "url=https://q4.qlogo.cn/headimg_dl?dst_uin={}&spec=640,".format(user_id)
        await join.send("旅行伙伴加入中...")
        state["image_processed"] = True
        state["image_user"] = True
    else:
        state["awaiting_image"] = True
        await join.send("请选择要加入的旅行伙伴~(图片)")

@join.got("image")
async def handle_image(bot: Bot, event: Event, state: T_State, image: Message = Arg("image")):
    if state.get("image_processed", False):
        full_message = await reply_merge.message_provider(event, state, bot)
        message_str = str(full_message)
        user_id = event.get_user_id()
        at_pattern = re.compile(r'\[CQ:at,qq=(\d+)\]')
        at_segments = at_pattern.findall(full_message)
    
        if at_segments:
            at_id = at_segments[0]
        if state.get("image_at", False):
            image_info = "url=https://q4.qlogo.cn/headimg_dl?dst_uin={}&spec=640,".format(at_id)
            state["image"] = image_info
            state["image_at"] = False
        elif state.get("self_join", False):
            image_info = "url=https://q4.qlogo.cn/headimg_dl?dst_uin={}&spec=640,".format(user_id)
            state["image"] = image_info
            state["self_join"] = False
        else:       
            image_pattern = re.compile(r'\[CQ:image,[^\]]*\]')
            image_segments = image_pattern.findall(message_str)
            image_info = image_segments[0]
            state["image"] = image_info
            state["image_processed"] = False
    else:    
        image = image.get("image")
        image_info = str (image)
        if image_info:
            if state.get("awaiting_image", False):
                state["image"] = image_info
                await join.send("旅行伙伴加入中...")
                state["awaiting_image"] = False
            else:
                if state.get("image_processed", False):
                    state["image"] = image_info
                    state["image_processed"] = False
                else:
                    await join.finish("加入取消~") 
        else:
            await join.finish("加入取消~") 

    url_pattern = re.compile(r'url=([^,]+)')
    match = url_pattern.search(image_info)
    if match:
        image_url = match.group(1)
        image_url = image_url.replace("&amp;", "&")
    else:
        print("未找到图片URL")


    async with httpx.AsyncClient() as client:
        response = await client.get(image_url)
        img_data = response.content

    img = Image.open(io.BytesIO(img_data))

    # 剪切成圆形
    if state.get("skip_gif", False):
        # 创建一个虚拟的GIF路径，保存经过圆形剪裁的GIF
        gif_path = os.path.join("data/join_cache", "placeholder.gif")
        os.makedirs("data/join_cache", exist_ok=True)      
        # 如果GIF是动画的，保存动态GIF
        if getattr(img, "is_animated", False):
            frames = [frame.copy() for frame in ImageSequence.Iterator(img)]
            frames[0].save(gif_path, save_all=True, append_images=frames[1:], loop=0, duration=img.info.get("duration", 100))
        else:
            img = circle_crop(img)
            img.save(gif_path, format='GIF')

        state["skip_gif"] = False
    else:
        img = circle_crop(img)
        gif_path = create_rotating_gif(img)

    background_path = os.path.join(os.path.dirname(__file__), "background", state["selected_background"])
    final_gif_path = composite_images(background_path, gif_path)

    if os.path.exists(final_gif_path):
        await join.send(MessageSegment.image(f"file:///{os.path.abspath(final_gif_path)}"))
    else:
        print("生成的GIF图像文件不存在。")
    
    if os.path.exists(gif_path):
        os.remove(gif_path)

def circle_crop(img: Image.Image) -> Image.Image:
    """将图像裁剪成圆形，保留动态效果"""
    is_animated = getattr(img, "is_animated", False)
    if is_animated:
        frames = []
        for frame in ImageSequence.Iterator(img):
            cropped_frame = crop_single_frame(frame)
            frames.append(cropped_frame)

        output = frames[0]
        output.info = img.info

        gif_path = os.path.join("data/join", f"cropped_{int(time.time())}.gif")
        os.makedirs("data/join", exist_ok=True)
        output.save(gif_path, save_all=True, append_images=frames[1:], loop=0, duration=img.info.get("duration", 100))
        
        return Image.open(gif_path)
    else:
        return crop_single_frame(img)

def crop_single_frame(frame: Image.Image) -> Image.Image:
    """对单个帧进行圆形裁剪"""
    width, height = frame.size
    radius = min(width, height) // 2
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    center_x, center_y = width // 2, height // 2
    draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=255)
    output = Image.new("RGBA", (width, height))
    output.paste(frame, (0, 0), mask)
    output = output.crop((center_x - radius, center_y - radius, center_x + radius, center_y + radius))
    return output

load_dotenv(dotenv_path='.env.prod')

fps = int(os.getenv("GIF_FPS", 30))
total_duration = int(os.getenv("GIF_TOTAL_DURATION", 2))
max_turns = int(os.getenv("GIF_MAX_TURNS", 4))
rotation_direction = int(os.getenv("GIF_ROTATION_DIRECTION", -1))

def create_rotating_gif(img: Image.Image) -> str:
    """创建旋转GIF，保留动态效果"""
    frames = []
    num_frames = total_duration * fps
    max_angle = 360 * max_turns

    is_animated = getattr(img, "is_animated", False)
    original_frames = []

    if is_animated:
        original_frames = [frame.copy() for frame in ImageSequence.Iterator(img)]

        original_num_frames = len(original_frames)
        if original_num_frames == num_frames:
            scaled_frames = original_frames
        elif original_num_frames < num_frames:
            # 如果原始帧数少于目标帧数，重复帧以填充
            repeat_count = (num_frames // original_num_frames) + 1
            scaled_frames = (original_frames * repeat_count)[:num_frames]
        else:
            # 如果原始帧数多于目标帧数，选择间隔帧进行等比缩放
            factor = original_num_frames / num_frames
            scaled_frames = [original_frames[int(i * factor)] for i in range(num_frames)]
    else:
        # 如果是静态图像，将静态图像处理为动态
        original_frames = [img] * num_frames
        scaled_frames = original_frames

    accel_duration = total_duration / 2  # 加速阶段和减速阶段时间相同
    accel_frames = accel_duration * fps
    decel_frames = accel_duration * fps
    total_frames = accel_frames + decel_frames

    # 计算加速阶段的角加速度
    accel_angle_change = 2 * max_angle / (accel_frames / fps) ** 2

    for i in range(num_frames):
        if i < accel_frames:
            # 加速阶段
            angle = 0.5 * accel_angle_change * (i / fps) ** 2
        else:
            # 减速阶段
            time_in_decel = i - accel_frames
            # 减速阶段角度计算
            angle = max_angle - 0.5 * accel_angle_change * ((accel_frames - time_in_decel) / fps) ** 2

        frame = scaled_frames[i].rotate(rotation_direction * angle, resample=Image.BICUBIC)
        frames.append(frame)

    output_dir = "data/join"
    os.makedirs(output_dir, exist_ok=True)
    
    gif_path = os.path.join(output_dir, f"rotating_{int(time.time())}.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=int(1000/fps), loop=0)
    
    return gif_path

def find_circle_diameter(mask: Image.Image) -> int:
    """计算掩码中圆形区域的直径"""
    width, height = mask.size
    center_x, center_y = width // 2, height // 2
    top_y = 0
    for y in range(center_y, -1, -1):
        if mask.getpixel((center_x, y)) > 0:
            top_y = y
            break
    bottom_y = height - 1
    for y in range(center_y, height):
        if mask.getpixel((center_x, y)) > 0:
            bottom_y = y
            break
    diameter = bottom_y - top_y + 1
    return diameter

def find_circle_center(mask: Image.Image) -> (int, int):
    """计算掩码中圆形区域的圆心"""
    width, height = mask.size
    center_x, center_y = width // 2, height // 2
    top_y = 0
    bottom_y = height - 1
    for y in range(center_y, -1, -1):
        if mask.getpixel((center_x, y)) > 0:
            top_y = y
            break
    for y in range(center_y, height):
        if mask.getpixel((center_x, y)) > 0:
            bottom_y = y
            break
    circle_center_y = top_y + (bottom_y - top_y) // 2
    return center_x, circle_center_y

def resize_gif_to_diameter(img: Image.Image, diameter: int) -> Image.Image:
    """将GIF图像等比缩放到指定的直径"""
    img = img.resize((diameter, diameter), Image.LANCZOS)
    return img

def composite_images(background_path: str, gif_path: str) -> str:
    """将GIF图像粘贴到背景图中"""
    background = Image.open(background_path).convert("RGBA")
    mask = background.split()[-1].convert("L")
    diameter = find_circle_diameter(mask)
    circle_center_x, circle_center_y = find_circle_center(mask)
    gif = Image.open(gif_path)

    gif_frames = []
    delays = []
    while True:
        try:
            frame = gif.copy()
            gif_frames.append(frame)
            delays.append(gif.info['duration'])
            gif.seek(gif.tell() + 1)
        except EOFError:
            break
    
    gif_frames = [circle_crop(frame) for frame in gif_frames]
    gif_frames = [resize_gif_to_diameter(frame, diameter) for frame in gif_frames]

    composite_frames = []
    for frame in gif_frames:
        composite_frame = background.copy()
        composite_frame.paste(frame, (circle_center_x - diameter // 2, circle_center_y - diameter // 2), frame.split()[-1])
        composite_frames.append(composite_frame)

    final_gif_path = os.path.join("data", "join", f"composite_{int(time.time())}.gif")
    
    composite_frames[0].save(
        final_gif_path,
        save_all=True,
        append_images=composite_frames[1:],
        duration=delays,
        loop=0
    )
    
    return final_gif_path