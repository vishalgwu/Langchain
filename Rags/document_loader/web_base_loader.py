from langchain_community.document_loaders import WebBaseLoader

url="https://www.amazon.com/dp/B0DZDBWM5B?aref=yRQvu2HzY6&aaxitk=3bfc25f94eff14befd3e3b16f0afec54&language=en_US&pd_rd_plhdr=t&smid=ATVPDKIKX0DER&ref=dacx_dp_579788288792070258_582931610648757706&th=1"
loader = WebBaseLoader(url)


docs = loader.load()

print(f"Total documents loaded: {len(docs)}")
print("First 500 characters of the document:")
print(docs[0].page_content)




from langchain_community.document_loaders import WebBaseLoader
import os

# set USER_AGENT to try to bypass bot detection (Amazon might still block you)
os.environ["USER_AGENT"] = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
)

# list of amazon product/store URLs
urls = [
    "https://www.amazon.com/dp/B0DZDBWM5B?aref=yRQvu2HzY6&aaxitk=3bfc25f94eff14befd3e3b16f0afec54&language=en_US&pd_rd_plhdr=t&smid=ATVPDKIKX0DER&ref=dacx_dp_579788288792070258_582931610648757706&th=1",
    "https://en.wikipedia.org/wiki/Samnites",
    "https://en.wikipedia.org/wiki/HMS_Neptune_(1909)",
    "https://en.wikipedia.org/wiki/Rajpur,_Buxar",
    "https://en.wikipedia.org/wiki/Home_Fleet",
    "https://en.wikipedia.org/wiki/Sir_Arthur_Wilson,_3rd_Baronet"
]

# loop through each URL
for url in urls:
    print(f"\n🔗 Loading from: {url}\n")
    loader = WebBaseLoader(url)
    try:
        docs = loader.load()
        print(f"✅ Total documents loaded: {len(docs)}")
        print("First 500 characters of the document:")
        print(docs[0].page_content[:500])  # only preview first 500 chars
    except Exception as e:
        print(f"❌ Error loading {url}: {e}")
