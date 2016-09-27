from app import app
from flask import render_template, request, redirect, url_for
import csv
from forms import SubdomainForm


@app.route('/', methods=['GET', ])
def index():

    subdomain_dict = get_subdomain_dict()

    form = SubdomainForm()
    form.subdomain.choices = [(item, item) for item in sorted(subdomain_dict.keys())]

    if 'subdomain' in request.args:
        return redirect(url_for('results', subdomain=request.args.get('subdomain')))

    return render_template('index.html', form=form)


@app.route('/results/<subdomain>')
def results(subdomain):

    subdomain_dict = get_subdomain_dict()

    form = SubdomainForm()
    form.subdomain.choices = [(item, item) for item in sorted(subdomain_dict.keys())]

    if subdomain in subdomain_dict:
        results = [(subdomain, url) for url in subdomain_dict[subdomain]]
        error = None
    else:
        results = None
        error = 'No Results Found'

    return render_template('index.html', form=form, results=results, error=error)


def get_subdomain_dict():
    subdomain_dict = dict()

    with open('app/urls.csv', 'rb') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row[0] != 'Site':
                site = row[0]
                url = row[1]

                if site in subdomain_dict:
                    subdomain_dict[site].append(url)
                else:
                    subdomain_dict[site] = [url, ]
    return subdomain_dict