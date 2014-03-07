



{



    'gpSettings':
    {
        'maxStartNodes':15,
        'maxDepth':5,
        'mutateMax':5,
        'runs':5,
        'penalty':.1,
    },
    'nodeSettings':
    {
        'scalarMult':
        {
            'scalar':
            {
                'value':0.0,
                'range':(-50.0,50.0),
                'type':'float',
            }
        }
    },
    
     
    'problems':
    [
        {
            'adj':np.matrix([[0,1,1],[1,0,0],[1,0,0]]),
            'deg':np.matrix([[2,0,0],[0,1,0],[0,0,1]]),
            'solution':5,
        },



    ]

}







