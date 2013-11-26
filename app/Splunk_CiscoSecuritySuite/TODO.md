Splunk for Cisco Security Suite TODO
====================================

The following items are on the to-do list for the the Splunk for Cisco Security Suite.

Urgents
--------------

* normalise field names (with alias if needbe)
    * use CIM
        * dvc, dvc_type (what is product?)
        * src_* and dst_*
        * need to get dst_ip from WSA and ESA logs for summarising
    * severity level (how to do this?)

* clean up and organise saved searches

* clean up sourcetyping for cisco sources
    * normalise naming (- vs _ vs :)
    * normalise prefixing
    * remove redundant (cisco_syslog)
    * check sourcetyping for ESA and WSA because of file naming and paths, DNS



Needs
--------------

* finish cisco security suite dashboards:
    * overview styling
    * pick chart colors

* reogranise apps
    * migrate all reports into cisco security suite as dashboards
    * move props/transforms/inputs into individual apps
    * consolidate eventtypes and lookups

* blacklist ESA events, i.e.:
    * Info: Outbreak Rule: OUTBREAK_0007570 has threat level 3

* tune and document ASA messages


Wants
--------------

* styling the new 3.0 app for splunk 6.x capability:
    * restore 2.0 UI banners, branding, etc to dashboard
    * can we move chart colors etc into application.js to be more uniform?
    * search UI styling in simple and/or advanced XML or do we need custom HTML?
    * same with report results styling... 
    * can we merge charts/modules into the same row?
    * lots of lost space with the map on front row
    * same for timerange picker...

* how to display complex src / dst from ESA, WSA, etc - i.e. google DDoS maps

