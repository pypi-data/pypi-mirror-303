from abc import ABCMeta
from enum import EnumType, IntEnum

from MrKWatkins.OakEmu.Machines.ZXSpectrum import Keys as DotNetKeys  # noqa
from MrKWatkins.OakEmu.Machines.ZXSpectrum.Game import Game as DotNetGame  # noqa

from oakemu.machines.zxspectrum.keys import Keys
from oakemu.machines.zxspectrum.stepresult import StepResult
from oakemu.machines.zxspectrum.zxspectrum import ZXSpectrum


class Game(metaclass=ABCMeta):  # noqa: B024
    def __init__(self, game: DotNetGame, action_type: EnumType):
        if not issubclass(action_type, IntEnum):
            raise TypeError("action is not an IntEnum.")

        game.InitializeAsync().Wait()

        self._game = game
        self._zx = ZXSpectrum(game.Spectrum)
        self._action_type = action_type
        self._actions = [e for e in action_type]

    @property
    def spectrum(self) -> ZXSpectrum:
        return self._zx

    @property
    def name(self) -> str:
        return self._game.Name

    @property
    def actions(self) -> list:
        return self._actions

    @property
    def action(self):
        return self._action_type(self._game.ActionIndex)

    @action.setter
    def action(self, action):
        self._game.ActionIndex = int(action)

    def reset(self) -> None:
        self._game.Reset()

    def start_episode(self) -> None:
        self._game.StartEpisode()

    def execute_step(self, action) -> StepResult:
        return StepResult(self._game.ExecuteStep(int(action)))

    def get_random_action(self):
        return self._game.GetRandomAction()

    def keys_to_action(self, keys: Keys):
        return self._action_type(self._game.KeysToActionIndex(DotNetKeys(int(keys))))

    def action_to_keys(self, action):
        return Keys(int(self._game.ActionIndexToKeys(int(action))))
