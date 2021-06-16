import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hai {}!!</b>
<i>I'm a Bot Created by @TiruppurPrabha for @CineGalaxy Group</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Contact @TiruppurPrabha</b>