const names = [
    "Aurora",
    "Basil",
    "Caspian",
    "Dahlia",
    "Esme",
    "Felix",
    "Giselle",
    "Hugo",
    "Ivy",
    "Jasper",
    "Kira",
    "Leo",
    "Mira",
    "Nico",
    "Ophelia",
    "Phoenix",
    "Quincy",
    "Ruby",
    "Silas",
    "Thea",
    "Ulysses",
    "Violet",
    "Wilder",
    "Xanthe",
    "Yara",
    "Zephyr",
    "Abe Ração",
    "Ace",
    "Adaptoide",
    "Adonis",
    "After Eita",
    "Amortyzador",
    "AnaChe",
    "Aquidisgraça",
    "Armigoonline",
    "ArsenalFunkeiro",
    "Avestruz que te seduz",
    "Badboy",
    "Bam Bam",
    "BatataSozinha",
    "Bear",
    "Beast",
    "Beef",
    "Biggie",
    "Bispo Pelado",
    "Boss",
    "Cabo Nero",
    "Cachorrão",
    "Capa Nera",
    "Catlucia",
    "CertouMiseravi",
    "Cruizcredo",
    "Daddy",
    "Dapra20comer",
    "Davyd Boyeae",
    "DiegoDanger",
    "Dildo Baggins",
    "Elmo",
    "Eilish Rijinha",
    "Erro 504",
    "FeraSokeRuim",
    "Fredo Mercurio",
    "Flamengolol",
    "Gangster",
    "Gasoline",
    "Gironda",
    "Gizmo",
    "Godzilla",
    "Grandpa",
    "Grasshopper",
    "Gustavo da 12",
    "Handsome",
    "Harvard",
    "Hero",
    "Hercules",
    "Hollywood",
    "Hoss",
    "Hunk",
    "Jedi",
    "JovemMistico",
    "Juan Casavelha",
    "Kharne Greylhada",
    "LaggandoD+",
    "LixoDeQualidade",
    "Lord fralda",
    "LucasLucão",
    "Major Morte",
    "Martaonde",
    "Mayhem",
    "Melado de óleo",
    "Melissagata",
    "Metira",
    "MineirodeChernobil",
    "MonkeeFeice",
    "Monster",
    "Morreu antes de ler",
    "Motown",
    "Nemo",
    "NickO Riginal",
    "NinguémJooga",
    "Nu Sertão",
    "Ouro que reluz",
    "Pablo Escovando",
    "Parcyal Mente",
    "Pickle",
    "Pirarucu Seboso",
    "Poker",
    "Pooh",
    "Pops",
    "Prince",
    "Pup",
    "Rockstar",
    "Romeo",
    "SawMasBom",
    "Scooter",
    "Severinnis",
    "Skipper",
    "Sniper Boleto",
    "SóXanaEAgua",
    "Sou1abismo",
    "Sparkie",
    "Superfly",
    "Teddy",
    "Tiger",
    "Tone Yorke",
    "Train",
    "Turtle",
    "Uhpapaichegou",
    "Urso Vago",
    "Vegas",
    "Vinho de Diezel",
    "Wakanda emRuim",
    "Waldo",
    "Winner",
    "Ze Morteiro"
  ];
  
  function generateName() {
    const generatedName = document.getElementById("generated-name");
    const randomIndex = Math.floor(Math.random() * names.length); 
    const randomName = names[randomIndex];
    generatedName.textContent = randomName;
  }
