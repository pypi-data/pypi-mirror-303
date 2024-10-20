import discord
from discord.ext import commands
from datetime import datetime

class DiscordBot:
    def __init__(self, discord_token, command_prefix, command_names):
        self.discord_token = discord_token
        
        intents = discord.Intents.default()
        intents.message_content = True  

        self.bot = commands.Bot(command_prefix=command_prefix, intents=intents)  

        self.register_events()
        self.register_commands(command_names)  

    def register_events(self):
        @self.bot.event
        async def on_ready():
            print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')

    def register_commands(self, command_names):
        if 'ping' in command_names:
            @self.bot.command(name='ping')
            async def ping(ctx):
                await ctx.send("Pong!")

        if 'hello' in command_names:
            @self.bot.command(name='hello')
            async def hello(ctx):
                await ctx.send(f"Hello, {ctx.author.name}!")

        if 'avatar' in command_names:
            @self.bot.command(name='avatar')
            async def avatar(ctx, user: discord.User = None):
                user = user or ctx.author  
                embed = discord.Embed(title=f"🖼️ {user.name}'s Avatar")
                embed.set_image(url=user.avatar.url)  

                button = discord.ui.Button(label="Open Avatar", url=user.avatar.url)

                view = discord.ui.View()
                view.add_item(button)

                await ctx.send(embed=embed, view=view)

        if 'servericon' in command_names:
            @self.bot.command(name='servericon')
            async def servericon(ctx):
                guild = ctx.guild
                embed = discord.Embed(title=f"🖼️ {guild.name}")
                
                embed.set_image(url=guild.icon.url if guild.icon else "https://via.placeholder.com/1024?text=No+Icon")  

                button = discord.ui.Button(label="Open Server Icon", url=guild.icon.url if guild.icon else "https://via.placeholder.com/1024?text=No+Icon")

                view = discord.ui.View()
                view.add_item(button)

                await ctx.send(embed=embed, view=view)

        if 'ban' in command_names:
            @self.bot.command(name='ban', description="Ban a user from the server")
            @commands.has_permissions(ban_members=True)
            async def ban(ctx, user: discord.Member = None, *, reason: str = "No reason provided"):
                if user is None:
                    await ctx.send("❌ You must mention a user to ban!")
                    return

                embed = discord.Embed(
                    title="User Banned",
                    description=f"🛑 **{user.name}** has been banned from the server.",
                    color=discord.Color.red()
                )
                embed.add_field(name="Reason", value=reason, inline=False)
                embed.set_footer(text=f"Banned by {ctx.author.name}", icon_url=ctx.author.avatar.url)

                button = discord.ui.Button(label="Confirm Ban", style=discord.ButtonStyle.danger)

                async def button_callback(interaction):
                    await ctx.guild.ban(user, reason=reason)
                    await interaction.response.edit_message(embed=embed, view=None)
                    await ctx.send(f"✅ **{user.name}** has been banned successfully!")

                button.callback = button_callback  

                view = discord.ui.View()
                view.add_item(button)

                await ctx.send(embed=embed, view=view)

        if 'unban' in command_names:
            @self.bot.command(name='unban', description="Unban a user from the server")
            @commands.has_permissions(ban_members=True)
            async def unban(ctx, user_id: int, *, reason: str = "No reason provided"):
                try:
                    user = await self.bot.fetch_user(user_id)  
                    await ctx.guild.unban(user, reason=reason)  
                    
                    embed = discord.Embed(
                        title="User Unbanned",
                        description=f"✅ **{user.name}** has been unbanned from the server.",
                        color=discord.Color.green()
                    )
                    embed.add_field(name="Reason", value=reason, inline=False)
                    embed.set_footer(text=f"Unbanned by {ctx.author.name}", icon_url=ctx.author.avatar.url)
                    
                    await ctx.send(embed=embed)

                except discord.NotFound:
                    await ctx.send("❌ The specified user ID does not correspond to a banned user.")
                except discord.Forbidden:
                    await ctx.send("❌ I do not have permission to unban this user.")
                except discord.HTTPException:
                    await ctx.send("❌ An error occurred while trying to unban the user.")

        if 'kick' in command_names:
            @self.bot.command(name='kick', description="Kick a user from the server")
            @commands.has_permissions(kick_members=True)
            async def kick(ctx, user: discord.Member = None, *, reason: str = "No reason provided"):
                if user is None:
                    await ctx.send("❌ You must mention a user to kick!")
                    return

                embed = discord.Embed(
                    title="User Kicked",
                    description=f"🚫 **{user.name}** has been kicked from the server.",
                    color=discord.Color.red()
                )
                embed.add_field(name="Reason", value=reason, inline=False)
                embed.set_footer(text=f"Kicked by {ctx.author.name}", icon_url=ctx.author.avatar.url)
                
                embed.set_image(url="") 

                button = discord.ui.Button(label="Confirm Kick", style=discord.ButtonStyle.danger)

                async def button_callback(interaction):
                    await ctx.guild.kick(user, reason=reason)
                    await interaction.response.edit_message(embed=embed, view=None)
                    await ctx.send(f"✅ **{user.name}** has been kicked successfully!")

                button.callback = button_callback  
                view = discord.ui.View()
                view.add_item(button)

                await ctx.send(embed=embed, view=view)

        if 'serverinfo' in command_names:
            @self.bot.command(name='serverinfo')
            async def serverinfo(ctx):
                guild = ctx.guild
                total_members = guild.member_count
                online_members = sum(1 for member in guild.members if member.status != discord.Status.offline)
                created_at = guild.created_at.strftime("%b %d, %Y")
                role_count = len(guild.roles)
                text_channels = len(guild.text_channels)
                voice_channels = len(guild.voice_channels)

                embed = discord.Embed(
                    title=f"Server Information: {guild.name}",
                    color=discord.Color.blurple(),
                    timestamp=datetime.utcnow()
                )

                embed.set_thumbnail(url=guild.icon.url)

                embed.add_field(name="🆔 Server ID", value=guild.id, inline=True)
                embed.add_field(name="🌍 Region", value=str(guild.region).capitalize(), inline=True)
                embed.add_field(name="👑 Owner", value=f"{guild.owner}", inline=True)
                embed.add_field(name="📅 Created on", value=created_at, inline=True)
                embed.add_field(name="👥 Total Members", value=total_members, inline=True)
                embed.add_field(name="🟢 Online Members", value=online_members, inline=True)
                embed.add_field(name="💬 Text Channels", value=text_channels, inline=True)
                embed.add_field(name="🔊 Voice Channels", value=voice_channels, inline=True)
                embed.add_field(name="🏅 Roles", value=role_count, inline=True)

                embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar.url)
                await ctx.send(embed=embed)
  
    def run(self):
        self.bot.run(self.discord_token)
