"""
MAI Evolution - Mock Data for Feature Demo
Fictional but data-informed audience growth trajectories
"""

EVOLUTION_DATA = {
    # Catriel y Paco Amoroso
    "catriel y paco amoroso": {
        "artist_name": "Catriel y Paco Amoroso",
        "spotify_id": "catriel_paco_amoroso",
        "available": True,
        "eras": [
            {
                "year_start": 2015,
                "year_end": 2016,
                "title": "Argentine Trap Pioneers",
                "trigger": "SoundCloud uploads → 'Bzrp Vol. 1' vibes",
                "audience_index": 1,
                "multiplier_vs_prev": None,
                "venue_level": "CLUB",
                "example_venues": ["La Otra Sala (Buenos Aires)", "Club Hipopótamo (CABA)"],
                "notes": "Underground trap argentino. Regional following en CABA y GBA.",
                "key_metric": "500K SoundCloud followers"
            },
            {
                "year_start": 2017,
                "year_end": 2018,
                "title": "Colabs & Breakthrough",
                "trigger": "Colaboraciones con Bizarrap, Ysy A",
                "audience_index": 3,
                "multiplier_vs_prev": 3.0,
                "venue_level": "THEATER",
                "example_venues": ["Teatro Ópera (CABA)", "Niceto Club (Buenos Aires)"],
                "notes": "Trap latino network effect. Spotify playlists de curador.",
                "key_metric": "15M Spotify monthly listeners"
            },
            {
                "year_start": 2019,
                "year_end": 2019,
                "title": "Album Breakthrough",
                "trigger": "Album de estudio con hits nacionales",
                "audience_index": 6,
                "multiplier_vs_prev": 2.0,
                "venue_level": "ARENA",
                "example_venues": ["Luna Park (Buenos Aires)", "Teatro Gran Rex (CABA)"],
                "notes": "Primeros conciertos en arenas. Hit regional en plataformas.",
                "key_metric": "40M Spotify streams"
            },
            {
                "year_start": 2020,
                "year_end": 2021,
                "title": "Pandemic Digital Growth",
                "trigger": "Streaming surge + TikTok virality",
                "audience_index": 12,
                "multiplier_vs_prev": 2.0,
                "venue_level": "ARENA",
                "example_venues": ["Estadio Obras Sanitarias (CABA)", "Festival Pepsi Music"],
                "notes": "TikTok placement en Latam. Crecimiento exponencial en streams.",
                "key_metric": "200M+ Spotify streams"
            },
            {
                "year_start": 2022,
                "year_end": 2023,
                "title": "Latin America Expansion",
                "trigger": "Tours por Colombia, México, Chile",
                "audience_index": 20,
                "multiplier_vs_prev": 1.67,
                "venue_level": "ARENA",
                "example_venues": ["Movistar Arena (CABA)", "Coliseo Jorge Fiallo (Medellín)"],
                "notes": "Expansión regional exitosa. Ascenso en charts regionales.",
                "key_metric": "500M+ total streams"
            },
            {
                "year_start": 2024,
                "year_end": 2026,
                "title": "Consolidación & Tour de Estadios",
                "trigger": "Festival appearances + International growth",
                "audience_index": 30,
                "multiplier_vs_prev": 1.5,
                "venue_level": "STADIUM",
                "example_venues": ["Estadio Tecnológico (Monterrey)", "Estadio Jorge Newbery (CABA)"],
                "notes": "Trap argentino mainstream. Considerados referentes del género.",
                "key_metric": "1B+ total streams"
            }
        ],
        "insights": [
            "🇦🇷 Trap argentino goes mainstream (CABA → Latam)",
            "📱 TikTok = critical growth driver for urban genres",
            "🎪 Regional duo → international touring en 8 años",
            "💿 Streaming democratiza acceso a arenas",
            "🎯 Genre-specific audience vs género pop genérico"
        ]
    },
    
    # Bad Bunny
    "bad bunny": {
        "artist_name": "Bad Bunny",
        "spotify_id": "4q3ewBCX7sLwd24euL69vQ",
        "available": True,
        "eras": [
            {
                "year_start": 2016,
                "year_end": 2017,
                "title": "Trap Breakout",
                "trigger": "SoundCloud releases → 'Soy Peor'",
                "audience_index": 1,
                "multiplier_vs_prev": None,
                "venue_level": "CLUB",
                "example_venues": ["Sala Clamores (Madrid)", "Brooklyn Steel (NYC)"],
                "notes": "Underground trap latino movement. Regional cult following.",
                "key_metric": "2M SoundCloud followers"
            },
            {
                "year_start": 2018,
                "year_end": 2018,
                "title": "Colabs + Crossover",
                "trigger": "Collaboration features: J Balvin, Drake",
                "audience_index": 3,
                "multiplier_vs_prev": 3.0,
                "venue_level": "THEATER",
                "example_venues": ["Palau Sant Jordi (Barcelona)", "Fillmore (SF)"],
                "notes": "Strategic features break through to mainstream. Spotify Billions playlist.",
                "key_metric": "30M Spotify monthly listeners"
            },
            {
                "year_start": 2019,
                "year_end": 2019,
                "title": "X 100pre Tour",
                "trigger": "Album 'X 100pre' → Historic Puerto Rico concerts",
                "audience_index": 8,
                "multiplier_vs_prev": 2.67,
                "venue_level": "ARENA",
                "example_venues": ["Madison Square Garden (NYC)", "José M. Figueroa (Puerto Rico)"],
                "notes": "First arena-level tour. International explosion. Reggaeton goes global.",
                "key_metric": "100M+ Spotify streams"
            },
            {
                "year_start": 2020,
                "year_end": 2022,
                "title": "Streaming Domination",
                "trigger": "Albums 'YHLQMDLG' + 'Las Que No Iban a Salir' during pandemic",
                "audience_index": 18,
                "multiplier_vs_prev": 2.25,
                "venue_level": "STADIUM",
                "example_venues": ["Yankee Stadium (NYC)", "SoFi Stadium (LA)"],
                "notes": "Pandemic pivot: streaming success. Becomes top global artist. Bilingual dominance.",
                "key_metric": "100B+ total streams"
            },
            {
                "year_start": 2022,
                "year_end": 2022,
                "title": "World's Hottest Tour",
                "trigger": "Highest-grossing tour by Latin artist",
                "audience_index": 30,
                "multiplier_vs_prev": 1.67,
                "venue_level": "STADIUM",
                "example_venues": ["SoFi Stadium (LA)", "Allegiant Stadium (Las Vegas)"],
                "notes": "Record-breaking tour revenue. Establishes touring dominance.",
                "key_metric": "$430M+ tour gross"
            },
            {
                "year_start": 2025,
                "year_end": 2026,
                "title": "Global #1 Artist",
                "trigger": "Consistent chart & streaming dominance",
                "audience_index": 40,
                "multiplier_vs_prev": 1.33,
                "venue_level": "STADIUM",
                "example_venues": ["Estadio Azteca (Mexico City)", "Global festivals"],
                "notes": "Cultural phenomenon. Streams across all demographics & geographies.",
                "key_metric": "12B+ annual streams"
            }
        ],
        "insights": [
            "🎯 Trap latino → global phenomenon in 8 years",
            "🌍 Bilingual strategy = unlimited market TAM",
            "📈 Venue progression: CLUB → STADIUM in 6 years",
            "💿 Streaming era = home advantage (no touring constraints)",
            "🎪 Tour revenue = 2nd pillar (streaming #1)"
        ],
        "audience_insights": [
            "Tras X 100pre, la audiencia se multiplica aproximadamente por x3, pasando de venues de 1.000–3.000 personas a arenas de 15.000–20.000, con expansión fuerte desde Latinoamérica hacia EE.UU.",
            "El salto a giras en estadios implica un crecimiento de ~x1.7, escalando de arenas a estadios de 60.000–80.000 personas y consolidando consumo simultáneo en América, Europa y otros mercados globales."
        ]
    },
    
    # Taylor Swift
    "taylor swift": {
        "artist_name": "Taylor Swift",
        "spotify_id": "06HL4z0CvFAxyc27GXpf94",
        "available": True,
        "eras": [
            {
                "year_start": 2006,
                "year_end": 2008,
                "title": "Country Debut",
                "trigger": "Debut album 'Taylor Swift' + 'Fearless'",
                "audience_index": 1,
                "multiplier_vs_prev": None,
                "venue_level": "CLUB",
                "example_venues": ["The Bluebird Cafe (Nashville)", "Troubadour (LA)"],
                "notes": "Country pop crossover artist. Teen fanbase in USA.",
                "key_metric": "3M album sales"
            },
            {
                "year_start": 2009,
                "year_end": 2010,
                "title": "Fearless Tour",
                "trigger": "Fearless album becomes cultural phenomenon",
                "audience_index": 4,
                "multiplier_vs_prev": 4.0,
                "venue_level": "ARENA",
                "example_venues": ["American Airlines Center (Dallas)", "Staples Center (LA)"],
                "notes": "First arena tour. Tween/teen sensation. MTV VMAs moment.",
                "key_metric": "100M+ album sales worldwide"
            },
            {
                "year_start": 2013,
                "year_end": 2014,
                "title": "Red Tour",
                "trigger": "Red album + adult fanbase growth",
                "audience_index": 9,
                "multiplier_vs_prev": 2.25,
                "venue_level": "ARENA",
                "example_venues": ["Madison Square Garden (NYC)", "O2 Arena (London)"],
                "notes": "Global arena. International expansion. Maturing fanbase.",
                "key_metric": "15M Red album sales"
            },
            {
                "year_start": 2015,
                "year_end": 2015,
                "title": "1989 World Tour",
                "trigger": "1989 album: pop reinvention",
                "audience_index": 14,
                "multiplier_vs_prev": 1.56,
                "venue_level": "STADIUM",
                "example_venues": ["MetLife Stadium (NJ)", "SoFi Stadium (LA)"],
                "notes": "Pop pivot. Stadium-ready production. Global superstar.",
                "key_metric": "10M+ 1989 sales"
            },
            {
                "year_start": 2018,
                "year_end": 2018,
                "title": "Reputation Tour",
                "trigger": "Reputation album: personal narrative, political stance",
                "audience_index": 20,
                "multiplier_vs_prev": 1.43,
                "venue_level": "STADIUM",
                "example_venues": ["MetLife Stadium (NJ)", "Nationwide Arena (Columbus)"],
                "notes": "Largest stadium tour. Cultural conversations. Billion-dollar gross.",
                "key_metric": "$345M tour gross"
            },
            {
                "year_start": 2023,
                "year_end": 2024,
                "title": "Eras Tour",
                "trigger": "Re-recordings (Taylor's Versions) + 10-era retrospective",
                "audience_index": 40,
                "multiplier_vs_prev": 2.0,
                "venue_level": "STADIUM",
                "example_venues": ["SoFi Stadium (LA)", "MetLife Stadium (NJ)"],
                "notes": "Highest-grossing tour ever ($2B+). Cultural juggernaut. Multi-generational.",
                "key_metric": "$2B+ tour gross"
            }
        ],
        "insights": [
            "🎵 Country → Pop = successful genre pivot",
            "📈 Re-recording strategy = ownership + fan deepening",
            "🎪 Eras Tour = cultural event (not just concert)",
            "💪 Fanbase loyalty = touring gold (repeat markets)",
            "🌐 Global reach = English-speaking TAM expansion"
        ],
        "audience_insights": [
            "Entre Fearless y Red, la audiencia se multiplica cerca de x4, pasando de teatros y arenas medianas (3.000–8.000) a arenas completas de 15.000–25.000 personas, con expansión fuera del mercado country de EE.UU.",
            "Con The Eras Tour, la audiencia se duplica (~x2), migrando de estadios de 40.000–55.000 personas a estadios de 70.000–90.000, alcanzando un pico de consumo global sostenido."
        ]
    }
}

def get_artist_evolution(artist_name_or_id):
    """Get evolution data for artist if available"""
    artist_key = artist_name_or_id.lower().strip()
    
    # Try direct match
    if artist_key in EVOLUTION_DATA:
        return EVOLUTION_DATA[artist_key]
    
    # Try Spotify ID match
    for key, data in EVOLUTION_DATA.items():
        if data.get("spotify_id") == artist_name_or_id:
            return data
    
    return None

def list_available_artists():
    """List artists with Evolution data"""
    return [data["artist_name"] for data in EVOLUTION_DATA.values() if data.get("available")]
