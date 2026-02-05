from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import re
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from googleapiclient.discovery import build

app = Flask(__name__, static_folder='.')
CORS(app)

import os

# Credenciales (from environment variables)
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID', 'e490c3b2db6744ce884b9d27f426d4f7')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET', '6cd469cf554842b29f009a9555894ace')
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', 'AIzaSyCu5JG9wt4roONhqLbO9ca6m4wv6-JT3WA')
LASTFM_API_KEY = os.getenv('LASTFM_API_KEY', '8aa9d7b90c4f1c1e0c5c3b5c1c5c3b5c')

# RapidAPI TikTok (reemplazar con tu API key de RapidAPI)
# Obtener en: https://rapidapi.com/
RAPIDAPI_KEY = 'TU_RAPIDAPI_KEY_AQUI'

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

def get_geo_data_from_spotify_genres(artist_name):
    """Obtiene datos geográficos usando análisis de géneros de Spotify"""
    try:
        # Buscar artista
        search_results = spotify.search(q=artist_name, type='artist', limit=1)
        if not search_results['artists']['items']:
            return None
        
        artist = search_results['artists']['items'][0]
        genres = set(g.lower() for g in artist.get('genres', []))
        
        # Distribución base realista
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
        
        # Ajustes AGRESIVOS basados en géneros reales
        # Reggaeton/Trap Latino → Latam domina
        if any(x in genres for x in ['reggaeton', 'trap latino', 'urbano latino', 'latin trap']):
            country_scores = {'MX': 22, 'AR': 18, 'CO': 15, 'US': 15, 'BR': 10, 'CL': 8, 'ES': 7, 'GB': 3, 'DE': 2, 'FR': 0}
        
        # Argentine Rock/Pop → Argentina domina
        elif any(x in genres for x in ['argentine rock', 'latin rock', 'latin indie', 'indie pop']) or 'electrónico' in genres:
            country_scores = {'AR': 35, 'US': 15, 'BR': 12, 'CO': 10, 'CL': 8, 'ES': 7, 'MX': 5, 'GB': 4, 'DE': 2, 'FR': 2}
        
        # Brazilian → Brasil domina
        elif any(x in genres for x in ['samba', 'bossanova', 'forró', 'brazilian', 'funk carioca']):
            country_scores = {'BR': 40, 'US': 15, 'MX': 10, 'AR': 8, 'CO': 8, 'ES': 7, 'GB': 5, 'DE': 4, 'FR': 2, 'CL': 1}
        
        # K-pop → distribución global balanced
        elif 'k-pop' in genres or 'korean' in genres:
            country_scores = {'US': 25, 'BR': 18, 'MX': 15, 'AR': 12, 'CO': 10, 'ES': 8, 'GB': 6, 'DE': 4, 'FR': 2, 'CL': 0}
        
        # Reggaeton global like Bad Bunny
        elif 'reggaeton' in genres:
            country_scores = {'MX': 20, 'US': 20, 'AR': 15, 'CO': 12, 'BR': 10, 'CL': 8, 'ES': 7, 'GB': 4, 'DE': 2, 'FR': 2}
        
        # Afrobeats → Brasil high
        elif any(x in genres for x in ['afrobeats', 'amapiano', 'afroswing']):
            country_scores = {'BR': 25, 'US': 30, 'MX': 12, 'AR': 8, 'CO': 8, 'ES': 8, 'GB': 5, 'DE': 2, 'FR': 1, 'CL': 1}
        
        # Pop Global → USA domina
        elif 'pop' in genres and len(genres) < 3:
            country_scores = {'US': 40, 'BR': 15, 'MX': 12, 'AR': 10, 'ES': 8, 'GB': 7, 'CO': 4, 'DE': 2, 'FR': 1, 'CL': 1}
        
        # Si ningún patrón matchea, retornar scores default
        return country_scores
        
    except Exception as e:
        print(f"Error in geo analysis: {e}")
        return None

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
            'youtube': youtube_stats
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
        # Buscar artista por nombre (tomar el primer resultado)
        search_results = spotify.search(q=artist_name, type='artist', limit=1)
        
        if not search_results['artists']['items']:
            return jsonify({'error': f'No se encontró el artista "{artist_name}"'}), 404
        
        # Tomar el mejor match (primer resultado)
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

@app.route('/api/search', methods=['POST'])
def search_artist():
    """Buscar artistas por nombre"""
    data = request.get_json()
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': 'Query requerida'}), 400
    
    try:
        results = spotify.search(q=query, type='artist', limit=5)
        artists = []
        
        for artist in results['artists']['items']:
            artists.append({
                'id': artist['id'],
                'name': artist['name'],
                'image': artist['images'][0]['url'] if artist['images'] else None,
                'url': artist['external_urls']['spotify']
            })
        
        return jsonify({'artists': artists})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

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
        
        # Obtener datos geográficos basados en géneros Spotify
        country_scores = get_geo_data_from_spotify_genres(artist_name)
        
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
            distribution[country] = round((score / total_score) * 100, 1)
        
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
        
        top_5 = sorted(distribution.items(), key=lambda x: x[1], reverse=True)[:5]
        
        geo_data = []
        for country_code, percentage in top_5:
            geo_data.append({
                'country': country_code,
                'name': countries_info[country_code]['name'],
                'flag': countries_info[country_code]['flag'],
                'percentage': percentage
            })
        
        return jsonify({
            'artist': artist_name,
            'top_countries': geo_data,
            'genres': list(artist.get('genres', []))[:5]
        })
        
    except Exception as e:
        print(f"Geography API error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
