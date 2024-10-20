# A PostgreSQL Database and Python Scripts for Lorcana


This database and subsequent python scripts leverages the Lorcana-API https://github.com/Dogloverblue/Lorcana-API.

I am not affiliated with the lorcana api.  And all copyrights beyond to their respective owners. i.e. Disney, Ravensburger, etc.  I am an enthusiast, just expanding the playability of the game.

# Update - 10/19/2024

Complete overhaul of postgres database.  It now uses Ravensburgs actual data.  Scripts are updated to handle this new data source.  Added encrypted to sensitive fields in database.

API is the next item on the agenda.

# Update - 9-25-2024

The lorcana api uses a mysql database, with each entry held as a json.  I pulled a copy of all of its contents, and then created a postgres database with each piece of information in its own relational table.  I used my database visualizer to identify typos and data duplicates, which I subsequently cleaned up.

The card_images folder is empty, as I have that included in the .gitignore for now.  The script to pull down your own copy of all images is in this repo.

The current version of this database includes cards up through Shimmering Skies.  I am currently working on adding the upcoming Azurite Sea release.

### Known issues:
1) Starter deck info is incomplete # As of 10/19/2024 this isnt included at all yet.  Will be added in the near future.
2) Azurite Sea Not included yet

### Planned Additions:
1) FastAPI scripts to host your own api.
2) Discord Bot script to show cards, and open random packs for fun.
3) Scripts to automate the adjustment of cards - i.e. resize, rotate, overlay, etc