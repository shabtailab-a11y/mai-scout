"""
MAI Reports Server - Serve research documents and databases
"""

from flask import Flask, send_file, jsonify
import json
from datetime import datetime

app = Flask(__name__)

# Enable CORS
from flask_cors import CORS
CORS(app)

@app.route('/reports/cities', methods=['GET'])
def cities_database():
    """Serve cities database as JSON"""
    try:
        with open('../reports/cities_database_20_principal.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reports/cities.csv', methods=['GET'])
def cities_csv():
    """Download cities as CSV"""
    try:
        return send_file('../reports/cities_database.csv', 
                        mimetype='text/csv',
                        as_attachment=True,
                        download_name='mai_cities_database.csv')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/reports/chartmetric', methods=['GET'])
def chartmetric_report():
    """Serve Chartmetric research report as JSON"""
    report = {
        "title": "Chartmetric API Research Report",
        "status": "Complete",
        "xp": 20,
        "date": "2026-02-07",
        "sections": {
            "executive_summary": "Chartmetric is recommended for integration. Provides 95%+ accuracy demographic data vs 70% from genre-based heuristics.",
            "key_endpoints": [
                "GET /v1/artist/{id}/audienceGeography - Country/city listener distribution",
                "GET /v1/artist/{id}/audienceDemographics - Age, gender, platform data",
                "GET /v1/artist/{id}/stats - Overall artist metrics"
            ],
            "pricing": {
                "free": "$0 (limited)",
                "pro": "$99-299/month (recommended)",
                "enterprise": "Custom"
            },
            "recommendation": "INTEGRATE - Will improve tour planning accuracy by 20%+"
        },
        "download_links": {
            "markdown": "https://raw.githubusercontent.com/shabtailab-a11y/mai-scout/main/reports/MAI_CHARTMETRIC_RESEARCH.md",
            "json": "/reports/chartmetric.json"
        }
    }
    return jsonify(report)

@app.route('/reports/demographics-scraper', methods=['GET'])
def demographics_scraper():
    """Serve demographics scraper documentation"""
    docs = {
        "title": "Demographics Scraper Demo",
        "status": "Complete",
        "xp": 50,
        "date": "2026-02-07",
        "description": "Python script for scraping artist demographic data from Spotify and mapping to city venues",
        "features": [
            "Genre-based demographic estimation",
            "City-level venue recommendations",
            "Multi-artist batch processing",
            "Growth rate analysis"
        ],
        "output": {
            "age_distribution": "Age brackets (13-17, 18-24, 25-34, 35-44, 45+)",
            "gender_split": "Male/Female percentage",
            "top_countries": "Country distribution with listener counts",
            "recommended_cities": "Top venues by suitability"
        },
        "github_link": "https://github.com/shabtailab-a11y/mai-scout/blob/main/reports/demographics_scraper_demo.py"
    }
    return jsonify(docs)

@app.route('/reports', methods=['GET'])
def reports_index():
    """Index of all reports"""
    reports = {
        "project": "MAI - Music Audience Insights",
        "execution_date": "2026-02-07 14:51 UTC",
        "total_xp": 130,
        "reports": [
            {
                "name": "Cities Database",
                "description": "20 principal cities for tour planning",
                "xp": 60,
                "formats": {
                    "json": "/reports/cities",
                    "csv": "/reports/cities.csv",
                    "html": "/reports/cities.html"
                }
            },
            {
                "name": "Chartmetric API Research",
                "description": "Integration feasibility study and recommendations",
                "xp": 20,
                "formats": {
                    "json": "/reports/chartmetric",
                    "markdown": "https://raw.githubusercontent.com/shabtailab-a11y/mai-scout/main/reports/MAI_CHARTMETRIC_RESEARCH.md"
                }
            },
            {
                "name": "Demographics Scraper Demo",
                "description": "Python script for demographic data extraction",
                "xp": 50,
                "formats": {
                    "json": "/reports/demographics-scraper",
                    "github": "https://github.com/shabtailab-a11y/mai-scout/blob/main/reports/demographics_scraper_demo.py"
                }
            }
        ]
    }
    return jsonify(reports)

@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        'status': 'ok',
        'service': 'MAI Reports Server',
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True)
