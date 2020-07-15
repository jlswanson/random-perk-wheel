import os

import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='?')

killers = [
    'Trapper',
    'Wraith',
    'Hillbilly',
    'Nurse',
    'Shape',
    'Hag',
    'Doctor',
    'Huntress',
    'Cannibal',
    'Nightmare',
    'Pig',
    'Clown',
    'Spirit',
    'Legion',
    'Plague',
    'Ghost Face',
    'Demogorgon',
    'Oni',
    'Deathslinger',
    'Executioner'
]

killer_perks = [
    'A Nurse\'s Calling',
    'Agitation',
    'Bamboozle',
    'Barbecue & Chilli',
    'Beast of Prey',
    'Bitter Murmur',
    'Blood Echo',
    'Blood Warden',
    'Bloodhound',
    'Brutal Strength',
    'Corrupt Intervention',
    'Coulrophobia',
    'Cruel Limits',
    'Dark Devotion',
    'Dead Man\'s Switch',
    'Deathbound',
    'Deerstalker',
    'Discordance',
    'Distressing',
    'Dying Light',
    'Enduring',
    'Fire Up',
    'Forced Penance',
    'Franklin\'s Demise',
    'Furtive Chase',
    'Gearhead',
    'Hangman\'s Trick',
    'Hex: Devour Hope',
    'Hex: Haunted Ground',
    'Hex: Huntress Lullaby',
    'Hex: No One Escapes Death',
    'Hex: Retribution',
    'Hex: Ruin',
    'Hex: The Third Seal',
    'Hex: Thrill of the Hunt',
    'I\'m All Ears',
    'Infections Fright',
    'Insidious',
    'Iron Grasp',
    'Iron Maiden',
    'Knock Out',
    'Lightborn',
    'Mad Grit',
    'Make Your Choice',
    'Mindbreaker',
    'Monitor & Abuse',
    'Monstrous Shrine',
    'Nemesis',
    'Overcharge',
    'Overwhelming Presence',
    'Play with Your Food',
    'Pop Goes the Weasel',
    'Predator',
    'Rancor',
    'Remember Me',
    'Save the Best for Last',
    'Shadowborn',
    'Sloppy Butcher',
    'Spies from the Shadows',
    'Spirit Fury',
    'Stridor',
    'Surge',
    'Surveillance',
    'Territorial Imperative',
    'Tinkerer',
    'Thanatophobia',
    'Thrilling Tremors',
    'Trail of Torment',
    'Unnerving Presence',
    'Unrelenting',
    'Whispers',
    'Zanshin Tactics'
]

survivor_perks = [
    'Ace in the Hole',
    'Adrenaline',
    'Aftercare',
    'Alert',
    'Any Means Necessary',
    'Autodidact',
    'Babysitter',
    'Balanced Landing',
    'Better Together',
    'Blood Pact',
    'Boil Over',
    'Bond',
    'Borrowed Time',
    'Botany Knowledge',
    'Breakdown',
    'Breakout',
    'Buckle Up',
    'Calm Spirit',
    'Camaraderie',
    'Dance With Me',
    'Dark Sense',
    'Dead Hard',
    'Decisive Strike',
    'Déjà Vu',
    'Deliverance',
    'Detective\'s Hunch',
    'Distortion',
    'Diversion',
    'Empathy',
    'Fixated',
    'Flip-Flop',
    'For the People',
    'Head On',
    'Hope',
    'Inner Strength',
    'Iron Will',
    'Kindred',
    'Leader',
    'Left Behind',
    'Lightweight',
    'Lithe',
    'Lucky Break',
    'Mettle of Man',
    'No Mither',
    'No One Left Behind',
    'Object of Obsession',
    'Off the Record',
    'Open-Handed',
    'Pharmacy',
    'Plunderer\'s Instinct',
    'Poised',
    'Premonition',
    'Prove Thyself',
    'Quick & Quiet',
    'Red Herring',
    'Repressed Alliance',
    'Resilience',
    'Saboteur',
    'Second Wind',
    'Self-Care',
    'Slippery Meat',
    'Small Game',
    'Sole Survivor',
    'Solidarity',
    'Soul Guard',
    'Spine Chill',
    'Sprint Burst',
    'Stake Out',
    'Streetwise',
    'This Is Not Happening',
    'Technician',
    'Tenacity',
    'Up the Ante',
    'Unbreakable',
    'Urban Evasion',
    'Vigil',
    'Wake Up!',
    'We\'ll Make It',
    'We\'re Gonna Live Forever',
    'Windows of Opportunity'
]

