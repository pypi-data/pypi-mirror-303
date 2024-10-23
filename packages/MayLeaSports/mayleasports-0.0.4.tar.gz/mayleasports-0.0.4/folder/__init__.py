class Team:
    def __init__(self, city, conference, division):
        self.city = city
        self.conference = conference
        self.division = division

class League:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams 

        for team_name in teams:
            setattr(self, team_name, teams[team_name])

class Sports:
    def __init__(self):
        self.nba = League("NBA", {
            "atlanta_hawks": Team("Atlanta", "Eastern", "Southeast"),
            "boston_celtics": Team("Boston", "Eastern", "Atlantic"),
            "brooklyn_nets": Team("Brooklyn", "Eastern", "Atlantic"),
            "charlotte_hornets": Team("Charlotte", "Eastern", "Southeast"),
            "chicago_bulls": Team("Chicago", "Eastern", "Central"),
            "cleveland_cavaliers": Team("Cleveland", "Eastern", "Central"),
            "dallas_mavericks": Team("Dallas", "Western", "Southwest"),
            "denver_nuggets": Team("Denver", "Western", "Northwest"),
            "detroit_pistons": Team("Detroit", "Eastern", "Central"),
            "golden_state_warriors": Team("San Francisco", "Western", "Pacific"),
            "houston_rockets": Team("Houston", "Western", "Southwest"),
            "indiana_pacers": Team("Indianapolis", "Eastern", "Central"),
            "los_angeles_clippers": Team("Los Angeles", "Western", "Pacific"),
            "los_angeles_lakers": Team("Los Angeles", "Western", "Pacific"),
            "memphis_grizzlies": Team("Memphis", "Western", "Southwest"),
            "miami_heat": Team("Miami", "Eastern", "Southeast"),
            "milwaukee_bucks": Team("Milwaukee", "Eastern", "Central"),
            "minnesota_timberwolves": Team("Minneapolis", "Western", "Northwest"),
            "new_orleans_pelicans": Team("New Orleans", "Western", "Southwest"),
            "new_york_knicks": Team("New York", "Eastern", "Atlantic"),
            "oklahoma_city_thunder": Team("Oklahoma City", "Western", "Northwest"),
            "orlando_magic": Team("Orlando", "Eastern", "Southeast"),
            "philadelphia_76ers": Team("Philadelphia", "Eastern", "Atlantic"),
            "phoenix_suns": Team("Phoenix", "Western", "Pacific"),
            "portland_trail_blazers": Team("Portland", "Western", "Northwest"),
            "sacramento_kings": Team("Sacramento", "Western", "Pacific"),
            "san_antonio_spurs": Team("San Antonio", "Western", "Southwest"),
            "toronto_raptors": Team("Toronto", "Eastern", "Atlantic"),
            "utah_jazz": Team("Salt Lake City", "Western", "Northwest"),
            "washington_wizards": Team("Washington", "Eastern", "Southeast"),
        })

        self.nfl = League("NFL", {
            "arizona_cardinals": Team("Glendale", "NFC", "West"),
            "atlanta_falcons": Team("Atlanta", "NFC", "South"),
            "baltimore_ravens": Team("Baltimore", "AFC", "North"),
            "buffalo_bills": Team("Orchard Park", "AFC", "East"),
            "carolina_panthers": Team("Charlotte", "NFC", "South"),
            "chicago_bears": Team("Chicago", "NFC", "North"),
            "cincinnati_bengals": Team("Cincinnati", "AFC", "North"),
            "cleveland_browns": Team("Cleveland", "AFC", "North"),
            "dallas_cowboys": Team("Arlington", "NFC", "East"),
            "denver_broncos": Team("Denver", "AFC", "West"),
            "detroit_lions": Team("Detroit", "NFC", "North"),
            "green_bay_packers": Team("Green Bay", "NFC", "North"),
            "houston_texans": Team("Houston", "AFC", "South"),
            "indianapolis_colts": Team("Indianapolis", "AFC", "South"),
            "jacksonville_jaguars": Team("Jacksonville", "AFC", "South"),
            "kansas_city_chiefs": Team("Kansas City", "AFC", "West"),
            "las_vegas_raiders": Team("Paradise", "AFC", "West"),
            "los_angeles_chargers": Team("Inglewood", "AFC", "West"),
            "los_angeles_rams": Team("Inglewood", "NFC", "West"),
            "miami_dolphins": Team("Miami Gardens", "AFC", "East"),
            "minnesota_vikings": Team("Minneapolis", "NFC", "North"),
            "new_england_patriots": Team("Foxborough", "AFC", "East"),
            "new_orleans_saints": Team("New Orleans", "NFC", "South"),
            "new_york_giants": Team("East Rutherford", "NFC", "East"),
            "new_york_jets": Team("East Rutherford", "AFC", "East"),
            "philadelphia_eagles": Team("Philadelphia", "NFC", "East"),
            "pittsburgh_steelers": Team("Pittsburgh", "AFC", "North"),
            "san_francisco_49ers": Team("Santa Clara", "NFC", "West"),
            "seattle_seahawks": Team("Seattle", "NFC", "West"),
            "tampa_bay_buccaneers": Team("Tampa", "NFC", "South"),
            "tennessee_titans": Team("Nashville", "AFC", "South"),
            "washington_football_team": Team("Landover", "NFC", "East"),
        })

        self.mlb = League("MLB", {
            "arizona_diamondbacks": Team("Phoenix", "National", "West"),
            "atlanta_braves": Team("Atlanta", "National", "East"),
            "baltimore_orioles": Team("Baltimore", "American", "East"),
            "boston_red_sox": Team("Boston", "American", "East"),
            "chicago_cubs": Team("Chicago", "National", "Central"),
            "chicago_white_sox": Team("Chicago", "American", "Central"),
            "cincinnati_reds": Team("Cincinnati", "National", "Central"),
            "cleveland_guardians": Team("Cleveland", "American", "Central"),
            "colorado_rockies": Team("Denver", "National", "West"),
            "detroit_tigers": Team("Detroit", "American", "Central"),
            "houston_astros": Team("Houston", "American", "West"),
            "kansas_city_royals": Team("Kansas City", "American", "Central"),
            "los_angeles_angels": Team("Anaheim", "American", "West"),
            "los_angeles_dodgers": Team("Los Angeles", "National", "West"),
            "miami_marlins": Team("Miami", "National", "East"),
            "milwaukee_brewers": Team("Milwaukee", "National", "Central"),
            "minnesota_twins": Team("Minneapolis", "American", "Central"),
            "new_york_mets": Team("Queens", "National", "East"),
            "new_york_yankees": Team("Bronx", "American", "East"),
            "oakland_athletics": Team("Oakland", "American", "West"),
            "philadelphia_phillies": Team("Philadelphia", "National", "East"),
            "pittsburgh_pirates": Team("Pittsburgh", "National", "Central"),
            "san_diego_padres": Team("San Diego", "National", "West"),
            "san_francisco_giants": Team("San Francisco", "National", "West"),
            "seattle_mariners": Team("Seattle", "American", "West"),
            "st_louis_cardinals": Team("St. Louis", "National", "Central"),
            "tampa_bay_rays": Team("St. Petersburg", "American", "East"),
            "texas_rangers": Team("Arlington", "American", "West"),
            "toronto_blue_jays": Team("Toronto", "American", "East"),
            "washington_nationals": Team("Washington", "National", "East"),
        })

        self.nhl = League("NHL", {
            "anaheim_ducks": Team("Anaheim", "Western", "Pacific"),
            "arizona_coyotes": Team("Glendale", "Western", "Pacific"),
            "boston_bruins": Team("Boston", "Eastern", "Atlantic"),
            "buffalo_sabres": Team("Buffalo", "Eastern", "Atlantic"),
            "calgary_flames": Team("Calgary", "Western", "Pacific"),
            "carolina_hurricanes": Team("Raleigh", "Eastern", "Metropolitan"),
            "chicago_blackhawks": Team("Chicago", "Western", "Central"),
            "colorado_avalanche": Team("Denver", "Western", "Central"),
            "columbus_blue_jackets": Team("Columbus", "Eastern", "Metropolitan"),
            "dallas_stars": Team("Dallas", "Western", "Central"),
            "detroit_red_wings": Team("Detroit", "Eastern", "Atlantic"),
            "edmonton_oilers": Team("Edmonton", "Western", "Pacific"),
            "florida_panthers": Team("Sunrise", "Eastern", "Atlantic"),
            "los_angeles_kings": Team("Los Angeles", "Western", "Pacific"),
            "minnesota_wild": Team("St. Paul", "Western", "Central"),
            "montreal_canadiens": Team("Montreal", "Eastern", "Atlantic"),
            "nashville_predators": Team("Nashville", "Western", "Central"),
            "new_jersey_devils": Team("Newark", "Eastern", "Metropolitan"),
            "new_york_islanders": Team("Elmont", "Eastern", "Metropolitan"),
            "new_york_rangers": Team("New York", "Eastern", "Metropolitan"),
            "ottawa_senators": Team("Ottawa", "Eastern", "Atlantic"),
            "philadelphia_flyers": Team("Philadelphia", "Eastern", "Metropolitan"),
            "pittsburgh_penguins": Team("Pittsburgh", "Eastern", "Metropolitan"),
            "san_jose_sharks": Team("San Jose", "Western", "Pacific"),
            "seattle_kraken": Team("Seattle", "Western", "Pacific"),
            "st_louis_blues": Team("St. Louis", "Western", "Central"),
            "tampa_bay_lightning": Team("Tampa", "Eastern", "Atlantic"),
            "toronto_maple_leafs": Team("Toronto", "Eastern", "Atlantic"),
            "vancouver_canucks": Team("Vancouver", "Western", "Pacific"),
            "vegas_golden_knights": Team("Las Vegas", "Western", "Pacific"),
            "washington_capitals": Team("Washington", "Eastern", "Metropolitan"),
            "winnipeg_jets": Team("Winnipeg", "Western", "Central"),
        })

sports = Sports()

# Accessing team attributes using dot notation
print(sports.nba.boston_celtics.city)  
print(sports.nfl.arizona_cardinals.conference) 
print(sports.mlb.minnesota_twins.city)    
print(sports.nhl.boston_bruins.division) 