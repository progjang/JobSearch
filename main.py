# BLUEPRINT | DONT EDIT

from flask import Flask, render_template, request
import json

app = Flask("JobScraper")


def load_jobs():
    with open("jobs.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        return data

# /BLUEPRINT


# 👇🏻 YOUR CODE 👇🏻:

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    jobs = load_jobs()
    print(jobs[0]['title'])
    filtered_jobs = list(filter(lambda x: keyword.lower() in x['title'].lower(), jobs))
    print(filtered_jobs)
    return render_template("search.html", keyword=keyword, jobs=filtered_jobs)


# BLUEPRINT | DONT EDIT

if __name__ == "__main__":
    app.run()

# /BLUEPRINT