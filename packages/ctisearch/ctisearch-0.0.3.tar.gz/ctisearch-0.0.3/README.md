# `ctisearch`

A collection of similar interfaces to Shodan, URLScan, and VirusTotal searches.

> [!WARNING]  
> This is under slow development in my spare time. You may experience bugs or
> breaking changes between versions.

This provides a consistent experience for searching:

* [Shodan search](https://shodan.io/)
* [URLScan search](https://urlscan.io/search/#)
* [VirusTotal intelligence search](https://virustotal.readme.io/reference/intelligence-search)

The motivation for this was to make automation of searches from all three feel
familiar and consistent, as well as provide asynchronous interfaces to Shodan
and URLScan at the same time. The official VirusTotal library is already
asynchronous, so under the hood, this package is a light wrapper around `vt-py`.

