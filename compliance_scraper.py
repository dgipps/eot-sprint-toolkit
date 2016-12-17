import json
import requests


def main():
    print('main')
    # r = requests.post('https://echo.epa.gov/facilities/facility-search/results', data={
    #     'formreq': 'mediaSelected=all data&us_mexico=Any&indianCountry=Any&indianCountryPgrm=Any&frsTribalLand=Any&tribedist=none&facNameType=ALL&permitAll=N&fedFacility=Any&issuingAgency=Any&msgpPermitType=Any&msgpSector=none&MS4=Any&mactSubpart=none&ownerOperator2=none&activeOp=Y&major=Any&major2=Any&combinedSewerSystem=none&permitExpirationDate=none&permitLimitsPresent=Any&mact=none&activeOp2=Any&yrsSinceLastInsp=NR&yrsSinceLastInspYr=1&formalEnfActions=NR&formalEnfActionsYr=1&informalEnfActions=NR&informalEnfActionsYr=1&penalties=none&monthsInHPV=none&complianceStatus=No Restrictions&noeep3y=none&numberOfCurrentViolations=none&facsWithContinuingViolations=none&qisncoc1v=none&qtrsInViolation=none&qtrsInSeriousViolation=none&stackTest=NR&stackTestYr=1&nonAttain=Any&impairedWater=Any&impairedPolls=Any&dtddwi=none&pollTriReporter=none&caaProgTRI=NR&caaProgNEI=NR&caaProgGHG=NR&caaProgCAMD=NR&onsiteChemRelease=none&onsiteLandRelease=none&offsiteChemTrans=none&waterMonPerYr=1&pollCat=none&directWaterDischarges=none&potwTransfers=none&pctMinority=none&popDensity=none',
    #     'state': 'AK'
    # })
    # print(r)

    r = requests.post('https://echo.epa.gov/app/proxy/proxy.php', data={
        's': 'fac',
        'responseset': 500,
        'p_st': 'AK',
        'p_act': 'Y',
        'qcolumns': '116,70,87,104,138,2,137,3,4,5,6,1,0,7,9,164,10,165,21,123,124,15,16,55,71,90,136,105,111,56,72,91,106,47,44,46,68,85,102,109,33,35,34,59,76,93,112,153,29,28,121,36,61,78,95,107,38,39,62,79,96,108,40,41,42,43,64,81,98,2,137,3,4,5,1,0,47,44,33,38,2,3,1,15,55,71,105,68,85,102,109,35,36,39,40,43',
    })
    responseJSON = json.loads(r.text)
    print(responseJSON['Results']['QueryID'])
    print(r.headers)
    # for chunk in r.iter_content(chunk_size=128):
    #     print(chunk)

if __name__ == '__main__':
    main()
