def state_tlaplus_to_latex(state_tlaplus: str) -> str:
  # TODO Surely there is a way to use TLA+'s own LaTeX-output
  #  programmatically somehow so we don't have to do this?
  #  Alternative: Use that TLA+-to-Unicode tool (forgot name)
  return (
    state_tlaplus.replace("/\\", "\\land")
    .replace(r"\/", "\\lor")
    .replace("|->", "\\mapsto")
    .replace("\n", " \\\\ ")
    .replace("FALSE", "\\mathrm{FALSE}")
    .replace("TRUE", "\\mathrm{TRUE}")
    .replace('"', '\\text{"}')  # these look like garbage otherwise
  )
