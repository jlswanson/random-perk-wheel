import os
import json

import random
import discord
from discord.ext import commands
from dotenv import load_dotenv

# firebase
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

load_dotenv()

# db config & initialization
CONFIG = json.loads(os.getenv('FIREBASE_CONFIG'))
cred = credentials.Certificate(CONFIG)
firebase_admin.initialize_app(cred)

# access db & collection
db = firestore.client()
quotes = db.collection('quotes')

# discord bot token
TOKEN = os.getenv('DISCORD_TOKEN')

# initialize the bot with a prefix
bot = commands.Bot(command_prefix='?')
client = discord.Client()

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
    'Executioner',
    'Blight',
    'Twins',
    'Trickster',
    'Nemesis',
    'Cenobite',
    'Artist',
    'Onryo',
    'Dredge'
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
    'Call of Brine',
    'Claustrophobia',
    'Corrupt Intervention',
    'Coulrophobia',
    'Coup de Grace',
    'Dark Devotion',
    'Darkness Revealed',
    'Dead Man\'s Switch',
    'Deadlock',
    'Deathbound',
    'Deerstalker',
    'Discordance',
    'Dissolution',
    'Distressing',
    'Dragon\'s Grip',
    'Dying Light',
    'Enduring',
    'Eruption',
    'Fearmonger',
    'Fire Up',
    'Forced Penance',
    'Franklin\'s Demise',
    'Furtive Chase',
    'Gearhead',
    'Grim Embrace',
    'Hangman\'s Trick',
    'Hex: Blood Favour',
    'Hex: Crowd Control',
    'Hex: Devour Hope',
    'Hex: Haunted Ground',
    'Hex: Huntress Lullaby',
    'Hex: No One Escapes Death',
    'Hex: Pentimento',
    'Hex: Plaything',
    'Hex: Retribution',
    'Hex: Ruin',
    'Hex: The Third Seal',
    'Hex: Thrill of the Hunt',
    'Hex: Undying',
    'Hoarder',
    'Hysteria',
    'I\'m All Ears',
    'Infectious Fright',
    'Insidious',
    'Iron Grasp',
    'Iron Maiden',
    'Jolt',
    'Knock Out',
    'Lethal Pursuer',
    'Lightborn',
    'Mad Grit',
    'Make Your Choice',
    'Merciless Storm',
    'Monitor & Abuse',
    'Monstrous Shrine',
    'Nemesis',
    'No Way Out',
    'Oppression',
    'Overcharge',
    'Overwhelming Presence',
    'Play with Your Food',
    'Pop Goes the Weasel',
    'Predator',
    'Rancor',
    'Remember Me',
    'Save the Best for Last',
    'Scourge Hook: Floods of Rage',
    'Scourge Hook: Gift of Pain',
    'Scourge Hook: Pain Resonance',
    'Septic Touch',
    'Shadowborn',
    'Sloppy Butcher',
    'Spies from the Shadows',
    'Spirit Fury',
    'Starstruck',
    'Stridor',
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
    'Appraisal',
    'Autodidact',
    'Balanced Landing',
    'Bite the Bullet',
    'Blast Mine',
    'Blood Pact',
    'Boil Over',
    'Bond',
    'Boon: Circle of Healing',
    'Boon: Dark Theory',
    'Boon: Exponential',
    'Boon: Shadow Step',
    'Borrowed Time',
    'Botany Knowledge',
    'Breakdown',
    'Breakout',
    'Buckle Up',
    'Built to Last',
    'Calm Spirit',
    'Clairvoyance',
    'Corrective Action',
    'Counterforce',
    'Dance With Me',
    'Dark Sense',
    'Dead Hard',
    'Deception',
    'Decisive Strike',
    'Deja Vu',
    'Deliverance',
    'Desperate Measures',
    'Detective\'s Hunch',
    'Distortion',
    'Diversion',
    'Empathic Connection',
    'Empathy',
    'Fast Track',
    'Flashbang',
    'Flip-Flop',
    'For the People',
    'Guardian',
    'Head On',
    'Hope',
    'Inner Focus',
    'Inner Healing',
    'Iron Will',
    'Kindred',
    'Kinship',
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
    'Overcome',
    'Overzealous',
    'Parental Guidance',
    'Pharmacy',
    'Plunderer\'s Instinct',
    'Poised',
    'Power Struggle',
    'Premonition',
    'Prove Thyself',
    'Quick & Quiet',
    'Red Herring',
    'Renewal',
    'Repressed Alliance',
    'Residual Manifest',
    'Resilience',
    'Resurgence',
    'Rookie Spirit',
    'Saboteur',
    'Self-Aware',
    'Self-Care',
    'Self-Preservation',
    'Situational Awareness',
    'Slippery Meat',
    'Small Game',
    'Smash Hit',
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
    'Visionary',
    'Wake Up!',
    'We\'ll Make It',
    'We\'re Gonna Live Forever',
    'Windows of Opportunity'
]

salt_supply = []

def get_salt():
    # get all documents
    query = quotes.stream()

    # doc comes back as generator object
    for q in query:
        value = q.get('value')
        salt_supply.append(value)

get_salt()

