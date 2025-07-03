from langchain.text_splitter import RecursiveCharacterTextSplitter


text= """ Space exploration has opened doors to some of humanity’s greatest discoveries, expanding our understanding of the universe far beyond Earth. From the first moon landing to advanced telescopes peering into distant galaxies, these missions have revealed astonishing truths about our solar system and the possibility of life elsewhere. Scientific experiments on the International Space Station, robotic rovers on Mars, and plans for lunar bases all illustrate how far technology and human curiosity have taken us.

Beyond scientific breakthroughs, space exploration also inspires global collaboration and hope. Agencies and private companies work together across borders, sharing knowledge and resources to push the limits of what’s possible. This spirit of cooperation fuels dreams of traveling to Mars or even deeper into space one day. As we invest in new propulsion systems, sustainable life-support technologies, and the ethical challenges of long-term missions, exploring space reminds us of our shared destiny among the stars."""


splitter= RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
    
)


chunk= splitter.split_text(text)

print(len(chunk))

print(chunk)