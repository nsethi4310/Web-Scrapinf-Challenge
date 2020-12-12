from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    heading = mongo.db.heading.find_one()
    return render_template("index.html", heading=heading)

@app.route("/mars_hemispheres")
def hem():
    listing = mongo.db.listing.find_one()
    return render_template("index1.html", listing=listing)

@app.route("/scrape")
def scraper():
    #listing = mongo.db.listing
    heading = mongo.db.heading
    heading_data = scrape_mars.scrape()
    #listing.update({},  upsert=True)
    heading.update({}, heading_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
