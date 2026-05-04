import urllib.request

urls = {
    "jars1": "https://images.unsplash.com/photo-1505935428862-770b6a2278d5",
    "jars2": "https://images.unsplash.com/photo-1605336109968-0d04c4033cc1",
    "towels": "https://images.unsplash.com/photo-1585421514738-01798e348b17",
    "baskets": "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace",
    "baskets2": "https://images.unsplash.com/photo-1595526114101-11b0e501a3cd",
    "tray": "https://images.unsplash.com/photo-1615873968403-89e068629265",
    "tray2": "https://images.unsplash.com/photo-1555507036-ab1e4006aa07",
    "suitcase": "https://images.unsplash.com/photo-1500835556837-99ac94a94552",
    "suitcase2": "https://images.unsplash.com/photo-1569949381669-ecf31ae8e613"
}

for name, url in urls.items():
    try:
        req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        print(f"{name}: {response.status}")
    except Exception as e:
        print(f"{name}: Failed - {e}")
