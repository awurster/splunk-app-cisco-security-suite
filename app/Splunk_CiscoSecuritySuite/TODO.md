Splunk for Cisco Security Suite TODO
====================================

The following items are on the to-do list for the the Splunk for Cisco Security Suite.

Short term TODO
--------------

* normalise field names (with alias if needbe)
    * use CIM
        * dvc, dvc_type (what is product?)
        * src_ and dst_ field names
        * need to get dst_ip from WSA and ESA logs for summarising
    * severity level (how to do this?)

* clean up sourcetyping for cisco sources
    * normalise naming (- vs _ vs :)
    * normalise prefixing
    * remove redundant sourcetype (cisco_ ... _syslog)
    * check sourcetyping for ESA and WSA because of file naming and paths, DNS

* re-establish event typing with standard naming conventions
    * currently all dashboards are done by sourcetype not event type
    * create new 6.x data model for key events (web sec, email sec, firewall, etc)
    
* speed up searches
    * can we use a central base search (cube?) and then refactor dashboards to feed off of the single search?
    
* splunk - please validate i am using github correctly with pushes, pulls, etc 
    * check if i need to cleanup file permissions before syncing up to git.  what are default file perms?

Long term TODO
--------------

* finish cisco security suite dashboards:
    * overview styling.  need to make the front map look more like old google one (see "Cyber Range Welcome")
    * clean up and organise saved searches; consider removing most of them and starting from scratch
    * migrate any leftover dashboards from old to new formats
    * global threat correlation is nice idea, but needs much refactoring
    * IPS analyst needs to be redone and cleaned up.  i dont believe it should be one of the main dashboards though...

* reorganise apps
    * migrate all reports into cisco security suite as dashboards
    * move props/transforms/inputs into individual apps
    * consolidate eventtypes and lookups

* testing / QA
    * try doing some PVT against large numbers of data (i.e. > 10 GB per day of each sourcetype)...
    * can we get a better data gen?
    
* data modeling and integrity checks
    * tune and document ASA messages
    * blacklist ESA events, i.e.:
        * Info: Outbreak Rule: OUTBREAK_0007570 has threat level 3
    * improve form searches... web tracking, client tracking, MAC address, etc

Future Enhancement Ideas
--------------

* styling the new 3.0 app for splunk 6.x capability:
    * restore 2.0 UI banners, branding, etc to dashboard
    * can we move chart colors etc into application.js to be more uniform?
    * custom chart colors - can we allow this from an external stylesheet and/or admin config during install?
    * search UI styling to match app theme... is it in simple and/or advanced XML or do we need custom HTML?
    * same with report results styling... 
    * can we merge charts/modules into the same row?
    * can we allow user to resize horizontal width?  would be nice to have a 80%/20% or so kind of column layout.
    * lots of lost space with the map on front row
    * same for timerange picker...

* LDAP / AD group lookup across all sourcetypes

* integrate with senderbase / cisco security sites for score checking, false positive submissions, etc

* integrate with sourcefire app and sourcetypes

* wireless / cisco prime infrastructure support

* asset management integration / lookup table
    * include cisco contract IDs, serial numbers
    * integrate with support cases?

* how to display complex src / dst from ESA, WSA, etc - i.e. google DDoS maps

