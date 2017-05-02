import googlemaps #googlemaps library is used to know locations and distances
import simplejson #to show in the json format
import urllib2

origin = str(raw_input('Enter Origin City: '))
origins = origin.replace(' ', '+') #replace all spaces with + so that while typing no errors

destination =str(raw_input('Enter Destination City: '))
destinations = destination.replace(' ', '+')

apikey = 'AIzaSyAhNrQUiopQZpKdnLifngOUyfAQc9rILiw' #This is my API Key. Do not use it elsewhere. 
url = 'https://maps.googleapis.com/maps/api/distancematrix/json?origins=' + origins + '&destinations=' + destinations + '&departure_time=1541202457&traffic_model=best_guess&key=' + apikey
#print url to check for exact details of the location

response = urllib2.urlopen(url) # this takes the display in variables in simplejason
res = simplejson.load(response)

gmaporigin = res['destination_addresses'][0] #in json we only need one element which is in this order
gmapdestination = res['origin_addresses'][0]

if res['rows'][0]['elements'][0]['status'] == 'NOT_FOUND':
    print origin + ' or ' + destination + ' does not exist'
    
elif res['rows'][0]['elements'][0]['status'] == 'ZERO_RESULTS':
    print 'No roads exist between ' + gmaporigin + ' and ' + gmapdestination
    
else:
    print "Distance between " + gmaporigin + " and " + gmapdestination + " is " + res['rows'][0]['elements'][0]['distance']['text']
