"""Owner-only, one-time reset of known installations' 2026-11-23 UTC caption budgets.

Standard library + existing Cloud Shell IAM. Does not reset registration, feedback,
minute limits, replay records, approvals or Groq quotas. No API keys are read.
"""
import hashlib
import json
import re
import subprocess
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime,timezone

DAY='2026-11-23'
PROJECT='yuntai-app'
MARKER='caption_daily_reset_20261123'

class ResetError(Exception):pass

class BudgetReset:
    def __init__(self,request,document_root,clock=time.time):
        self.request,self.root,self.clock=request,document_root,clock
    def check_date(self):
        if datetime.fromtimestamp(self.clock(),timezone.utc).strftime('%Y-%m-%d')!=DAY:
            raise ResetError('This one-time tool is valid only on '+DAY+' UTC. No changes made.')
    def run(self):
        self.check_date()
        marker_path='/yuntai_settings/'+MARKER
        if self.request(marker_path) is not None:
            return {'already_reset':True,'budget_documents_reset':0}
        devices=set();page='';count=0
        while True:
            query='?pageSize=300&mask.fieldPaths=device'
            if page:query+='&pageToken='+urllib.parse.quote(page,safe='')
            result=self.request('/yuntai_sessions'+query)
            for doc in result.get('documents',[]):
                count+=1
                if count>10000:raise ResetError('Too many session records; stopped without resetting.')
                device=doc.get('fields',{}).get('device',{}).get('stringValue','')
                if re.fullmatch(r'[a-f0-9]{64}',device):devices.add(device)
            page=result.get('nextPageToken','')
            if not page:break
        day=int(datetime.strptime(DAY,'%Y-%m-%d').replace(tzinfo=timezone.utc).timestamp()//86400)
        writes=[]
        for scope in ['audio:global']+['audio:'+d for d in sorted(devices)]:
            identifier=hashlib.sha256((str(day)+':'+scope).encode()).hexdigest()
            path='/yuntai_budgets/'+identifier
            doc=self.request(path)
            if doc is None:continue
            if doc.get('name')!=self.root+path or not doc.get('updateTime'):
                raise ResetError('Unexpected budget record; no changes made.')
            used=doc.get('fields',{}).get('used',{}).get('integerValue')
            if used is None or not re.fullmatch(r'[0-9]+',str(used)):
                raise ResetError('Unexpected budget units; no changes made.')
            writes.append({'update':{'name':doc['name'],'fields':{'used':{'integerValue':'0'}}},
                'updateMask':{'fieldPaths':['used']},'currentDocument':{'updateTime':doc['updateTime']}})
        if len(writes)>499:raise ResetError('Too many budget documents for one atomic reset; no changes made.')
        reset_count=len(writes)
        writes.append({'update':{'name':self.root+marker_path,'fields':{
            'utc_day':{'stringValue':DAY},'kind':{'stringValue':'one_time_caption_reset'},
            'reset_documents':{'integerValue':str(reset_count)}}},'currentDocument':{'exists':False}})
        self.check_date()
        # Preconditions prevent erasing concurrent usage; marker and counters commit atomically.
        self.request(':commit',{'writes':writes})
        return {'already_reset':False,'budget_documents_reset':reset_count,'known_installations':len(devices)}

def main():
    try:
        number=subprocess.check_output(['gcloud','projects','describe',PROJECT,'--format=value(projectNumber)'],text=True).strip()
        if number!='605035871673':raise ResetError('Project mismatch; stopped.')
        token=subprocess.check_output(['gcloud','auth','print-access-token'],text=True,stderr=subprocess.DEVNULL).strip()
        root='projects/'+PROJECT+'/databases/(default)/documents'
        def request(path,body=None):
            req=urllib.request.Request('https://firestore.googleapis.com/v1/'+root+path,
                data=json.dumps(body).encode() if body is not None else None,
                headers={'Authorization':'Bearer '+token,'Content-Type':'application/json'})
            try:
                with urllib.request.urlopen(req,timeout=20) as response:
                    raw=response.read(1048577)
                    if len(raw)>1048576:raise ResetError('Response too large; stopped.')
                    return json.loads(raw)
            except urllib.error.HTTPError as error:
                if error.code==404 and body is None:return None
                if error.code in (409,412):raise ResetError('Usage changed concurrently or reset already completed. Pause captions and rerun; no partial reset.') from None
                raise ResetError('Firestore HTTP '+str(error.code)+'. No credentials are printed.') from None
        result=BudgetReset(request,root).run()
        if result['already_reset']:print('Already reset once for '+DAY+' UTC. No further reset performed.')
        else:print('Reset completed for '+DAY+' UTC: '+str(result['budget_documents_reset'])+' daily caption budget records. Existing settings and authorizations retained.')
        print('Minute limits, feedback/registration limits, replay protection and Groq quotas are unchanged.')
    except ResetError as error:raise SystemExit(str(error)) from None
    except Exception:raise SystemExit('Operation could not be confirmed. Rerun to check the one-time marker; no credentials are printed.') from None

if __name__=='__main__':main()
