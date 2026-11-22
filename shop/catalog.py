"""Static cake catalog sourced from the supplied product descriptions."""

CAKES = (
    {
        "slug": "chocolate-raspberry-cheesecake",
        "name": "Шоколадно-малиновый чизкейк с ганашем",
        "catalog_title": "Шоколадно-малиновый чизкейк",
        "category": "Чизкейк",
        "image": "images/chocolate-raspberry-cheesecake.jpg",
        "composition": (
            "Песочная основа из темного какао, сливочный сыр (Филадельфия), "
            "бельгийский темный шоколад, свежая малина, малиновый кули, "
            "шоколадный ганаш, сливки 33%."
        ),
        "calories": "385 ккал",
        "proteins": "6.5 г",
        "fats": "26 г",
        "carbs": "32 г",
        "price_piece": "450 ₽",
        "price_full": "3 600 ₽",
        "portion": "8–10 порций",
    },
    {
        "slug": "blueberry-lavender-cake",
        "name": "«Прованс» (чернично-лавандовый муссовый)",
        "catalog_title": "Чернично-лавандовый муссовый торт",
        "category": "Муссовый торт",
        "image": "images/blueberry-lavender-cake.jpg",
        "composition": (
            "Шоколадный бисквит, черничный мусс с веточками лаванды, нежный "
            "ванильный крем-чиз, темный шоколадный велюр, свежая голубика, "
            "зеркальная глазурь."
        ),
        "calories": "310 ккал",
        "proteins": "5.2 г",
        "fats": "18 г",
        "carbs": "33 г",
        "price_piece": "520 ₽",
        "price_full": "4 200 ₽",
        "portion": "8–10 порций",
    },
    {
        "slug": "salted-caramel-snickers",
        "name": "Чизкейк «Соленая карамель» с арахисом",
        "catalog_title": "Соленая карамель со «Сникерсом»",
        "category": "Чизкейк",
        "image": "images/salted-caramel-snickers.jpg",
        "composition": (
            "Основа из песочного печенья, сливочный сыр, соленая карамель, "
            "жареный арахис, кусочки батончика «Сникерс», молочный шоколад, "
            "сливки."
        ),
        "calories": "420 ккал",
        "proteins": "7.0 г",
        "fats": "28 г",
        "carbs": "40 г",
        "price_piece": "480 ₽",
        "price_full": "3 800 ₽",
        "portion": "8–10 порций",
    },
    {
        "slug": "strawberry-cheesecake",
        "name": "Классический чизкейк с земляникой",
        "catalog_title": "Классический земляничный чизкейк",
        "category": "Чизкейк",
        "image": "images/strawberry-cheesecake.jpg",
        "composition": (
            "Песочная основа, сливочный сыр, сливки, яйца, ваниль, "
            "земляничный соус (пюре), свежая клубника."
        ),
        "calories": "330 ккал",
        "proteins": "5.8 г",
        "fats": "22 г",
        "carbs": "25 г",
        "price_piece": "390 ₽",
        "price_full": "3 200 ₽",
        "portion": "8–10 порций",
    },
    {
        "slug": "lime-cheesecake",
        "name": "Лаймовый чизкейк с меренгой",
        "catalog_title": "Лаймовый чизкейк",
        "category": "Чизкейк",
        "image": "images/lime-cheesecake.jpg",
        "composition": (
            "Песочная крошка, сливочный сыр, сок и цедра лайма, сливки, "
            "нежное безе (меренга), лаймовый курд, свежий лайм."
        ),
        "calories": "315 ккал",
        "proteins": "5.5 г",
        "fats": "19 г",
        "carbs": "28 г",
        "price_piece": "420 ₽",
        "price_full": "3 400 ₽",
        "portion": "8–10 порций",
    },
    {
        "slug": "chocolate-marshmallow-roll",
        "name": "Шоколадный рулет с маршмеллоу",
        "catalog_title": "Шоколадный рулет",
        "category": "Рулет",
        "image": "images/chocolate-marshmallow-roll.jpg",
        "composition": (
            "Влажный шоколадный бисквит, сливочный крем с маршмеллоу, "
            "молочный шоколад (декор), шоколадная стружка, дробленый орех."
        ),
        "calories": "360 ккал",
        "proteins": "5.0 г",
        "fats": "21 г",
        "carbs": "38 г",
        "price_piece": "280 ₽",
        "price_full": "1 800 ₽",
        "portion": "6–8 порций",
        "price_note": "Это рулет, поэтому цена за целый ниже.",
    },
    {
        "slug": "red-velvet",
        "name": "«Красный бархат» (Red Velvet)",
        "catalog_title": "Красный бархат",
        "category": "Бисквитный торт",
        "image": "images/red-velvet.jpg",
        "composition": (
            "Бисквит с какао и красным пищевым красителем, крем-чиз на основе "
            "сливочного масла и сливочного сыра, ванильный сахар."
        ),
        "calories": "380 ккал",
        "proteins": "5.5 г",
        "fats": "24 г",
        "carbs": "36 г",
        "price_piece": "400 ₽",
        "price_full": "3 300 ₽",
        "portion": "8–10 порций",
    },
    {
        "slug": "honey-cake-berries",
        "name": "Медовик «Классический» с ягодами",
        "catalog_title": "Медовик с ягодами",
        "category": "Медовик",
        "image": "images/honey-cake-berries.jpg",
        "composition": (
            "Тонкие медовые коржи, сметанный крем, свежая малина, голубика, "
            "мед, мята."
        ),
        "calories": "350 ккал",
        "proteins": "4.8 г",
        "fats": "20 г",
        "carbs": "37 г",
        "price_piece": "350 ₽",
        "price_full": "2 800 ₽",
        "portion": "8–10 порций",
    },
    {
        "slug": "coconut-ice-cream-cake",
        "name": "Кокосовый торт «Пломбир»",
        "catalog_title": "Кокосовый торт с пломбиром",
        "category": "Сливочный торт",
        "image": "images/coconut-ice-cream-cake.jpg",
        "composition": (
            "Ванильный бисквит, крем-пломбир, кокосовая стружка, кокосовый "
            "сироп, свежая клубника (или крем-чиз с кокосом)."
        ),
        "calories": "340 ккал",
        "proteins": "5.2 г",
        "fats": "22 г",
        "carbs": "29 г",
        "price_piece": "380 ₽",
        "price_full": "3 100 ₽",
        "portion": "8–10 порций",
    },
)

CAKE_BY_SLUG = {cake["slug"]: cake for cake in CAKES}
