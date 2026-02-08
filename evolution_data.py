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
        ],
        "audience_insights": [
            "Disrupción Viral (2018-19): La tracción digital de Ouke y Jala Jala generó un multiplicador de audiencia de x10, forzando la migración inmediata del circuito under a venues de 5.000 tickets (Obras Sanitarias), validando su modelo de performance híbrida.",
            "Consolidación Mainstream (2024): El impacto global del Tiny Desk y el lanzamiento de Baño María triplicaron la demanda (x3), agotando el Movistar Arena (15k) y habilitando giras transatlánticas con más de 30 fechas sold-out en Europa y Latam.",
            "Expansión Global (2025): La exposición masiva en Jimmy Fallon y el triunfo en los Grammys detonaron la entrada al mercado estadounidense, escalando a slots primarios en festivales de 40k+ (Coachella) y estadios en mercados clave como Brasil."
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
            "Trap King (2016-17): Viralidad digital y Soy Peor multiplican la audiencia x10, saltando de clubs de 1k a arenas latinas de 10k.",
            "Superestrella (2018-20): X 100PRE y el crossover con Drake (Mía) triplican el alcance (x3), consolidando arenas globales de 30k y entrada al mercado anglo.",
            "Icono Global (2022-26): Un Verano Sin Ti y el Super Bowl detonan un salto x2.5, desbloqueando estadios de 80k+ y residencias masivas, cimentando su estatus de 'Industry Plant' orgánica."
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
            "Crossover Country (2008-10): El éxito de Fearless detonó un crecimiento de x5, permitiendo la transición de telonera en teatros (2k) a headliner en arenas de 15k. La captura demográfica dual (Country/Pop) validó el modelo de consumo masivo temprano.",
            "Infraestructura de Estadios (2014-18): El pivote pop de 1989 y la estrategia de Reputation impulsaron un multiplicador x4, migrando definitivamente de arenas a estadios de 60k-80k, optimizando el yield por ticket mediante producción a gran escala.",
            "Economía de Escala (2023-Presente): The Eras Tour capitalizó la IP del catálogo completo para generar una densidad de demanda >x10, normalizando residencias de estadios multi-noche (70k x 3-6 fechas) por ciudad y rompiendo los techos históricos de recaudación bruta global."
        ]
    },
    
    # Peso Pluma
    "peso pluma": {
        "artist_name": "Peso Pluma",
        "spotify_id": "44O4JMsmU8hg6wMy3DHQvV",
        "available": True,
        "eras": [
            {
                "year_start": 2021,
                "year_end": 2022,
                "title": "Regional Mexican Trap Pioneer",
                "trigger": "SoundCloud releases → early regional Mexican trap",
                "audience_index": 1,
                "multiplier_vs_prev": None,
                "venue_level": "CLUB",
                "example_venues": ["Sala Luna (Monterrey)", "Club Vertigo (Mexico City)"],
                "notes": "Underground trap latino movement. Regional cult following in Northern Mexico.",
                "key_metric": "1M SoundCloud followers"
            },
            {
                "year_start": 2022,
                "year_end": 2023,
                "title": "Viral Breakthrough",
                "trigger": "TikTok virality + streaming playlist placement",
                "audience_index": 5,
                "multiplier_vs_prev": 5.0,
                "venue_level": "THEATER",
                "example_venues": ["Teatro Metropolitan (Mexico City)", "Auditorio Telmex (Guadalajara)"],
                "notes": "TikTok explosion in Latin America. Becomes fastest-growing Mexican artist.",
                "key_metric": "50M+ Spotify monthly listeners"
            },
            {
                "year_start": 2023,
                "year_end": 2024,
                "title": "Arena Domination",
                "trigger": "Multiple arena tours across Latam + US collaborations",
                "audience_index": 16,
                "multiplier_vs_prev": 3.2,
                "venue_level": "ARENA",
                "example_venues": ["Palacio de los Deportes (Mexico City)", "Auditorio Nacional (Mexico City)"],
                "notes": "Regional Mexican trap becomes mainstream. Crossover to US Latin charts.",
                "key_metric": "500M+ total Spotify streams"
            },
            {
                "year_start": 2024,
                "year_end": 2026,
                "title": "International Expansion",
                "trigger": "US tours + collaborations with global artists",
                "audience_index": 28,
                "multiplier_vs_prev": 1.75,
                "venue_level": "STADIUM",
                "example_venues": ["Estadio Vallehermoso (Mexico City)", "Climate Pledge Arena (Seattle)"],
                "notes": "Expansion beyond Latin America. First stadium tours in Mexico.",
                "key_metric": "1B+ total streams"
            }
        ],
        "insights": [
            "🎸 Regional Mexican trap = new mainstream genre",
            "📱 TikTok virality = fastest path to 50M+ monthly listeners",
            "🌎 US crossover = next growth phase for Latin artists",
            "🎪 Arena/Stadium touring = monetization of viral success",
            "🎯 Fastest-growing Mexican artist since reggaeton explosion"
        ],
        "audience_insights": [
            "Disrupción Regional (2022-23): La viralidad transfronteriza de Ella Baila Sola aplicó un multiplicador de audiencia de x20, forzando la migración inmediata de palenques locales de 2k a arenas estadounidenses de 12k-15k, rompiendo la barrera del idioma en el mercado general.",
            "Validación Hard-Ticket (2023): El lanzamiento de Génesis estabilizó la demanda en arenas mayores de 18k+ durante el Doble P Tour, transformando el volumen de streaming en venta dura de tickets y agotando 40 fechas en Norteamérica.",
            "Estatus de Headliner (2024-25): Con el ciclo Éxodo y el slot principal en Coachella (125k pax), la infraestructura escaló a festivales masivos y arenas premium (Madison Square Garden), diversificando el revenue con una producción escénica de alto coste."
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
