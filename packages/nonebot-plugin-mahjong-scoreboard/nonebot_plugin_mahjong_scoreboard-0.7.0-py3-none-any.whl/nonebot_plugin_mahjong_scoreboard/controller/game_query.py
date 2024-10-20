from datetime import datetime, date, timedelta, time

from nonebot import Bot
from ssttkkl_nonebot_utils.errors.errors import BadRequestError, QueryError
from ssttkkl_nonebot_utils.interceptor.handle_error import handle_error

from .mapper.game_mapper import map_game, map_game_lite
from .mapper.pagination_mapper import map_pagination
from .mg import matcher_group
from .utils.dep import GroupDep, UnaryArg, UserDep
from .utils.general_handlers import require_store_command_args, require_platform_group_id, require_platform_user_id
from .utils.parse import parse_int_or_error
from .utils.send_msg import send_msg
from ..model import Group, User
from ..service import game_service
from ..service.game_service import get_games
from ..utils.nickname import get_user_nickname
from ..utils.nonebot import default_cmd_start

# =============== 查询对局 ===============
query_by_code_matcher = matcher_group.on_command("查询对局", aliases={"对局"}, priority=5)
query_by_code_matcher.__help_info__ = f"{default_cmd_start}查询对局 [<编号>]"

require_store_command_args(query_by_code_matcher)
require_platform_group_id(query_by_code_matcher)


@query_by_code_matcher.handle()
@handle_error()
async def query_by_code(group: Group = GroupDep(),
                        game_code=UnaryArg(parser=lambda x: parse_int_or_error(x, '对局编号'))):
    if game_code is None:
        raise BadRequestError("请指定对局编号")

    game = await game_service.get_game(game_code, group.id)
    if game is None:
        raise QueryError("未找到指定对局")

    msg = await map_game(game, detailed=True)
    await send_msg(msg)


# ========== 个人最近对局 ==========
query_user_recent_games_matcher = matcher_group.on_command("个人最近对局", priority=5)
query_user_recent_games_matcher.__help_info__ = f"{default_cmd_start}个人最近对局 [@<用户>]"

require_store_command_args(query_user_recent_games_matcher)
require_platform_group_id(query_user_recent_games_matcher)
require_platform_user_id(query_user_recent_games_matcher)


@query_user_recent_games_matcher.handle()
@handle_error()
async def query_user_recent_games(bot: Bot,
                                  group: Group = GroupDep(),
                                  user: User = UserDep()):
    end_time = datetime.combine(date.today() + timedelta(days=1), time())
    start_time = datetime.combine(end_time - timedelta(days=7), time())

    games = await get_games(group.id, user.id, reverse_order=True, time_span=(start_time, end_time))
    msgs = await map_pagination(games.data, map_game_lite)
    if games.total != 0:
        msgs.insert(0, f"以下是[{await get_user_nickname(bot, user.platform_user_id, group.platform_group_id)}]"
                       f"最近七天的对局：")

        await send_msg(*msgs)
    else:
        raise QueryError("用户最近七天还没有进行过对局")


# ========== 群最近对局 ==========
query_group_recent_games_matcher = matcher_group.on_command("群最近对局", aliases={"最近对局"}, priority=5)
query_group_recent_games_matcher.__help_info__ = f"{default_cmd_start}群最近对局"

require_store_command_args(query_group_recent_games_matcher)
require_platform_group_id(query_group_recent_games_matcher)


@query_group_recent_games_matcher.handle()
@handle_error()
async def query_group_recent_games(group=GroupDep()):
    end_time = datetime.combine(date.today() + timedelta(days=1), time())
    start_time = datetime.combine(end_time - timedelta(days=7), time())

    games = await get_games(group.id, reverse_order=True, time_span=(start_time, end_time))
    msgs = await map_pagination(games.data, map_game_lite)
    if games.total != 0:
        msgs.insert(0, f"以下是本群最近七天的对局：")

        await send_msg(*msgs)
    else:
        raise QueryError("本群最近七天还没有进行过对局")


# ========== 个人未完成对局 ==========
query_user_uncompleted_games_matcher = matcher_group.on_command("个人未完成对局", priority=5)
query_user_uncompleted_games_matcher.__help_info__ = f"{default_cmd_start}个人未完成对局 [@<用户>]"

require_store_command_args(query_user_uncompleted_games_matcher)
require_platform_group_id(query_user_uncompleted_games_matcher)
require_platform_user_id(query_user_uncompleted_games_matcher)


@query_user_uncompleted_games_matcher.handle()
@handle_error()
async def query_user_uncompleted_games(bot: Bot,
                                       group=GroupDep(),
                                       user: User = UserDep()):
    games = await get_games(group.id, user.id, uncompleted_only=True, reverse_order=True)
    msgs = await map_pagination(games.data, map_game_lite)
    if games.total != 0:
        msgs.insert(0, f"以下是[{await get_user_nickname(bot, user.platform_user_id, group.platform_group_id)}]"
                       f"的未完成对局：")

        await send_msg(*msgs)
    else:
        raise QueryError("用户没有未完成的对局")


# ========== 群未完成对局 ==========
query_group_uncompleted_games_matcher = matcher_group.on_command("群未完成对局", aliases={"未完成对局"}, priority=5)
query_group_uncompleted_games_matcher.__help_info__ = f"{default_cmd_start}群未完成对局"

require_store_command_args(query_group_uncompleted_games_matcher)
require_platform_group_id(query_group_uncompleted_games_matcher)


@query_group_uncompleted_games_matcher.handle()
@handle_error()
async def query_group_uncompleted_games(group=GroupDep()):
    games = await get_games(group.id, uncompleted_only=True, reverse_order=True)
    msgs = await map_pagination(games.data, map_game_lite)
    if games.total != 0:
        msgs.insert(0, f"以下是本群的未完成对局：")

        await send_msg(*msgs)
    else:
        raise QueryError("本群没有未完成的对局")
