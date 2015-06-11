request_post={u"parkingspots": [u"0"], u"restrooms": [u"-1"], u"outsidealcohol": [u"-1"], 
              u"raita": [u""], u"maincourses": [u""], u"jainpreperation": [u"-1"],
             u"capacity_floating": [u"aa", u"aa"], u"tables": [u"-1"], u"speciliatycuisine": [u""], 
             u"projector": [u"-1", u"-1"], u"billing": [u"sadasd"], u"elevator": [u"-1"], 
             u"bridalroom": [u"-1"], u"starters": [u""], u"soundsystem": [u"-1"], u"rice": [u""], 
             u"neighbouhood": [u"a"], u"mike": [u"-1", u"-1"], u"_save": [u""], u"dal": [u""], 
             u"chaiecovers": [u"-1"], u"Ramp": [u"-1"], u"phone": [u"aa"], u"tablecovers": [u"-1"], 
             u"dj_setup": [u"-1"], u"name": [u"aa"], u"chairs": [u"-1"], u"non_veg": [u"-1"], 
             u"foreignalcoholpermit": [u"-1"], u"partylights": [u"-1"], 
             u"outsidegeneralcatering": [u"-1"], u"hallrental": [u""], u"ac": [u"0", u"-1"], 
             u"overmightroom": [u"-1"], u"firefighting": [u"-1"], u"firstaidkit": [u"-1"], 
             u"cluster": [u""], u"poolside": [u"-1"], u"food_type": [u"veg"], u"bikepark": [u""], 
             u"salads": [u""], u"floating": [u"sdfsdfsd"], u"drinks": [u""], u"shower": [u"-1"], 
             u"venutype": [u"sdasdasd"], u"sprinkler": [u"-1"], u"outsidecatering": [u"0"], 
             u"oncalldoctor": [u"-1"], u"musicsystem": [u"-1"], u"powerbackup": [u"-1"], 
             u"class": [u""], u"outsidespecialtycatering": [u"-1"], u"u_shape": [u""], 
             u"livestations": [u""], u"address": [u"aa"], u"wheelchairs": [u"-1"], 
             u"valetservice": [u"-1"], u"desert": [u""], u"theater": [u""], u"soups": [u""], 
             u"licenseliasion": [u"-1"], u"valetparking": [u"-1", u"-1"], 
             u"gps co_ordinates": [u"aaaaa"], u"breads": [u""]}

# TODO VALIDATE: name must be unique  

