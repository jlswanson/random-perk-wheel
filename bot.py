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
    'Infectious Fright',
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

bot.run(TOKEN)
