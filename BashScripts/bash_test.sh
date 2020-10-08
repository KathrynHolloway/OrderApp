#!/bin/bash
#in the BashScripts directory, run bash bash_test.shdocker version
set -eu
timeout=120
retry_delay=1
query_with_timeout () {
        echo "Triggering with timeout"
        curl --retry $timeout --retry-connrefused --retry-delay $retry_delay 'google.com' > /dev/null
}
print_were_online () {
        echo "we're online!"
}
query_with_timeout && print_were_online