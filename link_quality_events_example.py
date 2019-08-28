#
# Fetch link quality events for an Edge (consistent with Orchestrator UI usage)
# 
# Usage: VC_USERNAME='user@velocloud.net' VC_PASSWORD=s3cret python link_quality_events_example.py
#

import os
from datetime import datetime, timedelta
from client import *

# EDIT THESE
VCO_HOSTNAME = 'vcoX-usca1.velocloud.net'
ENTERPRISE_ID = 1
EDGE_ID = 1
INTERVAL_START = datetime.now() - timedelta(hours=12)
NUM_SAMPLES = 133

def main():

    client = VcoRequestManager(VCO_HOSTNAME)
    client.authenticate(os.environ['VC_USERNAME'], os.environ['VC_PASSWORD'], is_operator=os.environ.get('VC_OPERATOR', False))

    result = client.call_api('linkQualityEvent/getLinkQualityEvents', {
        "enterpriseId": ENTERPRISE_ID,
        "edgeId": EDGE_ID,
        "interval": {
            "start": INTERVAL_START.isoformat()
        },
        "maxSamples": NUM_SAMPLES
    })

    # `result` is a map where each key is a link `internalId`, values contain link-specific summary
    # QoE scores and a time series of event samples
    print result


if __name__ == '__main__':
    main()
