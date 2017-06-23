# RDSS-Archivematica Test Data Corpus

## Index
This [Index](INDEX.md) provides an overview of the collection contents with links to dataset source files and their SIP metadata.

## About
This repository contains a collection of research data files that are used as a test data corpus for analyzing and testing the integration of [Archivematica](https://archivematica.org) into JISC's [Research Data Shared Service](https://www.jisc.ac.uk/rd/projects/research-data-shared-service) (RDSS), beginning with an initial [Minimum Viable Product](about-rdss-am-MVP.md) release.

New dataset additions to the collection are guided by the corpus [appraisal criteria](crosswalk-datacite-rdss-am.md).

Only files with open access rights that are posted on public websites are collected. However, errors do occur. If you find a file in this collection that is in violation of a copyright, please [file an issue](https://github.com/artefactual-labs/rdss-archivematica-test-data-corpus/issues), include a link to right holder's information, and it will be deleted.

## Arrangement
```
INDEX.md
|-collection
|-- DOI
|--- crawlerInfo
|---- wget-log.txt
|--- SIPmetadata
|---- [last_4_DOI_characters]-SIP1-request.json
|---- [last_4_DOI_characters]-SIP2-request.json
|--- sourceFiles
```

The test datasets are organized under the `/collection/` directory using their [Digital Object Identifier](http://www.doi.org/). DOIs have broad adoption within the academic, public, and private research domains to identify and locate canonical versions of research articles and their related datasets.

An [index](INDEX.md) is provided as a collection finding aid.

Under each `/DOI/` test data directory, the `/crawerlInfo/` sub-directory contains information about the web crawler (WGET) settings, URLs, http requests, and http responses that were used to collect the digital resources stored in the `/sourceFiles/` sub-directory.

The `/SIPmetadata/` sub-directory contains re-formatted and newly generated metadata that is used to test a variety of preservation system submission scenarios using the research data source files and the `request.json` format that is specified by the RDSS Messaging API. *Note: SIP = Submission Information Package in the [ISO-14271 OAIS context](https://en.wikipedia.org/wiki/Open_Archival_Information_System)*.

### Helpers
A human-readable YAML template and yaml-2-json Python scripts are provided as [helpers](/helpers/) to organize and convert harvested metadata to the request.json schema which is used to send message payloads (i.e. metadata) between the JICS RDSS components, including Archivematica.

### Crosswalk
A [metadata crosswalk](crosswalk-datacite-rdss-am.md) is provided to map the movement of metadata values from DataCite properties to the JISC-RDSS Canonical Data Model (CDM) to the Dublin Core properties stored as PREMIS Intellectual Entities in Archivematica's Archival Information Packages (AIP).

## Attribution
This collective work and additional files created in the course of acquiring and curating this collection are freely re-usable under a [CC-BY-SA-4.0](https://creativecommons.org/licenses/by-sa/4.0/legalcode) license.

```
datacite.identifier: 10.5072/FK2JM29J5Z  (*)
datacite.identifierType: DOI
datacite.title: RDSS-Archivematica Test Data corpus
datacite.creator: Peter Van Garderen
datacite.publisher: Artefactual Systems
datacite.publicationYear: 2017
datacite.resourceTypeGeneral: collection
@context: http://schema.datacite.org/meta/kernel-4.0/metadata.xsd
```
( * ) _Please don't cite this particular DOI. This is a currently valid and functioning DOI (see [https://doi.org/10.5072/FK2JM29J5Z](https://doi.org/10.5072/FK2JM29J5Z)). However it is a temporary EZID DOI which expires 02-07-2017. It is given here as an attribution illustration. It will be replaced with a permanent DOI. This note will be erased when it does._