@bot.command(name='spin', help='Spin the wheel!  Get a random killer and four random perks.  Optionally pass in the survivor argument for 4 survivor perks instead.  Example: ?spin survivor')
async def spin_the_wheel(ctx, type='killer'):
    phrase = random.choice(salt_supply)
    killer = random.choice(killers)
    message = 'Invalid argument provided.  Valid arguments are: `killer` or `survivor`.  Example: `?spin survivor`'

    def get_formatted_perks(list):
        perk_list = random.sample(list, 4)
        perk_string = ''

        for item in perk_list:
            perk_string += item + '\n'
        return perk_string

    if type.lower() == 'survivor':
        message = f"""
> **{phrase}**\n
**Survivor Perks:**  
{get_formatted_perks(survivor_perks)}
"""

    if type.lower() == 'killer':
        message = f"""
> **{phrase}**\n
**Killer:**  
{killer}\n
**Perks:**  
{get_formatted_perks(killer_perks)}
"""

    await ctx.send(message)

@bot.command(name="killer", help="Get a random killer.")
async def random_killer(ctx):
    message = f'Random killer: **{random.choice(killers)}**'
    
    await ctx.send(message)

@bot.command(name='salt')
async def gimme_salt(ctx):
    salt = random.choice(salt_supply)

    message = f'> **{salt}**'
    await ctx.send(message)

# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return

#     if 'you like?' in message.content.lower():
#         await message.channel.send('You like this?')

# ------------------------------------
# MAP ROULETTE CODE BELOW THIS COMMENT
# ------------------------------------

roundStarted = False
roulette = []
realms = [
    'The MacMillan Estates',
    'Autohaven Wreckers',
    'Coldwind Farm',
    'Crotus Prenn Asylum',
    'Haddonfield',
    'Backwater Swamp',
    'Lery\'s Memorial Institute',
    'Red Forest',
    'Springwood',
    'Gideon Meat Plant',
    'Yamaoka Estate',
    'Ormond',
    'Grave of Glenvale',
    'Silent Hill',
    'Raccoon City',
    'Forsaken Boneyard',
    'Withered Isle',
]

# begin a round of map roulette
@bot.command(name="round", help="Start a new round of map roulette!  You will automatically be added to the round when using this command.")
async def start_round(ctx):
    author = ctx.author

    if len(roulette):
        await ctx.send('There\'s already a round in progress!  `?endround` will end the current round of map roulette.')
    else:
        # add the creator to the round
        # id is member ID
        roulette.append({"player": author})

        await ctx.send(f"""
**A new round of roulette has begun!**
Blame {author.mention} for your misfortune.
""")

@bot.command(name="join", help="Join the round of roulette.  The first four people to use this command will be entered into the round!")
async def add_to_round(ctx):
    author = ctx.author

    list_of_joined = [True for elem in roulette if author in elem.values()]

    if roundStarted == True:
        await ctx.send(f'The round has already started!  Sit tight for the next one.')
    elif any(list_of_joined):
        await ctx.send(f'You\'re already in this round, {author.mention}!')
    elif len(roulette) == 4:
        await ctx.send(f'Sorry, {author.mention}, this round is full!')
    else:
        # add the joiner to the round
        roulette.append({"player": author})

        await ctx.send(f'{author.mention} has joined the round!')

@bot.command(name="start", help="Start the game!")
async def start_roulette(ctx):
    global roundStarted
    message = ''
    listMessage = f"""
**Roulette is about to begin!**
Choose from the list of realms below to participate:\n
1. The MacMillan Estates
2. Autohaven Wreckers
3. Coldwind Farm
4. Crotus Prenn Asylum
5. Haddonfield
6. Backwater Swamp
7. Lery's Memorial Institute
8. Red Forest
9. Springwood
10. Gideon Meat Plant
11. Yamaoka Estate
12. Ormond
13. Grave of Glenvale
14. Silent Hill
15. Raccoon City
16. Forsaken Boneyard
17. Withered Isle\n
Reply with the number of the realm you'd like to pick, and let the games begin!"""

    if roundStarted == True:
        #if the round has been started
        message += f'The round has already started!  Sit tight for the next one.'
    elif roundStarted == False and len(roulette) > 0:
        # if the round has not been started AND there is at least one player in the list
        message += f"""**The game is afoot!**\n
These are your players:\n"""

        for item in roulette:
            message += f"""{item['player'].mention}\n"""
            await item['player'].send(listMessage)

        roundStarted = True
    elif roundStarted == False or len(roulette) == 0:
        # if the round has not been started OR there are no players in the list
        message += f"""There's no round in progress yet!  `?round` starts a new round of roulette."""
    else:
        message += 'Whoops!  Something went wrong.  Let Jess know by tagging her in a reply to this message.'

    await ctx.send(message)

    def check(msg):
        return msg.author == ctx.author

    # TODO: This still hits the timeout when replying to dm, need to fix.
    try:
        msg = await client.wait_for('message', check=check, timeout=30.0)
    except:
        await ctx.send(f'I didn\'t receive your message in time.  The round will start without you.')

    reply = int(msg.lower) - 1

    rouletteItem = next(item for items in roulette if item['id'] == msg.author['id'])
    rouletteItem = rouletteItem["realm": realms[reply]]
    print(rouletteItem)

@bot.command(name="clear", help="Clear the current round.  This deletes all players and choices from the round without resolving the round.")
async def clear_roulette(ctx):
    roulette.clear()

    global roundStarted
    roundStarted = False

    await ctx.send(f'Cleared the round.')

bot.run(TOKEN)
