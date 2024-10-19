from pyplanet.views.generics.widget import WidgetView
import asyncio


class AFKWidget(WidgetView):
    widget_x = 0
    widget_y = 50
    z_index = 130
    template_name = 'afk/AFK.xml'

    def __init__(self, app):
        super().__init__(self)
        self.app = app
        self.manager = app.context.ui
        self.id = 'pyplanet__AFK__Handling'
        self.subscribe("Player_AFK", self.handle_player_afk)
        self.subscribe("Player_Rejoin", self.action_player_rejoin)
        
    
    async def get_context_data(self):
        context = await super().get_context_data()
        self.afk_timeout = await self.app.setting_afk_timeout.get_value()
        self.afk_timeout_check_frequency = await self.app.setting_afk_timeout_check_frequency.get_value()
        self.afk_timeout_wait = await self.app.setting_afk_timeout_wait.get_value()
        self.rejoin_button_display = await self.app.setting_rejoin_button_display.get_value()
        context.update({'afktimeout': self.afk_timeout,
                        'afktimeoutcheckfrequency': self.afk_timeout_check_frequency,
                        'afktimeoutwait': self.afk_timeout_wait,
                        'rejoinbuttondisplay': self.rejoin_button_display
                        })
        return context
    
    async def handle_player_afk(self, player, action, values, *args, **kwargs):
        await self.app.instance.gbx('ForceSpectator', player.login, 3)
        afk_message = await self.app.setting_afk_message.get_value()
        if await self.app.setting_afk_message_display.get_value():
            await self.app.instance.chat(afk_message.format(nickname=player.nickname))
            
    async def action_player_rejoin(self, player, action, values, *args, **kwargs):
        print("Player rejoin")
        await self.app.instance.gbx('ForceSpectator', player.login, 2)
        await self.app.instance.gbx('ForceSpectator', player.login, 0)

    async def get_per_player_data(self, login):
        context = await super().get_per_player_data(login)
        player = await self.app.instance.player_manager.get_player(login)
        context["is_spec"] = player.flow.is_spectator

        return context