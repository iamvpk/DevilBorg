"""COMMAND : ./call"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 5

    animation_ttl = range(0, 18)

    input_str = event.pattern_match.group(1)

    if input_str == "/cull":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Telegram Headquarters...`",
            "`Call Connected.`",
            "`Telegram: Hello This is Telegram HQ. Who is this?`",
            "`Me: Yo this is` White Devil ,`Please Connect me to Dark Angel`",
            "`User Authorised.`",
            "`Calling Dark Angel At +002XYZZXY (ENCRYPTED NUMBER & CALL)`",
            "`Private  Call Connected...`",
            "`Me: Hello Sir, Please Ban This Telegram Account.`",    
            "`Darky: May I Know Who Is This?`",
            "`Me: Yo Bruh, I Am` White Devil",
            "`Darky: OMG!!! I Am FAN Of You Sir...\nI'll Make Sure That Guy Account Will Get Blocked Within 24Hrs.`",
            "`Me: Thanks, See You Later Dark Angel.`",
            "`Darky: Please Don't Thank me Boss, Telegram Is Your's. Just Gimme A Call When You Become Free.`",
            "`Me: Is There Any Issue/Emergency???`",
            "`Darky: Yes Sir, There Is A Bug In Telegram v5.12.1.\nI Am Not Able To Fix It. If Possible, Please Help Fix The Bug.`",
            "`Me: Send Me The App On My Telegram Account, I Will Fix The Bug & Send You.`",
            "`Darky: Sure Sir \nTC Bye Bye :)`",
            "`Private Call Disconnected.`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 18])
