import discord
from discord.ext import commands, tasks
import random
from datetime import  datetime
from datetime import time 
import os
import traceback

TOKEN = os.getenv("TOKEN")
MEU_ID = 883198811441344552
Ticket = 1522211118272217169

hoje = datetime.now()

dias = [
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo"
]

dia_semana = dias[hoje.weekday()]

agora = datetime.now()
hora = agora.strftime("%H:%M")

intents = discord.Intents.all()
bots = commands.Bot(command_prefix="!", intents=intents)

@bots.event
async def on_ready():
    enviar_mensagem.start()
    if not bom_dia_task.is_running():
        bom_dia_task.start()
    print("bot funcionando")

@bots.event
async def on_member_join(member):
    canal = bots.get_channel(1414607968795627642)

    embed = discord.Embed(
        title="Bem-vindo(a) 👋",
        description=f"Olá {member.mention}",
        color=discord.Color.purple()
    )

    embed.add_field(
        name="Informações",
        value=(
            f"nome do usuário : `{member}`"
        ),
        inline=False
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    embed.set_footer(
        text=f"{member.guild.name}"
    )
    await canal.send(embed=embed)

@bots.command(aliases=["bom dia"])
async def bom_dia(ctx:commands.Context):
    fala = random.choice(["bom dia neguin","eae mano bom dia","qual foi bom dia", "eu vou ter um bom dia"])
    await ctx.reply(f"{fala} 😑")
    return

@bots.command()
async def oi(ctx):
    fala = random.choice(["oi","...","sai daqui otario","qual foi neguin"])
    await ctx.channel.send(f"{fala} 😑")
    return

@bots.command(aliases=["hora do jogo"])
async def hora(ctx):
    await ctx.channel.send(f"hora de amassar esses mediocres👾")
    return

@bots.command()
async def intervalo(ctx):
    await ctx.channel.send(f"4x0 só, time lixo")
    return


@bots.command()
async def pais(ctx):
    await ctx.channel.send(f"🎵 meu proprio pais me enganou...🎵")
    return

@bots.command(aliases=["eu sou bom?"])
async def jogo(ctx):
    await ctx.channel.send("Você não é ruim, só tá jogando igual Bot")
    return

@bots.command()
async def rin(ctx):
    await ctx.channel.send(f"maninho ❤️")
    return

@bots.command()
async def isagi(ctx):
    await ctx.channel.send(f"cuzão do isagi")
    return

@bots.command()
async def bunny(ctx):
    fala = random.choice(["Rival? Ainda não. Quando eu tiver que levar ele a sério dentro de campo, aí a gente conversa","um certo otario da espanha"])
    await ctx.channel.send(fala)
    return

@bots.command(aliases=["voce e bom?"])
async def voce(ctx):
    await ctx.channel.send(f"não sou miudinho atoa, opa quis dizer newgen")
    return

@bots.command()
async def dado(ctx):
    canal_c = 1414462647037988894
    if ctx.channel.id != canal_c:
        return
    numero = random.randint(1, 20)
    if numero <= 5:
        await ctx.channel.send(f"Você tirou {numero} no 🎲 seu bosta")
    elif numero <=10:
        await ctx.channel.send(f"você tirou {numero} no 🎲 seu mediocre")
    elif numero <= 15:
        await ctx.channel.send(f"você tirou {numero} no 🎲 energumeno")
    elif numero <= 20:
        await ctx.channel.send(f"você tirou {numero} no 🎲 mera-sorte")

@bots.command()
async def fim(ctx):
    await ctx.channel.send(f"dava pra meter uns 8x0 nessa porra")
    return

@bots.command()
async def bot(ctx):
    await ctx.channel.send(f"eu sou o melhor bot desse server")
    return

@bots.command()
async def dia(ctx):
    await ctx.channel.send(f"hoje é {dia_semana}, {hoje.strftime('%d/%m')} é  agora são {agora.strftime('%H:%M')} ")
    return

@tasks.loop(time=time(9,29))
async def enviar_mensagem():
    canal = bots.get_channel(1522863442417942588)
    await canal.send("Bom-dia!")

@tasks.loop(time=time(9,30))
async def bom_dia_task():
    canal_c = bots.get_channel(1522863442417942588)

    minha_embed = discord.Embed()
    minha_embed.title = "Já são 6 da manhã, bora acordar!"
    minha_embed.description = ""

    Imagem = discord.File("bom_dia.jpg",filename="bom_a.jpg")
    minha_embed.set_image(url="attachment://bom_a.jpg")
    minha_embed.set_footer(text="Bom dia rapaziada😘")
    minha_embed.set_author(name="sae",icon_url="https://pbs.twimg.com/media/HCbPdWpX0AAhVtW.jpg")

    await canal_c.send(content="@everyone",embed=minha_embed, file=Imagem, allowed_mentions=discord.AllowedMentions(everyone=True))

@bots.command()
async def tk(ctx):
    
    if ctx.channel.id != Ticket:
            return
    canal_p = bots.get_channel(1522211118272217169)
    await ctx.send("Descreva seu problema.")

    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    try:
        resposta = await bots.wait_for("message", check=check, timeout=300)
    except Exception as e:
        traceback.print_exc()
        await ctx.send(f"Erro: {e}")
        return
        
    embed = discord.Embed(
    title="📩 Novo Ticket",
    color=discord.Color.purple()
    )

    embed.add_field(
    name="Usuário",
    value=f"{ctx.author.mention}\n{ctx.author}",
    inline=False
    )

    embed.add_field(
        name="Mensagem",
        value=resposta.content,
        inline=False
    )
    usuario = await bots.fetch_user(MEU_ID)
    await usuario.send(embed=embed)
    
    if canal_p is None:
        print("Canal não encontrado!")
    else:
        await canal_p.send(embed=embed)
        
    await ctx.send("Seu ticket foi enviado!")

bots.run(TOKEN)
