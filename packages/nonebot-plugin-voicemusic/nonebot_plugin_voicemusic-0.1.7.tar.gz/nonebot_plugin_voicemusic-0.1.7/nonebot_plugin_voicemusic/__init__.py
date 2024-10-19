import re
import shutil
import httpx
from pathlib import Path
from pydub import AudioSegment
from graiax import silkcoder
from nonebot import require
from nonebot import on_command
from nonebot import get_plugin_config
from .config import Config
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, Message, MessageSegment, Event
from .config import Config

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store

# 插件元数据
__plugin_meta__ = PluginMetadata(
    name="语音点歌",
    description="用语音收听点歌",
    usage="点歌 歌名 可选歌手",
    type="application",
    homepage="https://github.com/Onimaimai/nonebot-plugin-voicemusic",
    supported_adapters={"~onebot.v11"},
)

# 获取插件的缓存和数据目录
plugin_cache_dir: Path = store.get_plugin_cache_dir()
temp_folder = plugin_cache_dir / "temp"
temp_folder.mkdir(exist_ok=True)  # 创建temp目录

# 加载插件配置
plugin_config = get_plugin_config(Config)
uin = plugin_config.uin
skey = plugin_config.skey
if not uin or not skey:
    logger.warning("语音点歌未配置 UIN 或 SKEY，建议在 .env 文件中进行配置")


# 注册命令 "点歌"
music_handler = on_command("点歌", aliases={"点一首歌"}, priority=5)

@music_handler.handle()
async def handle_music_request(bot: Bot, event: Event, args: Message = CommandArg()):
    """处理用户的点歌请求"""
    music_name = args.extract_plain_text().strip()  # 获取指令参数

    if not music_name:
        await bot.send(event, "请提供歌曲名称，例如：点歌 告白气球")
        return

    await bot.send(event, f"收到点歌请稍等...\n《{music_name}》")

    # 获取音乐源 URL
    src = await get_music_src(music_name)

    if src:
        # 设置临时文件路径
        mp3_path = temp_folder / "temp.mp3"
        wav_path = temp_folder / "temp.wav"
        flac_path = temp_folder / "temp.flac"

        # 根据音频类型选择保存路径
        if re.search("flac", src):
            save_path = flac_path
        elif re.search("mp3", src):
            save_path = mp3_path
        else:
            save_path = wav_path

        # 下载音乐并转换为 SILK 格式
        if await download_audio(src, save_path):
            silk_file = convert_to_silk(save_path)
            if silk_file:
                await bot.send(event, MessageSegment.record(silk_file))
            else:
                await bot.send(event, "音频转换失败，请稍后再试。")
        else:
            await bot.send(event, "音频下载失败，请稍后再试。")
    else:
        await bot.send(event, "未能找到该音乐，请检查名称是否正确。")


# 音频下载函数
async def download_audio(audio_url: str, save_path: str) -> bool:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(audio_url)
            if response.status_code == 200:
                with open(save_path, "wb") as file:
                    file.write(response.content)
                logger.info(f"音频文件已成功保存为 '{save_path}'")
                return True
            else:
                logger.error(f"下载音频文件失败，状态码: {response.status_code}")
                return False
        except Exception as e:
            logger.error(f"下载音频文件发生异常: {str(e)}")
            return False

# 音频转换函数
def convert_to_silk(save_path: Path) -> str:
    silk_path = temp_folder / "temp.silk"
    wav_path = str(save_path)  # Convert Path to string

    if str(save_path).endswith(".mp3"):
        logger.info(f"正在将 MP3 文件 {save_path} 转换为 WAV")
        wav_path = temp_folder / "temp.wav"
        audio = AudioSegment.from_mp3(str(save_path))
        audio.export(str(wav_path), format="wav")
        logger.info(f"MP3 文件已成功转换为 WAV 文件 {wav_path}")

    elif str(save_path).endswith(".flac"):
        logger.info(f"正在将 FLAC 文件 {save_path} 转换为 WAV")
        wav_path = temp_folder / "temp.wav"
        audio = AudioSegment.from_file(str(save_path), format="flac")
        audio.export(str(wav_path), format="wav")
        logger.info(f"FLAC 文件已成功转换为 WAV 文件 {wav_path}")

    try:
        silkcoder.encode(str(wav_path), str(silk_path))
        logger.info(f"已将 WAV 文件 {wav_path} 转换为 SILK 文件 {silk_path}")
        return str(silk_path)
    except Exception as e:
        logger.error(f"SILK 文件转换失败: {str(e)}")
        return None

# 获取音乐直链函数
async def get_music_src(keyword: str) -> str:
    """根据关键词获取音乐直链"""
    url = "https://api.xingzhige.com/API/QQmusicVIP/"
    params = {
        "name": keyword,
        "uin": uin,
        "skey": skey,
        "max": 3,
        "n": 1
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            if data and data.get("code") == 0:
                return data["data"]["src"]
            else:
                logger.error(f"获取音乐直链失败: {data}")
                return None
        except httpx.HTTPStatusError as e:
            logger.error(f"获取音乐直链失败: {str(e)}")
            return None
