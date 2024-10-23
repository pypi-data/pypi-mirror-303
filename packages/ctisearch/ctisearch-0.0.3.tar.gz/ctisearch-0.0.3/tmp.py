import asyncio
from src.ctisearch import UrlscanSearch

async def test():
    import os

    apikey = os.environ.get("URLSCAN_API_KEY")

    async def my_callback(instance, d: dict):
        """My custom callback for processing urlscan.io reports"""
        iocs = []
        print(f"task url: {d['task']['url']}")
        for request_dict in d["data"]["requests"]:
            if (mal_js := request_dict["request"]["request"]["url"]).endswith(".js"):
                iocs.append(mal_js)

        return iocs

    s = UrlscanSearch(
        query="domain:kmsec.uk",
        apikey=apikey,
        get_task_details=True,
        callback=my_callback,
    )

    await s.search()
    print(s.since_date)
    print(
        f"my callback processed {s.resolved} results, and I have gathered {len(s.processed)} iocs:"
    )
    print(("\n").join(f"\t* {ioc}" for ioc in s.processed))

async def test2():
    import os

    apikey = os.environ.get("URLSCAN_API_KEY")

    s = UrlscanSearch(query="page.domain:reddit.com", apikey=apikey, since_date="1729006759000")
    await s.search()


async def test_shodan():
    """an example"""
    import os

    apikey = os.environ.get("SHODAN_API_KEY")

    async def my_callback(instance, d: dict):
        """my custom processor to extract the cobalt strike watermark only"""
        try:
            return d["cobalt_strike_beacon"]["x64"]["watermark"]
        except KeyError:
            return None

    cobalt_strike = ShodanSearch(
        query='product:"Cobalt Strike Beacon"',
        apikey=apikey,
        fields=["cobalt_strike_beacon"],
        callback=my_callback,
    )

    await cobalt_strike.search()

    # count watermarks
    counts = {}
    for watermark in cobalt_strike.processed:
        try:
            counts[watermark] += 1
        except KeyError:
            counts[watermark] = 1
    most_prevalent = max(counts, key=counts.get)
    print(
        f"The most popular Cobalt Strike Watermark is {most_prevalent} with {counts[most_prevalent]} on the internet"
    )

if __name__ == "__main__":
    asyncio.run(test())