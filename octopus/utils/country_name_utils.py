##
# Different country names between files:
#
# matches-schedule.csv:                     Iran,       South Korea,    USA
# historical-results.csv:                   Iran,       South Korea,    United States
# historical_win-loose-draw_ratios.csv:     Iran,       South Korea,    -
# ranking.csv:                              IR Iran,    Korea Republic, USA
# submission.csv:                           Iran,       South Korea,    USA
#
##
country_names_in_ranking = {
    'Iran': 'IR Iran',
    'South Korea': 'Korea Republic'
}

country_names_in_results = {
    'USA': 'United States'
}


def get_country_name_in_ranking(country_name):
    if country_name in country_names_in_ranking:
        return country_names_in_ranking[country_name]
    else:
        return country_name


def get_country_name_in_results(country_name):
    if country_name in country_names_in_results:
        return country_names_in_results[country_name]
    else:
        return country_name
