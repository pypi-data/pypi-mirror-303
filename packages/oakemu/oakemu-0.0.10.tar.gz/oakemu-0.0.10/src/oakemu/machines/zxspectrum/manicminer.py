from enum import IntEnum

from MrKWatkins.OakEmu.Machines.ZXSpectrum.Games import ManicMiner as CSharpManicMiner  # noqa

from oakemu.machines.zxspectrum.game import Game


class ManicMinerAction(IntEnum):
    NONE = (0,)
    MOVE_LEFT = (1,)
    MOVE_RIGHT = (2,)
    JUMP_UP = (3,)
    JUMP_LEFT = (4,)
    JUMP_RIGHT = 5


class ManicMiner(Game):
    def __init__(self):
        self._manic_miner = CSharpManicMiner()
        super().__init__(self._manic_miner, ManicMinerAction)

    @property
    def cavern(self) -> int:
        return self._manic_miner.Cavern

    @cavern.setter
    def cavern(self, value: int):
        self._manic_miner.Cavern = value

    @property
    def cavern_name(self) -> str:
        return self._manic_miner.CavernName

    @property
    def lives(self) -> int:
        return self._manic_miner.Lives

    @lives.setter
    def lives(self, value: int):
        self._manic_miner.Lives = value

    def start_episode(self, cavern: int = 0) -> None:
        self._game.StartEpisode(cavern)
