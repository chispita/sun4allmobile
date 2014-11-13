

def init_db():
    images = [
        {
            'id': 1,
            'description': u'Sun',
            'done': False,  
            'points':
            [
                { 'x':1, 'y':2 },
                { 'x':2, 'y':3 }
            ]
        },
        {
            'id': 2,
            'description': u'Moon',
            'done': False
        }
    ]

    return images
