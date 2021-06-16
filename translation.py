import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hai {}!!</b>
<i>I'm Prabha Movies Bot</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>1</b>
<b>• 2</b>
<b>• 3</b>
<b>• 4</b>
<b>• 5</b>
<b><u>6</b></u>
* 7 - <b>7</b>
* 8 - <b>8</b>
* 9 - <b>9</b>
* 10 - <b>10</b>"""
  ABOUT_TXT = """<b><u>My Info</b></u>
<b>Name :</b> <code>Prabha Movies Bot</code>
<b>Credit :</b> <code>Prabha</code>
<b>Language :</b> <code>Python3</code>
<b>Lybrary :</b> <code>Pyrogram v1.2.9</code>
<b>Server :</b> <code>Heroku</code>
<b>Build :</b><code>V1</code>"""
