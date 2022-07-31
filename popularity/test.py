
from popularity.estimate import estimate_score


aimyon = \
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/5kVZa4lFUmAQlBogl1fkd6"
        },
        "followers": {
            "href": None,
            "total": 3922598
        },
        "genres": [
            "j-acoustic",
            "j-pop"
        ],
        "href": "https://api.spotify.com/v1/artists/5kVZa4lFUmAQlBogl1fkd6",
        "id": "5kVZa4lFUmAQlBogl1fkd6",
        "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5eb74c0985f1edbc66e77297056",
                "width": 640
            },
            {
                "height": 320,
                "url": "https://i.scdn.co/image/ab6761610000517474c0985f1edbc66e77297056",
                "width": 320
            },
            {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f17874c0985f1edbc66e77297056",
                "width": 160
            }
        ],
        "name": "あいみょん",
        "popularity": 66,
        "type": "artist",
        "uri": "spotify:artist:5kVZa4lFUmAQlBogl1fkd6"
    }

beatles = {
    "external_urls": {
        "spotify": "https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2"
    },
    "followers": {
        "href": None,
        "total": 23232959
    },
    "genres": [
        "beatlesque",
        "british invasion",
        "classic rock",
        "merseybeat",
        "psychedelic rock",
        "rock"
    ],
    "href": "https://api.spotify.com/v1/artists/3WrFJ7ztbogyGnTHbHJFl2",
    "id": "3WrFJ7ztbogyGnTHbHJFl2",
    "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5ebe9348cc01ff5d55971b22433",
                "width": 640
            },
        {
                "height": 320,
                "url": "https://i.scdn.co/image/ab67616100005174e9348cc01ff5d55971b22433",
                "width": 320
            },
        {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f178e9348cc01ff5d55971b22433",
                "width": 160
            }
    ],
    "name": "ザ・ビートルズ",
    "popularity": 82,
    "type": "artist",
    "uri": "spotify:artist:3WrFJ7ztbogyGnTHbHJFl2"
}

john_lennon = \
    {
        "external_urls": {
            "spotify": "https://open.spotify.com/artist/4x1nvY2FN8jxqAFA0DA02H"
        },
        "followers": {
            "href": None,
            "total": 4985018
        },
        "genres": [
            "album rock",
            "art rock",
            "beatlesque",
            "classic rock",
            "folk rock",
            "mellow gold",
            "rock"
        ],
        "href": "https://api.spotify.com/v1/artists/4x1nvY2FN8jxqAFA0DA02H",
        "id": "4x1nvY2FN8jxqAFA0DA02H",
        "images": [
            {
              "height": 640,
              "url": "https://i.scdn.co/image/ab6761610000e5eb207c6849d1a1f4480e6aa222",
              "width": 640
            },
            {
                "height": 320,
                "url": "https://i.scdn.co/image/ab67616100005174207c6849d1a1f4480e6aa222",
                "width": 320
            },
            {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f178207c6849d1a1f4480e6aa222",
                "width": 160
            }
        ],
        "name": "ジョン・レノン",
        "popularity": 67,
        "type": "artist",
        "uri": "spotify:artist:4x1nvY2FN8jxqAFA0DA02H"
    }
billie = {
    "external_urls": {
        "spotify": "https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH"
    },
    "followers": {
        "href": None,
        "total": 66510965
    },
    "genres": [
        "art pop",
        "electropop",
        "pop"
    ],
    "href": "https://api.spotify.com/v1/artists/6qqNVTkY8uBg9cP3Jd7DAH",
    "id": "6qqNVTkY8uBg9cP3Jd7DAH",
    "images": [
            {
                "height": 640,
                "url": "https://i.scdn.co/image/ab6761610000e5ebd8b9980db67272cb4d2c3daf",
                "width": 640
            },
        {
                "height": 320,
                "url": "https://i.scdn.co/image/ab67616100005174d8b9980db67272cb4d2c3daf",
                "width": 320
            },
        {
                "height": 160,
                "url": "https://i.scdn.co/image/ab6761610000f178d8b9980db67272cb4d2c3daf",
                "width": 160
            }
    ],
    "name": "ビリー・アイリッシュ",
    "popularity": 87,
    "type": "artist",
    "uri": "spotify:artist:6qqNVTkY8uBg9cP3Jd7DAH"
}
score_a = estimate_score(billie)

print(score_a)
