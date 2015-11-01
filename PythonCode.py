import json
from json import load
from urllib2 import urlopen
from pprint import pprint
import pycassa
from pycassa.pool import ConnectionPool
from pycassa.columnfamily import ColumnFamily
from pycassa.index import *

pool = pycassa.ConnectionPool('hr')
crime = pycassa.ColumnFamily(pool, 'crime')

##Pull all of the data and convert to JSON 
data = json.dumps([columns for key, columns in crime.get_range()])
print data
