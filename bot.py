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

# ====================================
#
# HELLDIVERS BOT BELOW THIS LINE
#
# ====================================

armor_weight = [
    'Light',
    'Medium',
    'Heavy'
]

armor_passive = [
    'Democracy Protects',
    'Electrical Conduit',
    'Engineering Kit',
    'Extra Padding',
    'Fortified',
    'Inflammable',
    'Med-Kit',
    'Peak Physique',
    'Scout',
    'Servo-Assisted'
]

primary_weapon = [
    'AR-23 Liberator',
    'AR-23P Liberator',
    'Penetrator',
    'AR-23C Liberator Concussive',
    'AR-23A Liberator Carbine',
    'AR-61 Tenderizer',
    'BR-14 Adjudicator',
    'R-63 Diligence',
    'R-63CS Diligence Counter Sniper',
    'SMG-37 Defender',
    'SMG-72 Pummeler',
    'SG-8 Punisher',
    'SG-8S Slugger',
    'SG-451 Cookout',
    'SG-225 Breaker',
    'SG-225SP Breaker Spray & Pray',
    'SG-225IE Breaker Incendiary',
    'CB-9 Exploding Crossbow',
    'JAR-5 Dominator',
    'R-36 Eruptor',
    'SG-8P Punisher Plasma',
    'ARC-12 Blitzer',
    'LAS-5 Scythe',
    'LAS-16 Sickle',
    'PLAS-1 Scorcher',
    'PLAS-101 Purifier',
    'FLAM-66 Torcher'
]

secondary_weapon = [
    'P-2 Peacemaker',
    'P-19 Redeemer',
    'P-113 Verdict',
    'P-4 Senator',
    'SG-22 Bushwhacker',
    'P-72 Crisper',
    'GP-31 Grenade Pistol',
    'LAS-7 Dagger'
]

throwable = [
    'G-6 Frag',
    'G-12 High Explosive',
    'G-10 Incendiary',
    'G-16 Impact',
    'G-13 Incendiary Impact',
    'G-23 Stun',
    'G-3 Smoke',
    'G-123 Thermite',
    'K-2 Throwing Knife'
]

stratagem = [
    'Eagle 500kg Bomb',
    'Orbital Gatling Barrage',
    'Eagle Airstrike',
    'Orbital Walking Barrage',
    'Eagle Strafing Run',
    'Orbital EMS Strike',
    'Eagle Smoke Strike',
    'Orbital Gas Strike',
    'Orbital Railcannon Strike',
    'Eagle Cluster Bomb',
    'Orbital Smoke Strike',
    'Orbital Airburst Strike',
    'Orbital Laser',
    'Orbital Precision Strike',
    'Orbital 380mm HE Barrage',
    'Eagle Napalm Strike',
    'Orbital 120mm HE Barrage',
    'Eagle 110mm Rocket Pods',
    'MLS-4X Commando',
    'EXO-49 Emancipator Exosuit',
    'M-105 Stalwart',
    'AC-8 Autocannon',
    'EXO-45 Patriot Exosuit',
    'MG-206 Heavy Machine Gun',
    'SH-32 Shield Generator Pack',
    'RL-77 Airburst Rocket Launcher',
    'RS-422 Railgun',
    'LAS-98 Laser Cannon',
    'ARC-3 Arc Thrower',
    'AX/AR-23 "Guard Dog"',
    'FAF-14 Spear',
    'GL-21 Grenade Launcher',
    'MG-43 Machine Gun',
    'SH-20 Ballistic Shield Backpack',
    'B-1 Supply Pack',
    'FLAM-40 Flamethrower',
    'AX/LAS-5 "Guard Dog" Rover',
    'GR-8 Recoilless Rifle',
    'LIFT-850 Jump Pack',
    'APW-1 Anti-Materiel Rifle',
    'EAT-17 Expendable Anti-Tank',
    'LAS-99 Quasar Cannon',
    'MD-17 Anti-Tank Mines',
    'FX-12 Shield Generator Relay',
    'A/M-23 EMS Mortar Sentry',
    'A/MLS-4X Rocket Sentry',
    'A/G-16 Gatling Sentry',
    'A/ARC-3 Tesla Tower',
    'A/M-12 Mortar Sentry',
    'MD-6 Anti-Personnel Minefield',
    'A/MG-43 Machine Gun Sentry',
    'A/AC-8 Autocannon Sentry',
    'MD-14 Incendiary Mines',
    'E/MG-101 HMG Emplacement'
]

booster = [
    'Vitality Enhancement',
    'Stamina Enhancement',
    'Muscle Enhancement',
    'UAV Recon Booster',
    'Increased Reinforcement Budget',
    'Flexible Reinforcement Budget',
    'Hellpod Space Optimization',
    'Localization Confusion',
    'Expert Extraction Pilot',
    'Motivational Shocks',
    'Experimental Infusion',
    'Firebomb Hellpods'
]

mission_type = [
    'Blitz: Search and Destroy',
    'Conduct Geological Survey',
    'Emergency Evacuation',
    'Evacuate High-Value Assets (Defense Exclusive)',
    'Launch ICBM',
    'Retrieve Essential Personnel (Defense Exclusive)',
    'Retrieve Valuable Data',
    'Spread Democracy',
    'Purge Hatcheries','Enable E-710 Extraction',
    'Nuke Nursery',
    'Eradicate Terminid Swarm',
    'Sabotage Air Base',
    'Eradicate Automaton Forces',
    'Destroy Command Bunkers',
    'Neutralize Orbital Defenses'
]

@bot.command(name="freedom", help="Test your commitment to democracy, Helldiver.")
async def random_loadout(ctx):
    def get_formatted_stratagems(list):
        stratagem_list = random.sample(list, 4)
        stratagem_string = ''

        for item in stratagem_list:
            stratagem_string += item + '\n'
        return stratagem_string

    message = f"""
=======================
**FREEDOM LOADOUT**
=======================
**Primary weapon:** {random.choice(primary_weapon)}
**Secondary weapon:** {random.choice(secondary_weapon)}
**Throwable:** {random.choice(throwable)}

**Armor weight:** {random.choice(armor_weight)}
**Armor passive:** {random.choice(armor_passive)}

**Stratagems:**
{get_formatted_stratagems(stratagem)}
**Booster:** {random.choice(booster)}
    """

    await ctx.send(message)

@bot.command(name="mission", help="Where are you needed most in Super Earth's defense of the galaxy?")
async def random_mission(ctx):
    message = f"""
    Your mission is this: **{random.choice(mission_type)}** anywhere in the galaxy where managed democracy is under threat. Our continued freedom is counting on your success, Helldiver. Don't let us down!
    """

    await ctx.send(message)

bot.run(TOKEN)
