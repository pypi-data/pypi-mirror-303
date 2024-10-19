from dataclasses import dataclass


@dataclass
class RequiredExtraNotInstalled(Exception):
  missing_module: str
  requested_functionality: str
  required_extra: str

  def __str__(self) -> str:
    return (
      f"{self.missing_module} module not found - if you want to use "
      f"{self.requested_functionality} functionality, make sure you've "
      f'installed the `{self.required_extra}` optional dependency ("extra") '
      f"of tlaplus_state_graph_utils.py"
    )
