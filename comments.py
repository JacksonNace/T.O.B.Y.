#@client.tree.command(name="Hello", description="Say hello!") #this is a global version that applies to ALL servers
#async def sayHello(interaction:discord.Interaction):
  #await interaction.response.send_message("Hi there! ")

# DIFFERENT EVENTS:
# on_ready()
# on_message(message)
# on_message_edit(before, after)
# on_message_delete(message)
# on_member_join(member)
# on_member_remove(member)
# on_member_update(before, after)
# on_guild_join(guild)
# on_guild_remove(guild)
# on_reaction_add(reaction, user)
# on_reaction_remove(reaction, user)