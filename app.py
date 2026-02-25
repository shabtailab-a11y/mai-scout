import os
from dotenv import load_dotenv

load_dotenv()  # load .env before any os.getenv() call

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import re
import requests
from html import unescape
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from googleapiclient.discovery import build
from flask_caching import Cache

app = Flask(__name__, static_folder='.')
CORS(app)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache', 'CACHE_DEFAULT_TIMEOUT': 300})

# Validate required environment variables at startup
_missing = [k for k in ('SPOTIPY_CLIENT_ID', 'SPOTIPY_CLIENT_SECRET', 'YOUTUBE_API_KEY')
            if not os.getenv(k)]
if _missing:
    raise SystemExit(
        f"\n[MAI] Missing required environment variables: {', '.join(_missing)}\n"
        f"Copy .env.example to .env and fill in your API keys.\n"
    )

SPOTIPY_CLIENT_ID     = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
YOUTUBE_API_KEY       = os.getenv('YOUTUBE_API_KEY')
LASTFM_API_KEY        = os.getenv('LASTFM_API_KEY')
RAPIDAPI_KEY          = os.getenv('RAPIDAPI_KEY')

if not LASTFM_API_KEY:
    print("INFO: LASTFM_API_KEY not set — Last.fm section will be hidden.")
if not RAPIDAPI_KEY:
    print("INFO: RAPIDAPI_KEY not set — TikTok integration will run in demo mode.")

# Inicializar cliente de Spotify
auth_manager = SpotifyClientCredentials(
    client_id=SPOTIPY_CLIENT_ID,
    client_secret=SPOTIPY_CLIENT_SECRET
)
spotify = spotipy.Spotify(auth_manager=auth_manager)

