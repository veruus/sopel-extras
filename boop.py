# -*- coding: utf8 -*-
"""
boop.py - It boops.
Cribbed from lart.py written by Matteo Marchesotti https://www.sfwd.ws
Licensed under the Eiffel Forum License 2.

http://willie.dfbta.net
"""
import willie
import random
@willie.module.commands('boop')
def boop(bot, trigger):
    """Boop. Boops a target! Usage: .boop <target>"""
    try:
        collection = open('.willie/.boop.collection', 'r')
    except Exception as e:
        bot.say("No boops collection file found. Try with .help addboop")
        print e
        return

    messages = [line.decode('utf-8') for line in collection.readlines()]
    collection.close()

    if len(messages)== 0:
        bot.say("No boop found! Type .help addboop")
        return;

    if trigger.group(2) is None:
        user = trigger.nick.strip()
    else:
        user = trigger.group(2).strip()

    message = random.choice(messages).replace('TARGET', user).encode('utf_8')

    bot.action(message)

@willie.module.commands('addboop')
def addboop(bot, trigger):
    """
    Adds another boop to bot's collection with: .addboop <boop>. 'boop' will be sent as an action; 
    i.e., '$botnick boops TARGET with 'boop' (a horse with no name, a sexually frustrated tyranosaurus rex, 
    a fluffy cactus, etc.).
    """
    try:
        boop = trigger.group(2).replace('"','\"').encode('utf_8')
        collection = open('.willie/.boop.collection', 'a')
        collection.write("boops TARGET with %s\n"%boop)
        collection.close()
    except Exception as e:
        bot.say("Unable to write boop to collection file!")
        print e
        return

    bot.say("Thanks %s: Boop added!"%trigger.nick.strip())
