import discord
from discord.ext import commands
import os
import random

bot = commands.Bot(command_prefix='$')

@bot.command()
@commands.has_permissions(manage_roles=True)
async def make_campaign(ctx, arg = 'empty'): 
  if(arg == 'empty'):
    await ctx.send("Argument required")
  else:
    guild = ctx.guild
    role = await guild.create_role(name=arg)

    overwrites = {
    guild.default_role: discord.PermissionOverwrite(read_messages=False),
    role: discord.PermissionOverwrite(read_messages=True)
    }

    category = await guild.create_category(name=arg, overwrites=overwrites)
    await category.create_text_channel(name='termine')
    await category.create_text_channel(name='playchat')
    await category.create_voice_channel(name='Playing')
    await category.create_voice_channel(name='Charerstellung')
    await ctx.send("Created Role, Category and Channels")

@bot.command()
@commands.has_permissions(manage_roles=True)
async def rm_campaign(ctx, arg = 'empty'): 
  if(arg == 'empty'):
    await ctx.send("Argument required")
  else:
    guild = ctx.guild
    result = await guild.fetch_channels()
    found_channel = None
    for channel in result:
      if(channel.name == arg):
        found_channel = channel
    
    if(found_channel == None):
      await ctx.send("Category not found")
      return
    
    for channel in found_channel.channels:
      await channel.delete()

    await found_channel.delete()
    await ctx.send("Channels Deleted")

    found_role = None
    for role in guild.roles:
      if(role.name == arg):
        found_role = role
    
    if(found_role == None):
      await ctx.send("Category not found")
      return
    
    await found_role.delete()
    await ctx.send("Role Deleted")

with open('token', 'r') as file:
    token_text = file.read().rstrip()
    bot.run(token_text)
