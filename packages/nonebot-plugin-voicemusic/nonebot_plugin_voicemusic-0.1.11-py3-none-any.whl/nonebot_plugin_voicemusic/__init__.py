import httpx
from nonebot import on_command
from nonebot import get_plugin_config
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from .config import Config


# 插件元数据
__plugin_meta__ = PluginMetadata(
    name="语音点歌",
    description="用语音收听点歌",
    usage="点歌 歌名 可选歌手",
    config=Config,
    type="application",
    homepage="https://github.com/Onimaimai/nonebot-plugin-voicemusic",
    supported_adapters={"~onebot.v11"},
)

# 加载插件配置
plugin_config = get_plugin_config(Config)
uin = plugin_config.uin
skey = plugin_config.skey
if not uin or not skey:
    logger.warning("语音点歌未配置 UIN 或 SKEY，建议在 .env 文件中进行配置")


# 注册命令 "点歌"
music_handler = on_command("点歌", aliases={"点一首歌"}, priority=5)

@music_handler.handle()
async def handle_music_request(args: Message = CommandArg()):
    """处理用户的点歌请求"""
    music_name = args.extract_plain_text().strip()  # 获取指令参数

    if not music_name:
        await music_handler.send("请提供歌曲名称，例如：点歌 告白气球")
        return

    await music_handler.send(f"收到点歌请稍等...")

    # 获取音乐源 URL
    src = await get_music_src(music_name)

    if src:

        if content := (await download_audio(src)):
            await music_handler.finish(MessageSegment.record(content))
        else:
            await music_handler.finish("音频下载失败，请稍后再试。")
    else:
        await music_handler.finish("未能找到该音乐，请检查名称是否正确。")


# 音频下载函数
async def download_audio(audio_url: str) -> bytes | None:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(audio_url)
            if response.status_code == 200:
                return response.content
            else:
                logger.error(f"下载音频文件失败，状态码: {response.status_code}")
                return None
        except Exception as e:
            logger.error(f"下载音频文件发生异常: {repr(e)}")
            return None


# 获取音乐直链函数
async def get_music_src(keyword: str) -> str | None:
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
