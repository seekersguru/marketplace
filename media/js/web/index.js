$(document).ready(function() {
  $('#json_form').jsonForm({
    formData: {
      'bid': {
        'type': 'bid',
        'event_date': '1',
        'flexible_date': 'Flexible Date',
        'time_slot': {
          'name': 'Time Slot',
          'value': [
            [
              'all_day',
              'All Day'
            ],
            [
              'morning',
              'Morning'
            ],
            [
              'evening',
              'Evening'
            ]
          ]
        },
        'package_ios': {
          'name': 'Package',
          'value': [
            [
              'veg_package_1',
              'Veg Package 1'
            ],
            [
              'veg_package_2',
              'Veg Package 2'
            ]
          ]
        },
        'package': {
          'name': 'Package',
          'value': '',
          'package_list': {
            'veg_package_1': {
              'price': 500,
              'select_val': 'Veg Pakackage 1',
              'description': 'Description about veg package 1',
              'desscription_url': 'http://seekersguru.github.io/wwhtml/Venues-details.html',
              'pricing': {
                'line1': 'pricing line 1 veg pkg 1',
                'line2': 'pricing line 1 veg pkg 1'
              }
            },
            'veg_package_2': {
              'price': 700,
              'select_val': 'Veg Pakackage 2',
              'description': 'Description about veg package 2',
              'pricing': {
                'line1': 'pricing line 2 veg pkg 2',
                'line2': 'pricing line 2 veg pkg 2'
              }
            }
          },
          'package_order': [
            'veg_package_1',
            'veg_package_2'
          ]
        },
        'num_guests': {
          'min': 50,
          'max': 500
        },
        'notes': 'Description(optional)',
        'button': 'Express Interest'
      },
      'info': {
        'email': 'banquet_homotel@wedwise.in',
        'name': 'Grand Homotel Malad',
        'contact': '8298298982',
        'starting_price': '250000',
        'Hall Rental (If Any)': 'none /-',
        'top_name': 'Grand Homotel Malad',
        'hero_imgs': [
          '/media/vendor_image/18/1.jpg',
          '/media/vendor_image/18/2.jpg',
          '/media/vendor_image/18/3.jpg',
          '/media/vendor_image/18/4.jpg',
          '/media/vendor_image/18/5.jpg',
          '/media/vendor_image/18/6.jpg',
          '/media/vendor_image/18/7.jpg',
          '/media/vendor_image/18/8.jpg',
          '/media/vendor_image/18/9.jpg',
          '/media/vendor_image/18/10.jpg'
        ],
        '360_imgs': 'http://www.vrv.co.in/ftpupload/Jw-marriott/virtualtour.html',
        'top_address': 'Sun-n-Sand Mumbai, 39, Juhu Beach, Mumbai - 400049',
        'video_links': [
          'http://seekersguru.github.io/wwhtml/catring-video.html'
        ]
      },
      'sections': [
        {
          'heading': 'General Information',
          'data_display': [
            {
              'type': 'key_value',
              'key_values': [
                {
                  'Starting Price': 'Rs. 1,200 per plate'
                },
                {
                  'Capactiy': '200 - 800 guests'
                },
                {
                  'Venue Type': 'Hotel Banquet'
                }
              ]
            }
          ]
        },
        {
          'heading': 'Food Packages',
          'data_display': [
            {
              'type': 'key_value',
              'key_values': [
                {
                  'Package 1 (Lunch)': '600 /- per plate'
                },
                {
                  'Package 2 (Dinner)': '900 /- per plate'
                },
                {
                  'Package 3 (Lunch/Dinner)': '1100 /- per plate minimum 300 peoples'
                }
              ],
              'read_more': [
                {
                  'heading': 'Food Packages',
                  'data_display': [
                    {
                      'type': 'packages',
                      'Lunch': {
                        'package_values': [
                          {
                            'quoted': {
                              'Quoted Price': '1800'
                            },
                            'minimum': {
                              'Minimum Price': '1600'
                            },
                            'label': 'Veg Package 1 ( 600 /- per plate)',
                            'options': [
                              {
                                'Welcome Drink (2)': 'Pepsi / Coke / Jaljeera /'
                              },
                              {
                                'Starters (4)': 'Veg manchurian / Hara bhara kabab / paneer pakoda'
                              },
                              {
                                'Salads (4)': 'Veg'
                              },
                              {
                                'Soup (2)': 'Veg'
                              },
                              {
                                'Breads (4)': 'Veg'
                              },
                              {
                                'Main Courses (4)': 'Veg'
                              },
                              {
                                'Dal (1)': 'Veg'
                              },
                              {
                                'Rice (2)': 'Veg'
                              },
                              {
                                'Raita (1)': 'Veg'
                              },
                              {
                                'Desert (3)': 'Veg'
                              },
                              {
                                'Live Stations (1)': 'Veg'
                              }
                            ]
                          },

                          {
                            'quoted': {
                              'Quoted Price': '2200'
                            },
                            'minimum': {
                              'Minimum Price': '2000'
                            },
                            'label': 'Veg Package 2 ( 900 /- per plate)',
                            'options': [
                              {
                                'Welcome Drink (3)': 'Pepsi / Coke / Jaljeera /'
                              },
                              {
                                'Starters (5)': 'Veg manchurian / Hara bhara kabab / paneer pakoda'
                              },
                              {
                                'Salads (5)': 'Veg'
                              },
                              {
                                'Soup (4)': 'Veg'
                              },
                              {
                                'Breads (4)': 'Veg'
                              },
                              {
                                'Main Courses (6)': 'Veg'
                              },
                              {
                                'Dal (2)': 'Veg'
                              },
                              {
                                'Rice (2)': 'Veg'
                              },
                              {
                                'Raita (1)': 'Veg'
                              },
                              {
                                'Desert (5)': 'Veg'
                              },
                              {
                                'Live Stations (2)': 'Veg'
                              }
                            ]
                          },
                          {
                            'quoted': {
                              'Quoted Price': '2300'
                            },
                            'minimum': {
                              'Minimum Price': '2100'
                            },
                            'label': 'Non Veg Package 1 ( 1100 /- per plate)',
                            'options': [
                              {
                                'Welcome Drink (2)': 'Pepsi / Coke / Jaljeera /'
                              },
                              {
                                'Starters (4)': 'Veg manchurian / Hara bhara kabab / paneer pakoda'
                              },
                              {
                                'Salads (4)': 'Veg'
                              },
                              {
                                'Soup (2)': 'Veg'
                              },
                              {
                                'Breads (4)': 'Veg'
                              },
                              {
                                'Main Courses (4)': 'Veg'
                              },
                              {
                                'Dal (1)': 'Veg'
                              },
                              {
                                'Rice (2)': 'Veg'
                              },
                              {
                                'Raita (1)': 'Veg'
                              },
                              {
                                'Desert (3)': 'Veg'
                              },
                              {
                                'Live Stations (1)': 'Veg'
                              }
                            ]
                          },
                          {
                            'quoted': {
                              'Quoted Price': '2500'
                            },
                            'minimum': {
                              'Minimum Price': '2300'
                            },
                            'label': 'Non Veg Package 2 ( 600 /- per plate)',
                            'options': [
                              {
                                'Welcome Drink (3)': 'Pepsi / Coke / Jaljeera /'
                              },
                              {
                                'Starters (5)': 'Veg manchurian / Hara bhara kabab / paneer pakoda'
                              },
                              {
                                'Salads (5)': 'Veg'
                              },
                              {
                                'Soup (4)': 'Veg'
                              },
                              {
                                'Breads (4)': 'Veg'
                              },
                              {
                                'Main Courses (6)': 'Veg'
                              },
                              {
                                'Dal (2)': 'Veg'
                              },
                              {
                                'Rice (2)': 'Veg'
                              },
                              {
                                'Raita (1)': 'Veg'
                              },
                              {
                                'Desert (5)': 'Veg'
                              },
                              {
                                'Live Stations (2)': 'Veg'
                              }
                            ]
                          }
                        ]
                      },
                      'Dinner': {
                        'package_values': [
                          {
                            'quoted': {
                              'Quoted Price': '1800'
                            },
                            'minimum': {
                              'Minimum Price': '1600'
                            },
                            'label': 'Veg Package 1 ( 600 /- per plate)',
                            'options': [
                              {
                                'Welcome Drink (2)': 'Pepsi / Coke /'
                              },
                              {
                                'Starters (4)': 'Veg manchurian / Hara bhara kabab / paneer pakoda'
                              },
                              {
                                'Salads (4)': 'Veg'
                              },
                              {
                                'Soup (2)': 'Veg'
                              },
                              {
                                'Breads (4)': 'Veg'
                              },
                              {
                                'Main Courses (4)': 'Veg'
                              },
                              {
                                'Dal (1)': 'Veg'
                              },
                              {
                                'Rice (2)': 'Veg'
                              },
                              {
                                'Raita (1)': 'Veg'
                              },
                              {
                                'Desert (3)': 'Veg'
                              },
                              {
                                'Live Stations (1)': 'Veg'
                              }
                            ]
                          },
                          {
                            'quoted': {
                              'Quoted Price': '2200'
                            },
                            'minimum': {
                              'Minimum Price': '2000'
                            },
                            'label': 'Veg Package 2 ( 600 /- per plate)',
                            'options': [
                              {
                                'Welcome Drink (3)': 'Pepsi / Coke / Jaljeera /'
                              },
                              {
                                'Starters (5)': 'Veg manchurian / Hara bhara kabab / paneer pakoda'
                              },
                              {
                                'Salads (5)': 'Veg'
                              },
                              {
                                'Soup (4)': 'Veg'
                              },
                              {
                                'Breads (6)': 'Veg'
                              },
                              {
                                'Main Courses (6)': 'Veg'
                              },
                              {
                                'Dal (2)': 'Veg'
                              },
                              {
                                'Rice (2)': 'Veg'
                              },
                              {
                                'Raita (1)': 'Veg'
                              },
                              {
                                'Desert (5)': 'Veg'
                              },
                              {
                                'Live Stations (2)': 'Veg'
                              }
                            ]
                          },
                          {
                            'quoted': {
                              'Quoted Price': '2300'
                            },
                            'minimum': {
                              'Minimum Price': '2100'
                            },
                            'label': 'Non Veg Package 1 ( 600 /- per plate)',
                            'options': [
                              {
                                'Welcome Drink (2)': 'Pepsi / Coke /'
                              },
                              {
                                'Starters (4)': 'Veg manchurian / Hara bhara kabab / paneer pakoda'
                              },
                              {
                                'Salads (4)': 'Veg'
                              },
                              {
                                'Soup (2)': 'Veg'
                              },
                              {
                                'Breads (4)': 'Veg'
                              },
                              {
                                'Main Courses (4)': 'Veg'
                              },
                              {
                                'Dal (1)': 'Veg'
                              },
                              {
                                'Rice (2)': 'Veg'
                              },
                              {
                                'Raita (1)': 'Veg'
                              },
                              {
                                'Desert (3)': 'Veg'
                              },
                              {
                                'Live Stations (1)': 'Veg'
                              }
                            ]
                          },
                          {
                            'quoted': {
                              'Quoted Price': '2500'
                            },
                            'minimum': {
                              'Minimum Price': '2300'
                            },
                            'label': 'Non Veg Package 2 ( 600 /- per plate)',
                            'options': [
                              {
                                'Welcome Drink (3)': 'Pepsi / Coke / Jaljeera /'
                              },
                              {
                                'Starters (5)': 'Veg manchurian / Hara bhara kabab / paneer pakoda'
                              },
                              {
                                'Salads (5)': 'Veg'
                              },
                              {
                                'Soup (4)': 'Veg'
                              },
                              {
                                'Breads (4)': 'Veg'
                              },
                              {
                                'Main Courses (6)': 'Veg'
                              },
                              {
                                'Dal (2)': 'Veg'
                              },
                              {
                                'Rice (2)': 'Veg'
                              },
                              {
                                'Raita (1)': 'Veg'
                              },
                              {
                                'Desert (5)': 'Veg'
                              },
                              {
                                'Live Stations (2)': 'Veg'
                              }
                            ]
                          }
                        ]
                      }
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          'heading': 'Catering  Policies',
          'data_display': [
            {
              'type': 'key_value',
              'key_values': [
                {
                  'Veg': 'Yes'
                },
                {
                  'Jain': 'Yes'
                },
                {
                  'Non Veg': 'No'
                }
              ],
              'read_more': [
                {
                  'heading': 'Catering  Policies',
                  'data_display': [
                    {
                      'type': 'key_value',
                      'key_values': [
                        {
                          'Veg': 'Yes'
                        },
                        {
                          'Jain': 'Yes'
                        },
                        {
                          'Non Veg': 'No'
                        },
                        {
                          'General Outside Catering': 'Yes'
                        },
                        {
                          'Specialist Outside Catering': 'Yes'
                        },
                        {
                          'Outside Alchohol': 'Yes'
                        }
                      ]
                    }
                  ]
                }
              ]
            }
          ]
        },
        {
          'heading': 'Other Information',
          'data_display': [
            {
              'type': 'key_value',
              'key_values': [
                {
                  'Valet Service': 'Yes'
                },
                {
                  'Music System': 'Yes'
                },
                {
                  'DJ Booth': 'No'
                }
              ],
              'read_more': [
                {
                  'heading': 'Other Information',
                  'data_display': [
                    {
                      'type': 'key_value',
                      'key_values': [
                        {
                          'Valet Service': 'Yes'
                        },
                        {
                          'Music System': 'Yes'
                        },
                        {
                          'DJ Booth': 'No'
                        },
                        {
                          'Power Back Up': 'Yes'
                        },
                        {
                          'Projector': 'Yes'
                        },
                        {
                          '': ''
                        },
                        {
                          'Tie Ups': ''
                        },
                        {
                          'Caterer-1': 'Bhavik Caterer'
                        },
                        {
                          '': '90292092000'
                        } ,
                        {
                          'Caterer-2': 'Ramesh Caterer'
                        },
                        {
                          '': '9019019010'
                        },
                        {
                          'Floorist': 'Reema Flourist'
                        },
                        {
                          '': '9109091090'
                        }

                      ]
                    }

                  ]
                }
              ]
            }
          ]
        },
        {
          'heading': 'Locate us on map',
          'data_display': [
            {
              'lat': '19.1777352',
              'type': 'map',
              'long': '72.8343873'
            }
          ]
        },
        {
          'heading': 'Vendor Description',
          'data_display': [
            {
              'type': 'para',
              'para': 'This is Description of a Vendor which provide service to you'
            }
          ]
        }
      ]
    },
    renderData: {
      'bid': {
        'type': 'fix',
        'event_date': 'fix',
        'flexible_date': 'fix',
        'time_slot': 'checkbox__value__req__',
        'package_ios': 'add_more_package__value__req__package',
        'num_guests': 'key_value__{}__req__',
        'notes': 'textarea__ __opt__',
        'button': 'fix'
      },
      'info': {
        'name': 'text__ __req__',
        'contact': 'text__ __req__',
        'email': 'email__ __req__',
        'starting_price': 'number__ __req__',
        'Hall Rental (If Any)': 'text__ __opt__',
        'top_name': 'text__ __req__',
        'hero_imgs': 'add_more_text__[]__req__',
        '360_imgs': 'url__ __req__',
        'top_address': 'textarea__ __req__',
        'video_links': 'add_more_text__[]__req__'
      },
      'sections': {}
    },
    formSection: {
      'bid': {
        'type': 'json',
        'name': 'Inquire Data'
      },
      'info': {
        'type': 'json',
        'name': 'Infomation'
      },
      'sections': {
        'type': 'array',
        'name': 'General Sections'
      }
    },
    keyToName: {
      'num_guests': 'Number of Guests',
      'notes': 'Notes',
      'min': 'Min',
      'max': 'Max',
      'name': 'Name',
      'contact': 'Contact',
      'email': 'Email',
      'starting_price': 'Starting Price',
      'top_name': 'Top Name',
      'hero_imgs': 'Header Images',
      '360_imgs': '360 Degree Image Path',
      'top_address': 'Top Address',
      'video_links': 'Video Links'
    },
    saveFunction: function (obj, $msg) {
      console.log(obj);
      $msg.text('Saved Successfully!');
    }
  });
});
