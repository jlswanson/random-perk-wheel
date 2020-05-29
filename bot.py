import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

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
    'Deathslinger'
]

perks = [
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
    'Deerstalker',
    'Discordance',
    'Distressing',
    'Dying Light',
    'Enduring',
    'Fire Up',
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
    'Unnerving Presence',
    'Unrelenting',
    'Whispers',
    'Zanshin Tactics'
]

@bot.command(name='spin', help='Spin the wheel!  Get a random killer and four random perks.')
async def spin_the_wheel(ctx):
    await ctx.send('Wheel spun!')