import requests
from bs4 import BeautifulSoup, element

url = "https://covid19.who.int/region/searo/country/np"

res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')

confirmed_label = "Confirmed Cases"  # reference label for finding a `span` element
deaths_label = "Deaths"  # reference label for finding a `span` element

wrappers: element.ResultSet = soup.find_all(
    "div", {"data-id": "metric-wrapper"})

cc_element_wrapper = None  # Wrapper div element for Confirmed Cases
d_element_wrapper = None   # Wrapper div element for Deaths

# loop over all the elemets with data-id: "metric-wrapper"
for wrapper in wrappers:
    # if not found, continue searching
    if not cc_element_wrapper:
        # find a span element with data-id: "metric-label" and inside text as `confirmed_label`
        cc_element: element.Tag = wrapper.find(
            "span", {"data-id": "metric-label"}, string=confirmed_label)
        # assign the wrapper if found
        if cc_element != None:
            cc_element_wrapper = wrapper

    # if not found, continue searching
    if not d_element_wrapper:
        # find a span element with data-id: "metric-label" and inside text as `deaths_label`
        d_element: element.Tag = wrapper.find(
            "span", {"data-id": "metric-label"}, string=deaths_label)
        # assign the wrapper if found
        if d_element != None:
            d_element_wrapper = wrapper

# extract the data
confirmed_cases = cc_element_wrapper.find("span", {"data-id": "metric"}).text
# extract the data
deaths = d_element_wrapper.find("span", {"data-id": "metric"}).text

# Showing the results
print(f'Confirmed Cases: {confirmed_cases}')
print(f'Deaths: {deaths}')




# Section 3: Project
# Q.3. Solution
#
# MongoDB Commands
# use Covid
# db.Nepal.insertOne({
#   confirmedCases: 274721,
#   deaths: 3010
#   dateStart: new Date(2020, 01, 03)
#   dateEnd: new Date(2021, 03, 08)
# })