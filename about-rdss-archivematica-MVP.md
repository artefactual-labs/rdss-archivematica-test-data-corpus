
# About the RDSS Archivematica Minimum Viable Product (MVP)
The RDSS Archivematica MVP release included the objective to map the mandatory Datacite 4.0 properties to the latest version of the JISC Canonical Data Model. The CDM specifies the schema to use for RDSS Messaging API message payloads. It is the RDSS Rosetta Stone through which the containerized vendor products will post and subscribe information related to the provenance, physical control, and intellectual control of the research data that is managed and preserved by JISC's Research Data Shared Service.

Many (if not the majority) of UK HEI-based researchers use a DOI from DataCite when they publish their datasets. Therefore, the mandatory Datacite 4.0 properties are a pragmatic baseline to use for a "minimally viable" research data preservation service.

## RDSS Canonical Data Model crosswalk
[This table] (crosswalk-datacite-jisc_rdss-archivematica_dc.md) contains the crosswalk mapping that was used to determine which CDM properties applied to this task.

## Demonstration of core RDSS-Archivematica functionality
The RDSS-Archivematica MVP product demonstrates:

1. the flow of metadata external to the preservation system (e.g. from DataCite API, from a Figshare repository, from an Islandora repository, from ORCID, from an internal HEI Pure repository, from a customized Dspace repository, from an ePrints repository, etc.)
2. the flow of research dataset transfers from researchers to the RDSS AWS Cloud
3. the Data Producer's metadata normalized to the RDSS CDM,
4. the Data Producer's original files and metadata, mapped and normalized to Archivematica's preservation metadata and file formats,
5. the Data Producer's valuable research data securely stored in a future-aware rdss-achivematica Archival Information Package (AIP) on JISC's AWS Cloud storage and Arkivum's long-term data safeguarding products.

*Note*: There is no functioning RDSS Message Broker component available at the time of the RDSS-Archivematica MVP alpha release. To test and demonstrate the rdss-archivematica alpha release, we created a simple app to simulate the sending of messages compliant with the latest version of the rdss-messaging-api specification. These are serialized as JSON and given the default name `request.json` to match the specification.
