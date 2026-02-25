"""
MAI - Hard-coded show dates and merch for quick artists.
Last updated: 2026-02-25
Sources: Ticketmaster, Bandsintown, Songkick, official artist sites.
"""

SHOWS_DATA = {
    "bad bunny": {
        "merch_url": "https://badbunny.store",
        "upcoming_shows": [
            {"date": "2026-02-28", "venue": "ENGIE Stadium",                    "city": "Sydney",       "country": "Australia", "ticket_url": "https://www.ticketmaster.com.au"},
            {"date": "2026-03-01", "venue": "ENGIE Stadium",                    "city": "Sydney",       "country": "Australia", "ticket_url": "https://www.ticketmaster.com.au"},
            {"date": "2026-05-22", "venue": "Estadi Olímpic Lluís Companys",    "city": "Barcelona",    "country": "Spain",     "ticket_url": "https://www.ticketmaster.es"},
            {"date": "2026-05-26", "venue": "Estádio da Luz",                   "city": "Lisbon",       "country": "Portugal",  "ticket_url": "https://www.ticketmaster.pt"},
            {"date": "2026-05-30", "venue": "Riyadh Air Metropolitano",         "city": "Madrid",       "country": "Spain",     "ticket_url": "https://www.ticketmaster.es"},
        ],
    },

    "taylor swift": {
        "merch_url": "https://store.taylorswift.com",
        "upcoming_shows": [],  # Eras Tour ended Dec 2024. No new tour announced yet.
    },

    "peso pluma": {
        "merch_url": "https://store.pesopluma.com",
        "upcoming_shows": [
            {"date": "2026-03-01", "venue": "Climate Pledge Arena",             "city": "Seattle",          "country": "USA", "ticket_url": "https://www.axs.com"},
            {"date": "2026-03-03", "venue": "Chase Center",                     "city": "San Francisco",    "country": "USA", "ticket_url": "https://www.axs.com"},
            {"date": "2026-03-06", "venue": "Talking Stick Resort Amphitheatre","city": "Phoenix",          "country": "USA", "ticket_url": "https://www.ticketmaster.com"},
            {"date": "2026-03-11", "venue": "Honda Center",                     "city": "Anaheim",          "country": "USA", "ticket_url": "https://www.ticketmaster.com"},
            {"date": "2026-04-30", "venue": "Madison Square Garden",            "city": "New York",         "country": "USA", "ticket_url": "https://www.ticketmaster.com"},
        ],
    },

    "ca7riel & paco amoroso": {
        "merch_url": "https://tienda.ca7rielypacoamoroso.com",
        "upcoming_shows": [],  # No confirmed dates. New album "Free Spirits" out Mar 19, 2026.
    },

    "feli colina": {
        "merch_url": "https://www.merchbar.com/rock-alternative/feli-colina",
        "upcoming_shows": [],  # No confirmed dates as of 2026-02-25.
    },
}


def get_shows(artist_name: str) -> dict:
    """Return shows + merch for artist. Falls back to None if not in hard-coded data."""
    return SHOWS_DATA.get(artist_name.lower().strip())
