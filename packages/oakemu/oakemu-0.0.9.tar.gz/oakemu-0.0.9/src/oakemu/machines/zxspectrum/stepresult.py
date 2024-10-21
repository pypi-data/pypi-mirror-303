from MrKWatkins.OakEmu.Machines.ZXSpectrum.Game import StepResult as CSharpStepResult  # noqa

from oakemu.machines.zxspectrum.gameresult import GameResult


class StepResult:
    def __init__(self, step_result: CSharpStepResult):
        self.result: GameResult = GameResult(int(step_result.Result))
        self.score_increase = step_result.ScoreIncrease
