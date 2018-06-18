import re
import json
import consul
import pymssql
import pymysql

SCANNER_SOURCE_KEY_CONST = ["source/"]
SCANNER_REQUEST_KEY_CONST = ["scanner/", "/action/request/"]
SCANNER_HASHVAL_KEY_CONST = ["locationinfo/"]

class ConsulScannerHash:

    def __init__(self, mode, hostip, port, usrname, pwd, dbname):
        self.reqid = 0
        self.mode = mode
        self.hostip = hostip
        self.port = port
        self.usrname = usrname
        self.pwd = pwd
        self.dbname = dbname
        if self.mode == "mssql":
            self.conn = pymssql.connect(self.hostip, self.usrname, self.pwd, self.dbname)
        elif self.mode == "mysql":
            self.conn = pymysql.connect(host=self.hostip, user=self.usrname, password=self.pwd, db=self.dbname)
        self.alias = 'mssql_alias'
        self.tenantid = 'mssql_tenant_uuid'

    def consulkv_put_scanner_source(self, consul_ip, consul_port,
                                    sourceid, alias, scannerid, tenantid,
                                    keytabname, keycolname, tabname, colnames):

        alias = 'mssql_alias'
        tenantid = 'mssql_tenant_uuid'
        source_input = {
            'UUID': sourceid,
            'Alias': alias,
            'ScannerID': '',
            'TenantID': tenantid,
            'DbInfo': {'Host': self.hostip, 'Port': self.port, 'Dbtype': 0,
                       'Username': self.usrname, 'Password': self.pwd, 'Dbname': self.dbname},
            'State': 0,
            'Key': {'LastScanTime':'0001-01-01T00:00:00Z', 'Table': keytabname, 'Column': keycolname},
            'Tables': [
                {'TableName': tabname, 'Columns': colnames}],
            'LastScanTime': '0001-01-01T00:00:00Z',
            'SigUUID': ''
        }
        try:
            source_str = json.dumps(source_input, separators=(',', ':'))
        except TypeError:
            print("Unable to dump this source into json string")
            source_str = ""

        c = consul.Consul(host=consul_ip, port=consul_port)
        c.kv.put(SCANNER_SOURCE_KEY_CONST[0] + sourceid, source_str)
        ## actions to add source and process source, harded coded action id rely on scanner definition
        c.kv.put(SCANNER_REQUEST_KEY_CONST[0] + scannerid + SCANNER_REQUEST_KEY_CONST[1] + str(self.reqid),
                 json.dumps({'Action': 3, 'UUID': sourceid}, separators=(',', ':')))
        self.reqid += 1
        # action to make a on demand scan
        c.kv.put(SCANNER_REQUEST_KEY_CONST[0] + scannerid + SCANNER_REQUEST_KEY_CONST[1] + str(self.reqid),
                 json.dumps({'Action': 0, 'UUID': sourceid}, separators=(',', ':')))
        self.reqid += 1
        return self.reqid

    def consulkv_get_scanner_hashed(self, consul_ip, consul_port, tabname, colname):

        key = SCANNER_HASHVAL_KEY_CONST[0] + self.hostip + "_" + str(self.port) + "_" + self.dbname
        key += "_" + tabname + "_" + colname
        c = consul.Consul(host=consul_ip, port=consul_port)
        ## Here we need to try to get result first
        res = re.sub("\"", "", re.findall("(?<=\"Hashes\"\:\[\")(.*?)(?=\"\])",
                                          c.kv.get(key)[1]['Value'].decode())[0]).split(",")
        return res

#TODO, move this to unit test for consulscanner_hash.py
if __name__ == "__main__":

    myConsulScannerHash = ConsulScannerHash("mssql", "192.168.7.134", 1433, "SA", "Helios12$", "huaPIITest")
    #myConsulScannerHash.consulkv_put_scanner_source(
    #    "192.168.7.5", 8500,
    #    "mssql_uuid_2", 'mssql_alias', "helios_scanner_uuid", 'mssql_tenant_uuid',
    #    "pii_1st", "uid", "pii_2nd", ["firstname", "lastname", "gender"])
    #myConsulScannerHash.consulkv_put_scanner_source(
    #    "192.168.7.5", 8500,
    #    "mssql_uuid_3", 'mssql_alias', "helios_scanner_uuid",  'mssql_tenant_uuid',
    #    "pii_1st", "uid", "pii_3rd", ["phonenumber", "email"])
    #myConsulScannerHash.consulkv_put_scanner_source(
    #    "192.168.7.5", 8500,
    #    "mssql_uuid_4", 'mssql_alias', "helios_scanner_uuid", 'mssql_tenant_uuid',
    #    "pii_1st", "uid", "pii_4th", ["country", "city", "stateprovince"])
    res = myConsulScannerHash.consulkv_get_scanner_hashed("192.168.7.5", 8500, "pii_2nd", "firstname")
    print(len(res))
    print(type(res))
    print(type(res[0]))
    #print(myConsulScannerHash.consulkv_get_scanner_hashed("192.168.7.5", 8500, "pii_2nd", "firstname"))
    #print(len(myConsulScannerHash.consulkv_get_scanner_hashed("192.168.7.5", 8500, "pii_2nd", "lastname")))
    #print(len(myConsulScannerHash.consulkv_get_scanner_hashed("192.168.7.5", 8500, "pii_2nd", "gender")))
    #print(len(myConsulScannerHash.consulkv_get_scanner_hashed("192.168.7.5", 8500, "pii_3rd", "phonenumber")))
    #print(len(myConsulScannerHash.consulkv_get_scanner_hashed("192.168.7.5", 8500, "pii_3rd", "email")))
    #print(len(myConsulScannerHash.consulkv_get_scanner_hashed("192.168.7.5", 8500, "pii_4th", "country")))
    #print(len(myConsulScannerHash.consulkv_get_scanner_hashed("192.168.7.5", 8500, "pii_4th", "city")))
    #print(len(myConsulScannerHash.consulkv_get_scanner_hashed("192.168.7.5", 8500, "pii_4th", "stateprovince")))
