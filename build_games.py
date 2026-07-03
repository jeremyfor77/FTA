import json
import os

SITE = os.path.dirname(os.path.abspath(__file__))
GAMES_DIR = os.path.join(SITE, "games")
ASSETS = os.path.join(SITE, "assets")

# slug, name, genre, img (or None), players, platform, status, blurb paragraphs
GAMES = [
    dict(
        slug="7-days-to-die", name="7 Days to Die", genre="Survival Horror",
        img="7daystodie.jpg", players="1–6 Co-op", platform="PC (Steam)",
        status="Dedicated Server Live",
        blurb=[
            "This is the one with our own bunker. FTA runs a dedicated V3.0 “Dead Hot Summer” server on Navezgane, tuned with a custom SandboxCode and a four-mod loadout that adds crafting from nearby storage, denser biomes, steadier vehicles, and a cleaner HUD.",
            "The one house rule, enforced at the config level rather than asked nicely: zombies do not dig. Full connection details and the current mod package are posted on the front page.",
        ],
    ),
    dict(
        slug="path-of-exile-2", name="Path of Exile 2", genre="Action RPG",
        img="poe2.jpg", players="1–6 Co-op", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "A slower, heavier sequel to a game already known for burying players in mechanics. Passive tree the size of a small country, skill gems that combo into builds nobody asked for, and bosses that punish greed with a single mistimed dodge roll.",
            "FTA runs seasonal leagues together — same start, same league mechanic, compared loot at the end of the night.",
        ],
    ),
    dict(
        slug="league-of-legends", name="League of Legends", genre="MOBA",
        img="leagueoflegends.jpg", players="5v5", platform="PC (Riot Client)",
        status="Active Rotation",
        blurb=[
            "The one game on this list that isn't on Steam — Riot keeps its own client, its own launcher, and its own particular brand of chat restrictions. Photo above via Riot's official splash art library, not the store capsule everything else on this page borrows from.",
            "FTA runs normals and the occasional ranked flex night. Bring a champion pool, leave the tilt at the door.",
        ],
    ),
    dict(
        slug="arc-raiders", name="ARC Raiders", genre="Extraction Shooter",
        img="arcraiders.jpg", players="1–3 Squad", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "Third-person PvPvE extraction against a hostile world of machine swarms — raid a map, loot what you can carry, and get to evac before either the ARC or another squad ends your run early.",
            "High tension, short sessions, gear loss that actually stings. Good for a single fast round between other games.",
        ],
    ),
    dict(
        slug="atlas", name="Atlas", genre="Pirate MMO",
        img="atlas.jpg", players="Server-wide", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "A sprawling pirate-age MMO built on the bones of ARK's survival systems — crew a ship, chart open ocean, raid other companies' claims, and lose it all to a storm you didn't see coming.",
            "Slow burn, big payoff. Best played with a full crew and nobody in a hurry.",
        ],
    ),
    dict(
        slug="black-desert", name="Black Desert", genre="MMORPG",
        img="blackdesert.jpg", players="Server-wide", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "Action-combat MMO with a life-skill economy deep enough to play as its own game — fishing, cooking, trading, and node wars for players who'd rather not touch combat at all.",
            "FTA mostly shows up for world bosses and the occasional guild siege.",
        ],
    ),
    dict(
        slug="no-mans-sky", name="No Man's Sky", genre="Space Survival",
        img="nomanssky.jpg", players="1–4 Co-op", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "A procedurally generated galaxy that's gone from launch-week punchline to one of the most-updated games on Steam. Build a base, fly a freighter, land on a planet nobody in the squad has seen yet.",
            "Low-pressure, good for winding down after a harder game earlier in the night.",
        ],
    ),
    dict(
        slug="palworld", name="Palworld", genre="Creature Survival",
        img="palworld.jpg", players="1–4 Co-op", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "Open-world survival crafting with creatures that work the base, staff the production lines, and occasionally end up in a firearm. Equal parts monster-collector and factory game.",
            "Easy to pick up mid-session; the base-building alone eats an evening.",
        ],
    ),
    dict(
        slug="enshrouded", name="Enshrouded", genre="Survival Action RPG",
        img="enshrouded.jpg", players="1–16 Co-op", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "Voxel survival crafting under a toxic mist that mutates anything caught inside it after dark. Build vertical, dig deep, and time your Shroud runs carefully.",
            "The building tools alone have kept more than one FTA session running past bedtime.",
        ],
    ),
    dict(
        slug="dune-awakening", name="Dune: Awakening", genre="Survival MMO",
        img="dune.jpg", players="Server-wide", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "Arrakis, survival-crafted: manage water like it's currency, ride the worms if you're brave or foolish, and watch the horizon for a Coriolis storm rolling in over open sand.",
            "Faction politics run deep here — FTA plays it mostly as a co-op survival game and lets the politics happen around us.",
        ],
    ),
    dict(
        slug="deadside", name="Deadside", genre="Survival Shooter",
        img="deadside.jpg", players="1–4 Squad", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "Hardcore open-world survival shooter — Eastern-European backdrop, permadeath economy, and PvP that turns any loot run into a decision about how much you're willing to lose.",
            "Not for the faint of heart. Bring a squad and a plan for extraction.",
        ],
    ),
    dict(
        slug="rust", name="Rust", genre="Survival",
        img="rust.jpg", players="Server-wide", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "The one that started the modern survival-crafting genre and still runs the hardest version of it — base raids, geared roamers, and a wipe schedule the whole clan plans around.",
            "First few hours of a fresh wipe are, historically, when most of FTA's best and worst decisions get made.",
        ],
    ),
    dict(
        slug="satisfactory", name="Satisfactory", genre="Factory Builder",
        img="satisfactory.jpg", players="1–4 Co-op", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "First-person factory automation on an alien planet — belts, pipes, trains, and a production chain that eventually spans the whole map if nobody stops to touch grass.",
            "The most likely game on this list to make someone show up late to their own bedtime.",
        ],
    ),
    dict(
        slug="astroneer", name="Astroneer", genre="Space Exploration",
        img="astroneer.jpg", players="1–4 Co-op", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "Low-stakes planetary exploration and terrain deformation — dig, terraform, and build a research outpost across a handful of small, friendly planets.",
            "The easiest recommendation on this list for a new member's first FTA session.",
        ],
    ),
    dict(
        slug="conan-exiles-enhanced", name="Conan Exiles Enhanced", genre="Survival",
        img="conanexiles.jpg", players="1–40 Server", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "Sword-and-sorcery survival in the Exiled Lands — build a keep, wrestle thralls into servitude, and contend with a climate system that will kill you just as fast as any player raid.",
            "The Enhanced Edition brought a visual overhaul that finally makes the Exiled Lands look as brutal as they play.",
        ],
    ),
    dict(
        slug="dark-and-darker", name="Dark and Darker", genre="Extraction Fantasy",
        img="darkanddarker.jpg", players="1–3 Party", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "First-person dungeon-crawl extraction — pick a class, drop in low on gear, and fight your way to an exit against monsters and other parties who want exactly what you're carrying.",
            "Short, brutal rounds. Good for a tight two-or-three-person FTA squad on a weeknight.",
        ],
    ),
    dict(
        slug="necesse", name="Necesse", genre="Sandbox Survival",
        img="necesse.jpg", players="1–8 Co-op", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "Top-down sandbox survival with a town-builder's heart — recruit settlers, defend the walls come nightfall, and gradually turn a starting camp into a proper kingdom.",
            "Quietly one of the most relaxing games in the FTA rotation, right up until the raid horn sounds.",
        ],
    ),
    dict(
        slug="terraria", name="Terraria", genre="2D Sandbox Adventure",
        img="terraria.jpg", players="1–8 Co-op", platform="PC (Steam)",
        status="Active Rotation",
        blurb=[
            "The 2D sandbox that keeps getting content updates a decade past when anyone expected them. Dig down, build up, and work through a boss progression that still surprises people who think they've seen it all.",
            "A reliable FTA classic — easy to onboard a new member into, hard to actually finish.",
        ],
    ),
]