phrases = [
    'u are a cancer',
    'You can\'t play legit virgin jajajajaja',
    'You like deep cock?!',
    'You trans?',
    'find me at lxcoco.ttv',
    'die please',
    'fricken K pop jake jukes',
    'I didn\'t do anything to you to be toxic kanan',
    'lmao fuck off tattooed jake',
    'do you like male lips?',
    'pretty sure I just died to a virgin',
    'ole missing chromosome headas',
    'lookin like a trans karen',
    'WHO TOUCHED YOU',
    'yo Kenan, bet you look like the killer too.  git gud.',
    'You give a bad rep to all kenans',
    'don\'t smile at me',
    'i see you pointing hoe',
    'worthless aomeba cell',
    'serves you right camper',
    'I hope you catch covid and your last moments are you struggling to breathe <3',
    'gg stands for get gay',
    'every single person on the face of this earth wants to not play you cuz u make the game toxic',
    'get off video games u 30 year old',
    'kenan, you are very unnatractive',
    'you look like an absolute cuck',
    'I really wanna kill your mother',
    'camping piece of :heart: :heart: :heart: :heart: delete the game',
    'cool 10 year old, mommy really love you right bet she would love to take my bbc all night. get off my friends list',
    'I think Kenan is actually braindead.',
    'your profile pic literally looks like youre a 14 hyear old gay pirate musician who is on his way to court for undisclosed charges...',
    'you make an ugly trans person btw',
    'lemme fist u pls',
    'you play like a bitch honestly',
    'you look like a serial killer',
    'how about you shove a rusty fork up your dick next time instead',
    'You made the conscious decision, to be a deliberate dick.',
    'haha bitch boy',
    'u a chick or a dude?',
    'ooh it\'s the ugly guy that plays like a stupid bitch',
    'honestly uninstall this game',
    'gg tu madre',
    'Doesn\'t change the fact that you\'re a degenerate',
    'kenan try harder to look like a boy',
    'get fucked by a cactus',
    'you look like an absolute tranny',
    'kenan please unisall the game',
    'So take your merry christmas and your unironic smiley faces and shove it, kiddo :))',
    'gg hope you get cancer',
    'u look like a lesbian',
    'it was a sad day when you slithered out of the abortion bucket you sad limp dicked cum cumpster',
    'does mama wash your dick',
    'suck ten thousand cocks in hell',
    'ngl you look like someone who spends a lot of time on reddit',
    'do you watch golf unironically',
    'is your favorite sandwich mayo on white',
    'fuck you with that gaylord face',
    'Your 4k\'s are hollow just like you.',
    'Like are you that sad in real life that you can\'t let others have any joy whatsoever?',
    'he probably got a face only a mother can love and still she left him on a curb',
    'wow what a shit bag, must get it from his mother',
    'you look inbred as fuck you worthless piece of shit',
    'woof',
    'did you hide the trap with your body',
    'shat man',
    'sup of our flesh master',
    'you suck james charles off',
    'you look more like a real life dwight',
    'look what happened to all you dumbasses running into the meat gringer',
    'I know you like to suck rank 2 dicks but maybe get better on your own first',
    'you like anime men',
    'why the fuck u so ugly',
    'ur face looks like a hairy vagina with those lips',
    'god ur a pussy',
    'answer the call inbred',
    'u camping very gross xD',
    'jake you really like attention huh fat freadk',
    'go wipe your ass don\'t gg me bitch',
    'fuckin premade trash cans',
    'nice vpn, does it come in mens?',
    'UwU owO ;m; :3 stfu hore',
    'fucking bumm ass camper',
    'SpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicySpicy',
    'Fucking weirdo',
    'your profile makes you look like a douche',
    'how much did you pay for that account?',
    'i\'m sorry your dick is so small',
    'shame eugenics failed on your trash gene pool',
    'this dudes a POOCH',
    'fuck you kenan you smug piece of shit',
    'jesus christ your sound mormon as fuck',
    'ufff tsk tsk tsk you suck :)',
    'girl i just know your coochie stinks',
    'end ur petty life',
    'Go die in a fire',
    'you have no siginificant otehr you smelly whore',
    'youre trashh meanie camper killer',
    'shut up mother fucker noob',
    'you actually sweat hardcore kys kid',
    'ur ugly. unironically ugly. go back to reddit.',
    'cock smoker'
]

@bot.command(name='spin', help='Spin the wheel!  Get a random killer and four random perks.  Optionally pass in the survivor argument for 4 survivor perks instead.  Example: ?spin survivor')
async def spin_the_wheel(ctx, type='killer'):
    phrase = random.choice(phrases)
    killer = random.choice(killers)
    message = 'Invalid argument provided.  Valid arguments are: `killer` or `survivor`.  Example: `?spin survivor`'

    def get_formatted_perks(list):
        perk_list = random.sample(list, 4)
        perk_string = ''

        for item in perk_list:
            perk_string += item + '\n'
        return perk_string

    if type.lower() == 'survivor':
        message = """
> **{phrase}**\n
**Survivor Perks:**  
{perks}
""".format(phrase=phrase, perks=get_formatted_perks(survivor_perks))

    if type.lower() == 'killer':
        message = """
> **{phrase}**\n
**Killer:**  
{killer}\n
**Perks:**  
{perks}
""".format(phrase=phrase, killer=killer, perks=get_formatted_perks(killer_perks))

    await ctx.send(message)

@bot.command(name="killer", help="Get a random killer.")
async def random_killer(ctx):
    message='Random killer: **{killer}**'.format(killer=random.choice(killers))
    
    await ctx.send(message)

@bot.command(name='salt')
async def gimme_salt(ctx):
    salt = random.choice(phrases)

    message = '> **{salt}**'.format(salt=salt)
    await ctx.send(message)

bot.run(TOKEN)
