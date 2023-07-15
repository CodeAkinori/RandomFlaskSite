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
    "Zephyr"
  ];
  
  function generateName() {
    const generatedName = document.getElementById("generated-name");
    const randomIndex = Math.floor(Math.random() * names.length);
    const randomName = names[randomIndex];
    generatedName.textContent = randomName;
  }
  