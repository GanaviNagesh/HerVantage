from flask import Flask, request, render_template
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)

# MongoDB Connection
client = MongoClient("mongodb://localhost:27017")  # Connect to your MongoDB server
db = client.HACHTHON
  # Replace with your database name
collection = db.HACK
  # Replace with your collection name

# Route for the home page where the form will be displayed
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Collect user input from the form
        user_input = {
            "Skill": request.form["primary_skill"],
            "Investment Level": request.form["investment"],
            "Group Preference": request.form["gathering"],
            "Working Style": request.form["time_dedication"]
        }

        # Query MongoDB based on user input
        query = {
             "Skill": request.form["primary_skill"],
            "Investment Level": request.form["investment"],
            "Group Preference": request.form["gathering"],
            "Working Style": request.form["time_dedication"]
        }

        # Search for matching business ideas in MongoDB
        results = collection.find(query, {"Business Idea": 1, "_id": 0})
        
        # Prepare the list of business ideas from the results
        ideas = [result["Business Idea"] for result in results]
        
        # If no results, show a fallback message
        if not ideas:
            ideas = ["No matching business ideas found."]
        
        return render_template("results.html", ideas=ideas)

    return render_template("Business_ideas.html")

if __name__ == "__main__":
    app.run(debug=True)
