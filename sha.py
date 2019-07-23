import os
import willie
from willie.module import commands, interval

@willie.module.commands('sha')
@willie.module.example('.sha', 'sha')
def spacestate(bot, trigger):
  """Gives you a random SHA2021 slogan suggestion"""
  txt = "for v in s hack a; do w=$(grep \"^$v\" /usr/share/dict/cracklib-small | shuf -n1); echo -n \"${w^${v:0:1}} \"; done ; echo 2021"  
  bot.say(os.popen(txt).read())
  
