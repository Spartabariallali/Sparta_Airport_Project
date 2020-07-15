import pandas as pd




economy = { "econ_oneway": {"Paris":60,
                                "Madrid":75,
                                "Barcelona":78,
                                "Munich":80,
                                "Rome":90,
                                "Milan":120,
                                "Lisbon":80,
                                "Amsterdam":65,
                                "New York": 230,
                                "Tokyo": 450},

                "econ_return": {"Paris":100,
                                "Madrid":140,
                                "Barcelona":130,
                                "Munich":150,
                                "Rome":160,
                                "Milan":230,
                                "Lisbon":170,
                                "Amsterdam":110,
                                "New York": 396,
                                "Tokyo": 830}}

df_econ = pd.DataFrame({ "Economy OneWay": {"Paris":60,
                                "Madrid":75,
                                "Barcelona":78,
                                "Munich":80,
                                "Rome":90,
                                "Milan":120,
                                "Lisbon":80,
                                "Amsterdam":65,
                                "New York": 230,
                                "Tokyo": 450},

                "Economy Round Trip": {"Paris":100,
                                "Madrid":140,
                                "Barcelona":130,
                                "Munich":150,
                                "Rome":160,
                                "Milan":230,
                                "Lisbon":170,
                                "Amsterdam":110,
                                "New York": 396,
                                "Tokyo": 830}})

df_busines = pd.DataFrame({"Business One Way":{"Paris":120,
                                    "Madrid":140,
                                    "Barcelona":110,
                                    "Munich":130,
                                    "Rome":115,
                                    "Milan":160,
                                    "Lisbon":110,
                                    "Amsterdam":100,
                                    "New York": 350,
                                    "Tokyo": 560},

                "Business Round Trip": {"Paris":350,
                                    "Madrid":300,
                                    "Barcelona":320,
                                    "Munich":290,
                                    "Rome":380,
                                    "Milan":300,
                                    "Lisbon":280,
                                    "Amsterdam":180,
                                    "New York":550,
                                    "Tokyo":990}})


print(df_econ)
print(df_busines)