[Index to this Corpus](index-rdss-archivematica-test-data-corpus.md)

# RDSS-Archivematica Test Data Corpus

## About
This repository contains a collection of research data files that are used as a corpus for analyzing and testing the integration of [Archivematica](https://archivematica.org) into JISC's [Research Data Shared Service](https://www.jisc.ac.uk/rd/projects/research-data-shared-service), beginning with an initial [Minimum Viable Product](about-rdss-mvp.md) release.

The corpus [appraisal criteria](crosswalk-datacite-rdss-am.md) guide new accruals to the collection. Only files with open access rights that are posted on public websites are collected. However, errors do occur. If you find a file in this collection that is in violation of a copyright, please [file an issue](https://github.com/artefactual-labs/rdss-archivematica-test-data-corpus/issues), include a link to right holder's information, and it will be deleted.

## Arrangement
The test datasets are organized under their [Digital Object Identifier](http://www.doi.org/) which has broad adoption within the academic, public, and private research domains to identify and locate canonical versions of research articles and their related datasets.

A [Corpus Index](INDEX.md) is provided as a finding aid to this collection.

Within each test data directory, the `/crawlInfo/` folder contains information about the web crawler settings, URLs, http requests, and http responses that were used to collect the digital resources stored in the `/sourceFiles/` directory.

The `/SIPmetadata/` directory contains re-formatted and newly generated metadata that is used to test a variety of preservation system submission scenarios using the research data source files (where SIP = Submission Information Package).

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
( * ) _Note: Please don't cite this DOI. This is a valid and functioning DOI (see [https://doi.org/10.5072/FK2JM29J5Z](https://doi.org/10.5072/FK2JM29J5Z). However it is a temporary EZID DOI which expires 02-07-2017. It is given here as an attribution illustration. It will be replaced with a permanent DOI. This line will be erased when it does._
