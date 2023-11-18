import csv
from flask import Flask, render_template

def load_countries_from_csv(filepath):
    countries = []
    with open(filepath, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for idx, row in enumerate(reader):
            if idx < 250:
                countries.append({
                    "code": row['Iso Code'],
                    "name": row['Country Name'],
                    "original_name": row['Name in Original language'],
                    "population": row['Population'],
                    "pop_rank": row['Pop. Rank'],
                    "pop_rank_stars": int(row['Pop Rank Stars']),
                    "pop_growth": row['Pop Growth'],
                    "pop_growth_rank": row['Pop. Growth Rank'],
                    "pop_growth_rank_stars": int(row['Pop Growh Rank Stars']),
                    "gdp": row['GDP (Million US$)'],
                    "gdp_rank": row['GDP Rank'],
                    "gdp_rank_stars": int(row['GDP Rank Stars']),
                    "gdp_per_capita": row['GDP per capita (USD)'],
                    "gdp_per_capita_rank": row['GDP per capita Rank'],
                    "gdp_per_capita_rank_stars": int(row['GDP per capita Rank Stars']),
                    "continent": row['Continent'],
                    "capital": row['Capital'],
                    "government": row['Government'],
                    "area": row['Area, Sq km2'],
                    "area_rank": row['Area Rank'],
                    "area_rank_stars" : int(row['Area Rank Stars']),
                    "currency": row['Currency'],
                    "gini_index": row['Gini Index'],
                    "gini_rank": row['Gini Rank'],
                    "gini_index_rank_stars": int(row['Gini Index Rank Stars']),
                    "climate": row['Climate'],
                    "eu_member": row['EU?'],
                    "schengen_member": row['Schengen?'], 
                    "wpfi": row['WPFI'],
                    "wpfi_rank": row['WPFI Rank'],
                    "wpfi_rank_stars": int(row['WPFI Rank Stars']),
                    "hdi": row['HDI'],
                    "hdi_rank": row['HDI Rank'],
                    "hdi_rank_stars": int(row['HDI Rank Stars']),
                    "general_info": row['General info'],
                    "info_length": row['Len(info)'],
                    "name_length": row['Len(name)'],
                    "languages": row['Languages'],
                    "not_independent": row['Non-Independent'],
                    "chinese_name": row['Chinese'],
                    "flashcard_number": idx-2
                })

            else:
                break
    return countries


app = Flask(__name__)

@app.route('/')
def home():
    countries = load_countries_from_csv('data.csv')
    return render_template('flashcard_front_and_back.html', countries=countries)

@app.route('/front/')
def front_flashcards():
    countries = load_countries_from_csv('data.csv')
    return render_template('flashcard_front.html', countries=countries)

@app.route('/back/')
def back_flashcards():
    countries = load_countries_from_csv('data.csv')
    return render_template('flashcard_back.html', countries=countries)

@app.route('/complete/')
def all_flashcards():
    countries = load_countries_from_csv('data.csv')
    return render_template('flashcard_front_and_back.html', countries=countries)

@app.route('/chinese/')
def chinese_flashcards():
    countries = load_countries_from_csv('data.csv')
    return render_template('flashcard_front_and_back_chinese.html', countries=countries)

@app.route('/flashcard/<int:id>')
def single_flashcard(id):
    countries = load_countries_from_csv('data.csv')
    if id < len(countries):
        return render_template('flashcard_front.html', countries=[countries[id]])
    else:
        return "Invalid flashcard ID", 404


if __name__ == '__main__':
    app.run(debug=True)