def esc(s):
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


PAGE_TMPL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — FTA Field Gazette</title>
<meta name="description" content="{genre} — in active rotation with the FTA clan.">
<link rel="stylesheet" href="../assets/style.css">
</head>
<body>

<header class="masthead">
  <div class="wrap masthead-top">
    <span>Vol. I — No. 1</span>
    <button class="theme-toggle" id="themeToggle" type="button" aria-pressed="false">Night Edition</button>
    <span>Special Section — Games</span>
  </div>
  <div class="wrap masthead-name">
    <a href="../index.html"><span class="mast-word">FTA</span></a>
    <div class="mast-tagline">Founded on Spite &amp; Scrap Metal</div>
  </div>
  <nav class="wrap tabs" aria-label="Sections">
    <a class="tab" href="../index.html#dispatch">Front Page</a>
    <a class="tab" href="../index.html#games" aria-current="page">Games</a>
    <a class="tab" href="../index.html#roster">Roster</a>
    <a class="tab" href="../index.html#log">Field Log</a>
    <a class="tab" href="../index.html#comms">Comms</a>
  </nav>
</header>

<div class="wrap back-strip">
  <a href="../index.html#games">&#9668; Back to Front Page</a>
</div>

<main class="wrap">
  <section class="lead" style="padding-top:22px;">
    <span class="kicker">{genre}</span>
    <h1 class="headline">{name}</h1>
  </section>

  <div class="game-photo">
    {photo_inner}
  </div>
  <p class="game-caption">{caption}</p>

  <div class="game-body">
    <div class="game-story">
      {paragraphs}
    </div>
    <dl class="fact-box">
      <dt>Genre</dt><dd>{genre}</dd>
      <dt>Party Size</dt><dd>{players}</dd>
      <dt>Platform</dt><dd>{platform}</dd>
      <dt>FTA Status</dt><dd>{status}</dd>
    </dl>
  </div>
