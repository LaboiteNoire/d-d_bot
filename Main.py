import discord
from discord.ext import commands
import random
from discord.ext import commands
from discord_slash import ButtonStyle , SlashCommand
from discord_slash.utils.manage_components import *
import os
from LolaClass import *
from StorageSystem import *

bot = commands.Bot(command_prefix = "°", description = "LolaBot/DripBot")
slash = SlashCommand(bot, sync_commands=True)
User_Data = {}
nonetxt = "᲼"
Tick = 0








@bot.event
async def on_ready():
	print("Lola bot online")
	await bot.change_presence(activity=discord.Game(name="erp furry sonic loli rape"))


@bot.command()
async def embed(ctx):
        embed = discord.Embed(
                title='TITRE' ,
                description = 'description' ,
                color = discord.Colour.blue()
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/535987446278783012/958415924199845948/ddbfab2d89bfe468579fa2a7ee33ffed.jpg")
        
        #embed.add_field(name="Text 1 ", value="text1", inline=False)
        
        embed.set_footer(text="test test test test")
        embed.set_footer(text="mise a jour par: {}".format(ctx.author.display_name))
        #ctx.author.avatar_url
        await ctx.send(embed=embed)


def abszero(n : int):
    if n < 0:
        return 0
    else:
        return n
def startEmbed(ctx ,name : str , aseAImage : bool , link : str):
        embed = discord.Embed(
                title='__Statistiques__' ,
                description = "*Arme Utilisée :* " + "**" + name + "**" ,
                color = discord.Colour.blue()
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        if aseAImage:
                embed.set_thumbnail(url=link)
        else:
                embed.set_thumbnail(url=str(ctx.author.avatar_url))
        return embed
def startEmbedImage(ctx ,name : str , link : str):
        embed = discord.Embed(
                title='__Statistiques__' ,
                description = "*Arme Utilisée :* " + "**" + name + "**" ,
                color = discord.Colour.blue()
        )
        embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=link)
        return embed
def statInterfaceWeapon(embed , Statistiques : list):
        embed.add_field(name=":small_blue_diamond: __*Points__ `d'Offense`:*", value="*Po :* " + "`"+ str(Statistiques[0])+"`", inline=False)
        embed.add_field(name=":small_blue_diamond: __*Points__ __de__ `Precision:`*", value="*Ppr :* " + "`"+ str(Statistiques[1])+"`", inline=False)
        embed.add_field(name=":small_blue_diamond: __*Points__ __de__ `Posture:`*", value="*Pst :* " + "`"+ str(Statistiques[2])+"`", inline=False)
        embed.add_field(name=":small_blue_diamond: __*Points__ __de__ `Poison:`*", value="*Pp :* " + "`"+ str(Statistiques[3])+"`", inline=False) 
def statInterfacePlayer(embed , Statistiques : list):
        embed.add_field(name=":medical_symbol: __Level__ __du__ __Personage__ `:`", value="*Lv :* " + "`" + str(Statistiques[0])+ "`", inline=True)
        embed.add_field(name=":fleur_de_lis: __Sous__ __Palier__ `:`", value="*Pl :* " + "`" + str(Statistiques[1])+ "`", inline=True)
        embed.add_field(name=nonetxt, value=nonetxt, inline=False)
        embed.add_field(name=":crystal_ball: __Raprochement__ `:`", value="*Rp :* " + "`" + str(Statistiques[2])+ "`", inline=True)
        embed.add_field(name=":star_and_crescent: __Point__ __de__ __Folie__ `:`", value="*Fl :* " + "`" + str(Statistiques[3])+ "`", inline=True)
        embed.add_field(name=nonetxt, value=nonetxt, inline=False)
def CaraInterfaceWeapon(embed , Statistiques : list):
        embed.add_field(name="__Type__ __de__ __L'Arme__ `:`", value="*type :* " + "`" + str(Statistiques[0])+ "`", inline=True)
        embed.add_field(name="__Categorie__ __de__ __L'Arme__ `:`", value="*categorie :* " + "`" + str(Statistiques[1])+ "`", inline=True)
        embed.add_field(name=nonetxt, value=nonetxt, inline=False)
        embed.add_field(name="__Sous__ __Palier__ `:`", value="*palier :* " + "`" + str(Statistiques[2])+ "`", inline=True)
        embed.add_field(name="__Infusion__ __d'Arme__ `:`", value="*Fl :* " + "`" + str(Statistiques[3])+ "`", inline=True)
        embed.add_field(name=nonetxt, value=nonetxt, inline=False)
def healthInterface(embed, Statistiques : list):
        embed.add_field(name=" :purple_heart: __*Santé__ `point de vie :`:*", value="*Hp :* " + "`" + str(Statistiques[0])+ "/" + str(Statistiques[1]) + "`", inline=False)
def esquiveInterface(embed, Esquive : int):
        embed.add_field(name=" :loop: __*Esquive__ `esquive :`:*", value="*Pe :* " + "`" + str(Esquive) + "`", inline=False)
def diceInterface(embed, De : int):
        embed.add_field(name=" :game_die: __*Dé__ `d'Arme :`:*", value="*Dé :* " + "`" + str(De) + "`", inline=False)
def accessoryInterface(embed, Palier : int , Type : str):
        embed.add_field(name=" :prayer_beads: __*Accessoire__ `type/palier :`:*", value= "`" + Type + "/" + str(Palier) + "`", inline=False)
def attackInterfaceWeapon(embed , Competences : list , Tick : int):
        embed.add_field(name="Competences d'armes" , value="`_________________________________________`", inline=False)
        embed.add_field(name=Competences[0][1][0], value="```Cd = " + str(abszero(Competences[0][2][0] - (int(Tick) - Competences[0][2][1]))) + "```" + "du :" + str(Competences[0][2][1]), inline=True)
        embed.add_field(name=Competences[1][1][0], value="```Cd = " + str(abszero(Competences[1][2][0] - (int(Tick) - Competences[1][2][1]))) + "```" + "du :" + str(Competences[1][2][1]), inline=True)
        embed.add_field(name=Competences[2][1][0], value="```Cd = " + str(abszero(Competences[2][2][0] - (int(Tick) - Competences[2][2][1]))) + "```" + "du :" + str(Competences[2][2][1]), inline=True)
        embed.add_field(name=Competences[3][1][0], value="```Cd = " + str(abszero(Competences[3][2][0] - (int(Tick) - Competences[3][2][1]))) + "```" + "du :" + str(Competences[3][2][1]), inline=True)
def competencesInterfaceUser(embed , Competences : list , Tick : int):
        embed.add_field(name="Competences" , value="`_________________________________________`", inline=False)
        embed.add_field(name=Competences[0][1][0], value="```Cd = " + str(abszero(Competences[0][2][0] - (int(Tick) - Competences[0][2][1]))) + "```" + "du :" + str(Competences[0][2][1]), inline=True)
        embed.add_field(name=Competences[1][1][0], value="```Cd = " + str(abszero(Competences[1][2][0] - (int(Tick) - Competences[1][2][1]))) + "```" + "du :" + str(Competences[1][2][1]), inline=True)
        embed.add_field(name=Competences[2][1][0], value="```Cd = " + str(abszero(Competences[2][2][0] - (int(Tick) - Competences[2][2][1]))) + "```" + "du :" + str(Competences[2][2][1]), inline=True)
        embed.add_field(name=Competences[3][1][0], value="```Cd = " + str(abszero(Competences[3][2][0] - (int(Tick) - Competences[3][2][1]))) + "```" + "du :" + str(Competences[3][2][1]), inline=True)
def movesInterfaceUser(embed , Competences : list , Tick : int):
        embed.add_field(name="Mouvements" , value="`_________________________________________`", inline=False)
        embed.add_field(name=Competences[0][1][0], value="```Cd = " + str(abszero(Competences[0][2][0] - (int(Tick) - Competences[0][2][1]))) + "```" + "du :" + str(Competences[0][2][1]), inline=True)
        embed.add_field(name=Competences[1][1][0], value="```Cd = " + str(abszero(Competences[1][2][0] - (int(Tick) - Competences[1][2][1]))) + "```" + "du :" + str(Competences[1][2][1]), inline=True)
def getAvatar(embed, aseAAvatar : bool , link : str , ctx):
        if aseAAvatar:
                embed.add_field(name="```Avatar:```", value="```"+nonetxt+"```", inline=False)
                embed.set_image(url=link)
        else:
                embed.add_field(name="```Avatar:```", value="```"+nonetxt+"```", inline=False)
                embed.set_image(url=str(ctx.author.avatar_url))
def userName(embed , ctx):
        embed.add_field(name="*```Nom du Personnage```**:***", value="`**"+ctx.author.display_name+"**`", inline=False)
def setIterface(ctx ,embed , Unpile : list):
        userName(embed, ctx)
        healthInterface(embed , [Unpile[0].hp,Unpile[0].maxhp])
        esquiveInterface(embed , Unpile[1][2])
        diceInterface(embed , Unpile[6].depo)
        accessoryInterface(embed , 0 , "none")
        statInterfacePlayer(embed , [Unpile[0].lv,Unpile[0].pal,Unpile[1][0],Unpile[1][1]])
        CaraInterfaceWeapon(embed , [Unpile[6].__class__.__name__,Unpile[6].catg,Unpile[6].palier,"none"])
        statInterfaceWeapon(embed , Unpile[6].statistiques)
        print(str(Unpile[6].statistiques[0]) + str(Unpile[6].statistiques[1]))

        getAvatar(embed, Unpile[3][1] , Unpile[3][0] , ctx)
        embed.set_footer(text="test test test test")
        embed.set_footer(text="mise a jour par: {}".format(ctx.author.display_name))
def createWeapon(ctx):
        pass
def setTypeWeapon(ctx , name : str):
        select = create_select(
        options=[
                create_select_option("Dovoke", value="Dovoke"),
                create_select_option("Hirokami", value="Hirokami"),
                create_select_option("Kataro", value="Kataro"),
                create_select_option("Korechika", value="Korechika"),
                create_select_option("Riini", value="Riini"),
                create_select_option("Sekina", value="Sekina"),
                create_select_option("Sekriyina", value="Sekriyina"),
                create_select_option("Taviris", value="Taviris"),
                create_select_option("Thriallis", value="Thriallis"),
                create_select_option("Tlallassa", value="Tlallassa"),
                create_select_option("Triiana", value="Triiana"),
                create_select_option("Easthee", value="Easthee"),
                create_select_option("Ehara", value="Ehara"),
                create_select_option("Yagi", value="Yagi"),
                create_select_option("Hassan", value="Hassan")
                ],
        placeholder="Type de : " + name,
        min_values=1,
        max_values=1
    )
        return select
def setCategoryWeapon(ctx , name : str):
        select = create_select(
        options=[
                create_select_option("Lapis", value="Lapis"),
                create_select_option("Irlis", value="Irlis"),
                create_select_option("Jaade Vert", value="Jaade_Vert"),
                create_select_option("Jaade Noir", value="Jaade_Noir"),
                create_select_option("Easthee", value="Easthee")
                ],
        placeholder="Categorie de : " + name,
        min_values=1,
        max_values=1
    )
        return select
def setLevelWeapon(ctx , name : str):
        select = create_select(
        options=[
                create_select_option("*:+0 : Pale", value="0"),
                create_select_option("*:+1 : Tranchante", value="1"),
                create_select_option("*:+2 : Lunaire", value="2"),
                create_select_option("*:+3 : Azure", value="3"),
                create_select_option("*:+4 : Cyan", value="4"),
                create_select_option("*:+5 : Graphite", value="5"),
                create_select_option("*:+6 : Vèrnine", value="6"),
                create_select_option("*:+7 : Désertique", value="7"),
                create_select_option("*:+8 : Ancienne", value="8")
                ],
        placeholder="Palier de : " + name,
        min_values=1,
        max_values=1
    )
        return select
def setUserPl(ctx , name : str):
        select = create_select(
        options=[
                create_select_option("*:+0 : Foillia", value="0"),
                create_select_option("*:+1 : Pralea", value="1"),
                create_select_option("*:+2 : Nimée", value="2"),
                create_select_option("*:+3 : Galathéas", value="3"),
                create_select_option("*:+4 : Nivelia", value="4"),
                create_select_option("*:+5 : Nemezoryus", value="5"),
                create_select_option("*:+6 : Théidroph", value="6"),
                create_select_option("*:+7 : Srethillo", value="7"),
                create_select_option("*:+8 : Applinéath", value="8"),
                create_select_option("*:+9 : Vient", value="9")
                ],
        placeholder="Palier de : " + name,
        min_values=1,
        max_values=1
    )
        return select
def utility(Unpile : list, tick : int , result , nom : str):
        if result == "a":
                Stats , tick , Statut = Unpile[6].Attack(tick , nom)
                return Stats , tick , Statut
        if result == "u":
                Stats , tick , Statut = Unpile[0].use(tick , nom)
                return Stats , tick , Statut
        if resul == "m":
                Stats , tick , Statut = Unpile[0].use(tick , nom)
                return Stats , tick , Statut
        else:
                return [0,0,0] , tick , "none"

@bot.command()
async def statistiques(ctx):
        display_name = ctx.author.display_name
        User_Data = loadDict()
        if researchUser(User_Data , display_name):
            Unpile = dirUser(User_Data , display_name)
            embed = startEmbed(ctx , Unpile[6].name , Unpile[3][1] , Unpile[3][0])
            setIterface(ctx ,embed , Unpile)
            await ctx.send(embed=embed)
        else:
            await ctx.send("vous ne vous etes pas enregistrer")





@bot.command()
async def setWeapon1(ctx , *txt):
        name = " ".join(txt)
        select = setTypeWeapon(ctx , str(name))
        fait_choix = await ctx.send("`Choisissez le type de : `"+"__"+ str(name) + "__", components=[create_actionrow(select)])
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id 
        typageWeapon = await wait_for_component(bot, components=select, check=check)
        typeWea = typageWeapon.values[0]
        await typageWeapon.send("__" + str(name) +"__ : " + typeWea)





        select = setCategoryWeapon(ctx , str(name))
        fait_choix = await ctx.send("`Choisissez la Categorie de : `"+"__"+ str(name) + "__", components=[create_actionrow(select)])
        CatalogWeapon = await wait_for_component(bot, components=select, check=check)
        categoryWea = CatalogWeapon.values[0]
        await typageWeapon.send("__" + str(name) +"__ : " + categoryWea)


        select = setLevelWeapon(ctx , str(name))
        fait_choix = await ctx.send("`Choisissez le Palier de : `"+"__"+ str(name) + "__", components=[create_actionrow(select)])
        LevelingWeapon = await wait_for_component(bot, components=select, check=check)
        lvWea = LevelingWeapon.values[0]
        await typageWeapon.send("__" + str(name) +"__ : " + lvWea)

        await ctx.send("**nom de l'arme** : " + "`" + name +"`" + " , " + "**type de l'arme** : " + "`" + typeWea + "`" + " , " + "**categorie de l'arme** : " + "`" + categoryWea + "`" + " , " "**palier de l'arme** : " + "`" + lvWea + "`")
  


@bot.command()
async def registerUser(ctx):
        await ctx.send("`Nom de votre Personage :` " + ctx.author.display_name)
        #Level du personnage
        await ctx.send("`Veuillez entrer le Level de votre personnage: `")
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        try:
                lv = await bot.wait_for("message" , check = checkMessage)
                await ctx.send("**Lv du Personnage :**" + "`"+str(lv.content)+"`")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return
        #Vie max du personnage
        await ctx.send("`Veuillez entrer la santé maximale de votre personnage: `")
        try:
                hpmax = await bot.wait_for("message", timeout = 80, check = checkMessage)
                await ctx.send("**Vie du Personnage : **" + "`"+str(hpmax.content)+"/"+str(hpmax.content)+"`")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return




        user_name = ctx.author.display_name
        user_level = int(lv.content)
        user_maxhp = int(hpmax.content)
        select = setUserPl(ctx , user_name)
        fait_choix = await ctx.send("`Choisissez le niveau de plafond de : `"+"__"+ user_name + "__", components=[create_actionrow(select)])
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id 
        typageUser = await wait_for_component(bot, components=select, check=check)
        plafond = typageUser.values[0]
        await typageUser.send("__" + "Level de Plafond de " + user_name +"__ : " + plafond)




        #Image du personnage
        await ctx.send("`Entrez l'url de l'image de votre personnage(discord si possible). Si il n'en a pas ne repondez pas: `")
        try:
                User_Image_Url = (await bot.wait_for("message", timeout = 40, check = checkMessage)).content
                haveAImage = True
        except:
                User_Image_Url = " "
                haveAImage = False



        #Po du personnage
        await ctx.send("`Entrez la valeur des Points d'offense de base de votre personnage: `")
        try:
                Stat1 = await bot.wait_for("message", timeout = 80, check = checkMessage)
                await ctx.send("**__Po du Personnage :__**" + "`"+ str(Stat1.content)+ "`")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return
        #Ppr du personnage
        await ctx.send("`Entrez la valeur des Points de precision de base de votre personnage: `")
        try:
                Stat2 = await bot.wait_for("message", timeout = 80, check = checkMessage)
                await ctx.send("**__Ppr du Personnage :__**" + "`"+ str(Stat2.content)+ "`")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return
        #Pp du personnage
        await ctx.send("`Entrez la valeur des Points de Poison de base de votre personnage: `")
        try:
                Stat3 = await bot.wait_for("message", timeout = 80, check = checkMessage)
                await ctx.send("**__Pp du Personnage :__**" + "`"+ str(Stat3.content)+ "`")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return
        #Rp du personnage
        await ctx.send("`Entrez la valeur des Points de Raprochement de base de votre personnage: `")
        try:
                Cart1 = await bot.wait_for("message", timeout = 80, check = checkMessage)
                await ctx.send("**__Rp du Personnage :__**" + "`"+str(Cart1.content)+"`")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return
        #Pe du personnage
        await ctx.send("`Entrez la valeur des Points d'esquive' de base de votre personnage: `")
        try:
                Cart3 = await bot.wait_for("message", timeout = 80, check = checkMessage)
                await ctx.send("**__Rp du Personnage :__**" + "`"+str(Cart3.content)+"`")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return







        #Arme n * 1
        await ctx.send("```Nous allons a present enregistrer vos arme```")
        await ctx.send("__Arme__ __numero__ __1__")


        await ctx.send("`Quel est le nom de votre premiere Arme?: `")
        try:
                Weapon1_name = (await bot.wait_for("message", timeout = 80, check = checkMessage)).content
                await ctx.send("**__Nom de l'arme :__**" + "`"+str(Weapon1_name)+"`")
        except:
                Weapon1_name = "Weapon 1"
                await ctx.send("**__Nom de l'arme :__**" + "`"+str(Weapon1_name)+"`")




        #Weapon Type
        select = setTypeWeapon(ctx , Weapon1_name)
        fait_choix = await ctx.send("`Choisissez le type de : `"+"__"+ Weapon1_name + "__", components=[create_actionrow(select)])
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id 
        typageWeapon = await wait_for_component(bot, components=select, check=check)
        typeWea1 = typageWeapon.values[0]
        await typageWeapon.send("__" + Weapon1_name +"__ : " + typeWea1)




        #Weapon Category
        select = setCategoryWeapon(ctx , Weapon1_name)
        fait_choix = await ctx.send("`Choisissez la Categorie de : `"+"__"+ Weapon1_name + "__", components=[create_actionrow(select)])
        CatalogWeapon = await wait_for_component(bot, components=select, check=check)
        categoryWea1 = CatalogWeapon.values[0]
        print(categoryWea1)
        await typageWeapon.send("__" + Weapon1_name +"__ : " + categoryWea1)


        #Weapon Lv
        select = setLevelWeapon(ctx , Weapon1_name)
        fait_choix = await ctx.send("`Choisissez le Palier de : `"+"__"+ Weapon1_name + "__", components=[create_actionrow(select)])
        LevelingWeapon = await wait_for_component(bot, components=select, check=check)
        lvWea1 = LevelingWeapon.values[0]
        await typageWeapon.send("__" + Weapon1_name +"__ : " + lvWea1)

        await ctx.send("**nom de l'arme** : " + "`" + Weapon1_name +"`" + " , " + "**type de l'arme** : " + "`" + typeWea1 + "`" + " , " + "**categorie de l'arme** : " + "`" + categoryWea1 + "`" + " , " "**palier de l'arme** : " + "`" + lvWea1 + "`")



        




        #Arme n * 2
        await ctx.send("__Arme__ __numero__ __2__")


        await ctx.send("`Quel est le nom de votre deuxieme Arme?: `")
        try:
                Weapon2_name = (await bot.wait_for("message", timeout = 80, check = checkMessage)).content
                await ctx.send("**__Nom de l'arme :__**" + "`"+str(Weapon1_name)+"`")
        except:
                Weapon2_name = "Weapon 2"
                await ctx.send("**__Nom de l'arme :__**" + "`"+str(Weapon1_name)+"`")




        #Weapon Type
        select = setTypeWeapon(ctx , Weapon2_name)
        fait_choix = await ctx.send("`Choisissez le type de : `"+"__"+ Weapon2_name + "__", components=[create_actionrow(select)])
        def check(m):
                return m.author_id == ctx.author.id and m.origin_message.id == fait_choix.id 
        typageWeapon = await wait_for_component(bot, components=select, check=check)
        typeWea2 = typageWeapon.values[0]
        await typageWeapon.send("__" + Weapon2_name +"__ : " + typeWea2)




        #Weapon Category
        select = setCategoryWeapon(ctx , Weapon2_name)
        fait_choix = await ctx.send("`Choisissez la Categorie de : `"+"__"+ Weapon2_name + "__", components=[create_actionrow(select)])
        CatalogWeapon = await wait_for_component(bot, components=select, check=check)
        categoryWea2 = CatalogWeapon.values[0]
        await typageWeapon.send("__" + Weapon2_name +"__ : " + categoryWea2)


        #Weapon Lv
        select = setLevelWeapon(ctx , Weapon2_name)
        fait_choix = await ctx.send("`Choisissez le Palier de : `"+"__"+ Weapon2_name + "__", components=[create_actionrow(select)])
        LevelingWeapon = await wait_for_component(bot, components=select, check=check)
        lvWea2 = LevelingWeapon.values[0]
        await typageWeapon.send("__" + Weapon2_name +"__ : " + lvWea2)

        await ctx.send("**nom de l'arme** : " + "`" + Weapon2_name +"`" + " , " + "**type de l'arme** : " + "`" + typeWea2 + "`" + " , " + "**categorie de l'arme** : " + "`" + categoryWea2 + "`" + " , " "**palier de l'arme** : " + "`" + lvWea2 + "`")















        #regroupement   
        Statistiques_de_personnage = [int(Stat1.content),int(Stat2.content),0,int(Stat3.content),0]
        Caracteristiques_de_personnage = [int(Cart1.content),0,int(Cart3.content)]
        NewUser = User(user_name , user_maxhp , user_level , plafond)
        Weapon1 = createNewWeapon(typeWea1,Weapon1_name,categoryWea1,int(lvWea1),Statistiques_de_personnage)
        Weapon2 = createNewWeapon(typeWea2,Weapon2_name,categoryWea2,int(lvWea2),Statistiques_de_personnage)
        Main_Weapon = Weapon1
        User_Image = [User_Image_Url,haveAImage]
        RegisterListe = [NewUser , Caracteristiques_de_personnage , Statistiques_de_personnage, User_Image ,Weapon1,Weapon2,Main_Weapon]
        

        

        updateValue(User_Data,user_name,RegisterListe)
        embed = startEmbed(ctx , RegisterListe[6].name , RegisterListe[3][1] , RegisterListe[3][0])
        setIterface(ctx ,embed , RegisterListe)
        await ctx.send(embed=embed)






@bot.command()
async def switch(ctx):
        display_name = ctx.author.display_name
        User_Data = loadDict()
        if researchUser(User_Data , display_name):
            if User_Data[display_name][6] == User_Data[display_name][4]:
                User_Data[display_name][6] = User_Data[display_name][5]
                saveDict(User_Data)
            else:
                User_Data[display_name][6] = User_Data[display_name][4]
                saveDict(User_Data)
            Unpile = dirUser(User_Data , display_name)
            embed = startEmbed(ctx , Unpile[6].name , Unpile[3][1] , Unpile[3][0])
            setIterface(ctx ,embed , Unpile)
            await ctx.send(embed=embed)
        else:
            await ctx.send("vous ne vous etes pas enregistrer")


@bot.command()
async def competences(ctx ,Tick):
        display_name = ctx.author.display_name
        User_Data = loadDict()
        if researchUser(User_Data , display_name):
            Unpile = User_Data[display_name]
            embed = startEmbedImage(ctx ,Unpile[6].name, Unpile[6].image)
            attackInterfaceWeapon(embed , Unpile[6].Competences , Tick)
            competencesInterfaceUser(embed , Unpile[0].Competences , Tick)
            movesInterfaceUser(embed , Unpile[0].moveCompetences , Tick)
            embed.set_footer(text="mise a jour par: {}".format(ctx.author.display_name))
            await ctx.send(embed=embed)
            print(str(Tick))
        else:
            await ctx.send("vous ne vous etes pas enregistrer")    

@bot.command()
async def useCompetence(ctx , Tick1):
        display_name = ctx.author.display_name
        User_Data = loadDict()
        await ctx.send("`a : pour une attaque , u : pour une competence , m : pour un mouvement `")
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        try:
                result = (await bot.wait_for("message" , check = checkMessage)).content
                await ctx.send("```"+str(result)+"```")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return
        await ctx.send("`nom de la competence `")
        try:
                nom = (await bot.wait_for("message" , check = checkMessage)).content
                await ctx.send("```"+str(nom)+"```")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return
        if researchUser(User_Data , display_name):
            Unpile = User_Data[display_name]
            Stats , t , Etat = utility(Unpile, int(Tick1) , result , nom)
            await ctx.send(str(Stats[0]) + " " + str(Stats[1]) + " " + str(Stats[2]))
            await ctx.send("Tick :" + str(t))
        else:
            await ctx.send("vous ne vous etes pas enregistrer")
@bot.command()
async def infoUser(ctx):
        display_name = ctx.author.display_name
        User_Data = loadDict()
        if researchUser(User_Data , display_name):
            Unpile = User_Data[display_name]
            await ctx.send("**Vie :**" + "`"+str(Unpile[0].hp)+"/"+str(Unpile[0].maxhp)+"`")
            await ctx.send("**Pe :**" + "`"+str(Unpile[1][2])+"`")
        else:
            await ctx.send("vous ne vous etes pas enregistrer")
@bot.command()            
async def helpComp(ctx):
        display_name = ctx.author.display_name
        User_Data = loadDict()
        await ctx.send("`competence? `")
        def checkMessage(message):
                return message.author == ctx.message.author and ctx.message.channel == message.channel
        try:
                competence = (await bot.wait_for("message" , check = checkMessage)).content
                await ctx.send("```"+str(competence)+"```")
        except:
                await ctx.send("__Veuillez__ __réitérer__ __la__ __commande.__")
                return        
        if researchUser(User_Data , display_name):
            Unpile = User_Data[display_name]
            a , b , c , d , e = Unpile[6].helpCompetence(competence)
            print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e))
            await ctx.send(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e))
        else:
            await ctx.send("vous ne vous etes pas enregistrer")
