# Load depedencies and set up env

library(tidyverse)
library(charlatan)
library(generator)
library(jsonlite)

sample_size <- 10
set.seed(42)

# Produce bespoke fake data to simulate API data

# Messages data -----------------------
## intended for the db.prepoc_messages table

geboorteplaats_opties <- c("Den Haag", "Rotterdam", "Enschede", "Franeker", "Athene", "Buenos Aires", "Berlijn", "Syracuse", "Kampala", "Mumbai")
geboorteland_opties <- c("Nederland", "Griekenland", "Argentinië", "Duitsland", "Italië", "Uganda", "India")
gemeenten_opties1 <- c("Den Haag", "Utrecht", "Maastricht", "Valkenburg", "Lisse", "Losser", "Oldenzaal", "Eindhoven")
gemeenten_opties2 <- c("Den Bosch", "Vianen", "Apeldoorn", "Middelburg", "Otterlo", "Dirksland", "Leiden", "Groningen", "Alphen a/d Rijn")
nationaliteiten_opties1 <- c("Nederlandse", "Deense", "Japanse", "Argentijnse", "Duitse")
nationaliteiten_opties2 <- c("Griekse", "Braziliaanse", "Italiaanse", "Ugandese", "Indiaase", NA_character_, NA_character_, NA_character_, NA_character_, NA_character_)
geslacht_opties <- c("M", "V")
recipient_opties <- c("A", "B")

fake_brp_messages <- tibble::tibble(
    id = seq(sample_size),
    aNummer = as.character(seq(sample_size)),
    bsn = r_national_identification_numbers(sample_size), 
    naam = ch_name(n = sample_size, locale = "nl_NL"),
    telefoon = ch_phone_number(n = sample_size, locale = "nl_NL"),
    geboorteDatum = r_date_of_births(sample_size),
    geboortePlaats = sample(geboorteplaats_opties, size = sample_size, replace = T),
    geboorteLand = sample(geboorteland_opties, size = sample_size, replace = T),
    geslachtsaanduiding = sample(geslacht_opties, size = sample_size, replace = T),
    nationaliteit1 = sample(nationaliteiten_opties1, size = sample_size, replace = T),
    nationaliteit2 = sample(nationaliteiten_opties2, size = sample_size, replace = T), 
    huidigePostcode = str_c(
        sample(1:9, sample_size, replace = TRUE),
        sample(1:9, sample_size, replace = TRUE),
        sample(1:9, sample_size, replace = TRUE),
        sample(1:9, sample_size, replace = TRUE),
        sample(LETTERS, sample_size, replace = TRUE),
        sample(LETTERS, sample_size, replace = TRUE),
        sep = ""
    ), 
    huidigeHuisnummer = sample(1:999, size = sample_size, replace = T),
    huidigeWoonplaats = sample(gemeenten_opties1, size = sample_size, replace = T),
    huidigeAdresGeldig = r_date_of_births(sample_size),
    vorigePostcode = str_c(
      sample(1:9, sample_size, replace = TRUE),
      sample(1:9, sample_size, replace = TRUE),
      sample(1:9, sample_size, replace = TRUE),
      sample(1:9, sample_size, replace = TRUE),
      sample(LETTERS, sample_size, replace = TRUE),
      sample(LETTERS, sample_size, replace = TRUE),
      sep = ""
    ), 
    vorigeHuisnummer = sample(1:999, size = sample_size, replace = T),
    vorigeWoonplaats = sample(gemeenten_opties2, size = sample_size, replace = T),
    vorigeAdresGeldig = r_date_of_births(sample_size),
    volgnummer = 1
)


fake_brp_messages_nested <- fake_brp_messages |> 
  group_by(aNummer, naam, recipientId) |> 
  nest(
    recipient = recipientId,
    persoon = c(bsn, naam, geboortePlaats, geboorteLand, geboorteDatum, geslachtsaanduiding, telefoon),
    huidigeAdres = c(huidigePostcode, huidigeHuisnummer, huidigeWoonplaats, huidigeAdresGeldig),
    vorigeAdres = c(vorigePostcode, vorigeHuisnummer, vorigeWoonplaats, vorigeAdresGeldig),
    nationaliteit = c(nationaliteit1, nationaliteit2)
  ) |> 
  nest(
    verblijfplaats = c(huidigeAdres, vorigeAdres)
  ) |> 
  group_split(id, .keep = T)

# Convert to JSON
fake_brp_messages_json <- map(
  .x = fake_brp_messages_nested, 
  .f = \(x) as.character(toJSON(x, dataframe = "rows", pretty = T))
) |> 
  enframe() |>
  transmute(
    id = name,
    messageId = letters[1:10],
    message = as.character(value),
    recipientId = sample(recipient_opties, sample_size, replace = T)
  )

# Check fake brp data
glimpse(fake_brp_messages_json)

#write_csv(fake_brp_messages_json, here::here("prepoc", "fake_brp_message_data.csv"))

# Make meta data table -----------------------


messageSize = sample(x = 15:30000, size = 10, replace = T)

fake_brp_summary_data <- fake_brp_messages_json |> 
  select(1, 2) |> 
  mutate(
    generationDate = r_date_of_births(n = 10, end = as.Date("2023-12-01"), start = as.Date("2023-07-01")),
    endpoint = sample(x = c("/messages/", "/summaryMessages/"), size = 10, replace = T),
    callMethods = sample(x = c("GET", "PUT", "POST"), size = 10, replace = T),
    messageSize = gdata::humanReadable(messageSize, units = "bytes"),
    senderId = sample(x = LETTERS[1:2], size = 10, replace = T),
    recipientId = if_else(senderId == "A", "B", "A"),
    callResponseTimeMs = sample(x = 1.1:3.4, size = 10, replace = T), 
    callResponse = sample(x = c("401 UNAUTHORIZED", "200 OK", "400 BAD REQUEST", "201 CREATED", "404 NOT FOUND", "500 INTERNAL SERVER ERROR"), size = 10, replace = T)
  )

glimpse(fake_brp_summary_data)

#write_csv(fake_brp_summary_data, here::here("prepoc", "fake_brp_summary_data.csv"))