banquet_rule_m =\
[
    {
        "label":"Basic Info",
        "fields":[
            {
                "min_length":2,
                "max_length":50,
                "name":"name",
                "validations":[

                ],
                "help_text":"Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
                "required":1,
                "type":"input",
                "label":"Name"
            },
            {
                "min_length":2,
                "max_length":70,
                "name":"address",
                "validations":[

                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Address"
            },
            {
                "min_length":2,
                "max_length":12,
                "name":"phone",
                "validations":[

                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Phone"
            },
            {
                "min_length":2,
                "max_length":50,
                "name":"neighbouhood",
                "validations":[

                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Neighbouhood"
            },
            {
                "min_length":2,
                "max_length":50,
                "name":"gps co_ordinates",
                "validations":[

                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"GPS Co_Ordinates"
            },
            {
                "required":1,
                "name":"capacity_floating",
                "validations":[

                ],
                "label":"Capacity_floating",
                "help_text":"Please enter min and max capacity ",
                "type":"range"
            },
            {
                "required":1,
                "name":"food_type",
                "validations":[

                ],
                "label":"Food Type",
                "help_text":"",
                "choices":[
                    [
                        "veg",
                        "Veg"
                    ],
                    [
                        "non_veg",
                        "Non-Veg"
                    ],
                    [
                        "jain_only",
                        "Jain only"
                    ],
                    [
                        "alcohol",
                        "Alcohol"
                    ]
                ],
                "type":"checkbox"
            },
            {
                "required":1,
                "name":"parkingspots",
                "validations":[

                ],
                "label":"Parking Spots",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"ac",
                "validations":[

                ],
                "label":"AC",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "min_length":2,
                "max_length":50,
                "name":"speciliatycuisine",
                "validations":[

                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Speciliaty Cuisine"
            },
            {
                "min_length":2,
                "max_length":50,
                "name":"venutype",
                "validations":[

                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Venu Type"
            },
            {
                "required":1,
                "name":"outsidecatering",
                "validations":[

                ],
                "label":"Outside Catering",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            }
        ]
    },
#######################Here come the prcing section #############################
    {
        "label":"Pricing",
        "fields":[
            {
                "min_length":2,
                "max_length":50,
                "name":"billing",
                "validations":[

                ],
                "help_text":"Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
                "required":1,
                "type":"input",
                "label":"Billing"
            },
            {
                "min_length":2,
                "max_length":70,
                "name":"hallrental",
                "validations":[

                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Hallrental"
            }
        ]
    },

#######################Here come the Extra section #############################
 
    
    {
          
        "label":"Other/Extras [Only if applicable]",
        "fields":[
            {
                "required":1,
                "name":"valetservice",
                "validations":[
    
                ],
                "label":"Valet Service",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"projector",
                "validations":[
    
                ],
                "label":"Projector",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"soundsystem",
                "validations":[
    
                ],
                "label":"Sound System",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"mike",
                "validations":[
    
                ],
                "label":"Mike",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            }
        ]
     },
                
    {
        "label":"Facilites",
        "fields":[
            {
                "required":1,
                "name":"venuetype",
                "validations":[
    
                ],
                "label":"Venue_Type",
                "help_text":"",
                "choices":[
                    [
                        "hotel",
                        "Hotel"
                    ],
                    [
                        "banquette hall",
                        "Banquette Hall"
                    ],
                    [
                        "party lawn",
                        "Party Lawn"
                    ],
                    [
                        "farmhouse",
                        "Farm House"
                    ]
                ],
                "type":"checkbox"
            },
            {
                "required":1,
                "name":"ac",
                "validations":[
    
                ],
                "label":"Ac",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"powerbackup",
                "validations":[
    
                ],
                "label":"PowerBackup",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"restrooms",
                "validations":[
    
                ],
                "label":"Restrooms",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"shower",
                "validations":[
    
                ],
                "label":"Shower",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"bridalroom",
                "validations":[
    
                ],
                "label":"BridalRoom",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"elevator",
                "validations":[
    
                ],
                "label":"Elevator",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"Ramp",
                "validations":[
    
                ],
                "label":"Ramp",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"wheelchairs",
                "validations":[
    
                ],
                "label":"Wheelchairs",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"chairs",
                "validations":[
    
                ],
                "label":"Chairs",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"chaiecovers",
                "validations":[
    
                ],
                "label":"Chaircovers",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"tables",
                "validations":[
    
                ],
                "label":"Tables",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"tablecovers",
                "validations":[
    
                ],
                "label":"Tablecovers",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"poolside",
                "validations":[
    
                ],
                "label":"Poolside",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"overmightroom",
                "validations":[
    
                ],
                "label":"OvermightRoom",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            }
        ]
    },
      
############## Food and Drin section               
    {
        "label":"Food&Drinks",
        "fields":[
            {
                "required":1,
                "name":"jainpreperation",
                "validations":[
    
                ],
                "label":"JainPreperation",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"non_veg",
                "validations":[
    
                ],
                "label":"Non_Veg",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"outsidegeneralcatering",
                "validations":[
    
                ],
                "label":"Outside General Catering",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"outsidespecialtycatering",
                "validations":[
    
                ],
                "label":"Outside Specialty Catering",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"foreignalcoholpermit",
                "validations":[
    
                ],
                "label":"Foreign Alcohol Permit",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"outsidealcohol",
                "validations":[
    
                ],
                "label":"Outside Alcohol",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            }
        ]
    },
          
    {
        "label":"Safety",
        "fields":[
            {
                "required":1,
                "name":"firstaidkit",
                "validations":[
    
                ],
                "label":"First Aid Kit",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"firefighting",
                "validations":[
    
                ],
                "label":"Fire Fighting",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"sprinkler",
                "validations":[
    
                ],
                "label":"Sprinkler",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"oncalldoctor",
                "validations":[
    
                ],
                "label":"On Call Doctor",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            }
        ]
    },
            
##########################Capacity section         
    {
        "label":"Capacity",
        "fields":[
            {
                "min_length":2,
                "max_length":50,
                "name":"floating",
                "validations":[
    
                ],
                "help_text":"Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
                "required":1,
                "type":"input",
                "label":"Floating"
            },
            {
                "min_length":2,
                "max_length":70,
                "name":"u_shape",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"U Shape"
            },
            {
                "min_length":2,
                "max_length":70,
                "name":"cluster",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Cluster"
            },
            {
                "min_length":2,
                "max_length":70,
                "name":"theater",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Theater"
            },
            {
                "min_length":2,
                "max_length":70,
                "name":"class",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Class"
            },
            {
                "min_length":2,
                "max_length":70,
                "name":"bikepark",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Bike Park"
            },
            {
                "required":1,
                "name":"valetparking",
                "validations":[
    
                ],
                "label":"Valet Parking",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            }
        ]
    },
          
################  AV / Music      
    {
        "label":"AV/Music",
        "fields":[
            {
                "required":1,
                "name":"musicsystem",
                "validations":[
    
                ],
                "label":"Music System",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"dj_setup",
                "validations":[
    
                ],
                "label":"DJ Setup",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"partylights",
                "validations":[
    
                ],
                "label":"Party Lights",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"mike",
                "validations":[
    
                ],
                "label":"Mike",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"projector",
                "validations":[
    
                ],
                "label":"Projector",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            },
            {
                "required":1,
                "name":"licenseliasion",
                "validations":[
    
                ],
                "label":"License Liasion",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            }
        ]
    },
             
    ## Menu Pckage Lunch Dinner 
    {
        "label":"MENU/Veg Package1[Lunch/Dinner]",
        "fields":[
            {
                "min_length":2,
                "max_length":1000,
                "name":"drinks",
                "validations":[
    
                ],
                "help_text":"Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.",
                "required":1,
                "type":"input",
                "label":"Drinks"
            },
            {
                "min_length":2,
                "max_length":700,
                "name":"starters",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Starters"
            },
            {
                "min_length":2,
                "max_length":700,
                "name":"salads",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Salads"
            },
            {
                "min_length":2,
                "max_length":700,
                "name":"soups",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Soups"
            },
            {
                "min_length":2,
                "max_length":700,
                "name":"breads",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Breads"
            },
            {
                "min_length":2,
                "max_length":700,
                "name":"maincourses",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Main Courses"
            },
            {
                "min_length":2,
                "max_length":700,
                "name":"dal",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Dal"
            },
            {
                "min_length":2,
                "max_length":700,
                "name":"rice",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Rice"
            },
            {
                "min_length":2,
                "max_length":700,
                "name":"raita",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Raita"
            },
            {
                "min_length":2,
                "max_length":70,
                "name":"desert",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Desert"
            },
            {
                "min_length":2,
                "max_length":70,
                "name":"livestations",
                "validations":[
    
                ],
                "help_text":"",
                "required":1,
                "type":"input",
                "label":"Live Stations"
            },
            {
                "required":1,
                "name":"valetparking",
                "validations":[
    
                ],
                "label":"Valet Parking",
                "help_text":"",
                "choices":[
                    [
                        -1,
                        "---"
                    ],
                    [
                        0,
                        "Yes"
                    ],
                    [
                        1,
                        "No"
                    ]
                ],
                "type":"select"
            }
        ]
    }
]


if __name__ == "__main__":
    banquet_rule_copy = banquet_rule_m[:]
    for index in range(len(banquet_rule_m)):
        section=banquet_rule_m[index]
        for index_field in range(len(section["fields"])):
            field =section["fields"][index_field]
            field_name = field["name"]
            #print  field_name,request_post.get(field_name)
            #import pdb;pdb.set_trace()
            banquet_rule_copy[index]["fields"][index_field]["value"]=request_post.get(field_name)
            if banquet_rule_copy[index]["fields"][index_field]["value"]["required"] \
                and (not request_post.get(field_name).strip()):
                    banquet_rule_copy[index]["fields"][index_field]["error"]=1
                
    banquet_rule_m = banquet_rule_copy
    import pdb;pdb.set_trace()        
            
            
            
        