import re
import shutil
import httpx
from pathlib import Path
from pydub import AudioSegment
from graiax import silkcoder
from nonebot import require
from nonebot import get_driver
from nonebot.plugin import PluginMetadata
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Bot, Message, MessageSegment, Event
from nonebot.plugin import on_message

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
    extra={
        "author": "QiYork",
        "version": "0.1.1"
    }
)

# 获取插件的缓存和数据目录
plugin_cache_dir: Path = store.get_plugin_cache_dir()
temp_folder = plugin_cache_dir / "temp"
temp_folder.mkdir(exist_ok=True)  # 创建temp目录

driver = get_driver()
uin = driver.config.uin or None
skey = driver.config.skey or None

music_handler = on_message(priority=999)

@music_handler.handle()
async def handle_music_request(bot: Bot, event: Event):
    receive_text = event.get_plaintext().strip()

    MUSIC_PATTERN = re.compile(r"点歌\s+(.+)")
    match = MUSIC_PATTERN.search(receive_text)

    if match:
        music_name = match.group(1)
        await bot.send(event, "收到点歌，请稍等...")        
        src = await get_music_src(music_name)

        if src:
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
    else:
        return

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
