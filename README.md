# rdss-archivematica-test-data-corpus

This repository contains a collection of research data files that are used as a data corpus for analyzing and testing the integration of Archivematica into JISC's [Research Data Shared Service ](https://www.jisc.ac.uk/rd/projects/research-data-shared-service).

Only files with open access rights that are posted on public websites are collected. However, errors do occur. If you find a file in this collection that is in violation of a copyright, please [file an issue](https://github.com/artefactual-labs/rdss-archivematica-test-data-corpus/issues), include a link to right holder's information, and it will be deleted.

The test datasets are organized under their [Digital Object Identifier](http://www.doi.org/). 

The `/metadataFiles/` folder contains information about the http requests used to collect the `/sourceFiles/` along with re-formatted or newly generated metadata related to these files.

## Attribution
Additional files created in the course of acquiring and curating this collection are freely available under CC-BY-SA-4.0 license.

```
datacite.identifier: 10.5072/FK2JM29J5Z
datacite.identifierType: DOI
datacite.title: RDSS-Archivematica Test Data corpus
datacite.creator: Peter Van Garderen
datacite.publisher: Artefactual Systems
datacite.publicationYear: 2017
datacite.resourceType: collection
```

## Collection criteria
The following criteria were used to evaluate the dataset files added to this collection:

1. **License and rights**: The corpus files must be in the public domain or be published under a valid re-use license so that they can be freely shared amongst the many collaborators within the RDSS project as well as for the benefit of other interested parties.

2. **Project relevance**:
+ Preference for datasets with a connection to a HEI that is piloting RDSS-Archivematica.
+ Preference for datasets that come from UK HEI research institutions and/or UK funded research.  
+ Preference for datasets that have been exported from RDSS-HEI repository applications and/or with metadata from other integrated systems. **_NOTE_**: As of 18-06-2017 these are not yet known to the *rdss-archivematica team* but likely two or more of: Figshare, Pure, Eprints, Dspace (or localized forks/branches, eg Vivo), Fedora/Hydra (or localized forks/branches, eg Willow), as well as RDM services such as DataCite and ORCID.

3. **RDSS Alpha MVP performance tests**: bitstreams =< 5 GB, files < 1000, file =< 1MB // **_NOTE_**: Github 1GB limit for free public repos. Will need to resolve out links for 20MB?+ files to other storage domain. See https://git-lfs.github.com/

4. **RDSS Beta performance tests**: bitstreams =< 5 TB, files < 1000000, file =< 1TB

5. **Dataset complexity**: Preference is for dataset collections with moderately complex content, context, resource types, media types and file formats. Ideally at least three of the following are present:
+ structured data (eg. csv, delimited text, json, xml, sql, rdf)
+ tabular datasets, statistical datasets, n-dimensional datasets
+ 'science domain' formats (e.g. Matlab, Jupyter, JMOL)
+ geodata and shape files
+ instrument logs
+ 3D models
+ obscure or custom file formats (e.g. .dat)
+ images and diagrams: (e.g. SVG, PNG, TIFF, IIIF)
+ audio-visual recordings (e.g. wav, ogg, mp3, mp4)
+ experiment software (e.g. R scripts, Javascript apps)
+ research notebooks, experiment VMs, custom sandboxes
+ document types (eg. pdf, word, powerpoint)
+ researcher logs/journals
+ analysis outputs: graphs, figures, diagrams, spreadsheets
+ scanned documents, screencaps, and whiteboard snapshots
+ published article(s) with a DOI
+ supplementary material (e.g. algorithms, formulas, codebooks)
+ publisher/reviewer/reader comments
+ access and use statistics

7. **Dataset Packaging**:	At a minimum, one data set that contains a 'simple' package (e.g. a zip or tar file). A 'nice to have' feature would be a package with some standard semantics (e.g. a Bag with a manifest file)

8. **Metadata Quality**:
+ Sample datasets and related articles must have a DOI.
+ Datacite has a mandatory core set of properties that must be provided in order for a dataset to receive a DOI. This is used as the minimum metadata requirement.
+ Preference is for higher quality metadata that includes more detailed technical, administrative, and descriptive information about the dataset creators and its context of creation and use.
+ Preference is for metadata that is serialized (eg. XML, JSON, CSV) and standardized (e.g. Dublin Core, DATS, DCAT, PROV-O) in formats that are equivalent to those used by RDSS HEI pilot institutions in their RDM repositories. **_NOTE_** focus on application-specific metadata exports/APIs? eg Figshare, ePrints, Dspace, Fedora.
+ Preference is for files that include published checksums.
