import json
import re
import requests


state_array = [
    "AK - AK - Alaska",
    "AL - AL - Alabama",
    "AR - AR - Arkansas",
    "AS - AS - American Samoa",
    "AT - AT - Atlantic Offshore",
    "AZ - AZ - Arizona",
    "CA - CA - California",
    "CO - CO - Colorado",
    "CT - CT - Connecticut",
    "DC - DC - Dist. Of Columbia",
    "DE - DE - Delaware",
    "FL - FL - Florida",
    "FM - FM - Fed. Micronesia",
    "GA - GA - Georgia",
    "GB - GB - George's Bank",
    "GM - GM - Gulf of Mexico",
    "GU - GU - Guam",
    "HI - HI - Hawaii",
    "IA - IA - Iowa",
    "ID - ID - Idaho",
    "IL - IL - Illinois",
    "IN - IN - Indiana",
    "JA - JA - Johnston Atoll",
    "KS - KS - Kansas",
    "KY - KY - Kentucky",
    "LA - LA - Louisiana",
    "MA - MA - Massachusetts",
    "MD - MD - Maryland",
    "ME - ME - Maine",
    "MH - MH - Marshall Islands",
    "MI - MI - Michigan",
    "MN - MN - Minnesota",
    "MO - MO - Missouri",
    "MP - MP - Mariana Islands",
    "MS - MS - Mississippi",
    "MT - MT - Montana",
    "MW - MW - Midway Islands",
    "NC - NC - North Carolina",
    "ND - ND - North Dakota",
    "NE - NE - Nebraska",
    "NH - NH - New Hampshire",
    "NI - NI - No. Marianas Isl.",
    "NJ - NJ - New Jersey",
    "NM - NM - New Mexico",
    "NN - NN - Navajo Nation",
    "NV - NV - Nevada",
    "NY - NY - New York",
    "OH - OH - Ohio",
    "OK - OK - Oklahoma",
    "OR - OR - Oregon",
    "PA - PA - Pennsylvania",
    "PR - PR - Puerto Rico",
    "PW - PW - Palau",
    "RI - RI - Rhode Island",
    "SC - SC - South Carolina",
    "SD - SD - South Dakota",
    "TN - TN - Tennessee",
    "TT - TT - Trust Territory",
    "TX - TX - Texas",
    "UM - UM - U.S. Minor Islands",
    "UT - UT - Utah",
    "VA - VA - Virginia",
    "VI - VI - Virgin Islands",
    "VT - VT - Vermont",
    "WA - WA - Washington",
    "WI - WI - Wisconsin",
    "WV - WV - West Virginia",
    "WY - WY - Wyoming",
]

def get_state_array():
    search_lookup = requests.get('https://echo.epa.gov/app/scripts/facility_search/search_lookups.js')
    state_ids_string = re.search(
        r'stateArray\s*=\s*\[(?P<state_ids>(.+?))\]',
        search_lookup.text,
        re.DOTALL
    ).groupdict()['state_ids']
    state_id_lines = re.findall(r'"(.+?)"', state_ids_string)
    return list(map((lambda line: line.split(' - ', 2)[0]), state_id_lines))

def download_csv(state):
    print('Working on {}'.format(state))
    q_columns = '116,70,87,104,138,2,137,3,4,5,6,1,0,7,9,164,10,165,21,123,124,15,16,55,71,90,136,105,111,56,72,91,106,47,44,46,68,85,102,109,33,35,34,59,76,93,112,153,29,28,121,36,61,78,95,107,38,39,62,79,96,108,40,41,42,43,64,81,98,2,137,3,4,5,1,0,47,44,33,38,2,3,1,15,55,71,105,68,85,102,109,35,36,39,40,43'
    r = requests.post('https://echo.epa.gov/app/proxy/proxy.php', data={
        's': 'fac',
        'responseset': 500,
        'p_st': state,
        'p_act': 'Y',
        'qcolumns': q_columns,
    })
    responseJSON = json.loads(r.text)
    query_id = responseJSON['Results']['QueryID']

    r_csv = requests.get('https://ofmpub.epa.gov/echo/echo_rest_services2.get_download', params={
        'qid': query_id,
        'qcolumns': q_columns,
    })
    with open('compliance_{0}.csv'.format(state), 'wb') as fd:
        for chunk in r_csv.iter_content(chunk_size=128):
            fd.write(chunk)


def main():
    print('main')
    for state_string in state_array:
        download_csv(state_string[:2])


if __name__ == '__main__':
    main()
