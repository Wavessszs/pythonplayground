import random
import time

factions = ["Bandits","Bandit", "Hyperion", "Jakobs", "Maliwan", "Torgue", "Vladof","Tediore"]

adjectives = ['Savage', 'Fierce', 'Ruthless', 'Fearless', 'Reckless', 'Badass', 'Intense', 'Brutal', 'Hardcore', 'Tenacious', 'Ferocious', 'Relentless', 'Unstoppable', 'Merciless', 'Formidable', 'Dangerous', 'Unforgiving', 'Wild', 'Fermenting', 'Challenging','Benevolent', 'Malevolent', 'Stellar', 'Ethereal', 'Celestial', 'Majestic', 'Radiant', 'Spectral', 'Cosmic', 'Enchanted', 'Mystical', 'Magical', 'Mythical', 'Legendary', 'Divine', 'Arcane', 'Fabled', 'Epic', 'Legendary', 'Furtive', 'Stealthy', 'Nimble', 'Sneaky', 'Shadowy', 'Elusive', 'Covert', 'Slippery', 'Mysterious', 'Cryptic', 'Arcane', 'Enigmatic', 'Shrouded', 'Inscrutable', 'Whimsical', 'Wacky', 'Kooky', 'Silly', 'Goofy', 'Zany', 'Funky', 'Quirky', 'Offbeat', 'Oddball', 'Romantic', 'Passionate', 'Amorous', 'Enamored', 'Sensual', 'Intimate', 'Affectionate', 'Tender', 'Adoring', 'Devoted', 'Loving']

vladof = ['Zarnikov', 'Volkov', 'Chernov', 'Vysotka', 'Strykerov', 'Krukov', 'Valkyrie', 'Hammerov', 'Havocov', 'Tunguskov']
hyperion = ['Protos', 'Eridian Edge', 'Razorwire', 'Omega Striker', 'Xion Cannon', 'Reactor', 'Taser', 'Dominator', 'Eon Blaster', 'Chronos Beam']
maliwan = ['Inferno', 'Frostbite', 'Stormfront', 'Venomous', 'Corrosive Cloud', 'Necrosis', 'Radiant', 'Atomic Ray', 'Electric Arc', 'Sonic Wave']
bandit = ['Rampage', 'Skag Launcher', 'Buzzaxe', 'Shank', 'Carnage', 'Slag Gun', 'Brutality', 'Punk Pistol', 'Mayhem Machine', 'Boomstick']
torgue = ['Explosion', 'Rocketeer', 'Grenadier', 'Shrapnel', 'Cannonade', 'Blastwave', 'Demolition', 'Pummeler', 'Barrage', 'Detonator']
jakobs = ['Deadshot', 'Lawmaker', 'Sharpshooter', 'Marksman', 'Ranger', 'Gunslinger', 'Deadeye', 'Outlaw', 'High Noon', 'Sniper']
tediore = ["Baby Maker", "Blockhead", "Chopper", "Deliverance", "Expeditious Slow Hand", "Gunerang", "Infection Cleaner", "Leverage", "Reloaded", "Splattergun"]

verbs = ['Charming', 'Endearing', 'Flattering', 'Captivating', 'Enamoring', 'Adoring', 'Bewitching', 'Enchanting', 'Alluring', 'Entrancing', 'Fascinating', 'Glamorous', 'Gorgeous', 'Stunning', 'Appealing', 'Attractive', 'Mesmerizing', 'Seductive', 'Sensual', 'Passionate', 'Intoxicating', 'Irresistible','Annihilator', 'Exterminator', 'Obliterator', 'Incinerator', 'Decimator', 'Demolisher', 'Eviscerator', 'Vaporizer', 'Devastator', 'Corruptor', 'Disintegrator', 'Annihilator', 'Eradicator', 'Humiliator', 'Inflictor', 'Mauler', 'Neutralizer', 'Pulverizer', 'Ravager', 'Saboteur', 'Terminator','Splishsplashtor', 'Bamboozlator', 'Hoodwinkator', 'Ticklefightor', 'Flippityflopator', 'Gigglesnortor', 'Wigglewormor', 'Smoochinator', 'Jibberjabberor', 'Crisscrossor', 'Flibbertigibbetor', 'Brouhahahor', 'Bamboozlor', 'Kerfufflor', 'Pifflepuffor', 'Willynillyor', 'Jabberwockor', 'Snickersnackor', 'Sassafrasor']

print("gun assembly simulator")
hidden = factions.pop(1)
print(factions)
factions.insert(1, hidden)
while True:

    user = random.choice(factions)
    print(user)

    try:
        if user in factions:
            adj = random.choice(adjectives)
            verb = random.choice(verbs)
            user = user.lower()
            if user == "vladof":
                v_result = random.choice(vladof)
                print(adj+' '+v_result+' '+verb)
            elif user == "hyperion":
                h_result = random.choice(hyperion)
                print(adj+' '+h_result+' '+verb)
            elif user == "maliwan":
                m_result = random.choice(maliwan)
                print(adj +' '+ m_result +' '+ verb)
            elif user == "bandits" or user == "bandit":
                b_result = random.choice(bandit)
                print(adj +' '+ b_result +' '+ verb)
            elif user == "torgue":
                t_result = random.choice(torgue)
                print(adj + ' '+t_result +' '+ verb)
            elif user == "jakobs":
                j_result = random.choice(jakobs)
                print(adj + ' '+j_result +' '+ verb)
            elif user == "tediore":
                td_result = random.choice(tediore)
                print(adj +' '+ td_result +' '+ verb)
        else:
            raise TypeError
    except TypeError:
        print("haha, type a real faction bro.")
    time.sleep(3)