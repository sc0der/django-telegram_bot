API_TOKEN = "1864593736:AAGnOmd87-dQWSdVYEEpxpyNGVcik74Ap6k"
host = "http://localhost:8000/"


products_urls = {
    "add_product": host + 'product/add',
    "product_list": host + 'product/all',
    "product":host + 'product/' , # + <product_slug>
    "product_images": host + "product/image/"
}

members_urls = {
    "add_member": host + 'member/add',
    "member_list": host + 'member/all',
}

cart_urls = {
    "cart_add": host + 'cart/add',
    "cart_list": host + 'cart/all',
}

cart_items_urls = {
    "cart_item_add": host + 'cart_item/add',
    "cart_item": host + 'cart_item/', # + <cItem_id>
}

order_urls = {
    "order_add": host + 'order/add',
    "order_list": host + 'order/all' 
}

category_urls = {
    "category_list": host + 'category/all',
    "category": host + 'category/', # + <category_slug>
    "products_by_category": host + 'products/category/' # + <category_slug>
}


character_pages = [
    '*Harry*\nHarry Potter is the Boy Who Lived, the Chosen One, the hero of the Wizarding world. He grew up with Muggles, and then came to Hogwarts where he faced dangers and terrors beyond his years. He, along with his friends Hermione Granger, Ron Weasley and Neville Longbottom, destroyed Voldemort’s Horcruxes. Harry faced Voldemort at the end of a climactic battle in Hogwarts castle and defeated him.',
    '*Dumbledore*\nAlbus Dumbledore was the Headmaster of Hogwarts for close to forty years, a time period that encompassed both of Voldemort’s attempts to take over the Wizarding world. Considered to be the most powerful wizard of his time, Dumbledore was awarded the Order of Merlin, First Class, and was the Supreme Mugwump of the International Confederation of Wizards as well as the Chief Warlock of the Wizengamot.',
    '*Voldemort*\nLord Voldemort, born Tom Marvolo Riddle, was the son of Merope Gaunt (a descendent of Salazar Slytherin) and Tom Riddle, a handsome, wealthy Muggle from Little Hangleton whom Merope ensnared with a love potion. When her husband found out she was a witch, he abandoned her while she was pregnant (HBP10). Tom’s mother died shortly after giving birth to him one December 31, living just long enough to name him Tom Riddle, after his father and Marvolo, after his grandfather.',
    '*Snape*\nSeverus Snape was Potions Master, Defense Against the Dark Arts teacher, and Head of Slytherin at Hogwarts School of Witchcraft and Wizardry; he succeeded Dumbledore as Headmaster. He was personally killed by Lord Voldemort and his snake, Nagini.',
    '*Sirius*\nSirius Black was James Potter’s closest friend, Harry Potter’s godfather, and an Animagus, who was falsely accused of betrayal and murder and imprisoned in Azkaban.',
    '*Hermione*\nResourceful, principled and brilliant, Hermione Jean Granger is easily the brightest witch of her generation. She, along with Ron Weasley, is one of Harry Potter’s closest friends. She is also Muggle-born (her parents were dentists – PS12), and so is a living, breathing example of the fallacy of pureblood wizard supremacy.',
    '*Ron*\nRon Weasley is Harry Potter’s best friend and the youngest son of Molly and Arthur Weasley. The story of Ron’s life is one of being overshadowed by his family and friends, yet it is Ron’s heart and humor that have solidified his friendships and given those around him the support they needed to carry through (BLC). ',
    '*Draco*\nDraco Malfoy is the son and only child of Lucius and Narcissa Malfoy and was a student at Hogwarts in the same year as Harry Potter. He is a rival of Harry, actively trying to undermine him in any way he can. Draco has white-blond hair and a pale, pointed face. He owns an eagle owl which made almost daily deliveries of sweets from home. Draco became the Slytherin Quidditch Seeker after his father made a generous donation of Nimbus 2001 brooms to the team (CS7).',
    '*Hagrid*\nRubeus Hagrid is a half-giant with shaggy hair and a “wild, tangled beard” (PS1) who serves as the Keeper of Keys and Grounds, Gamekeeper, and Care of Magical Creatures professor at Hogwarts (PS4, PA6).',
    '*Dobby*\nDobby was a house-elf, for years indentured to the Malfoy family, until his admiration for Harry Potter goaded him into trying to warn Harry against coming to school in his second year because he knew what Lucius was planning with the diary.',
    '*Moody*\nAlastor “Mad-Eye” Moody is a retired Auror, considered one of the best Dark Wizard catchers the Ministry has ever had.',
]