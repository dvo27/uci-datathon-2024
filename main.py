import csv

'''
searches.tsv : Contains a row for each set of searches that a user does for Dublin.
    ds : Date of the search
    id_user : Alphanumeric user_id
    ds_checkin : Date stamp of the check-in date of the search
    ds_checkout : Date stamp of the check-out date of the search
    n_searches : Number of searches in the search set
    n_nights : The number of nights the search was for
    n_guests_min : The minimum number of guests selected in a search set
    n_guests_max : The maximum number of guests selected in a search set
    origin_country : The country the search was from
    filter_price_min : The value of the lower bound of the price filter, if the user used it
    filter_price_max : The value of the upper bound of the price filter, if the user used it
    filter_room_types : The room types that the user filtered by, if the user used the room_types filter
    filter_neighborhoods : The neighborhoods types that the user filtered by, if the user used the neighborhoods filter

- Find most frequent search dates for Dublin (most popular time of travel; holidays etc)
- How long an average stay is (ds_checkin, ds_checkout, n_nights)
- Average number of guests in a search set
- Where do the guests come from (origin_country)
- Average price of bookings
- Most popular neighborhoods
- What kind of room types are most popular?
'''


def tsv_reader(path):
    with open(path) as fd:
        rd = csv.reader(fd, delimiter="\t", quotechar='"')
        for row in rd:
            print(row)