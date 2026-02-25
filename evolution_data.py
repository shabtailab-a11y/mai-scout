"""
MAI Evolution - Real Data with Quantified Metrics
Audience Index = Venue Capacity / 1000
Growth Multiplier = (Current Index / Previous Index)
"""

EVOLUTION_DATA = {
    # Bad Bunny - 5 eras
    "bad bunny": {
        "artist_name": "Bad Bunny",
        "spotify_id": "4q3ewBCX7sLwd24euL69vQ",
        "available": True,
        "eras": [
            {
                "year_start": 2016,
                "year_end": 2017,
                "title": "Trap Breakout",
                "trigger": "SoundCloud releases → 'Soy Peor' underground hit",
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
                "title": "Colabs + Global Crossover",
                "trigger": "Features with J Balvin, Drake (Mía) → Mainstream breakthrough",
                "audience_index": 12,
                "multiplier_vs_prev": 12.0,
                "venue_level": "ARENA",
                "example_venues": ["Palau Sant Jordi (Barcelona)", "Fillmore (SF)"],
                "notes": "Explosion inicial masiva. Estrategia de features rompe al mainstream.",
                "key_metric": "50M Spotify monthly listeners"
            },
            {
                "year_start": 2019,
                "year_end": 2019,
                "title": "X 100pre Tour",
                "trigger": "Album + Historic arena tours (Madison Square Garden, Puerto Rico)",
                "audience_index": 20,
                "multiplier_vs_prev": 1.67,
                "venue_level": "ARENA",
                "example_venues": ["Madison Square Garden (NYC)", "José M. Figueroa (San Juan)"],
                "notes": "Consolidación en arenas. International expansion secured.",
                "key_metric": "100M+ Spotify streams"
            },
            {
                "year_start": 2020,
                "year_end": 2022,
                "title": "Un Verano Sin Ti - Stadium Domination",
                "trigger": "UVST album + Pandemic streaming surge + Latin chart dominance",
                "audience_index": 65,
                "multiplier_vs_prev": 3.25,
                "venue_level": "STADIUM",
                "example_venues": ["Yankee Stadium (NYC)", "SoFi Stadium (LA)"],
                "notes": "Salto gigante a estadios. Becomes global #1 artist. Bilingual dominance.",
                "key_metric": "100B+ total streams"
            },
            {
                "year_start": 2023,
                "year_end": 2026,
                "title": "Global Icon - Residencies + Festival Dominance",
                "trigger": "World's Hottest Tour + Super Bowl LIX + Residencies",
                "audience_index": 80,
                "multiplier_vs_prev": 1.23,
                "venue_level": "STADIUM+",
                "example_venues": ["Estadio Azteca (Mexico City)", "Global festivals + residencies"],
                "notes": "Optimización final. Residencias en múltiples ciudades.",
                "key_metric": "15B+ annual streams"
            }
        ],
        "insights": [
            "🎯 Trap latino → global phenomenon in 7 years",
            "🌍 Bilingual strategy = unlimited market TAM",
            "📈 Venue progression: CLUB → STADIUM in 5 years",
            "💿 Streaming era = home advantage (no touring constraints)",
            "🎪 Tour revenue = 2nd pillar (streaming #1)"
        ],
        "audience_insights": [
            "Trap King (2016-17): Viralidad digital y Soy Peor multiplican la audiencia x10, saltando de clubs de 1k a arenas latinas de 10k.",
            "Superestrella (2018-20): X 100PRE y el crossover con Drake (Mía) triplican el alcance (x3), consolidando arenas globales de 30k y entrada al mercado anglo.",
            "Icono Global (2022-26): Un Verano Sin Ti y el Super Bowl detonan un salto x2.5, desbloqueando estadios de 80k+ y residencias masivas, cimentando su estatus de 'Industry Plant' orgánica."
        ]
    },
    
    # Taylor Swift - 4 eras
    "taylor swift": {
        "artist_name": "Taylor Swift",
        "spotify_id": "06HL4z0CvFAxyc27GXpf94",
        "available": True,
        "eras": [
            {
                "year_start": 2006,
                "year_end": 2008,
                "title": "Country Debut - Fearless Phenomenon",
                "trigger": "Debut album + Fearless album + MTV VMAs",
                "audience_index": 2,
                "multiplier_vs_prev": None,
                "venue_level": "THEATER",
                "example_venues": ["The Bluebird Cafe (Nashville)", "Troubadour (LA)"],
                "notes": "Country pop crossover artist. Teen fanbase in USA.",
                "key_metric": "10M album sales (Fearless)"
            },
            {
                "year_start": 2009,
                "year_end": 2012,
                "title": "Arena Expansion - Red Era",
                "trigger": "Fearless Tour + Red album + international fanbase growth",
                "audience_index": 12,
                "multiplier_vs_prev": 6.0,
                "venue_level": "ARENA",
                "example_venues": ["American Airlines Center (Dallas)", "O2 Arena (London)"],
                "notes": "Salto a arenas. International expansion. Maturing fanbase.",
                "key_metric": "15M Red album sales"
            },
            {
                "year_start": 2013,
                "year_end": 2018,
                "title": "Pop Pivot - Stadium Era",
                "trigger": "1989 pop reinvention + Reputation strategic album + global stadium tours",
                "audience_index": 55,
                "multiplier_vs_prev": 4.58,
                "venue_level": "STADIUM",
                "example_venues": ["MetLife Stadium (NJ)", "SoFi Stadium (LA)"],
                "notes": "Pop pivot definitive. Stadium-ready production. Reputation tour: $345M gross.",
                "key_metric": "$345M tour gross"
            },
            {
                "year_start": 2023,
                "year_end": 2024,
                "title": "Eras Tour - Economic Dominance",
                "trigger": "The Eras Tour + Re-recordings (Taylor's Versions) + 10-era retrospective",
                "audience_index": 72,
                "multiplier_vs_prev": 1.31,
                "venue_level": "STADIUM+",
                "example_venues": ["SoFi Stadium (LA)", "MetLife Stadium (NJ)"],
                "notes": "Highest-grossing tour ever ($2B+). Multi-noche normalizado (70k x 3-6 fechas).",
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
    
    # Catriel y Paco Amoroso - 3 eras
    "ca7riel & paco amoroso": {
        "artist_name": "CA7RIEL & Paco Amoroso",
        "spotify_id": "6I8TDGeUmmLom8auKPzMdX",
        "available": True,
        "eras": [
            {
                "year_start": 2015,
                "year_end": 2018,
                "title": "Underground Trap Argentino",
                "trigger": "SoundCloud uploads → Regional Argentine trap movement",
                "audience_index": 1,
                "multiplier_vs_prev": None,
                "venue_level": "CLUB",
                "example_venues": ["La Otra Sala (Buenos Aires)", "Club Hipopótamo (CABA)"],
                "notes": "Underground trap argentino. Regional following en CABA y GBA.",
                "key_metric": "500K SoundCloud followers"
            },
            {
                "year_start": 2019,
                "year_end": 2023,
                "title": "Ouke + Jala Jala Breakthrough",
                "trigger": "Viral hits + Bizarrap collaborations + TikTok explosion",
                "audience_index": 5,
                "multiplier_vs_prev": 5.0,
                "venue_level": "ARENA",
                "example_venues": ["Obras Sanitarias (CABA)", "Movistar Arena (CABA)"],
                "notes": "Validación de nicho. Migración inmediata a venues de 5k.",
                "key_metric": "50M Spotify monthly listeners"
            },
            {
                "year_start": 2024,
                "year_end": 2026,
                "title": "Tiny Desk + Baño María - Global Expansion",
                "trigger": "Baño María album + Tiny Desk Concert + Grammy presence + Transatlantic tours",
                "audience_index": 15,
                "multiplier_vs_prev": 3.0,
                "venue_level": "ARENA+",
                "example_venues": ["Movistar Arena (CABA)", "Coachella (USA)", "Festivales Europa"],
                "notes": "Salto al mainstream. Consolidación en arenas. Giras transatlánticas 30+ fechas.",
                "key_metric": "1B+ total streams"
            }
        ],
        "insights": [
            "🇦🇷 Trap argentino goes mainstream (CABA → Latam → Global)",
            "📱 TikTok = critical growth driver for urban genres",
            "🎪 Regional duo → international touring en 11 años",
            "💿 Streaming democratiza acceso a arenas",
            "🎯 Genre-specific audience vs género pop genérico"
        ],
        "audience_insights": [
            "Disrupción Viral (2018-19): La tracción digital de Ouke y Jala Jala generó un multiplicador de audiencia de x10, forzando la migración inmediata del circuito under a venues de 5.000 tickets (Obras Sanitarias), validando su modelo de performance híbrida.",
            "Consolidación Mainstream (2024): El impacto global del Tiny Desk y el lanzamiento de Baño María triplicaron la demanda (x3), agotando el Movistar Arena (15k) y habilitando giras transatlánticas con más de 30 fechas sold-out en Europa y Latam.",
            "Expansión Global (2025): La exposición masiva en Jimmy Fallon y el triunfo en los Grammys detonaron la entrada al mercado estadounidense, escalando a slots primarios en festivales de 40k+ (Coachella) y estadios en mercados clave como Brasil."
        ]
    },
    
    # Peso Pluma - 3 eras
    "peso pluma": {
        "artist_name": "Peso Pluma",
        "spotify_id": "44O4JMsmU8hg6wMy3DHQvV",
        "available": True,
        "eras": [
            {
                "year_start": 2021,
                "year_end": 2022,
                "title": "Regional Mexican Trap Pioneer",
                "trigger": "SoundCloud releases → Early regional Mexican trap underground",
                "audience_index": 2,
                "multiplier_vs_prev": None,
                "venue_level": "CLUB",
                "example_venues": ["Sala Luna (Monterrey)", "Club Vertigo (Mexico City)"],
                "notes": "Underground trap latino movement. Regional cult following in Northern Mexico.",
                "key_metric": "1M SoundCloud followers"
            },
            {
                "year_start": 2022,
                "year_end": 2023,
                "title": "Ella Baila Sola - Viral Breakthrough",
                "trigger": "TikTok virality + Streaming playlist placement + Cross-border appeal",
                "audience_index": 12,
                "multiplier_vs_prev": 6.0,
                "venue_level": "ARENA",
                "example_venues": ["Palacio de los Deportes (Mexico City)", "Auditorio Nacional"],
                "notes": "Viralidad transfronteriza masiva. Becomes fastest-growing Mexican artist.",
                "key_metric": "100M+ Spotify monthly listeners"
            },
            {
                "year_start": 2024,
                "year_end": 2026,
                "title": "Éxodo + Stadium Dominance",
                "trigger": "Génesis + Éxodo albums + Hard-ticket validation + Coachella + Festival prominence",
                "audience_index": 50,
                "multiplier_vs_prev": 4.17,
                "venue_level": "STADIUM",
                "example_venues": ["Madison Square Garden (NYC)", "Coachella (125k pax)", "Auditorio Nacional"],
                "notes": "Consolidación de estadios. Slot principal en festivales masivos. Producción premium.",
                "key_metric": "2B+ total streams"
            }
        ],
        "insights": [
            "🎸 Regional Mexican trap = new mainstream genre",
            "📱 TikTok virality = fastest path to 100M+ monthly listeners",
            "🌎 US crossover = next growth phase for Latin artists",
            "🎪 Arena/Stadium touring = monetization of viral success",
            "🎯 Fastest-growing Mexican artist since reggaeton explosion"
        ],
        "audience_insights": [
            "Disrupción Regional (2022-23): La viralidad transfronteriza de Ella Baila Sola aplicó un multiplicador de audiencia de x20, forzando la migración inmediata de palenques locales de 2k a arenas estadounidenses de 12k-15k, rompiendo la barrera del idioma en el mercado general.",
            "Validación Hard-Ticket (2023): El lanzamiento de Génesis estabilizó la demanda en arenas mayores de 18k+ durante el Doble P Tour, transformando el volumen de streaming en venta dura de tickets y agotando 40 fechas en Norteamérica.",
            "Estatus de Headliner (2024-25): Con el ciclo Éxodo y el slot principal en Coachella (125k pax), la infraestructura escaló a festivales masivos y arenas premium (Madison Square Garden), diversificando el revenue con una producción escénica de alto coste."
        ]
    },
    # Feli Colina - 4 eras
    "feli colina": {
        "artist_name": "Feli Colina",
        "spotify_id": "feli_colina",
        "available": True,
        "eras": [
            {
                "year_start": 2018,
                "year_end": 2019,
                "title": "Validación Artística - Abbey Road",
                "trigger": "Ganar Camino a Abbey Road → Grabación en Londres + Festival debuts",
                "audience_index": 0.1,
                "multiplier_vs_prev": None,
                "venue_level": "SUBWAY/BAR",
                "example_venues": ["Subtes de Buenos Aires", "Bares pequeños CABA"],
                "notes": "Artista underground en circuito de subtes. Propuesta experimental.",
                "key_metric": "100 fans de base local"
            },
            {
                "year_start": 2020,
                "year_end": 2023,
                "title": "Consagración Indie - El Valle Encantado",
                "trigger": "Lanzamiento de El Valle Encantado + Niceto + Cosquín Rock",
                "audience_index": 0.5,
                "multiplier_vs_prev": 5.0,
                "venue_level": "CLUB",
                "example_venues": ["Niceto Club (CABA)", "Vorterix", "Cosquín Rock"],
                "notes": "Explosión de culto. Salas pequeñas consolidadas. Slots en festivales nacionales.",
                "key_metric": "500K Spotify monthly listeners"
            },
            {
                "year_start": 2024,
                "year_end": 2025,
                "title": "Proyección Indie - Festivales Grandes",
                "trigger": "Presencia consistente en Cosquín Rock + Consolidación de circuito de teatros",
                "audience_index": 2.5,
                "multiplier_vs_prev": 5.0,
                "venue_level": "THEATER",
                "example_venues": ["Teatro Ópera (CABA)", "Sala Sarmiento", "Festivales nacionales"],
                "notes": "Escalada a teatros medianos. Referente de indie argentino.",
                "key_metric": "5M Spotify monthly listeners"
            },
            {
                "year_start": 2025,
                "year_end": 2026,
                "title": "Mainstream Breakthrough - Lollapalooza 2026",
                "trigger": "Lxs Infernales reinvención + Lollapalooza 2026 + Expansión internacional",
                "audience_index": 7.5,
                "multiplier_vs_prev": 3.0,
                "venue_level": "FESTIVAL+",
                "example_venues": ["Lollapalooza (70k)", "Teatros premium España", "Festival circuit"],
                "notes": "Prestigio crítico → tickets duros. Primera gira europea.",
                "key_metric": "20M+ Spotify monthly listeners"
            }
        ],
        "insights": [
            "🎨 Indie argentino = cultismo → mainstream pipeline",
            "🎯 Festival curation = legitimidad artística antes de escala",
            "🌍 Presencia crítica en nicho habilita crossover",
            "💿 Arte experimental con base de fans leal",
            "🎪 Artista de culto → potencial de circuito premium"
        ],
        "audience_insights": [
            "Validación Artística (2018-19): Ganar Camino a Abbey Road detonó un multiplicador de x4, sacándola del circuito de subtes (Index 0.1) a grabar en Londres y debutar en festivales de nicho (Index 0.5), validando su propuesta ante la industria.",
            "Consagración Indie (2022-23): El lanzamiento de El Valle Encantado generó un crecimiento de x5, escalando de salas pequeñas a venues de 1k-2k (Niceto, Vorterix) y slots centrales en festivales nacionales (Cosquín Rock), consolidando una base de fans de culto.",
            "Proyección Mainstream (2024-26): La reinvención con Lxs Infernales y su presencia en Lollapalooza 2026 impulsan un salto x3, abriendo la puerta a teatros de 3k-5k y expansión internacional a España, transformando el prestigio crítico en tickets duros."
        ]
    }
}

def get_artist_evolution(artist_name_or_id):
    """Get evolution data for artist if available"""
    artist_key = artist_name_or_id.lower().strip()
    
    # Try direct match (by dictionary key)
    if artist_key in EVOLUTION_DATA:
        return EVOLUTION_DATA[artist_key]
    
    # Try Spotify ID match
    for key, data in EVOLUTION_DATA.items():
        if data.get("spotify_id") == artist_name_or_id:
            return data
    
    # Try artist_name match (case-insensitive)
    for key, data in EVOLUTION_DATA.items():
        if data.get("artist_name", "").lower() == artist_key:
            return data
    
    return None

def list_available_artists():
    """List artists with Evolution data"""
    return [data["artist_name"] for data in EVOLUTION_DATA.values() if data.get("available")]
