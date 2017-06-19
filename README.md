# rdss-archivematica-test-data-corpus

This repository contains a collection of research data files that are used as a data corpus for analyzing and testing the integration of Archivematica into JISC's [Research Data Shared Service ](https://www.jisc.ac.uk/rd/projects/research-data-shared-service).

Only files with open access rights are collected but errors do occur. If you find a file in this collection that is in violation of copyright, please [file an issue](https://github.com/artefactual-labs/rdss-archivematica-test-data-corpus/issues), include a link to rights holder information, and it will be deleted.

## Collection criteria
The following criteria were used to evaluate the dataset files added to this collection:

1. **License / Rights**: The corpus files must be in the public domain or valid re-use license so that they can be freely shared amongst the many collaborators within the RDSS project as well as for the benefit of other interested parties.
2. **Project Relevance**:
+ Preference for datasets with a connection to a HEI that is piloting RDSS-Archivematica.
+ Preference for datasets that come from UK HEI research institutions and/or UK funded research.  
+ Preference for datasets that have been exported from RDSS-HEI repository applications and/or with metadata from other integrated systems. **_NOTE_**: As of 18-06-2017 these are not yet known to the *rdss-archivematica team* but likely two or more of: Figshare, Pure, Eprints, Dspace (or localized forks/branches, eg Vivo), Fedora/Hydra (or localized forks/branches, eg Willow), as well as RDM services such as DataCite and ORCID.
3. **RDSS Alpha MVP performance tests**: bitstreams =< 5 GB, files < 1000, file =< 1MB // **_NOTE_**: Github 1GB limit for free public repos. Will need to resolve out links for 20MB?+ files to other storage domain. See https://git-lfs.github.com/
4. **RDSS Beta performance tests**: bitstreams =< 5 TB, files < 1000000, file =< 1TB
5. **Format Types & Variation**: ideally a small number / mix from each of the following types:
+ raw data (json, tabular text etc.);
+ media types (audio, video);
+ document types (pdf, word etc);
+ statistics (Matlab files);
+ science domain formats (e.g. Jupyter notebooks, data for JMOL tool);
+ simple software (e.g. R scripts, Javascript apps)
6. **Dataset Structure**: Ideally we would have at least one dataset collection with moderately complex content, context, and file structures, i.e. some combination of:
+ tabular datasets
+ n-dimensional datasets
+ questionnaires and surveys
+ geodataset and shapefiles
+ 3D models
+ instrument logs
+ audio-visual recordings
+ research notebooks, experiment VMs, custom sandboxes
+ researcher logs/journals
+ analysis outputs: graphs, figures, diagrams, spreadsheets
+ scanned documents, screencaps, and whiteboard snapshots
+ a published article with a DOI
+ supplementary material (e.g. algorithms, formulas, codebooks used)
+ publisher/reviewer/reader comments
+ access and use statistics
7. **Dataset Packaging**:	At a minimum, one data set that contains a 'simple' package (e.g. a zip or tar file). A 'nice to have' feature would be a package with some standard semantics (e.g. a Bag with a manifest file)
8. **Metadata Quality**:
+ Datacite has a mandatory core set of properties that must be provided in order for a dataset to receive a DOI. These are a minimum requirement.
+ Preference is for higher quality metadata that includes more detailed technical, administrative, and descriptive information about the dataset creators and its context of creation and use.
+ Preference is for metadata that is serialized (eg. XML, JSON, CSV) and standardized (e.g. Dublin Core, DATS, DCAT, PROV-O) in formats that are equivalent to those used by RDSS HEI pilot institutions in their RDM repositories. **_NOTE_** focus on application-specific metadata exports/APIs? eg Figshare, ePrints, Dspace, Fedora.