@bot.command()
async def say(ctx, *txt):
        await ctx.send(" ".join(txt))
@bot.command()
async def sayA(ctx, *txt):
        mess = await ctx.channel.history(limit = 1).flatten()
        await mess[0].delete()
        await ctx.send(" ".join(txt))

@bot.command()
async def nB(ctx):
        mess = await ctx.channel.history(limit = 1).flatten()
        await mess[0].delete()
        await ctx.send('me trying to find the bitches' , file=discord.File("lolaImg1.png"))
@bot.command()
async def cringe(ctx):
        mess = await ctx.channel.history(limit = 1).flatten()
        await mess[0].delete()
        await ctx.send(file=discord.File("lolaImg3.gif"))
@bot.command()
async def br(ctx ,txt):
        num = random.randint(0, 5)
        liste = ['why did you post that?"', 'delete your account','stop posting', 'stop using twiter' , 'go touch grass bro', 'why are u gay?']
        mess = await ctx.channel.history(limit = 1).flatten()
        await mess[0].delete()
        await ctx.send('Wait this is cringe ' + str(txt) + liste[num] ,file=discord.File("lolaImg6.png"))
bot.run("OTU2Mzk1NDgxODM4MjgwNzM0.Yjvmsw.mrpqPIQZAn4Lh4v4E5iJzAKfVD8")
