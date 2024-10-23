<h1 align="center">💫 PoroPilot 💫</h1>
<p align="center">
  <em>Riot API made easy</em>
</p>

🚀 **Features**

PoroPilot is a Python library designed to simplify interactions with the Riot Games API. With a suite of classes tailored for ease of use, here’s what PoroPilot offers:

- **PoroPilot**: Your primary interface to the Riot API, handling initialization of essential details like the API key, region, and debug mode.

- **RequestHandler**: Manages the creation of requests to the Riot Games API, utilizing `UrlBuilder`for URL construction.

- **MatchApi** and **SummonerApi**: Facilitate querying of match and summoner information, respectively.

<br>

🛠️ Usage

Initially, you can start with `main.py`, but this approach will be phased out in future versions.

Here's a quick start guide to get you up and running:

      from poropilot import PoroPilot
      
      # Initialize PoroPilot with your API key and region
      euw1_pp = PoroPilot(api_key="your_api_key", region="euw1")
      
      # Fetch match details by its ID
      match_info = euw1_pp.match.by_match_id(match_id="your_match_id")
      
      # Fetch player details by summoner name
      summoner_info = euw1_pp.summoner.by_name(summoner_name="your_summoner_name")

<br>