# afk

PyPlanet plugin to detect AFK players and move them into spectator mode.

This plugin works by repeatedly querying the player's inputs and checking if the player is currently steering, braking or pressing the gas pedal.
If the player is found not to be pressing any inputs for a (configurable) period of time, they are considered AFK and moved to spectator.

The plugin also lets you adda a button to rejoin the game for new players who may be confused with the spectator mode.

### Installation

    python -m pip install --upgrade pyplanet-afk-spec

Then open `settings/apps.py` with a text editor and append to the list in 'default':

    'feor.afk'

### Configuration

- AFK Duration Allowed: Duration players can stay inactive until they are declared AFK, in seconds. [Default: 120]

- AFK Check Frequency: Time to wait before querying a player's inputs again, in ms. Lower values may impact performance. [Default: 1000]

- AFK Wait: Time to wait before checking again whether a player is AFK, in seconds. [Default: 10]

- Display AFK Message: If this setting is enabled, a message will be displayed when a player is moved to spectator. [Default: True]

- AFK Message: Message to display when a player is moved to spectator. Use `{nickname}` to insert the player's nickname. [Default: `{nickname}$z has been moved to spectator due to inactivity.`]

- Display Rejoin Button: If this setting is enabled, players in spectator mode will see a "Rejoin Game" button at the center of the screen.


### Changelog

0.7.2

- Renamed plugin

0.7.1

- Moved position of rejoin button and added icon

0.7.0

- Added a rejoin button that displays for players in spectator mode
- Added a setting to disable the rejoin button

0.6.0

- Removed Grace Period/Timeout Delay settings in favor of a single AFK Wait setting
- Added Display AFK Message setting
- Added AFK Message setting
- Refactored AFK checking code and removed some checks (PendingEvents, UISequence)
