import taxjar as jar
client = jar.Client(api_key='36e5eb69d62562d468b07da2ef8252e4')


class TaxProfile:
    def __init__(self, state, city, zip_code):
        self.zip_code = zip_code
        self.state = state
        self.city = city

    def get_rate(self):
        rates = client.rates_for_location(self.zip_code, {
            'city': self.city,
            'state': self.state
        })
        return rates

    def print_profile(self):
        rates = self.get_rate()
        print("User is from {0}, {1} their zip code is {2} and their tax rate is %{3}"
              .format(self.city, self.state, self.zip_code, rates.combined_rate))
