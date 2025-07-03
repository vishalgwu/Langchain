from langchain.text_splitter import CharacterTextSplitter


text = """
This article is about the country. For other uses, see India (disambiguation).
Republic of India
Bhārat Gaṇarājya
Horizontal tricolour flag bearing, from top to bottom, deep saffron, white, and green horizontal bands. In the centre of the white band is a navy-blue wheel with 24 spokes.
Flag

State emblem
Motto: Satyameva Jayate (Sanskrit)
"Truth Alone Triumphs"[1]
Anthem: Jana Gana Mana (Hindi)[a][2][3]
"Thou Art the Ruler of the Minds of All People"[4][2]
Duration: 1 minute and 4 seconds.1:04
National song: Vande Mataram (Sanskrit)[c]
"I Bow to Thee, Mother"[b][1][2]
Duration: 2 minutes and 26 seconds.2:26
Image of a globe centred on India, with India highlighted.
  Territory controlled by India
  Territory claimed but not controlled
Capital	New Delhi
28°36′50″N 77°12′30″E
Largest city by city proper population	Mumbai
Largest city by metropolitan area population	Delhi
Official languages	
HindiEnglish[d][8]
Recognised regional languages	
State level and Eighth Schedule[9]
Native languages	424 languages[g]
Religion (2011)[11]	
79.8% Hinduism
14.2% Islam
2.3% Christianity
1.7% Sikhism
0.7% Buddhism
0.4% Jainism
0.23% unaffiliated
0.65% other
Demonym(s)	
Indianothers
Government	Federal parliamentary republic
• President
Droupadi Murmu
• Prime Minister
Narendra Modi
Legislature	Parliament
• Upper house
Rajya Sabha
• Lower house
Lok Sabha
Independence from the United Kingdom
• Dominion
15 August 1947
• Republic
26 January 1950
Area
• Total
3,287,263 km2 (1,269,219 sq mi)[2][h] (7th)
• Water (%)
9.6
Population
• 2023 estimate
Neutral increase 1,428,627,663[13] (1st)
• 2011 census
Neutral increase 1,210,854,977[14][15] (2nd)
• Density
430.1/km2 (1,114.0/sq mi) (30th)
GDP (PPP)	2025 estimate
• Total
Increase $17.647 trillion[16] (3rd)
• Per capita
Increase $12,132[16] (119th)
GDP (nominal)	2025 estimate
• Total
Increase $4.187 trillion[16] (4th)
• Per capita
Increase $2,878[16] (136th)
Gini (2021)	Positive decrease 32.8[17]
medium inequality
HDI (2023)	Increase 0.685[18]
medium (130th)
Currency	Indian rupee (₹) (INR)
Time zone	UTC+05:30 (IST)
Date format	
dd-mm-yyyy[i]
Calling code	+91
ISO 3166 code	IN
Internet TLD	.in (others)
India, officially the Republic of India,[j][20] is a country in South Asia. It is the seventh-largest country by area; the most populous country since 2023;[21] and, since its independence in 1947, the world's most populous democracy.[22][23][24] Bounded by the Indian Ocean on the south, the Arabian Sea on the southwest, and the Bay of Bengal on the southeast, it shares land borders with Pakistan to the west;[k] China, Nepal, and Bhutan to the north; and Bangladesh and Myanmar to the east. In the Indian Ocean, India is near Sri Lanka and the Maldives; its Andaman and Nicobar Islands share a maritime border with Thailand, Myanmar, and Indonesia.

Modern humans arrived on the Indian subcontinent from Africa no later than 55,000 years ago.[26][27][28] Their long occupation, predominantly in isolation as hunter-gatherers, has made the region highly diverse.[29] Settled life emerged on the subcontinent in the western margins of the Indus river basin 9,000 years ago, evolving gradually into the Indus Valley Civilisation of the third millennium BCE.[30] By 1200 BCE, an archaic form of Sanskrit, an Indo-European language, had diffused into India from the northwest.[31][32] Its hymns recorded the early dawnings of Hinduism in India.[33] India's pre-existing Dravidian languages were supplanted in the northern regions.[34] By 400 BCE, caste had emerged within Hinduism,[35] and Buddhism and Jainism had arisen, proclaiming social orders unlinked to heredity.[36] Early political consolidations gave rise to the loose-knit Maurya and Gupta Empires.[37] Widespread creativity suffused this era,[38] but the status of women declined,[39] and untouchability became an organized belief.[l][40] In South India, the Middle kingdoms exported Dravidian language scripts and religious cultures to the kingdoms of Southeast Asia.[41]

In the early medieval era, Christianity, Islam, Judaism, and Zoroastrianism became established on India's southern and western coasts.[42] Muslim armies from Central Asia intermittently overran India's northern plains in the second millennium.[43] The resulting Delhi Sultanate drew northern India into the cosmopolitan networks of medieval Islam.[44] In south India, the Vijayanagara Empire created a long-lasting composite Hindu culture.[45] In the Punjab, Sikhism emerged, rejecting institutionalised religion.[46] The Mughal Empire ushered in two centuries of economic expansion and relative peace,[47] leaving a rich architectural legacy.[48][49] Gradually expanding rule of the British East India Company turned India into a colonial economy but consolidated its sovereignty.[50] British Crown rule began in 1858. The rights promised to Indians were granted slowly,[51][52] but technological changes were introduced, and modern ideas of education and the public life took root.[53] A nationalist movement emerged in India, the first in the non-European British empire and an influence on other nationalist movements.[54][55] Noted for nonviolent resistance after 1920,[56] it became the primary factor in ending British rule.[57] In 1947, the British Indian Empire was partitioned into two independent dominions,[58][59][60][61] a Hindu-majority dominion of India and a Muslim-majority dominion of Pakistan. A large-scale loss of life and an unprecedented migration accompanied the partition.[62]

India has been a federal republic since 1950, governed through a democratic parliamentary system. It is a pluralistic, multilingual and multi-ethnic society. India's population grew from 361 million in 1951 to over 1.4 billion in 2023.[63] During this time, its nominal per capita income increased from US$64 annually to US$2,601, and its literacy rate from 16.6% to 74%. A comparatively destitute country in 1951,[64] India has become a fast-growing major economy and hub for information technology services; it has an expanding middle class.[65] Indian movies and music increasingly influence global culture.[66] India has reduced its poverty rate, though at the cost of increasing economic inequality.[67] It is a nuclear-weapon state that ranks high in military expenditure. It has disputes over Kashmir with its neighbours, Pakistan and China, unresolved since the mid-20th century.[68] Among the socio-economic challenges India faces are gender inequality, child malnutrition,[69] and rising levels of air pollution.[70] India's land is megadiverse with four biodiversity hotspots.[71] India's wildlife, which has traditionally been viewed with tolerance in its culture,[72] is supported in protected habitats.

Etymology
Main article: Names for India
According to the Oxford English Dictionary (2009), the name "India" is derived from the Classical Latin India, a reference to South Asia and an uncertain region to its east. In turn "India" derived successively from Hellenistic Greek India (Ἰνδία), Ancient Greek Indos (Ἰνδός), Old Persian Hindush (an eastern province of the Achaemenid Empire), and ultimately its cognate, the Sanskrit Sindhu, or 'river'—specifically the Indus River, and by extension its well-settled southern basin.[73][74] The Ancient Greeks referred to the Indians as Indoi, 'the people of the Indus'.[75]

The term Bharat (Bhārat; pronounced [ˈbʱaːɾət] ⓘ), mentioned in both Indian epic poetry and the Constitution of India,[76][77] is used in its variations by many Indian languages. A modern rendering of the historical name Bharatavarsha, which applied originally to North India,[78][79] Bharat gained increased currency from the mid-19th century as a native name for India.[76][80]

Hindustan ([ɦɪndʊˈstaːn] ⓘ) is a Middle Persian name for India that became popular by the 13th century,[81] and was used widely since the era of the Mughal Empire. The meaning of Hindustan has varied, referring to a region encompassing the northern Indian subcontinent (present-day northern India and Pakistan) or to India in its near entirety.[76][80][82]

History
Main articles: History of India and History of the Republic of India
Ancient India

Manuscript illustration, c. 1650, of the Sanskrit epic Ramayana, composed in story-telling fashion c. 400 BCE – c. 300 CE[83]
By 55,000 years ago, the first modern humans, or Homo sapiens, had arrived on the Indian subcontinent from Africa.[26][27][28] The earliest known modern human remains in South Asia date to about 30,000 years ago.[26] After 6500 BCE, evidence for domestication of food crops and animals, construction of permanent structures, and storage of agricultural surplus appeared in Mehrgarh and other sites in Balochistan, Pakistan.[84] These gradually developed into the Indus Valley Civilisation,[85][84] the first urban culture in South Asia,[86] which flourished during 2500–1900 BCE in Pakistan and western India.[87] Centred around cities such as Mohenjo-daro, Harappa, Dholavira, and Kalibangan, and relying on varied forms of subsistence, the civilisation engaged robustly in crafts production and wide-ranging trade.[86]

During the period 2000–500 BCE, many regions of the subcontinent transitioned from the Chalcolithic cultures to the Iron Age ones.[88] The Vedas, the oldest scriptures associated with Hinduism,[89] were composed during this period,[90] and historians have analysed these to posit a Vedic culture in the Punjab region and the upper Gangetic Plain.[88] Most historians also consider this period to have encompassed several waves of Indo-Aryan migration into the subcontinent from the north-west.[89] The caste system, which created a hierarchy of priests, warriors, and free peasants, but which excluded indigenous peoples by labelling their occupations impure, arose during this period.[91] On the Deccan Plateau, archaeological evidence from this period suggests the existence of a chiefdom stage of political organisation.[88] In South India, a progression to sedentary life is indicated by the large number of megalithic monuments dating from this period,[92] as well as by nearby traces of agriculture, irrigation tanks, and craft traditions.[92]


Cave 26 of the rock-cut Ajanta Caves
In the late Vedic period, around the 6th century BCE, the small states and chiefdoms of the Ganges Plain and the north-western regions had consolidated into 16 major oligarchies and monarchies that were known as the mahajanapadas.[93][94] The emerging urbanisation gave rise to non-Vedic religious movements, two of which became independent religions. Jainism came into prominence during the life of its exemplar, Mahavira.[95] Buddhism, based on the teachings of Gautama Buddha, attracted followers from all social classes excepting the middle class; chronicling the life of the Buddha was central to the beginnings of recorded history in India.[96][97][98] In an age of increasing urban wealth, both religions held up renunciation as an ideal,[99] and both established long-lasting monastic traditions. Politically, by the 3rd century BCE, the kingdom of Magadha had annexed or reduced other states to emerge as the Maurya Empire.[100] The empire was once thought to have controlled most of the subcontinent except the far south, but its core regions are now thought to have been separated by large autonomous areas.[101][102] The Mauryan kings are known as much for their empire-building and determined management of public life as for Ashoka's renunciation of militarism and far-flung advocacy of the Buddhist dhamma.[103][104]

The Sangam literature of the Tamil language reveals that, between 200 BCE and 200 CE, the southern peninsula was ruled by the Cheras, the Cholas, and the Pandyas, dynasties that traded extensively with the Roman Empire and with West and Southeast Asia.[105][106] In North India, Hinduism asserted patriarchal control within the family, leading to increased subordination of women.[107][100] By the 4th and 5th centuries, the Gupta Empire had created a complex system of administration and taxation in the greater Ganges Plain; this system became a model for later Indian kingdoms.[108][109] Under the Guptas, a renewed Hinduism based on devotion, rather than the management of ritual, began to assert itself.[110] This renewal was reflected in a flowering of sculpture and architecture, which found patrons among an urban elite.[109] Classical Sanskrit literature flowered as well, and Indian science, astronomy, medicine, and mathematics made significant advances.[109]

Medieval India
Main article: Medieval India

Brihadeshwara temple, Thanjavur, completed in 1010 CE

The Qutub Minar, 73 m (240 ft) tall, completed by the Sultan of Delhi, Iltutmish
The Indian early medieval age, from 600 to 1200 CE, is defined by regional kingdoms and cultural diversity.[111] When Harsha of Kannauj, who ruled much of the Indo-Gangetic Plain from 606 to 647 CE, attempted to expand southwards, he was defeated by the Chalukya ruler of the Deccan.[112] When his successor attempted to expand eastwards, he was defeated by the Pala king of Bengal.[112] When the Chalukyas attempted to expand southwards, they were defeated by the Pallavas from farther south, who in turn were opposed by the Pandyas and the Cholas from still farther south.[112] No ruler of this period was able to create an empire and consistently control lands much beyond their core region.[111] During this time, pastoral peoples, whose land had been cleared to make way for the growing agricultural economy, were accommodated within caste society, as were new non-traditional ruling classes.[113] The caste system consequently began to show regional differences.[113]

In the 6th and 7th centuries, the first devotional hymns were created in the Tamil language.[114] They were imitated all over India and led to both the resurgence of Hinduism and the development of all modern languages of the subcontinent.[114] Indian royalty, big and small, and the temples they patronised drew citizens in great numbers to the capital cities, which became economic hubs as well.[115] Temple towns of various sizes began to appear everywhere as India underwent another urbanisation.[115] By the 8th and 9th centuries, the effects were felt in Southeast Asia, as South Indian culture and political systems were exported to lands that became part of modern-day Myanmar, Thailand, Laos, Brunei, Cambodia, Vietnam, Philippines, Malaysia, and Indonesia.[116] Indian merchants, scholars, and sometimes armies were involved in this transmission; Southeast Asians took the initiative as well, with many sojourning in Indian seminaries and translating Buddhist and Hindu texts into their languages.[116]

After the 10th century, Muslim Central Asian nomadic clans, using swift-horse cavalry and raising vast armies united by ethnicity and religion, repeatedly overran South Asia's north-western plains, leading eventually to the establishment of the Islamic Delhi Sultanate in 1206.[117] The sultanate was to control much of North India and to make many forays into South India. Although at first disruptive for the Indian elites, the sultanate largely left its vast non-Muslim subject population to its own laws and customs.[118][119] By repeatedly repulsing Mongol raiders in the 13th century, the sultanate saved India from the devastation visited on West and Central Asia, setting the scene for centuries of migration of fleeing soldiers, learned men, mystics, traders, artists, and artisans from that region into the subcontinent, thereby creating a syncretic Indo-Islamic culture in the north.[120][121] The sultanate's raiding and weakening of the regional kingdoms of South India paved the way for the indigenous Vijayanagara Empire.[122] Embracing a strong Shaivite tradition and building upon the military technology of the sultanate, the empire came to control much of peninsular India,[123] and was to influence South Indian society for long afterwards.[122]

Early modern India

A distant view of the Taj Mahal from the Agra Fort

A two mohur Company gold coin, issued in 1835, the obverse inscribed "William IIII, King"
In the early 16th century, northern India, then under mainly Muslim rulers,[124] fell again to the superior mobility and firepower of a new generation of Central Asian warriors.[125] The resulting Mughal Empire did not stamp out the local societies it came to rule. Instead, it balanced and pacified them through new administrative practices[126][127] and diverse and inclusive ruling elites,[128] leading to more systematic, centralised, and uniform rule.[129] Eschewing tribal bonds and Islamic identity, especially under Akbar, the Mughals united their far-flung realms through loyalty, expressed through a Persianised culture, to an emperor who had near-divine status.[128] The Mughal state's economic policies, deriving most revenues from agriculture[130] and mandating that taxes be paid in the well-regulated silver currency,[131] caused peasants and artisans to enter larger markets.[129] The relative peace maintained by the empire during much of the 17th century was a factor in India's economic expansion,[129] resulting in greater patronage of painting, literary forms, textiles, and architecture.[132] Newly coherent social groups in northern and western India, such as the Marathas, the Rajputs, and the Sikhs, gained military and governing ambitions during Mughal rule, which, through collaboration or adversity, gave them both recognition and military experience.[133] Expanding commerce during Mughal rule gave rise to new Indian commercial and political elites along the coasts of southern and eastern India.[133] As the empire disintegrated, many among these elites were able to seek and control their own affairs.[134]

By the early 18th century, with the lines between commercial and political dominance being increasingly blurred, a number of European trading companies, including the English East India Company, had established coastal outposts.[135][136] The East India Company's control of the seas, greater resources, and more advanced military training and technology led it to increasingly assert its military strength and caused it to become attractive to a portion of the Indian elite; these factors were crucial in allowing the company to gain control over the Bengal region by 1765 and sideline the other European companies.[137][135][138][139] Its further access to the riches of Bengal and the subsequent increased strength and size of its army enabled it to annex or subdue most of India by the 1820s.[140] India was then no longer exporting manufactured goods as it long had, but was instead supplying the British Empire with raw materials. Many historians consider this to be the onset of India's colonial period.[135] By this time, with its economic power severely curtailed by the British parliament and having effectively been made an arm of British administration, the East India Company began more consciously to enter non-economic arenas, including education, social reform, and culture.[141]

Modern India
Main article: History of India (1947–present)

1909 map of the British Indian Empire

Jawaharlal Nehru sharing a light moment with Mahatma Gandhi, Mumbai, 6 July 1946
Historians consider India's modern age to have begun sometime between 1848 and 1885. The appointment in 1848 of Lord Dalhousie as Governor General of the East India Company set the stage for changes essential to a modern state. These included the consolidation and demarcation of sovereignty, the surveillance of the population, and the education of citizens. Technological changes—among them, railways, canals, and the telegraph—were introduced not long after their introduction in Europe.[142][143][144][145] However, disaffection with the company also grew during this time and set off the Indian Rebellion of 1857. Fed by diverse resentments and perceptions, including invasive British-style social reforms, harsh land taxes, and summary treatment of some rich landowners and princes, the rebellion rocked many regions of northern and central India and shook the foundations of Company rule.[146][147] Although the rebellion was suppressed by 1858, it led to the dissolution of the East India Company and the direct administration of India by the British government. Proclaiming a unitary state and a gradual but limited British-style parliamentary system, the new rulers also protected princes and landed gentry as a feudal safeguard against future unrest.[148][149] In the decades following, public life gradually emerged all over India, leading eventually to the founding of the Indian National Congress in 1885.[150][151][152][153]

The rush of technology and the commercialisation of agriculture in the second half of the 19th century was marked by economic setbacks, and many small farmers became dependent on the whims of far-away markets.[154] There was an increase in the number of large-scale famines,[155] and, despite the risks of infrastructure development borne by Indian taxpayers, little industrial employment was generated for Indians.[156] There were also salutary effects: commercial cropping, especially in the newly canalled Punjab, led to increased food production for internal consumption.[157] The railway network provided critical famine relief,[158] notably reduced the cost of moving goods,[158] and helped nascent Indian-owned industry.[157]

After World War I, in which approximately one million Indians served,[159] a new period began. It was marked by British reforms but also repressive legislation, by more strident Indian calls for self-rule, and by the beginnings of a nonviolent movement of non-co-operation, of which Mahatma Gandhi would become the leader and enduring symbol.[160] During the 1930s, slow legislative reform was enacted by the British; the Indian National Congress won victories in the resulting elections.[161] The next decade was beset with crises: Indian participation in World War II, the Congress's final push for non-co-operation, and an upsurge of Muslim nationalism. All were capped by the advent of independence in 1947, but tempered by the partition of India into two states: India and Pakistan.[162]

Vital to India's self-image as an independent nation was its constitution, completed in 1950, which put in place a secular and democratic republic.[163] Economic liberalisation, which began in the 1980s and the collaboration with Soviet Union for technical know-how,[164] has created a large urban middle class, transformed India into one of the world's fastest-growing economies,[165] and increased its geopolitical status. Yet, India is also shaped by seemingly unyielding poverty, both rural and urban;[166] by religious and caste-related violence;[167] by Maoist-inspired Naxalite insurgencies;[168] and by separatism in Jammu and Kashmir and in Northeast India.[169] It has unresolved territorial disputes with China and with Pakistan.[170] India's sustained democratic freedoms are unique among the world's newer nations; however, in spite of its recent economic successes, freedom from want for its disadvantaged population remains a goal yet to be achieved.[171]

Geography
Main article: Geography of India

The Tungabhadra, with rocky outcrops, flows into the peninsular Krishna River[172]

Fishing boats lashed together in a tidal creek in Anjarle village, Maharashtra
India accounts for the bulk of the Indian subcontinent, lying atop the Indian tectonic plate, a part of the Indo-Australian Plate.[173] India's defining geological processes began 75 million years ago when the Indian Plate, then part of the southern supercontinent Gondwana, began a north-eastward drift caused by seafloor spreading to its south-west, and later, south and south-east.[173] Simultaneously, the vast Tethyan oceanic crust, to its northeast, began to subduct under the Eurasian Plate.[173] These dual processes, driven by convection in the Earth's mantle, both created the Indian Ocean and caused the Indian continental crust eventually to under-thrust Eurasia and to uplift the Himalayas.[173] Immediately south of the emerging Himalayas, plate movement created a vast crescent-shaped trough that rapidly filled with river-borne sediment[174] and now constitutes the Indo-Gangetic Plain.[175] The original Indian plate makes its first appearance above the sediment in the ancient Aravalli range, which extends from the Delhi Ridge in a southwesterly direction. To the west lies the Thar Desert, the eastern spread of which is checked by the Aravallis.[176][177][178]

The remaining Indian Plate survives as peninsular India, the oldest and geologically most stable part of India. It extends as far north as the Satpura and Vindhya ranges in central India. These parallel chains run from the Arabian Sea coast in Gujarat in the west to the coal-rich Chota Nagpur Plateau in Jharkhand in the east.[179] To the south, the remaining peninsular landmass, the Deccan Plateau, is flanked on the west and east by coastal ranges known as the Western and Eastern Ghats;[180] the plateau contains the country's oldest rock formations, some over one billion years old. Constituted in such fashion, India lies to the north of the equator between 6° 44′ and 35° 30′ north latitude[m] and 68° 7′ and 97° 25′ east longitude.[181]

India's coastline measures 7,517 kilometres (4,700 mi) in length; of this distance, 5,423 kilometres (3,400 mi) belong to peninsular India and 2,094 kilometres (1,300 mi) to the Andaman, Nicobar, and Lakshadweep island chains.[182] According to the Indian naval hydrographic charts, the mainland coastline consists of the following: 43% sandy beaches; 11% rocky shores, including cliffs; and 46% mudflats or marshy shores.[182] Major Himalayan-origin rivers that substantially flow through India include the Ganges and the Brahmaputra, both of which drain into the Bay of Bengal.[183] Important tributaries of the Ganges include the Yamuna and the Kosi; the latter's extremely low gradient, caused by long-term silt deposition, leads to severe floods and course changes.[184][185] Major peninsular rivers, whose steeper gradients prevent their waters from flooding, include the Godavari, the Mahanadi, the Kaveri, and the Krishna, which also drain into the Bay of Bengal;[186] and the Narmada and the Tapti, which drain into the Arabian Sea.[187] Coastal features include the marshy Rann of Kutch of western India and the alluvial Sundarbans delta of eastern India; the latter is shared with Bangladesh.[188] India has two archipelagos: the Lakshadweep, coral atolls off India's south-western coast; and the Andaman and Nicobar Islands, a volcanic chain in the Andaman Sea.[189]

Indian climate is strongly influenced by the Himalayas and the Thar Desert, both of which drive the economically and culturally pivotal summer and winter monsoons.[190] The Himalayas prevent cold Central Asian katabatic winds from blowing in, keeping the bulk of the Indian subcontinent warmer than most locations at similar latitudes.[191][192] The Thar Desert plays a crucial role in attracting the moisture-laden south-west summer monsoon winds that, between June and October, provide the majority of India's rainfall.[190] Four major climatic groupings predominate in India: tropical wet, tropical dry, subtropical humid, and montane.[193] Temperatures in India have risen by 0.7 °C (1.3 °F) between 1901 and 2018.[194] Climate change in India is often thought to be the cause. The retreat of Himalayan glaciers has adversely affected the flow rate of the major Himalayan rivers, including the Ganges and the Brahmaputra.[195] According to some current projections, the number and severity of droughts in India will have markedly increased by the end of the present century.[196]

Biodiversity
Main articles: Forestry in India and Wildlife of India

India has the majority of the world's wild tigers, approximately 3,170 in 2022.[197]

A chital (Axis axis) stag in the Nagarhole National Park in a region covered by a moderately dense[n] forest.

Three of the last Asiatic cheetahs in India were shot dead in 1948 in Surguja district, Madhya Pradesh, Central India by Maharajah Ramanuj Pratap Singh Deo. The young male cheetahs, all from the same litter, were sitting together when they were shot at night.
India is a megadiverse country, a term employed for 17 countries that display high biological diversity and contain many species exclusively indigenous, or endemic, to them.[198] India is the habitat for 8.6% of all mammals, 13.7% of bird species, 7.9% of reptile species, 6% of amphibian species, 12.2% of fish species, and 6.0% of all flowering plant species.[199][200] Fully a third of Indian plant species are endemic.[201] India also contains four of the world's 34 biodiversity hotspots,[71] or regions that display significant habitat loss in the presence of high endemism.[o][202]

India's most dense forests, such as the tropical moist forest of the Andaman Islands, the Western Ghats, and Northeast India, occupy approximately 3% of its land area.[203][204] Moderately dense forest, whose canopy density is between 40% and 70%, occupies 9.39% of India's land area.[203][204] It predominates in the temperate coniferous forest of the Himalayas, the moist deciduous sal forest of eastern India, and the dry deciduous teak forest of central and southern India.[205] India has two natural zones of thorn forest, one in the Deccan Plateau, immediately east of the Western Ghats, and the other in the western part of the Indo-Gangetic plain, now turned into rich agricultural land by irrigation, its features no longer visible.[206] Among the Indian subcontinent's notable indigenous trees are the astringent Azadirachta indica, or neem, which is widely used in rural Indian herbal medicine,[207] and the luxuriant Ficus religiosa, or peepul,[208] which is displayed on the ancient seals of Mohenjo-daro,[209] and under which the Buddha is recorded in the Pali canon to have sought enlightenment.[210]

Many Indian species have descended from those of Gondwana, the southern supercontinent from which India separated more than 100 million years ago.[211] India's subsequent collision with Eurasia set off a mass exchange of species. However, volcanism and climatic changes later caused the extinction of many endemic Indian forms.[212] Still later, mammals entered India from Asia through two zoogeographic passes flanking the Himalayas.[213] This had the effect of lowering endemism among India's mammals, which stands at 12.6%, contrasting with 45.8% among reptiles and 55.8% among amphibians.[200] Among endemics are the vulnerable[214] hooded leaf monkey[215] and the threatened Beddome's toad[216][217] of the Western Ghats.

India contains 172 IUCN-designated threatened animal species, or 2.9% of endangered forms.[218] These include the endangered Bengal tiger and the Ganges river dolphin. Critically endangered species include the gharial, a crocodilian; the great Indian bustard; and the Indian white-rumped vulture, which has become nearly extinct by having ingested the carrion of diclofenac-treated cattle.[219] Before they were extensively used for agriculture and cleared for human settlement, the thorn forests of Punjab were mingled at intervals with open grasslands that were grazed by large herds of blackbuck preyed on by the Asiatic cheetah; the blackbuck, no longer extant in Punjab, is now severely endangered in India, and the cheetah is extinct.[220] The pervasive and ecologically devastating human encroachment of recent decades has critically endangered Indian wildlife. In response, the system of national parks and protected areas, first established in 1935, was expanded substantially. In 1972, India enacted the Wildlife Protection Act[221] and Project Tiger to safeguard crucial wilderness; the Forest Conservation Act was enacted in 1980 and amendments added in 1988.[222] India hosts more than five hundred wildlife sanctuaries and eighteen biosphere reserves,[223] four of which are part of the World Network of Biosphere Reserves; its eighty-nine wetlands are registered under the Ramsar Convention.[224]

Politics and government
Politics
Main article: Politics of India

As part of Janadesh 2007, 25,000 pro–land reform landless people in Madhya Pradesh listen to Rajagopal P. V.[225]

US president Barack Obama addresses the members of the Parliament of India in New Delhi in November 2010.
India is a parliamentary republic with a multi-party system.[226] It has six recognised national parties, including the Indian National Congress (INC) and the Bharatiya Janata Party (BJP), and over 50 regional parties.[227] Congress is considered the ideological centre in Indian political culture,[228] whereas the BJP is right-wing.[229][230][231] From 1950 to the late 1980s, Congress held a majority in the India's parliament. Afterwards, it increasingly shared power with the BJP,[232] as well as with powerful regional parties, which forced multi-party coalition governments at the centre.[233]

In the Republic of India's general elections in 1951, 1957, and 1962, Congress, led by Jawaharlal Nehru, won easy victories. On Nehru's death in 1964, Lal Bahadur Shastri briefly became prime minister; he was succeeded in 1966, by Nehru's daughter Indira Gandhi, who led the Congress to election victories in 1967 and 1971. Following public discontent with the state of emergency Indira Gandhi had declared in 1975, Congress was voted out of power in 1977; Janata Party, which had opposed the emergency, was voted in. Its government lasted two years; Morarji Desai and Charan Singh served as prime ministers. After Congress was returned to power in 1980, Indira Gandhi was assassinated and succeeded by Rajiv Gandhi, who won easily in the elections later that year. In the 1989 elections a National Front coalition, led by the Janata Dal in alliance with the Left Front, won, lasting just under two years, and V.P. Singh and Chandra Shekhar serving as prime ministers.[234] In the 1991 Indian general election, Congress, as the largest single party, formed a minority government led by P. V. Narasimha Rao.[235]

After the 1996 Indian general election, the BJP formed a government briefly; it was followed by United Front coalitions, which depended on external political support. Two prime ministers served during this period: H.D. Deve Gowda and I.K. Gujral. In 1998, the BJP formed a coalition—the National Democratic Alliance (NDA). Led by Atal Bihari Vajpayee, the NDA became the first non-Congress, coalition government to complete a five-year term.[236] In the 2004 Indian general elections, no party won an absolute majority. Still, the Congress emerged as the largest single party, forming another successful coalition: the United Progressive Alliance (UPA). It had the support of left-leaning parties and MPs who opposed the BJP. The UPA returned to power in the 2009 general election with increased numbers, and it no longer required external support from India's communist parties.[237] Manmohan Singh became the first prime minister since Jawaharlal Nehru in 1957 and 1962 to be re-elected to a consecutive five-year term.[238] In the 2014 general election, the BJP became the first political party since 1984 to win an absolute majority.[239] In the 2019 general election, the BJP regained an absolute majority. In the 2024 general election, a BJP-led NDA coalition formed the government. Narendra Modi, a former chief minister of Gujarat, is serving as the prime minister of India in his third term since May 26, 2014.[240]

Government
Main articles: Government of India and Constitution of India

Rashtrapati Bhavan, the official residence of the President of India, was designed by British architects Edwin Lutyens and Herbert Baker for the Viceroy of India, and constructed between 1911 and 1931 during the British Raj.[241]
India is a federation with a parliamentary system governed under the Constitution of India. Federalism in India defines the power distribution between the union and the states. India's form of government, traditionally described as "quasi-federal" with a strong centre and weak states,[242] has grown increasingly federal since the late 1990s as a result of political, economic, and social changes.[243][244]

The Government of India comprises three branches: the Executive, Legislature, and Judiciary.[245] The President of India is the ceremonial head of state,[246] who is elected indirectly for a five-year term by an electoral college comprising members of national and state legislatures.[247][248] The Prime Minister of India is the head of government and exercises most executive power.[249] Appointed by the president,[250] the prime minister is supported by the party or political alliance with a majority of seats in the lower house of parliament.[249] The executive of the Indian government consists of the president, the vice-president, and the Union Council of Ministers—with the cabinet being its executive committee—headed by the prime minister. Any minister holding a portfolio must be a member of one of the houses of parliament.[246] In the Indian parliamentary system, the executive is subordinate to the legislature; the prime minister and their council are directly responsible to the lower house of the parliament. Civil servants act as permanent executives and all decisions of the executive are implemented by them.[251]

The legislature of India is the bicameral parliament. Operating under a Westminster-style parliamentary system, it comprises an upper house called the Rajya Sabha (Council of States) and a lower house called the Lok Sabha (House of the People).[252] The Rajya Sabha is a permanent body of 245 members who serve staggered six-year terms with elections every 2 years.[253] Most are elected indirectly by the state and union territorial legislatures in numbers proportional to their state's share of the national population.[250] The Lok Sabha's 543 members are elected directly by popular vote among citizens aged at least 18;[254] they represent single-member constituencies for five-year terms.[255] Several seats from each state are reserved for candidates from Scheduled Castes and Scheduled Tribes in proportion to their population within that state.[254]

India has a three-tier unitary independent judiciary[256] comprising the supreme court, headed by the Chief Justice of India, 25 high courts, and a large number of trial courts.[256] The supreme court has original jurisdiction over cases involving fundamental rights and over disputes between states and the centre and has appellate jurisdiction over the high courts.[257] It has the power to both strike down union or state laws which contravene the constitution[258] and invalidate any government action it deems unconstitutional.[259]

Administrative divisions
Main article: Administrative divisions of India
See also: Political integration of India

A clickable map of the 28 states and 8 union territories of India
India is a federal union comprising 28 states and 8 union territories.[12] All states, as well as the union territories of Jammu and Kashmir, Puducherry and the National Capital Territory of Delhi, have elected legislatures and governments following the Westminster system. The remaining five union territories are directly ruled by the central government through appointed administrators. In 1956, under the States Reorganisation Act, states were reorganised on a linguistic basis.[260] There are over a quarter of a million local government bodies at city, town, block, district and village levels.[261]

States
Andhra Pradesh
Arunachal Pradesh
Assam
Bihar
Chhattisgarh
Goa
Gujarat
Haryana
Himachal Pradesh
Jharkhand
Karnataka
Kerala
Madhya Pradesh
Maharashtra
Manipur
Meghalaya
Mizoram
Nagaland
Odisha
Punjab
Rajasthan
Sikkim
Tamil Nadu
Telangana
Tripura
Uttar Pradesh
Uttarakhand
West Bengal
Union territories
Andaman and Nicobar Islands
Chandigarh
Dadra and Nagar Haveli and Daman and Diu
Jammu and Kashmir
Ladakh
Lakshadweep
National Capital Territory of Delhi
Puducherry
Foreign, economic, and strategic relations
Main articles: Foreign relations of India and Indian Armed Forces

During the 1950s and 60s, India played a pivotal role in the Non-Aligned Movement.[262] From left to right: Gamal Abdel Nasser of United Arab Republic (now Egypt), Josip Broz Tito of Yugoslavia and Jawaharlal Nehru in Belgrade, September 1961.
India became a republic in 1950, remaining a member of the Commonwealth of Nations.[263][264] India strongly supported decolonisation in Africa and Asia in the 1950s; it played a leading role in the Non-Aligned Movement.[265] After cordial relations initially, India went to war with China in 1962. It was widely thought to have been humiliated.[266] Another military conflict followed in 1967 in which India successfully repelled a Chinese attack.[267] India has had uneasy relations with its western neighbour, Pakistan. The two countries went to war in 1947, 1965, 1971, and 1999. Three of these wars were fought over the disputed territory of Kashmir. In contrast, the 1971 war followed India's support for the independence of Bangladesh.[268] After the 1965 war with Pakistan, India began to pursue close military and economic ties with the Soviet Union; by the late 1960s, the Soviet Union was its largest arms supplier.[269] India has played a key role in the South Asian Association for Regional Cooperation and the World Trade Organization. The nation has supplied 100,000 military and police personnel in 35 UN peacekeeping operations.


The Indian Air Force contingent marching at the 221st Bastille Day military parade in Paris, on 14 July 2009. The parade at which India was the foreign guest was led by India's oldest regiment, the Maratha Light Infantry, founded in 1768.[270]
China's nuclear test of 1964 and threats to intervene in support of Pakistan in the 1965 war caused India to produce nuclear weapons.[271] India conducted its first nuclear weapons test in 1974 and carried out additional underground testing in 1998. India has signed neither the Comprehensive Nuclear-Test-Ban Treaty nor the Nuclear Non-Proliferation Treaty, considering both to be flawed and discriminatory.[272] India maintains a "no first use" nuclear policy and is developing a nuclear triad capability as a part of its "Minimum Credible Deterrence" doctrine.[273][274]

Since the end of the Cold War, India has increased its economic, strategic, and military cooperation with the United States and the European Union.[275] In 2008, a civilian nuclear agreement was signed between India and the United States. Although India possessed nuclear weapons at the time and was not a party to the Nuclear Non-Proliferation Treaty, it received waivers from the International Atomic Energy Agency and the Nuclear Suppliers Group, ending earlier restrictions on India's nuclear technology and commerce; India subsequently signed co-operation agreements involving civilian nuclear energy with Russia,[276] France,[277] the United Kingdom,[278] and Canada.[279]

The President of India is the supreme commander of the nation's armed forces; with 1.45 million active troops, they compose the world's second-largest military. It comprises the Indian Army, the Indian Navy, the Indian Air Force, and the Indian Coast Guard.[280] The official Indian defence budget for 2011 was US$36.03 billion, or 1.83% of GDP.[281] Defence expenditure was pegged at US$70.12 billion for fiscal year 2022–23 and, increased 9.8% than previous fiscal year.[282][283] India is the world's second-largest arms importer; between 2016 and 2020, it accounted for 9.5% of the total global arms imports.[284] Much of the military expenditure was focused on defence against Pakistan and countering growing Chinese influence in the Indian Ocean.[285]

Economy
Main article: Economy of India

In 2019, 43% of India's total workforce was employed in agriculture.[286]

India is the world's largest producer of milk, with the largest population of cattle. In 2018, nearly 80% of India's milk was sourced from small farms with herd size between one and two, the milk harvested by hand milking.[288]

55% of India's female workforce was employed in agriculture in 2019.[287]
According to the International Monetary Fund (IMF), the Indian economy in 2024 was nominally worth $3.94 trillion; it was the fifth-largest economy by market exchange rates and is, at around $15.0 trillion, the third-largest by purchasing power parity (PPP).[16] With its average annual GDP growth rate of 5.8% over the past two decades, and reaching 6.1% during 2011–2012,[289] India is one of the world's fastest-growing economies.[290] However, due to its low GDP per capita—which ranks 136th in the world in nominal per capita income and 125th in per capita income adjusted for purchasing power parity (PPP)—the vast majority of Indians fall into the low-income group.[291][292] Until 1991, all Indian governments followed protectionist policies that were influenced by socialist economics. Widespread state intervention and regulation largely walled the economy off from the outside world. An acute balance of payments crisis in 1991 forced the nation to liberalise its economy;[293] since then, it has moved increasingly towards a free-market system[294][295] by emphasising both foreign trade and direct investment inflows.[296] India has been a member of World Trade Organization since 1 January 1995.[297]

The 522-million-worker Indian labour force is the world's second largest, as of 2017.[280] The service sector makes up 55.6% of GDP, the industrial sector 26.3% and the agricultural sector 18.1%. India's foreign exchange remittances of US$100 billion in 2022,[298] highest in the world, were contributed to its economy by 32 million Indians working in foreign countries.[299] In 2006, the share of external trade in India's GDP stood at 24%, up from 6% in 1985.[294] In 2008, India's share of world trade was 1.7%;[300] In 2021, India was the world's ninth-largest importer and the sixteenth-largest exporter.[301] Between 2001 and 2011, the contribution of petrochemical and engineering goods to total exports grew from 14% to 42%.[302] India was the world's second-largest textile exporter after China in the 2013 calendar year.[303]

Averaging an economic growth rate of 7.5% for several years before 2007,[294] India has more than doubled its hourly wage rates during the first decade of the 21st century.[304] Some 431 million Indians have left poverty since 1985; India's middle classes are projected to number around 580 million by 2030.[305] In 2023, India's consumer market was the world's fifth largest.[306] India's nominal GDP per capita increased steadily from US$308 in 1991, when economic liberalisation began, to US$1,380 in 2010, to an estimated US$2,731 in 2024. It is expected to grow to US$3,264 by 2026.[16]

Industries

A tea garden in Sikkim. India, the world's second-largest producer of tea, is a nation of one billion tea drinkers, who consume 70% of India's tea output.
The Indian automotive industry, the world's second-fastest growing, increased domestic sales by 26% during 2009–2010,[307] and exports by 36% during 2008–2009.[308] In 2022, India became the world's third-largest vehicle market after China and the United States, surpassing Japan.[309] At the end of 2011, the Indian IT industry employed 2.8 million professionals, generated revenues close to US$100 billion equalling 7.5% of Indian GDP, and contributed 26% of India's merchandise exports.[310]

The pharmaceutical industry in India includes 3,000 pharmaceutical companies and 10,500 manufacturing units; India is the world's third-largest pharmaceutical producer, largest producer of generic medicines and supply up to 50–60% of global vaccines demand, these all contribute up to US$24.44 billions in exports and India's local pharmaceutical market is estimated up to US$42 billion.[311][312] India is among the top 12 biotech destinations in the world.[313][314] The Indian biotech industry grew by 15.1% in 2012–2013, increasing its revenues from ₹204.4 billion (Indian rupees) to ₹235.24 billion (US$3.94 billion at June 2013 exchange rates).[315]

Energy
Main articles: Energy in India and Energy policy of India
India's capacity to generate electrical power is 300 gigawatts, of which 42 gigawatts is renewable.[316] The country's usage of coal is a major cause of greenhouse gas emissions by India but its renewable energy is competing strongly.[317] India emits about 7% of global greenhouse gas emissions. This equates to about 2.5 tons of carbon dioxide per person per year, which is half the world average.[318][319] Increasing access to electricity and clean cooking with liquefied petroleum gas have been priorities for energy in India.[320]

Socio-economic challenges

Health workers about to begin another day of immunisation against infectious diseases in 2006. Eight years later, and three years after India's last case of polio, the World Health Organization declared India to be polio-free.[321]
Despite economic growth during recent decades, India continues to face socio-economic challenges. In 2006, India contained the largest number of people living below the World Bank's international poverty line of US$1.25 per day.[322] The proportion decreased from 60% in 1981 to 42% in 2005.[323] Under the World Bank's later revised poverty line, it was 21%-22.5 in 2011.[p][325][326] In 2019, the estimates had gone down to 10.2%.[326] In 2014, 30.7% of India's children under the age of five were underweight.[327] According to a Food and Agriculture Organization report in 2015, 15% of the population was undernourished.[328][329] The Midday Meal Scheme attempts to lower these rates.[330]

A 2018 Walk Free Foundation report estimated that nearly 8 million people in India were living in different forms of modern slavery, such as bonded labour, child labour, human trafficking, and forced begging.[331] According to the 2011 census, there were 10.1 million child labourers in the country, a decline of 2.6 million from 12.6 million in 2001.[332]

Since 1991, economic inequality between India's states has consistently grown: the per-capita net state domestic product of the richest states in 2007 was 3.2 times that of the poorest.[333] Corruption in India is perceived to have decreased. According to the Corruption Perceptions Index, India ranked 78th out of 180 countries in 2018, an improvement from 85th in 2014.[334][335]

Demographics, languages, and religion
Main articles: Demographics of India, Languages of India, and Religion in India
See also: South Asian ethnic groups

A Sikh pilgrim at the Harmandir Sahib, or Golden Temple, in Amritsar, Punjab

The interior of San Thome Basilica, Chennai, Tamil Nadu. Christianity is believed to have been introduced to India by the late 2nd century by Syriac-speaking Christians.
With an estimated 1,428,627,663 residents in 2023, India is the world's most populous country.[13] 1,210,193,422 residents were reported in the 2011 provisional census report.[336] Its population grew by 17.64% from 2001 to 2011,[337] compared to 21.54% growth in the previous decade (1991–2001).[337] The human sex ratio, according to the 2011 census, is 940 females per 1,000 males.[336] The median age was 28.7 in 2020.[280] The first post-colonial census, conducted in 1951, counted 361 million people.[338] Medical advances made in the last 50 years as well as increased agricultural productivity brought about by the "Green Revolution" have caused India's population to grow rapidly.[339]

The life expectancy in India is at 70 years—71.5 years for women, 68.7 years for men.[280] There are around 93 physicians per 100,000 people.[340] Migration from rural to urban areas has been an important dynamic in India's recent history. The number of people living in urban areas grew by 31.2% between 1991 and 2001.[341] Yet, in 2001, over 70% still lived in rural areas.[342][343] The level of urbanisation increased further from 27.81% in the 2001 Census to 31.16% in the 2011 Census. The slowing down of the overall population growth rate was due to the sharp decline in the growth rate in rural areas since 1991.[344] According to the 2011 census, there are 53 million-plus urban agglomerations in India; among them Mumbai, Delhi, Kolkata, Chennai, Bengaluru, Hyderabad and Ahmedabad, in decreasing order by population.[345] The literacy rate in 2011 was 74.04%: 65.46% among females and 82.14% among males.[346] The rural-urban literacy gap, which was 21.2 percentage points in 2001, dropped to 16.1 percentage points in 2011. The improvement in the rural literacy rate is twice that of urban areas.[344] Kerala is the most literate state with 93.91% literacy; while Bihar the least with 63.82%.[346]

Among speakers of the Indian languages, 74% speak Indo-Aryan languages, the easternmost branch of the Indo-European languages; 24% speak Dravidian languages, indigenous to South Asia and spoken widely before the spread of Indo-Aryan languages and 2% speak Austroasiatic languages or the Sino-Tibetan languages. India has no national language.[347] Hindi, with the largest number of speakers, is the official language of the government.[348][349] English is used extensively in business and administration and has the status of a "subsidiary official language";[6] it is important in education, especially as a medium of higher education. Each state and union territory has one or more official languages, and the constitution recognises in particular 22 "scheduled languages".

The 2011 census reported the religion in India with the largest number of followers was Hinduism (79.80% of the population), followed by Islam (14.23%); the remaining were Christianity (2.30%), Sikhism (1.72%), Buddhism (0.70%), Jainism (0.36%) and others[q] (0.9%).[11] India has the third-largest Muslim population—the largest for a non-Muslim majority country.[350][351]

Culture
Main article: Culture of India
Visual art
Main article: Indian art
India has a very ancient tradition of art, which has exchanged many influences with the rest of Eurasia, especially in the first millennium, when Buddhist art spread with Indian religions to Central, East and Southeast Asia, the last also greatly influenced by Hindu art.[352] Thousands of seals from the Indus Valley Civilization of the third millennium BCE have been found, usually carved with animals, but a few with human figures. The "Pashupati" seal, excavated in Mohenjo-daro, Pakistan, in 1928–29, is the best known.[353][354] After this there is a long period with virtually nothing surviving.[354][355] Almost all surviving ancient Indian art thereafter is in various forms of religious sculpture in durable materials, or coins. There was probably originally far more in wood, which is lost. In north India Mauryan art is the first imperial movement.[356][357][358] In the first millennium CE, Buddhist art spread with Indian religions to Central, East and Southeast Asia, the last also greatly influenced by Hindu art.[359] Over the following centuries a distinctly Indian style of sculpting the human figure developed, with less interest in articulating precise anatomy than ancient Greek sculpture but showing smoothly flowing forms expressing prana ("breath" or life-force).[360][361] This is often complicated by the need to give figures multiple arms or heads, or represent different genders on the left and right of figures, as with the Ardhanarishvara form of Shiva and Parvati.[362][363]

Most of the earliest large sculpture is Buddhist, either excavated from Buddhist stupas such as Sanchi, Sarnath and Amaravati,[364] or is rock cut reliefs at sites such as Ajanta, Karla and Ellora. Hindu and Jain sites appear rather later.[365][366] In spite of this complex mixture of religious traditions, generally, the prevailing artistic style at any time and place has been shared by the major religious groups, and sculptors probably usually served all communities.[367] Gupta art, at its peak c. 300 CE – c. 500 CE, is often regarded as a classical period whose influence lingered for many centuries after; it saw a new dominance of Hindu sculpture, as at the Elephanta Caves.[368][369] Across the north, this became rather stiff and formulaic after c. 800 CE, though rich with finely carved detail in the surrounds of statues.[370] But in the South, under the Pallava and Chola dynasties, sculpture in both stone and bronze had a sustained period of great achievement; the large bronzes with Shiva as Nataraja have become an iconic symbol of India.[371][372]

Ancient painting has only survived at a few sites, of which the crowded scenes of court life in the Ajanta Caves are by far the most important, but it was evidently highly developed, and is mentioned as a courtly accomplishment in Gupta times.[373][374] Painted manuscripts of religious texts survive from Eastern India about the 10th century onwards, most of the earliest being Buddhist and later Jain. No doubt the style of these was used in larger paintings.[375] The Persian-derived Deccan painting, starting just before the Mughal miniature, between them give the first large body of secular painting, with an emphasis on portraits, and the recording of princely pleasures and wars.[376][377] The style spread to Hindu courts, especially among the Rajputs, and developed a variety of styles, with the smaller courts often the most innovative, with figures such as Nihâl Chand and Nainsukh.[378][379] As a market developed among European residents, it was supplied by Company painting by Indian artists with considerable Western influence.[380][381] In the 19th century, cheap Kalighat paintings of gods and everyday life, done on paper, were urban folk art from Calcutta, which later saw the Bengal School of Art, reflecting the art colleges founded by the British, the first movement in modern Indian painting.[382][383]

Bhutesvara Yakshis, Buddhist reliefs from Mathura, 2nd century CE
Bhutesvara Yakshis, Buddhist reliefs from Mathura, 2nd century CE
 
Gupta terracotta relief, Krishna Killing the Horse Demon Keshi, 5th century
Gupta terracotta relief, Krishna Killing the Horse Demon Keshi, 5th century
 
Elephanta Caves, triple-bust (trimurti) of Shiva, 18 feet (5.5 m) tall, c. 550
Elephanta Caves, triple-bust (trimurti) of Shiva, 18 feet (5.5 m) tall, c. 550
 
Chola bronze of Shiva as Nataraja ("Lord of Dance"), Tamil Nadu, 10th or 11th century
Chola bronze of Shiva as Nataraja ("Lord of Dance"), Tamil Nadu, 10th or 11th century
 
Jahangir Receives Prince Khurram at Ajmer on His Return from the Mewar Campaign, Balchand, c. 1635
Jahangir Receives Prince Khurram at Ajmer on His Return from the Mewar Campaign, Balchand, c. 1635
 
Krishna Fluting to the Milkmaids, Kangra painting, 1775–1785
Krishna Fluting to the Milkmaids, Kangra painting, 1775–1785
Society

Muslims offer namaz at a mosque in Srinagar, Jammu and Kashmir.
The Indian caste system embodies much of the social stratification and many of the social restrictions found on the Indian subcontinent. Social classes are defined by thousands of endogamous hereditary groups, often termed as jātis, or "castes".[384] India abolished untouchability in 1950 with the adoption of the constitution and has since enacted other anti-discriminatory laws and social welfare initiatives.[r]

Multi-generational patrilineal joint families have been the norm in India, though nuclear families are becoming common in urban areas.[386] An overwhelming majority of Indians have their marriages arranged by their parents or other family elders.[387] Marriage is thought to be for life,[387] and the divorce rate is extremely low,[388] with less than one in a thousand marriages ending in divorce.[389] Child marriages are common, especially in rural areas; many women wed before reaching 18, which is their legal marriageable age.[390] Female infanticide in India, and lately female foeticide, have created skewed gender ratios; the number of missing women in the country quadrupled from 15 million to 63 million in the 50 years ending in 2014, faster than the population growth during the same period.[391] According to an Indian government study, an additional 21 million girls are unwanted and do not receive adequate care.[392] Despite a government ban on sex-selective foeticide, the practice remains commonplace in India, the result of a preference for boys in a patriarchal society.[393] The payment of dowry, although illegal, remains widespread across class lines.[394] Deaths resulting from dowry, mostly from bride burning, are on the rise, despite stringent anti-dowry laws.[395]

Education
Main articles: Education in India, Literacy in India, and History of education in the Indian subcontinent

Children awaiting school lunch in Rayka (also Raika), a village in rural Gujarat. The salutation Jai Bhim written on the blackboard honours the jurist, social reformer, and Dalit leader B. R. Ambedkar.
In the 2011 census, about 73% of the population was literate, with 81% for men and 65% for women. This compares to 1981 when the respective rates were 41%, 53% and 29%. In 1951 the rates were 18%, 27% and 9%. In 1921 the rates 7%, 12% and 2%. In 1891 they were 5%, 9% and 1%,[396][397] According to Latika Chaudhary, in 1911 there were under three primary schools for every ten villages. Statistically, more caste and religious diversity reduced private spending. Primary schools taught literacy, so local diversity limited its growth.[398]

The education system of India is the world's second-largest.[399] India has over 900 universities, 40,000 colleges[400] and 1.5 million schools.[401] In India's higher education system, a significant number of seats are reserved under affirmative action policies for the historically disadvantaged. In recent decades India's improved education system is often cited as one of the main contributors to its economic development.[402][403]

Clothing
Main article: Clothing in India

Women in sari at an adult literacy class in Tamil Nadu

Women (from left to right) in churidars and kameez (with back to the camera), jeans and sweater, and pink shalwar kameez
From ancient times until the advent of the modern, the most widely worn traditional dress in India was draped.[404] For women it took the form of a sari, a single piece of cloth many yards long.[404] The sari was traditionally wrapped around the lower body and the shoulder.[404] In its modern form, it is combined with an underskirt, or Indian petticoat, and tucked in the waist band for more secure fastening. It is also commonly worn with an Indian blouse, or choli, which serves as the primary upper-body garment, the sari's end—passing over the shoulder—covering the midriff and obscuring the upper body's contours.[404] For men, a similar but shorter length of cloth, the dhoti, has served as a lower-body garment.[405]

The use of stitched clothes became widespread after Muslim rule was established at first by the Delhi sultanate (c. 1300 CE) and then continued by the Mughal Empire (c. 1525 CE).[406] Among the garments introduced during this time and still commonly worn are: the shalwars and pyjamas, both styles of trousers, and the tunics kurta and kameez.[406] In southern India, the traditional draped garments were to see much longer continuous use.[406]

Salwars are atypically wide at the waist but narrow to a cuffed bottom. They are held up by a drawstring, which causes them to become pleated around the waist.[407] The pants can be wide and baggy, or they can be cut quite narrow, on the bias, in which case they are called churidars. When they are ordinarily wide at the waist and their bottoms are hemmed but not cuffed, they are called pyjamas. The kameez is a long shirt or tunic,[408] its side seams left open below the waistline.[409] The kurta is traditionally collarless and made of cotton or silk; it is worn plain or with embroidered decoration, such as chikan; and typically falls to either just above or just below the wearer's knees.[410]

In the last 50 years, fashions have changed a great deal in India. Increasingly, in urban northern India, the sari is no longer the apparel of everyday wear, though they remain popular on formal occasions.[411] The traditional shalwar kameez is rarely worn by younger urban women, who favour churidars or jeans.[411] In office settings, ubiquitous air conditioning allows men to wear sports jackets year-round.[411] For weddings and formal occasions, men in the middle and upper classes often wear bandgala, or short Nehru jackets, with pants, with the groom and his groomsmen sporting sherwanis and churidars.[411] The dhoti, once the universal garment of Hindu males, the wearing of which in the homespun and handwoven khadi allowed Gandhi to bring Indian nationalism to the millions,[412] is seldom seen in the cities.[411]

Cuisine
Main article: Indian cuisine

South Indian vegetarian thali, or platter
The foundation of a typical Indian meal is a cereal cooked plainly and complemented with flavourful savoury dishes.[413] The cooked cereal could be steamed rice; chapati, a thin unleavened bread;[414] the idli, a steamed breakfast cake; or dosa, a griddled pancake.[415] The savoury dishes might include lentils, pulses and vegetables commonly spiced with ginger and garlic, but also with a combination of spices that may include coriander, cumin, turmeric, cinnamon, cardamon and others.[413] They might also include poultry, fish, or meat dishes. In some instances, the ingredients may be mixed during the cooking process.[416]

A platter, or thali, used for eating usually has a central place reserved for the cooked cereal, and peripheral ones for the flavourful accompaniments. The cereal and its accompaniments are eaten simultaneously rather than a piecemeal manner. This is accomplished by mixing—for example of rice and lentils—or folding, wrapping, scooping or dipping—such as chapati and cooked vegetables.[413]

Duration: 14 seconds.0:14
A tandoor chef in the Turkman Gate, Old Delhi, makes Khameeri roti (a Muslim-influenced style of leavened bread).[417]
India has distinctive vegetarian cuisines, each a feature of the geographical and cultural histories of its adherents.[418] The appearance of ahimsa, or the avoidance of violence toward all forms of life in many religious orders early in Indian history, especially Upanishadic Hinduism, Buddhism and Jainism, is thought to have contributed to the predominance of vegetarianism among a large segment of India's Hindu population, especially in southern India, Gujarat, the Hindi-speaking belt of north-central India, as well as among Jains.[418] Although meat is eaten widely in India, the proportional consumption of meat in the overall diet is low.[419] Unlike China, which has increased its per capita meat consumption substantially in its years of increased economic growth, in India the strong dietary traditions have contributed to dairy, rather than meat, becoming the preferred form of animal protein consumption.[420]

The most significant import of cooking techniques into India during the last millennium occurred during the Mughal Empire. Dishes such as the pilaf,[421] developed in the Abbasid caliphate,[422] and cooking techniques such as the marinating of meat in yogurt, spread into northern India from regions to its northwest.[423] To the simple yogurt marinade of Persia, onions, garlic, almonds, and spices began to be added in India.[423] Rice was partially cooked and layered alternately with the sauteed meat, the pot sealed tightly, and slow cooked according to another Persian cooking technique, to produce what has today become biryani,[423] a feature of festive dining in many parts of India.[424] In the food served in Indian restaurants worldwide, the diversity of Indian food has been partially concealed by the dominance of Punjabi cuisine. The popularity of tandoori chicken—cooked in the tandoor oven, which had traditionally been used for baking bread in the rural Punjab and the Delhi region, especially among Muslims, but which is originally from Central Asia—dates to the 1950s, and was caused in large part by an entrepreneurial response among people from the Punjab who had been displaced by the 1947 partition.[418]"""



splitter= CharacterTextSplitter(
    chunk_size= 1000,
    chunk_overlap = 0,
    separator=" "
)

result= splitter.split_text(text)

print(result)