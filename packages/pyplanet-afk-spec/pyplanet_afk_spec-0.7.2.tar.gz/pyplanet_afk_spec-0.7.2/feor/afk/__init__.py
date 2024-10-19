import logging
import asyncio

from pyplanet.apps.config import AppConfig

from pyplanet.apps.core.maniaplanet import callbacks as mp_signals
from .views import AFKWidget
from pyplanet.core.signals import pyplanet_start_after
from pyplanet.contrib.setting import Setting

logger = logging.getLogger(__name__)


class AfkSpecApp(AppConfig):
    game_dependencies = ['trackmania']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.widget = AFKWidget(self)
        self.setting_afk_timeout = Setting(
            'afk_timeout', 'AFK Duration Allowed', Setting.CAT_BEHAVIOUR, type=int,
            description='Duration players can stay inactive until they are declared AFK, in seconds.',
            default=120
        )
        
        self.setting_afk_timeout_check_frequency = Setting(
            'afk_timeout_check_frequency', 'AFK Check Frequency', Setting.CAT_BEHAVIOUR, type=int,
            description="Time to wait before querying a player's inputs again, in ms. Lower values are more precise but may impact performance.",
            default=1000)
        
        self.setting_afk_timeout_wait = Setting(
            'afk_timeout_wait', 'Time between AFK checks', Setting.CAT_BEHAVIOUR, type=int,
            description='Extra time to wait before checking again whether a player is AFK, in seconds.',
            default=10)
        
        self.setting_afk_message_display = Setting(
            'afk_message_display', 'Display AFK Message', Setting.CAT_BEHAVIOUR, type=bool,
            description='If this setting is enabled, a message will be displayed when a player is moved to spectator.',
            default=True
        )

        self.setting_afk_message = Setting(
            'afk_message', 'AFK Message', Setting.CAT_DESIGN, type=str,
            description='Message to display when a player is moved to spectator. Use \'{nickname}\' to insert the player\'s nickname.',
            default='{nickname}$z$s$fff has been moved to spectator due to inactivity.'
        )
        
        self.setting_rejoin_button_display = Setting(
            'rejoin_button_display', 'Display Rejoin Button', Setting.CAT_DESIGN, type=bool,
            description='If this setting is enabled, a button will be displayed to allow players to rejoin the game when they are in spectator mode.',
            default=True
        )
        
        
        
    async def on_start(self):
        self.context.signals.listen(mp_signals.player.player_connect, self.player_connect)
        self.context.signals.listen(mp_signals.map.map_begin, self.map_start)
        self.context.signals.listen(pyplanet_start_after, self.on_after_start)
        self.context.signals.listen(mp_signals.player.player_info_changed, self.handle_player_info_changed)
        
        # Register settings
        await self.context.setting.register(self.setting_afk_timeout)
        await self.context.setting.register(self.setting_afk_timeout_check_frequency)
        await self.context.setting.register(self.setting_afk_timeout_wait)
        await self.context.setting.register(self.setting_afk_message_display)
        await self.context.setting.register(self.setting_afk_message)
        await self.context.setting.register(self.setting_rejoin_button_display)
        
    async def handle_player_info_changed(self, player_login, is_spectator, **kwargs):
        await self.widget.refresh(player_login)
        
    async def player_connect(self, player, **kwargs):
        await self.widget.display(player)

    async def map_start(self, *args, **kwargs):
        await self.widget.display()

    async def on_after_start(self, *args, **kwargs):
        await asyncio.sleep(1)
        asyncio.ensure_future(asyncio.gather(*[
            self.player_connect(p) for p in self.instance.player_manager.online
        ]))
