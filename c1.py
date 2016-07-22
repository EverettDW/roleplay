items = {'food':{'Apple':50,},\
         'weapon':{'None':[5,10],},\
         'drink':{'Water Bottle':50,}}

player = {'name':'',\
'inv_size':15,\
'inv':{'food':'Apple','weapon':'None','drink':'Water Bottle'},\
'health':100,\
'hunger':100,\
'thirst':100,\
'gold':100,\
}

chap_info_evs = {'SP - Entrance':{'desc':"""     You walk into the Savage Palace
     entrance.  Straight ahead is a doorway leading to
     a hallway.  To the left of you is a doorway leading
     outside to the park.  There is a peanut butter fountain to
     your right.""",\
                              'items':[],\
                              'dirs':{'go left':'SP - Park',\
                                      'go forward':'SP - Entry Hallway',\
                                      'go right':'SP - Peanut Butter Fountain'}},\
'SP - Entry Hallway':{'desc':"""     Walking into the hallway, you notice a room on the
     right of you with the label \'Evs\' Room\'.  Straight
     ahead is another room with the label \'Adi\'s Room\'.
     Behind you is the entrance to the pallace.""",\
                      'items':[],\
                      'dirs':{'go right':'SP - Evs\' Room',
                              'go back':'SP - Entrance',\
                              'go forward':'SP - Adi\'s Room'}},\
'SP - Peanut Butter Fountain':{'desc':"""     You turn to the right and walk towards the peanut
     butter fountain.  You see the way the peanut butter
     softly rolls out of the spout into the giant pool
     of peanut butter surrounding the base.""",\
                               'items':[],\
                               'dirs':{'go back':'SP - Entrance'}},\
'SP - Park':{'desc':"""     You walk through the door behind you into a beautiful
     park.  A sign above you says \'Savage Park\'.  You walk
     underneath it and see a bunch of flowers and herbs.
     Potential ingredients for potions?  To the right and straight
     ahead are other parts of the park.""",\
             'items':[],\
             'dirs':{'go back':'SP - Entrance',\
                     'go forward':'SP - Park 1',\
                     'go right':'SP - Park 3'}},\
'SP - Park 1':{'desc':"""     To the right of you is a darker almost hidden path
     that says it leads to gold and happiness.  More flowers around.""",\
               'items':[],\
               'dirs':{'go right':'SP - Park 2',\
                       'go back':'SP - Park'}},\
'SP - Park 2':{'desc':"""     The trail get's darker but you continue onward. in front
     of you is an even darker path but the sign still reads the
     same, \'Gold and Happiness await\'.""",\
               'items':[],\
               'dirs':{'go back':'SP - Park 1',\
                       'go forward':'SP - Park 5'}},\
'SP - Park 3':{'desc':"""     Just some more flowers.  Could be something up ahead
     but who knows?  Besides you, the player, of course ;)""",\
               'items':[],\
               'dirs':{'go back':'SP - Park',\
                       'go forward':'SP - Park 4'}},\
'SP - Park 4':{'desc':"""     So you decided to come up here.  Why's that?  Nevermind
     that for now but hey you should look around.""",\
               'items':[],\
               'dirs':{'go back':'SP - Park 3'}},\
'SP - Park 5':{'desc':"""     Just when it couldn't get any darker, you see a light
     and Adi is standing right in front of you.  You could
     talk to her about what is going on or you can just leave.""",\
               'items':[],\
               'dirs':{'go back':'SP - Park 2'}},\
'SP - Evs\' Room':{'desc':"""     Really messy but you know Evs, always has something
     of great value in his messes and mistakes.  Look around.""",\
                   'items':[],\
                   'dirs':{'go back':'SP - Entry Hallway'}},\
'SP - Adi\'s Room':{'desc':"""     Lelz Adi you can just describe whatever kinda room
     you want here.""",\
                    'items':[],\
                    'dirs':{'go back':'SP - Entry Hallway'}},\
}