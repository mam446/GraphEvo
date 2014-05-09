



{



    'gpSettings':
    {
        'maxStartNodes':15,
        'maxDepth':5,
        'mutateMax':5,
        'runs':20,
        'penalty':1,
        'maxSize':300,
        'fitness':'resilient'
    },
    'nodeSettings':
    {
        'randSubset':
        {
            'num':
            {
                'value':0,
                'range':(1,50),
                'type':'int',
            }
        },
        'relRandSubset':
        {
            'relNum':
            {
                'value':0,
                'range':(1,50),
                'type':'int',
            }
        },
        'pSelect':
        {
            'p':
            {
                'value':0.0,
                'range':(0,1.0),
                'type':'float',
            }
        },
        'kTourn':
        {
            'k':
            {
                'value':0,
                'range':(1,50),
                'type':'int',
            },
            'num':
            {
                'value':0,
                'range':(1,50),
                'type':'int',
            },
            'opt':
            {
                'value':"",
                'range':['min','max'],
                'type':'choice',
            },
            'val':
            {
                'value':"",
                'range':['degree'],
                'type':'choice',
            },
        },
        'trunc':
        {
            'num':
            {
                'value':0,
                'range':(1,50),
                'type':'int',
            },
            'opt':
            {
                'value':"",
                'range':['min','max'],
                'type':'choice',
            },
            'val':
            {
                'value':"",
                'range':['degree'],
                'type':'choice',
            },
        },
        'relKTourn':
        {
            'relK':
            {
                'value':0,
                'range':(1,50),
                'type':'int',
            },
            'relNum':
            {
                'value':0,
                'range':(1,50),
                'type':'int',
            },
            'opt':
            {
                'value':"",
                'range':['min','max'],
                'type':'choice',
            },
            'val':
            {
                'value':"",
                'range':['degree'],
                'type':'choice',
            },
        },
        'relTrunc':
        {
            'relNum':
            {
                'value':0,
                'range':(1,50),
                'type':'int',
            },
            'opt':
            {
                'value':"",
                'range':['min','max'],
                'type':'choice',
            },
            'val':
            {
                'value':"",
                'range':['degree'],
                'type':'choice',
            },
        },
    },


    'problems':
    [
        None,

    ]

}







