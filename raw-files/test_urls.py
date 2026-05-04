import urllib.request

urls = {
    "caixas": "https://images.unsplash.com/photo-1585421514738-01798e348b17",
    "caixas2": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace",
    "viagem": "https://images.unsplash.com/photo-1569949381669-ecf31ae8e613",
    "viagem2": "https://images.unsplash.com/photo-1500835556837-99ac94a94552",
    "potes": "https://images.unsplash.com/photo-1590005354167-6da97ce2b4dc",
    "servir": "https://images.unsplash.com/photo-1615873968403-89e068629265"
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        print(f"{name}: {response.status}")
    except Exception as e:
        print(f"{name}: Failed - {e}")
