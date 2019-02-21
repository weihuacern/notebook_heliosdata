from collections import defaultdict
from datetime import datetime, timedelta
import json
import time

import consul

from common.log import FUZZY, EXCEPT
from ddn_req_base import DdnState, DdnReq
from frontend.demo.demo_constants import TEST_QUERIERS_FAKE
from utils.utils import local_2_utctimestamp, except_handler_wrapper

#4 states for this state machine
class PIIFLInit(DdnState):
    pass

class ProcessPIIFL(DdnState):
    pass

class WaitForScanCompleted(DdnState):
    TIMEOUT = 600

    @staticmethod
    def get_state_timeout():
        return WaitForScanCompleted.TIMEOUT

class PIIFLCompleted(DdnState):
    pass

#Event condition of the state machine
class Event(object):
    class Timeout(object):
        pass

    class GetPIIInfo(object):
        pass

    class PIIInfoLookup(object):
        pass

    class PIIInfoNeedScan(object):
        pass

    class FailedToGetPIIInfo(object):
        pass

    class NoEntryFound(object):
        pass

    class RefreshPIIState(object):
        pass

    class WaitForScan(object):
        pass

class PIIFLHandler(DdnReq):
    def __init__(self, query_handler, consul_host):
        super(PIIFLHandler, self).__init__()
        self._db = query_handler
        self._start_time = datetime.now() + timedelta(-30)
        self._start_time = local_2_utctimestamp(str(self._start_time).split('.')[0].split(' ')[0] + ' 00:00:00')
        self._current_time = 0
        self._to_be_consume = []
        self._log_state = 'Success'
        self._consul = consul.Consul(host=consul_host)
        #count var, global
        self._hits_total = 0
        self._hits_pii = 0
        self._hits_nopii = 0
        #count var, source
        self._hits_per_form = defaultdict(int)
        self._hits_per_piicol = defaultdict(int)
        #count var, data
        self._hits_per_user = defaultdict(int)
        self._hits_per_querier = defaultdict(defaultdict)
        #dict for the sha1 - file name
        self._fc_sha1_fname = defaultdict(str)
        #name of not none column in the form name
        self._fname_person_colname = defaultdict(defaultdict)

    # here we define the state machine: pre-state -> condition -> action -> post-state, close topo
    def _set_up_state_machine(self):
        state_machine = {
            PIIFLInit: [(Event.GetPIIInfo, self._piifl_query, ProcessPIIFL),
                        (Event.NoEntryFound, None, PIIFLCompleted),
                        (Event.FailedToGetPIIInfo, self._piifl_query_failed, PIIFLCompleted)],
            ProcessPIIFL: [(Event.PIIInfoLookup, self._piifl_entry_lookup, PIIFLCompleted),
                           (Event.PIIInfoNeedScan, self._piifl_entry_trigger_scan, WaitForScanCompleted)],
            WaitForScanCompleted: [(Event.WaitForScan, self._piifl_checkscan, ProcessPIIFL),
                                   (Event.Timeout, self._piifl_scantimetout, PIIFLCompleted)],
            PIIFLCompleted: []
        }

        self.set_sm_table(state_machine)
        self.init(PIIFLInit)

    # process the fuzzy log that contain the file extraction
    @except_handler_wrapper
    def _fuzzy_extract_process(self, filename, parent):
        if parent and len(parent):
            self._fc_sha1_fname[parent] = filename

    # this is a function to revert the dictionary
    @except_handler_wrapper
    def _person_colname_dict(self, colhash):
        person_colname_dict = defaultdict(list)
        colname_person_dict = json.loads(colhash)
        for colname in colname_person_dict.keys():
            person_dict = colname_person_dict[colname]
            for person in person_dict.keys():
                #FIXME
                # this is the nan md5 hashed value! how to avoid hard coded???
                if person_dict[person] != "06d5345e23a9051a02d86ddd22345998":
                #if person_dict[person] != "a3d2de7675556553a5f08e4c88d2c228":
                    person_colname_dict[person].append(colname)
        return person_colname_dict

    # process the fuzzy log that contain the hash of all columns contents
    @except_handler_wrapper
    def _fuzzy_content_process(self, filename, colhash):
        if filename and len(filename):
            person_colname_dict = self._person_colname_dict(colhash)
            self._fname_person_colname[filename] = person_colname_dict

    @except_handler_wrapper
    def _file_entry_process(self, sha1, tx_hosts, rx_hosts):
        if sha1 not in self._fc_sha1_fname.keys():
            self._hits_nopii += 1
            return None

        self._hits_total += 1
        filename = self._fc_sha1_fname[sha1]
        if filename not in self._fname_person_colname.keys():
            return None

        self._hits_pii += 1
        self._hits_per_form[filename] += 1
        for person in self._fname_person_colname[filename].keys():
            #per user
            uid = filename + "_" + person
            self._hits_per_user[uid] += 1
            colnames = self._fname_person_colname[filename][person]
            for colname in colnames:
                self._hits_per_piicol[colname] += 1
            #per querier, rx_hosts
            for q in rx_hosts: #should be only 1 element
                if q in self._hits_per_querier.keys():
                    if uid in self._hits_per_querier[q].keys():
                        self._hits_per_querier[q][uid] += 1
                    else:
                        self._hits_per_querier[q][uid] = 1
                else:
                    self._hits_per_querier[q]["fullname"] = TEST_QUERIERS_FAKE[q]["fullname"]
                    self._hits_per_querier[q]["type"] = "Form HTTP Req"
                    self._hits_per_querier[q][uid] = 1

        return None

    #Here we define the actions, some are still empty, need to be filled
    #PIIFLInit -> ProcessPIIFL, Event.GetPIIInfo
    @except_handler_wrapper
    def _piifl_query(self, events, ev_data):
        try:
            self._current_time = local_2_utctimestamp()
            fuzzy_result, file_result = self._db.get_piifl_select(self._start_time, self._current_time)

            if fuzzy_result:
                hits = fuzzy_result.get('hits')
                if hits:
                    all_hits = hits.get('hits')
                    for i in all_hits or []:
                        source = i.get('_source')
                        if source is None:
                            continue
                        #FUZZY("#Here we have fuzzy_result!")
                        #FUZZY(source)
                        #FUZZY(type(source.get('hash')))
                        #FUZZY(source.get('hash'))
                        if 'container' in source.keys():
                            #FUZZY("#Here we have extract log!")
                            #FUZZY(source)
                            self._fuzzy_extract_process(source.get('filename'), source.get('parent'))
                        else:
                            #FUZZY("#Here we have content log!")
                            #FUZZY(source)
                            self._fuzzy_content_process(source.get('filename'), source.get('hash'))

            if file_result:
                hits = file_result.get('hits')
                if hits:
                    all_hits = hits.get('hits')
                    for i in all_hits or []:
                        source = i.get('_source')
                        if source is None:
                            continue
                        #FUZZY("#Here we have file_result!")
                        #FUZZY(source.get('sha1'))
                        #FUZZY(source.get('tx_hosts'))
                        #FUZZY(source.get('rx_hosts'))
                        # sha1 is a string, tx_hosts and rx_hosts are list of string!
                        self._file_entry_process(source.get('sha1'), source.get('tx_hosts'), source.get('rx_hosts'))

            FUZZY(self._fc_sha1_fname.keys())
            FUZZY(self._fname_person_colname.keys())
            #dump json at after each _piifl_query
            stat_input = {
                'total': self._hits_total,
                'pii': self._hits_pii,
                'nopii': self._hits_nopii,
                'per_form': self._hits_per_form,
                'per_piicol': self._hits_per_piicol,
                'per_user': self._hits_per_user,
                'per_querier': self._hits_per_querier
            }
            stat_str = json.dumps(stat_input, indent=4)
            ofname = 'piifl_basic_stat_sample.json'
            with open(ofname, 'w') as outfile:
                outfile.write(stat_str)

            FUZZY("Stat summary after this batch:")
            FUZZY(stat_str)

            self._start_time = local_2_utctimestamp()
            if self._to_be_consume:
                self.throw_event(Event.PIIInfoLookup, None)
                return True
            self.throw_event(Event.NoEntryFound, None)
        except Exception as e:
            EXCEPT(str(e))
            self._log_state = 'Failed to fetch the piifl log(fuzzy log)'
            self.throw_event(Event.FailedToGetPIIInfo, None)
        return True

    #PIIFLInit -> PIIFLCompleted, Event.FailedToGetPIIInfo
    @except_handler_wrapper
    def _piifl_query_failed(self, events, ev_data):
        FUZZY("%s" % self._log_state)
        return True

    #ProcessPIIFL -> PIIFLCompleted, Event.PIIInfoLookup
    @except_handler_wrapper
    def _piifl_entry_lookup(self, event, ev_data):
        return True

    #ProcessPIIFL -> WaitForScanCompleted, Event.PIIInfoNeedScan
    @except_handler_wrapper
    def _piifl_entry_trigger_scan(self, event, ev_data):
        pass

    #WaitForScanCompleted -> ProcessPIIFL, Event.WaitForScan
    @except_handler_wrapper
    def _piifl_checkscan(self, event, ev_data):
        pass

    #WaitForScanCompleted -> PIIFLCompleted, Event.Timeout
    @except_handler_wrapper
    def _piifl_scantimetout(self, event, ev_data):
        pass

    def scan(self):
        while True:
            self.process_event(Event.GetPIIInfo, None)
            self.set_state(PIIFLInit)
            time.sleep(1)
