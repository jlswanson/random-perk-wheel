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
    'Onryo'
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
    'Corrupt Intervention',
    'Coulrophobia',
    'Coup de Grace',
    'Cruel Limits',
    'Dark Devotion',
    'Dead Man\'s Switch',
    'Deadlock',
    'Deathbound',
    'Deerstalker',
    'Discordance',
    'Distressing',
    'Dragon\'s Grip',
    'Dying Light',
    'Enduring',
    'Eruption',
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
    'Knock Out',
    'Lethal Pursuer',
    'Lightborn',
    'Mad Grit',
    'Make Your Choice',
    'Merciless Storm',
    'Mindbreaker',
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
    'Shadowborn',
    'Sloppy Butcher',
    'Spies from the Shadows',
    'Spirit Fury',
    'Starstruck',
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
    'Appraisal',
    'Autodidact',
    'Babysitter',
    'Balanced Landing',
    'Better Together',
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
    'Camaraderie',
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
    'Fixated',
    'Flashbang',
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
    'Overcome',
    'Parental Guidance',
    'Pharmacy',
    'Plunderer\'s Instinct',
    'Poised',
    'Power Struggle',
    'Premonition',
    'Prove Thyself',
    'Quick & Quiet',
    'Red Herring',
    'Repressed Alliance',
    'Resilience',
    'Resurgence',
    'Rookie Spirit',
    'Saboteur',
    'Second Wind',
    'Self-Care',
    'Self-Preservation',
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

bot.run(TOKEN)