</main>

<footer>
  FTA Field Gazette &middot; Special Section: Games &middot; <a href="../index.html">Return to Front Page</a>
</footer>

<script src="../assets/script.js"></script>
</body>
</html>
"""

for g in GAMES:
    if g["img"]:
        photo_inner = (
            f'<img src="../assets/img/games/{g["img"]}" alt="{esc(g["name"])}">'
            f'<div class="halftone-overlay"></div>'
        )
        if g["slug"] == "league-of-legends":
            caption = f'Official splash art, {esc(g["name"])}. Reproduced from Riot Games assets.'
        else:
            caption = f'Official capsule art, {esc(g["name"])}. Reproduced from Steam store assets.'
    else:
        photo_inner = (
            '<div style="aspect-ratio:616/353;display:flex;align-items:center;'
            'justify-content:center;font-family:var(--font-mono);font-size:12px;'
            'text-transform:uppercase;letter-spacing:0.06em;color:var(--ink-faint);'
            'background:var(--paper-raised);">Photograph Not Available</div>'
        )
        caption = f'No wire photo on file for {esc(g["name"])} — not distributed via Steam.'

    paragraphs = "\n      ".join(f"<p>{esc(p)}</p>" for p in g["blurb"])

    html = PAGE_TMPL.format(
        name=esc(g["name"]),
        genre=esc(g["genre"]),
        players=esc(g["players"]),
        platform=esc(g["platform"]),
        status=esc(g["status"]),
        photo_inner=photo_inner,
        caption=caption,
        paragraphs=paragraphs,
    )
    with open(os.path.join(GAMES_DIR, g["slug"] + ".html"), "w", encoding="utf-8") as f:
        f.write(html)

# shared data file for the front-page index grid
js_games = [
    dict(slug=g["slug"], name=g["name"], genre=g["genre"], img=g["img"])
    for g in GAMES
]
with open(os.path.join(ASSETS, "games-data.js"), "w", encoding="utf-8") as f:
    f.write("var GAMES = " + json.dumps(js_games, indent=2) + ";\n")

print(f"Generated {len(GAMES)} game pages + games-data.js")