# Inicializar cliente de YouTube
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def extract_artist_id(url):
    """Extrae el ID del artista de una URL de Spotify"""
    patterns = [
        r'artist/([a-zA-Z0-9]+)',
        r'artist:([a-zA-Z0-9]+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    
    return None

@cache.memoize(timeout=21600)  # 6 hours
def get_youtube_stats(artist_name):
    """Obtiene estadísticas de YouTube del artista"""
    try:
        # Buscar canal del artista
        search_response = youtube.search().list(
            q=artist_name + ' official',
            type='channel',
            part='id,snippet',
            maxResults=5
        ).execute()
        
        if not search_response.get('items'):
            return None
        
        # Buscar el canal más probable (el primero suele ser el oficial)
        channel_id = None
        channel_title = None
        
        for item in search_response['items']:
            snippet = item['snippet']
            title = snippet['title'].lower()
            # Verificar que el nombre del artista esté en el título
            if artist_name.lower() in title:
                channel_id = item['id']['channelId']
                channel_title = snippet['title']
                break
        
        if not channel_id:
            # Si no encontramos match exacto, usar el primero
            channel_id = search_response['items'][0]['id']['channelId']
            channel_title = search_response['items'][0]['snippet']['title']
        
        # Obtener estadísticas del canal
        channel_response = youtube.channels().list(
            part='statistics,snippet',
            id=channel_id
        ).execute()
        
        if not channel_response.get('items'):
            return None
        
        channel_data = channel_response['items'][0]
        stats = channel_data['statistics']
        snippet = channel_data['snippet']
        
        # Obtener top videos más vistos
        top_videos_response = youtube.search().list(
            channelId=channel_id,
            type='video',
            order='viewCount',
            part='id,snippet',
            maxResults=3
        ).execute()
        
        top_videos = []
        top_video_ids = [item['id']['videoId'] for item in top_videos_response.get('items', [])]
        
        if top_video_ids:
            top_video_stats = youtube.videos().list(
                part='statistics,snippet',
                id=','.join(top_video_ids)
            ).execute()
            
            for video in top_video_stats.get('items', []):
                top_videos.append({
                    'title': video['snippet']['title'],
                    'views': int(video['statistics'].get('viewCount', 0)),
                    'likes': int(video['statistics'].get('likeCount', 0)),
                    'thumbnail': video['snippet']['thumbnails']['medium']['url'],
                    'url': f"https://www.youtube.com/watch?v={video['id']}"
                })
        
        # Obtener videos recientes
        recent_videos_response = youtube.search().list(
            channelId=channel_id,
            type='video',
            order='date',
            part='id,snippet',
            maxResults=3
        ).execute()
        
        recent_videos = []
        recent_video_ids = [item['id']['videoId'] for item in recent_videos_response.get('items', [])]
        
        if recent_video_ids:
            recent_video_stats = youtube.videos().list(
                part='statistics,snippet',
                id=','.join(recent_video_ids)
            ).execute()
            
            for video in recent_video_stats.get('items', []):
                recent_videos.append({
                    'title': video['snippet']['title'],
                    'views': int(video['statistics'].get('viewCount', 0)),
                    'likes': int(video['statistics'].get('likeCount', 0)),
                    'thumbnail': video['snippet']['thumbnails']['medium']['url'],
                    'url': f"https://www.youtube.com/watch?v={video['id']}"
                })
        
        result = {
            'channel_name': channel_title,
            'channel_url': f"https://www.youtube.com/channel/{channel_id}",
            'subscribers': int(stats.get('subscriberCount', 0)),
            'total_views': int(stats.get('viewCount', 0)),
            'video_count': int(stats.get('videoCount', 0)),
            'top_videos': top_videos,
            'recent_videos': recent_videos
        }
        
        return result
        
    except Exception as e:
        print(f"Error fetching YouTube data: {e}")
        return None

@cache.memoize(timeout=43200)  # 12 hours
def get_geo_data_from_spotify_genres_improved(artist_name):
    """Obtiene datos geográficos usando análisis de géneros + mejora heurística"""
    try:
        # Buscar artista
        search_results = spotify.search(q=artist_name, type='artist', limit=1)
        if not search_results['artists']['items']:
            return None
        
        artist = search_results['artists']['items'][0]
        genres = [g.lower() for g in artist.get('genres', [])]
        
        # Distribución base
        country_scores = {
            'US': 30,
            'MX': 10,
            'BR': 10,
            'AR': 8,
            'CO': 8,
            'ES': 7,
            'GB': 6,
            'DE': 5,
            'FR': 5,
            'CL': 5
        }
        
        # Lógica mejorada y más específica
        # Reggaeton/Trap Latino → Latam alto
        if any(x in genres for x in ['reggaeton', 'trap latino', 'urbano latino']):
            country_scores = {'MX': 25, 'AR': 20, 'CO': 18, 'US': 12, 'BR': 8, 'CL': 7, 'ES': 5, 'GB': 2, 'DE': 2, 'FR': 1}
        
        # Argentine indie/rock → Argentina muy alto
        elif any(x in genres for x in ['latin indie', 'indie pop', 'argentine rock']):
            country_scores = {'AR': 40, 'US': 15, 'BR': 12, 'CO': 8, 'CL': 8, 'ES': 8, 'MX': 5, 'GB': 2, 'DE': 1, 'FR': 1}
        
        # Brazilian música → Brasil dominante
        elif any(x in genres for x in ['samba', 'bossanova', 'funk carioca', 'brazilian']):
            country_scores = {'BR': 50, 'US': 15, 'MX': 8, 'AR': 8, 'CO': 7, 'ES': 6, 'GB': 3, 'DE': 1, 'FR': 1, 'CL': 1}
        
        # Variante reggaeton más global (Bad Bunny type)
        elif 'reggaeton' in genres or 'latin trap' in genres:
            country_scores = {'MX': 22, 'US': 18, 'AR': 16, 'CO': 14, 'BR': 10, 'CL': 8, 'ES': 7, 'GB': 3, 'DE': 1, 'FR': 1}
        
        # Pop Latino
        elif 'latin pop' in genres:
            country_scores = {'MX': 20, 'BR': 18, 'US': 18, 'AR': 12, 'CO': 10, 'ES': 8, 'CL': 7, 'GB': 4, 'DE': 2, 'FR': 1}
        
        # K-pop → distribuido
        elif 'k-pop' in genres or 'korean' in genres:
            country_scores = {'US': 28, 'BR': 20, 'MX': 16, 'AR': 12, 'CO': 8, 'ES': 8, 'GB': 4, 'DE': 2, 'FR': 1, 'CL': 1}
        
        # Afrobeats
        elif any(x in genres for x in ['afrobeats', 'amapiano']):
            country_scores = {'US': 35, 'BR': 22, 'MX': 12, 'AR': 10, 'ES': 10, 'CO': 5, 'GB': 3, 'DE': 2, 'FR': 1, 'CL': 0}
        
        # Pop global → USA fuerte
        elif 'pop' in genres and len(genres) <= 2:
            country_scores = {'US': 45, 'BR': 15, 'MX': 12, 'AR': 10, 'ES': 8, 'GB': 5, 'CO': 3, 'DE': 1, 'FR': 1, 'CL': 0}
        
        return country_scores
        
    except Exception as e:
        print(f"Error in improved geo analysis: {e}")
        return None

@cache.memoize(timeout=7200)  # 2 hours
def get_lastfm_data(artist_name):
    """Fetches listeners, play count, bio, tags and top tracks from Last.fm"""
    if not LASTFM_API_KEY:
        return None
    try:
        # Artist info: listeners, playcount, bio, tags
        info = requests.get('https://ws.audioscrobbler.com/2.0/', params={
            'method': 'artist.getinfo',
            'artist': artist_name,
            'api_key': LASTFM_API_KEY,
            'format': 'json',
            'autocorrect': 1
        }, timeout=10).json()

        if 'error' in info:
            print(f"Last.fm error: {info.get('message')}")
            return None

        artist = info.get('artist', {})
        stats  = artist.get('stats', {})

        # Top tracks with play counts
        tracks_json = requests.get('https://ws.audioscrobbler.com/2.0/', params={
            'method': 'artist.gettoptracks',
            'artist': artist_name,
            'api_key': LASTFM_API_KEY,
            'format': 'json',
            'limit': 5,
            'autocorrect': 1
        }, timeout=10).json()

        top_tracks = [
            {
                'name':      t.get('name', ''),
                'playcount': int(t.get('playcount', 0)),
                'listeners': int(t.get('listeners', 0)),
                'url':       t.get('url', '')
            }
            for t in tracks_json.get('toptracks', {}).get('track', [])[:5]
        ]

        # Strip HTML tags and decode entities from bio summary
        bio = artist.get('bio', {}).get('summary', '')
        if bio:
            bio = re.sub(r'<a[^>]*>.*?</a>', '', bio, flags=re.IGNORECASE | re.DOTALL)
            bio = re.sub(r'<[^>]+>', '', bio)
            bio = unescape(bio).strip()

        tags = [
            {'name': t.get('name', ''), 'url': t.get('url', '')}
            for t in artist.get('tags', {}).get('tag', [])[:5]
        ]

        return {
            'listeners':  int(stats.get('listeners', 0)),
            'playcount':  int(stats.get('playcount', 0)),
            'bio':        bio,
            'tags':       tags,
            'top_tracks': top_tracks,
            'url':        artist.get('url', '')
        }

    except Exception as e:
        print(f"Error fetching Last.fm data: {e}")
        return None


@cache.memoize(timeout=7200)  # 2 hours
def get_artist_data(artist_id):
    """Obtiene datos completos del artista desde la API de Spotify"""
    try:
        # Datos básicos del artista
        artist = spotify.artist(artist_id)
        
        # Top tracks
        top_tracks_data = spotify.artist_top_tracks(artist_id, country='US')
        top_tracks = []
        for track in top_tracks_data['tracks'][:5]:
            top_tracks.append({
                'name': track['name'],
                'preview_url': track.get('preview_url'),
                'album_image': track['album']['images'][0]['url'] if track['album']['images'] else None,
                'duration_ms': track['duration_ms'],
                'spotify_url': track['external_urls']['spotify']
            })
        
        # Artistas similares (puede fallar para algunos artistas)
        similar_artists = []
        try:
            related_artists_data = spotify.artist_related_artists(artist_id)
            for related in related_artists_data['artists'][:6]:
                similar_artists.append({
                    'id': related['id'],
                    'name': related['name'],
                    'image': related['images'][0]['url'] if related['images'] else None,
                    'spotify_url': related['external_urls']['spotify']
                })
        except Exception as e:
            print(f"Could not fetch related artists via API: {e}")
            # Fallback 1: buscar artistas del mismo género
            if artist['genres']:
                try:
                    # Usar el primer género para buscar artistas similares
                    genre = artist['genres'][0]
                    # Buscar simplemente por género como término
                    search_results = spotify.search(
                        q=genre, 
                        type='artist', 
                        limit=20
                    )
                    
                    # Filtrar artistas que tengan géneros en común y no sean el mismo
                    for search_artist in search_results['artists']['items']:
                        if search_artist['id'] != artist_id and len(similar_artists) < 6:
                            # Verificar si tiene géneros en común
                            search_genres = set(search_artist['genres'])
                            artist_genres = set(artist['genres'])
                            if search_genres & artist_genres:  # Intersección
                                similar_artists.append({
                                    'id': search_artist['id'],
                                    'name': search_artist['name'],
                                    'image': search_artist['images'][0]['url'] if search_artist['images'] else None,
                                    'spotify_url': search_artist['external_urls']['spotify']
                                })
                    
                    print(f"Found {len(similar_artists)} similar artists via genre search")
                except Exception as e2:
                    print(f"Genre search also failed: {e2}")
            
            # Fallback 2: si no hay géneros, buscar artistas populares generales
            if len(similar_artists) == 0:
                try:
                    # Buscar artistas populares en la misma categoría de popularidad
                    search_results = spotify.search(
                        q='pop', 
                        type='artist', 
                        limit=20
                    )
                    
                    # Tomar artistas con popularidad similar (+/- 10 puntos)
                    target_pop = artist['popularity']
                    for search_artist in search_results['artists']['items']:
                        if search_artist['id'] != artist_id and len(similar_artists) < 6:
                            artist_pop = search_artist['popularity']
                            if abs(artist_pop - target_pop) < 15:  # Popularidad similar
                                similar_artists.append({
                                    'id': search_artist['id'],
                                    'name': search_artist['name'],
                                    'image': search_artist['images'][0]['url'] if search_artist['images'] else None,
                                    'spotify_url': search_artist['external_urls']['spotify']
                                })
                    
                    print(f"Found {len(similar_artists)} similar artists via popularity search")
                except Exception as e3:
                    print(f"Popularity search also failed: {e3}")
        
        # Últimos lanzamientos (albums y singles)
        albums_data = spotify.artist_albums(artist_id, album_type='album,single', limit=5)
        recent_releases = []
        for album in albums_data['items']:
            recent_releases.append({
                'name': album['name'],
                'type': album['album_type'],
                'release_date': album['release_date'],
                'image': album['images'][0]['url'] if album['images'] else None,
                'spotify_url': album['external_urls']['spotify']
            })
        
        # Obtener estadísticas de YouTube
        youtube_stats = get_youtube_stats(artist['name'])

        # Get Last.fm data
        lastfm_data = get_lastfm_data(artist['name'])

        # Extraer datos relevantes
        result = {
            'name': artist['name'],
            'image': artist['images'][0]['url'] if artist['images'] else 'https://via.placeholder.com/300x300/667eea/ffffff?text=Artist',
            'popularity': artist['popularity'],
            'followers': artist['followers']['total'],
            'genres': artist['genres'][:5],
            'top_tracks': top_tracks,
            'similar_artists': similar_artists,
            'recent_releases': recent_releases,
            'youtube': youtube_stats,
            'lastfm': lastfm_data
        }
        
        return result
        
    except Exception as e:
        print(f"Error fetching artist from Spotify API: {e}")
        return None

def calculate_mai_pulse(popularity, followers):
    """Calcula la métrica MAI Pulse"""
    score = (popularity * 1.5) + (followers / 1000)
    
    # Umbrales ajustados para artistas reales
    if score > 50000:  # >50M seguidores aprox
        category = "🔥 TENDENCIA GLOBAL"
        color = "red"
    elif score > 10000:  # >10M seguidores aprox
        category = "🚀 EN ASCENSO"
        color = "orange"
    elif score > 1000:   # >1M seguidores aprox
        category = "⭐ ESTABLECIDO"
        color = "yellow"
    else:
        category = "🌱 EMERGENTE"
        color = "green"
    
    return {
        'score': round(score, 2),
        'category': category,
        'color': color
    }

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/scout', methods=['POST'])
def scout_artist():
    data = request.get_json()
    artist_name = data.get('artist_name', '').strip()
    
    if not artist_name:
        return jsonify({'error': 'Nombre del artista requerido'}), 400
    
    try:
        # If input is a Spotify URL or URI, extract the ID directly
        artist_id = extract_artist_id(artist_name)

        if not artist_id:
            # Fall back to name search
            search_results = spotify.search(q=artist_name, type='artist', limit=1)

            if not search_results['artists']['items']:
                return jsonify({'error': f'No se encontró el artista "{artist_name}"'}), 404

            artist_id = search_results['artists']['items'][0]['id']

        # Obtener datos completos del artista
        artist_data = get_artist_data(artist_id)
        
        if not artist_data:
            return jsonify({'error': 'No se pudo obtener información del artista'}), 404
        
        # Calcular MAI Pulse
        mai_pulse = calculate_mai_pulse(artist_data['popularity'], artist_data['followers'])
        
        response = {
            'artist': artist_data,
            'mai_pulse': mai_pulse,
            'demo_mode': False,
            'real_api': True
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': f'Error al buscar artista: {str(e)}'}), 500

@cache.memoize(timeout=300)  # 5 minutes — autocomplete fires on every keystroke
def _search_spotify_artists(query):
    results = spotify.search(q=query, type='artist', limit=5)
    return [
        {
            'id':    a['id'],
            'name':  a['name'],
            'image': a['images'][0]['url'] if a['images'] else None,
            'url':   a['external_urls']['spotify']
        }
        for a in results['artists']['items']
    ]

@app.route('/api/search', methods=['POST'])
def search_artist():
    """Buscar artistas por nombre"""
    data = request.get_json()
    query = data.get('query', '')

    if not query:
        return jsonify({'error': 'Query requerida'}), 400

    try:
        return jsonify({'artists': _search_spotify_artists(query)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/compare', methods=['POST'])
def compare_artists():
    """Compare two artists side by side"""
    data = request.get_json()
    artist1_name = data.get('artist1', '').strip()
    artist2_name = data.get('artist2', '').strip()

    if not artist1_name or not artist2_name:
        return jsonify({'error': 'Two artist names required'}), 400

    results = {}
    for key, name in [('artist1', artist1_name), ('artist2', artist2_name)]:
        try:
            search = spotify.search(q=name, type='artist', limit=1)
            if not search['artists']['items']:
                return jsonify({'error': f'Artist not found: "{name}"'}), 404
            artist_id = search['artists']['items'][0]['id']
            artist_data = get_artist_data(artist_id)
            if not artist_data:
                return jsonify({'error': f'Could not fetch data for: "{name}"'}), 500
            results[key] = {
                'artist': artist_data,
                'mai_pulse': calculate_mai_pulse(artist_data['popularity'], artist_data['followers'])
            }
        except Exception as e:
            return jsonify({'error': f'Error fetching "{name}": {str(e)}'}), 500

    return jsonify(results)


def get_tiktok_stats(username):
    """Obtiene estadísticas de TikTok usando RapidAPI"""
    
    # Si no hay API key configurada, retornar datos demo
    if not RAPIDAPI_KEY or RAPIDAPI_KEY == 'TU_RAPIDAPI_KEY_AQUI':
        return {
            'username': username,
            'followers': 0,
            'following': 0,
            'likes': 0,
            'videos': 0,
            'bio': 'Configura tu RapidAPI key para ver datos reales',
            'avatar': 'https://via.placeholder.com/150/667eea/ffffff?text=TT',
            'verified': False,
            'demo_mode': True
        }
    
    try:
        url = "https://tiktok-scraper7.p.rapidapi.com/user/info"
        
        querystring = {"unique_id": username}
        
        headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": "tiktok-scraper7.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            
            # Extraer datos del usuario
            user_data = data.get('data', {}).get('user', {})
            stats = user_data.get('stats', {})
            
            return {
                'username': user_data.get('uniqueId', username),
                'nickname': user_data.get('nickname', username),
                'followers': stats.get('followerCount', 0),
                'following': stats.get('followingCount', 0),
                'likes': stats.get('heartCount', 0),
                'videos': stats.get('videoCount', 0),
                'bio': user_data.get('signature', ''),
                'avatar': user_data.get('avatarLarger', ''),
                'verified': user_data.get('verified', False),
                'demo_mode': False
            }
        else:
            print(f"TikTok API error: {response.status_code}")
            return None
            
    except Exception as e:
        print(f"Error fetching TikTok data: {e}")
        return None

@app.route('/api/tiktok', methods=['POST'])
def scout_tiktok():
    """Obtener estadísticas de TikTok"""
    data = request.get_json()
    username = data.get('username', '').strip().replace('@', '')
    
    if not username:
        return jsonify({'error': 'Username de TikTok requerido'}), 400
    
    tiktok_data = get_tiktok_stats(username)
    
    if not tiktok_data:
        return jsonify({'error': 'No se pudo obtener información de TikTok'}), 404
    
    return jsonify(tiktok_data)

@app.route('/api/geography', methods=['POST'])
def get_geography():
    """Obtener datos geográficos del artista desde Spotify Charts"""
    data = request.get_json()
    artist_name = data.get('artist_name')
    
    if not artist_name:
        return jsonify({'error': 'Artist name required'}), 400
    
    try:
        # Obtener artista info
        search_results = spotify.search(q=artist_name, type='artist', limit=1)
        
        if not search_results['artists']['items']:
            return jsonify({'error': 'Artist not found'}), 404
        
        artist = search_results['artists']['items'][0]
        total_followers = artist['followers']['total']
        
        # Obtener datos geográficos (usando heurística mejorada de géneros)
        country_scores = get_geo_data_from_spotify_genres_improved(artist_name)
        
        if not country_scores:
            return jsonify({'error': 'Could not fetch geographic data'}), 500
        
        # Normalizar scores para que sumen 100%
        total_score = sum(country_scores.values())
        
        if total_score == 0:
            # Si no aparece en ningún chart, usar distribución por defecto
            country_scores = {
                'US': 35,
                'MX': 12,
                'BR': 10,
                'AR': 8,
                'CO': 8,
                'ES': 7,
                'GB': 6,
                'DE': 5,
                'FR': 4,
                'CL': 5
            }
            total_score = sum(country_scores.values())
        
        distribution = {}
        for country, score in country_scores.items():
            percentage = (score / total_score) * 100
            # Calcular absolute followers
            absolute_followers = int((percentage / 100) * total_followers)
            distribution[country] = {
                'percentage': round(percentage, 1),
                'followers': absolute_followers
            }
        
        # Top 5 países
        countries_info = {
            'US': {'name': 'United States', 'flag': '🇺🇸'},
            'MX': {'name': 'Mexico', 'flag': '🇲🇽'},
            'BR': {'name': 'Brazil', 'flag': '🇧🇷'},
            'AR': {'name': 'Argentina', 'flag': '🇦🇷'},
            'CO': {'name': 'Colombia', 'flag': '🇨🇴'},
            'CL': {'name': 'Chile', 'flag': '🇨🇱'},
            'ES': {'name': 'Spain', 'flag': '🇪🇸'},
            'GB': {'name': 'United Kingdom', 'flag': '🇬🇧'},
            'DE': {'name': 'Germany', 'flag': '🇩🇪'},
            'FR': {'name': 'France', 'flag': '🇫🇷'},
        }
        
        top_5 = sorted(distribution.items(), key=lambda x: x[1]['followers'], reverse=True)[:5]
        
        geo_data = []
        for country_code, data in top_5:
            geo_data.append({
                'country': country_code,
                'name': countries_info[country_code]['name'],
                'flag': countries_info[country_code]['flag'],
                'percentage': data['percentage'],
                'followers': data['followers']
            })
        
        return jsonify({
            'artist': artist_name,
            'total_followers': total_followers,
            'top_countries': geo_data,
            'genres': list(artist.get('genres', []))[:5]
        })
        
    except Exception as e:
        print(f"Geography API error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/evolution', methods=['POST'])
def get_evolution():
    """Get Evolution data for artist"""
    data = request.get_json()
    artist_name = data.get('artist_name', '').strip()

    if not artist_name:
        return jsonify({'error': 'Artist name required'}), 400

    try:
        from evolution_data import get_artist_evolution, list_available_artists

        evolution = get_artist_evolution(artist_name)

        if evolution and evolution.get('available'):
            return jsonify({'status': 'available', 'data': evolution})
        else:
            return jsonify({
                'status': 'coming_soon',
                'available_artists': list_available_artists(),
                'message': f'Evolution data coming soon for {artist_name}'
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/evolution/email', methods=['POST'])
def subscribe_evolution():
    """Subscribe to Evolution feature notification"""
    data = request.get_json()
    email = data.get('email', '').strip()
    role = data.get('role', '').strip()
    artist = data.get('artist', '').strip()

    if not email or not role:
        return jsonify({'error': 'Email and role required'}), 400

    try:
        return jsonify({
            'status': 'success',
            'message': f"Thanks! We'll notify you when Evolution launches for {artist}",
            'incentive': '2 months free when available'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/unlock-feature', methods=['POST'])
def unlock_feature():
    """Subscribe to unlock feature (Instagram, TikTok Advanced, etc)"""
    data = request.get_json()
    email = data.get('email', '').strip()
    role = data.get('role', '').strip()
    feature = data.get('feature', '').strip()
    artist = data.get('artist', '').strip()

    if not email or not role or not feature:
        return jsonify({'error': 'Email, role, and feature required'}), 400

    try:
        feature_names = {
            'instagram': 'Instagram Stats',
            'tiktok_advanced': 'TikTok Advanced Stats'
        }
        feature_name = feature_names.get(feature, feature)
        return jsonify({
            'status': 'success',
            'message': f"Thanks! We'll notify you when {feature_name} launches for {artist}"
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# ========== SPOTLIGHT ==========

SPOTLIGHT_SUBSCRIBERS = {}

@app.route('/api/spotlight-subscribe', methods=['POST'])
def spotlight_subscribe():
    """Subscribe to artist Spotlight updates"""
    try:
        data = request.get_json()
        artist_name = data.get('artist_name', '').strip()
        email = data.get('email', '').strip()

        if not artist_name or not email:
            return jsonify({'error': 'Artist name and email required'}), 400

        if artist_name not in SPOTLIGHT_SUBSCRIBERS:
            SPOTLIGHT_SUBSCRIBERS[artist_name] = []
        if email not in SPOTLIGHT_SUBSCRIBERS[artist_name]:
            SPOTLIGHT_SUBSCRIBERS[artist_name].append(email)

        return jsonify({
            'status': 'success',
            'message': f"Thanks! You'll get updates about {artist_name}'s new music, videos, and shows."
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def _get_spotlight_data(artist_name):
    """Fetch all data needed for Spotlight: artist, YouTube, latest release, shows, bio."""
    search_results = spotify.search(q=artist_name, type='artist', limit=1)
    if not search_results['artists']['items']:
        return None
    artist = search_results['artists']['items'][0]

    # YouTube — last uploaded video
    yt_stats = get_youtube_stats(artist['name'])
    last_video = yt_stats['recent_videos'][0] if yt_stats and yt_stats.get('recent_videos') else None

    # Latest Spotify release
    albums = spotify.artist_albums(artist['id'], album_type='album,single', limit=1)
    latest_release = albums['items'][0] if albums['items'] else None

    # Upcoming shows — hard-coded data first, fallback to Bandsintown
    from shows_data import get_shows as _get_shows
    hc = _get_shows(artist['name'])
    if hc is not None:
        shows = hc['upcoming_shows']
    else:
        shows = []
        try:
            bt = requests.get(
                f"https://rest.bandsintown.com/artists/{requests.utils.quote(artist['name'])}/events",
                params={'app_id': 'mai-scout', 'date': 'upcoming'},
                timeout=5
            )
            if bt.ok and isinstance(bt.json(), list):
                shows = bt.json()[:4]
        except Exception:
            pass

    # Smart bio — Last.fm first, then generated
    bio = ''
    if LASTFM_API_KEY:
        lastfm = get_lastfm_data(artist['name'])
        if lastfm:
            bio = lastfm.get('bio', '')
    if not bio:
        genres_str = ', '.join(artist['genres'][:2]) if artist['genres'] else 'music'
        followers = artist['followers']['total']
        bio = (f"{artist['name']} is a {genres_str} artist with "
               f"{followers:,} followers on Spotify.")

    # Merch — hard-coded official store first, fallback to search
    from shows_data import get_shows as _get_shows_merch
    hc_merch = _get_shows_merch(artist['name'])
    if hc_merch and hc_merch.get('merch_url'):
        merch_url = hc_merch['merch_url']
    else:
        merch_url = f"https://www.google.com/search?q={requests.utils.quote(artist['name'])}+merch+official"

    # Flag: artist is in our hard-coded list but has no dates yet
    shows_tba = (hc is not None and len(shows) == 0)

    return {
        'artist': artist,
        'yt_stats': yt_stats,
        'last_video': last_video,
        'latest_release': latest_release,
        'shows': shows,
        'shows_tba': shows_tba,
        'bio': bio,
        'merch_url': merch_url,
    }


def _build_spotlight_body(d, subscribe_form_js):
    """Build the inner HTML body content for Spotlight (modal + public page)."""
    artist = d['artist']
    last_video = d['last_video']
    latest_release = d['latest_release']
    shows = d['shows']
    shows_tba = d.get('shows_tba', False)
    bio = d['bio']
    merch_url = d['merch_url']
    yt_stats = d['yt_stats']

    name = artist['name']
    image = artist['images'][0]['url'] if artist['images'] else 'https://via.placeholder.com/200'
    genres = ', '.join(artist['genres'][:3]) if artist['genres'] else 'Artist'
    spotify_url = artist['external_urls'].get('spotify', '#')

    # Smart bio block
    bio_block = f"""
    <div class="glass rounded-lg p-4 mb-4">
        <h2 class="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-2">🧠 Smart Bio</h2>
        <p class="text-gray-200 text-sm leading-relaxed">{bio[:300]}{'…' if len(bio) > 300 else ''}</p>
    </div>""" if bio else ''

    # Latest YouTube video block
    if last_video:
        yt_block = f"""
    <div class="glass rounded-lg overflow-hidden mb-4">
        <h2 class="text-sm font-semibold text-gray-400 uppercase tracking-wider px-4 pt-4 mb-2">▶️ Latest Video</h2>
        <a href="{last_video['url']}" target="_blank" class="flex items-center gap-3 px-4 pb-4 hover:bg-white hover:bg-opacity-5 transition">
            <img src="{last_video['thumbnail']}" class="w-20 h-14 object-cover rounded flex-shrink-0">
            <div class="min-w-0">
                <p class="text-white text-sm font-medium truncate">{last_video['title']}</p>
                <p class="text-gray-400 text-xs">{last_video['views']:,} views</p>
            </div>
        </a>
    </div>"""
    else:
        yt_block = ''

    # Latest Spotify release block
    if latest_release:
        rel_img = latest_release['images'][0]['url'] if latest_release.get('images') else ''
        rel_url = latest_release['external_urls'].get('spotify', '#')
        rel_date = latest_release.get('release_date', '')[:4]
        rel_type = latest_release.get('album_type', 'release').capitalize()
        release_block = f"""
    <div class="glass rounded-lg overflow-hidden mb-4">
        <h2 class="text-sm font-semibold text-gray-400 uppercase tracking-wider px-4 pt-4 mb-2">🎵 Latest Release</h2>
        <a href="{rel_url}" target="_blank" class="flex items-center gap-3 px-4 pb-4 hover:bg-white hover:bg-opacity-5 transition">
            {'<img src="' + rel_img + '" class="w-14 h-14 object-cover rounded flex-shrink-0">' if rel_img else ''}
            <div>
                <p class="text-white text-sm font-medium">{latest_release['name']}</p>
                <p class="text-gray-400 text-xs">{rel_type} · {rel_date}</p>
            </div>
        </a>
    </div>"""
    else:
        release_block = ''

    # Upcoming shows block
    if shows_tba and not shows:
        shows_block = """
    <div class="glass rounded-lg p-4 mb-4">
        <h2 class="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-2">📅 Upcoming Shows</h2>
        <p class="text-gray-400 text-sm">No confirmed dates yet — follow the artist for announcements.</p>
    </div>"""
    elif shows:
        show_items = ''
        for s in shows:
            # Support both hard-coded flat format and Bandsintown nested format
            venue_raw = s.get('venue', '')
            if isinstance(venue_raw, dict):
                venue_name = venue_raw.get('name', '')
                city = venue_raw.get('city', '')
                country = venue_raw.get('country', '')
            else:
                venue_name = venue_raw
                city = s.get('city', '')
                country = s.get('country', '')
            raw_date = s.get('date') or s.get('datetime', '')[:10]
            ticket_url = s.get('ticket_url', '')
            if not ticket_url:
                for offer in s.get('offers', []):
                    if offer.get('type') == 'Tickets':
                        ticket_url = offer.get('url', '')
                        break
            ticket_btn = (f'<a href="{ticket_url}" target="_blank" '
                          f'class="text-xs bg-orange-600 hover:bg-orange-700 text-white px-3 py-1 rounded-full whitespace-nowrap">🎟 Tickets</a>'
                          ) if ticket_url else ''
            show_items += f"""
            <div class="flex items-center justify-between py-2 border-b border-white border-opacity-10 last:border-0">
                <div>
                    <p class="text-white text-sm font-medium">{venue_name}</p>
                    <p class="text-gray-400 text-xs">{city}, {country} · {raw_date}</p>
                </div>
                {ticket_btn}
            </div>"""
        shows_block = f"""
    <div class="glass rounded-lg p-4 mb-4">
        <h2 class="text-sm font-semibold text-gray-400 uppercase tracking-wider mb-3">📅 Upcoming Shows</h2>
        {show_items}
    </div>"""
    else:
        shows_block = ''

    return f"""
<div class="max-w-md mx-auto">
    <!-- Header -->
    <div class="text-center mb-6">
        <img src="{image}" class="w-28 h-28 rounded-full mx-auto mb-3 object-cover">
        <h1 class="text-2xl font-bold text-white mb-1">{name}</h1>
        <p class="text-gray-400 text-sm">{genres}</p>
    </div>

    <!-- Quick links -->
    <div class="flex gap-2 mb-4">
        <a href="{spotify_url}" target="_blank"
           class="flex-1 glass rounded-lg p-3 text-center text-white text-sm hover:bg-white hover:bg-opacity-10 transition">
            🎵 Spotify
        </a>
        {'<a href="' + yt_stats["channel_url"] + '" target="_blank" class="flex-1 glass rounded-lg p-3 text-center text-white text-sm hover:bg-white hover:bg-opacity-10 transition">📺 YouTube</a>' if yt_stats else ''}
        <a href="{merch_url}" target="_blank"
           class="flex-1 glass rounded-lg p-3 text-center text-white text-sm hover:bg-white hover:bg-opacity-10 transition">
            🛍️ Merch
        </a>
    </div>

    {bio_block}
    {yt_block}
    {release_block}
    {shows_block}

    <!-- Subscribe (collapsed) -->
    <div class="text-center mt-2">
        <button id="subscribeToggle" onclick="document.getElementById('subscribeBox').classList.toggle('hidden');this.classList.add('hidden');"
                class="text-gray-500 text-sm hover:text-gray-300 transition">
            📧 Subscribe for updates
        </button>
    </div>
    <div id="subscribeBox" class="glass rounded-lg p-5 mt-3 hidden">
        {subscribe_form_js}
        <p class="text-gray-400 text-xs mt-3">Get notified when {name} releases new music or announces shows.</p>
    </div>
</div>"""


@app.route('/api/spotlight-full/<artist_slug>')
def spotlight_full(artist_slug):
    """Get full Spotlight HTML content for embedding in modal"""
    try:
        artist_name = artist_slug.replace('_', ' ').replace(' and ', ' & ')
        d = _get_spotlight_data(artist_name)
        if not d:
            return jsonify({'error': 'Artist not found'}), 404

        subscribe_form = f"""<form onsubmit="return spotlightSubscribe(event, '{d['artist']['name']}')">
                    <input type="email" placeholder="your@email.com"
                           class="w-full p-3 rounded-lg bg-white bg-opacity-10 text-white placeholder-gray-500 border border-white border-opacity-20 mb-3">
                    <button type="submit" class="w-full bg-orange-600 hover:bg-orange-700 text-white font-bold py-3 rounded-lg">Subscribe</button>
                </form>"""

        return _build_spotlight_body(d, subscribe_form)
    except Exception as e:
        print(f"Error in spotlight_full: {e}")
        return jsonify({'error': str(e)}), 500


@app.route('/spotlight/<artist_slug>')
def public_spotlight(artist_slug):
    """Public Spotlight page for artist"""
    try:
        artist_name = artist_slug.replace('_', ' ').replace(' and ', ' & ')
        d = _get_spotlight_data(artist_name)
        if not d:
            return jsonify({'error': 'Artist not found'}), 404

        name = d['artist']['name']
        subscribe_form = f"""<form onsubmit="return subscribe()">
                <input type="email" id="email" placeholder="your@email.com"
                       class="w-full p-3 rounded-lg bg-white bg-opacity-10 text-white placeholder-gray-500 border border-white border-opacity-20 mb-3">
                <button type="submit" class="w-full bg-orange-600 hover:bg-orange-700 text-white font-bold py-3 rounded-lg">Subscribe</button>
            </form>"""

        body = _build_spotlight_body(d, subscribe_form)

        html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Spotlight</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background: #0a0e27; color: #e0e6ed; }}
        .glass {{ background: rgba(255,255,255,0.05); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }}
    </style>
</head>
<body class="p-4 md:p-8">
    {body}
    <script>
        async function subscribe() {{
            const email = document.getElementById('email').value;
            try {{
                const r = await fetch('/api/spotlight-subscribe', {{
                    method: 'POST',
                    headers: {{'Content-Type': 'application/json'}},
                    body: JSON.stringify({{ artist_name: '{name}', email: email }})
                }});
                const data = await r.json();
                if (data.status === 'success') {{ alert('✅ Subscribed!'); document.getElementById('email').value = ''; }}
            }} catch (e) {{ alert('Error subscribing'); }}
            return false;
        }}
    </script>
</body>
</html>"""
        return html, 200, {'Content-Type': 'text/html; charset=utf-8'}
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
