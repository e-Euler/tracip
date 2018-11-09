import json
import requests
import IpInfo
import shodan

def setGeoInfo(ip):
    url = "http://ip-api.com/json/"+ip
    info = requests.get(url)
    data = info.json()
    ip = IpInfo
    ip.business = data["as"]
    ip.city = data["city"]
    ip.country = data["country"]
    ip.countryCd = data["countryCode"]
    ip.isp = data["isp"]
    ip.lat = data["lat"]
    ip.lon = data["lon"]
    ip.org = data["org"]
    ip.ip = data["query"]
    ip.regioncode = data["region"]
    ip.regionName = data["regionName"]
    ip.status = data["status"]
    ip.timezone = data["timezone"]
    ip.zipcode = data["zip"]
    return ip


def printFindings(ip):
    print("Company: \t"+ip.business+"\n"+
        "City: \t\t"+ip.city+"\n"+
        "Country: \t"+ip.country+ " ["+ip.countryCd+"]\n"+
        "ISP: \t\t"+ip.isp+"\n"+
        "Lattitude: \t"+str(ip.lat)+"\n"+
        "Longitude: \t"+str(ip.lon)+"\n"+
        "Organization: \t"+ip.org+"\n"+
        "Region: \t"+ip.regionName+" ["+ip.regioncode+"]\n"+
        "Timezone: \t"+ip.timezone+"\n"+
        "Zipcode: \t"+ip.zipcode+"\n")
    print("\n\n")

def shodanInfo(business):
    key = ""
    api = shodan.Shodan(key)
    results = api.search(business)
    for result in results['matches']:
        print('IP: {}'.format(result['ip_str']))
        print('Hostname: {} '.format(result['hostnames'] or ' unavailable'))
        print('Port: {}'.format(result['port']))
        print('OS: {}'.format(result['os'] or 'unavailable'))
        print("\n")

if __name__ == '__main__':
    ip = raw_input("IP:")
    related = raw_input("use shodan? [y/n]\n")
    print("\n\n\n")
    data = setGeoInfo(ip)
    printFindings(data)
    if related == 'y':
        shodanInfo(data.org)
 
    

print("If banned visit http://ip-api.com/docs/unban")