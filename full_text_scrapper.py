# Example usage of Scraper class for full text recollection

from scraper import Scraper
import tqdm
from selenium.webdriver.common.by import By
import pickle
import pandas as pd


class TextScraper(Scraper):
    def get_text(
        self,
        *,
        url="https://ciudadseva.com/texto/abel-y-cain-borges/",
        html_tag="div",
        html_class="text-justify"
    ):
        self.driver.get(url)
        text_metadata = self.driver.find_elements(By.XPATH,
            "//" + html_tag + '[@class="' + "text-center" + '"]'
        )
        metadata = text_metadata[0].text.split("\n")
        metadata_sanit = {
            "title": metadata[0],
            "metadata": metadata[1],
            "author": metadata[2],
        }
        print("- ", metadata_sanit["title"])
        raw_text = self.driver.find_elements(By.XPATH,
            "//" + html_tag + '[@class="' + html_class + '"]'
        )
        if(raw_text == []):
            print(f'No text found for {url}')
            return "", metadata_sanit
        
        content = raw_text[0].text
        sanit_text = content.replace("\n", " ")  # for whole sentence

        return sanit_text, metadata_sanit


def build_text_dataset(*, links_file="./links.txt"):
    results = []
    scr = TextScraper(browser='Chrome')
    with open(links_file, "r") as file:
        links = file.read().split("\n")
    links = links[:-1]
    for link in tqdm.tqdm(links):
        row = {}
        sanit_text, text_metadata = scr.get_text(url=link)
        row["link"] = link
        row["text_metadata"] = text_metadata
        row["text"] = sanit_text
        results.append(row)
    scr.close()
    return results


def run(*, save=True):
    autores = [{
        'author_name': "asturias",
        'url': 'https://ciudadseva.com/autor/miguel-angel-asturias/cuentos/'
    }, {
        'author_name': "aub",
        'url': 'https://ciudadseva.com/autor/max-aub/cuentos/'
    }, {
        'author_name': 'barreto',
        'url': 'https://ciudadseva.com/autor/hector-barreto/cuentos/'
    }, {
        'author_name': 'belaval',
        'url': 'https://ciudadseva.com/autor/emilio-s-belaval/cuentos/'
    }, {
        'author_name': 'benitez_rojo',
        'url': 'https://ciudadseva.com/autor/antonio-benitez-rojo/cuentos/'
    }, {
        'author_name': 'blanco',
        'url': 'https://ciudadseva.com/autor/andres-eloy-blanco/cuentos/'
    }, {
        'author_name': 'caceres',
        'url': 'https://ciudadseva.com/autor/victor-caceres-lara/cuentos/'
    }, {
        'author_name': 'camacho',
        'url': 'https://ciudadseva.com/autor/juan-vicente-camacho/cuentos/'
    }, {
        'author_name': 'cardenal',
        'url': 'https://ciudadseva.com/autor/ernesto-cardenal/cuentos/'
    }, {
        'author_name': 'cardoso',
        'url': 'https://ciudadseva.com/autor/onelio-jorge-cardoso/cuentos/'
    }, {
        'author_name': 'carrasquilla',
        'url': 'https://ciudadseva.com/autor/tomas-carrasquilla/cuentos/'
    }, {
        'author_name': 'castellanos',
        'url': 'https://ciudadseva.com/autor/rosario-castellanos/cuentos/'
    }, {
        'author_name': 'castillo',
        'url': 'https://ciudadseva.com/autor/abelardo-castillo/cuentos/'
    }, {
        'author_name': 'cepeda_samudio',
        'url': 'https://ciudadseva.com/autor/alvaro-cepeda-samudio/cuentos/'
    }, {
        'author_name': 'cerruto',
        'url': 'https://ciudadseva.com/autor/oscar-cerruto/cuentos/'
    }, {
        'author_name': 'coll',
        'url': 'https://ciudadseva.com/autor/pedro-emilio-coll/cuentos/'
    }, {
        'author_name': 'coloane',
        'url': 'https://ciudadseva.com/autor/francisco-coloane/cuentos/'
    }, {
        'author_name': 'congrains',
        'url': 'https://ciudadseva.com/autor/enrique-congrains-martin/cuentos/'
    }, {
        'author_name': 'conti',
        'url': 'https://ciudadseva.com/autor/haroldo-conti/cuentos/'
    }, {
        'author_name': 'd_halmar',
        'url': 'https://ciudadseva.com/autor/augusto-dhalmar/cuentos/'
    }, {
        'author_name': 'dario',
        'url': 'https://ciudadseva.com/autor/ruben-dario/cuentos/'
    }, {
        'author_name': 'denevi',
        'url': 'https://ciudadseva.com/autor/marco-denevi/cuentos/'
    }, {
        'author_name': 'diaz_alfaro',
        'url': 'https://ciudadseva.com/autor/abelardo-diaz-alfaro/cuentos/'
    }, {
        'author_name': 'diaz_grullon',
        'url': 'https://ciudadseva.com/autor/virgilio-diaz-grullon/cuentos/'
    }, {
        'author_name': 'diaz_rodriguez',
        'url': 'https://ciudadseva.com/autor/manuel-diaz-rodriguez/cuentos/'
    }, {
        'author_name': 'diaz_valcarcel',
        'url': 'https://ciudadseva.com/autor/emilio-diaz-valcarcel/cuentos/'
    }, {
        'author_name': 'fonseca',
        'url': 'https://ciudadseva.com/autor/rubem-fonseca/cuentos/'
    }, {
        'author_name': 'fuentes',
        'url': 'https://ciudadseva.com/autor/carlos-fuentes/cuentos/'
    }, {
        'author_name': 'garcia_marquez',
        'url': 'https://ciudadseva.com/autor/gabriel-garcia-marquez/cuentos/'
    }, {
        'author_name': 'garcia_marquez',
        'url': 'https://ciudadseva.com/autor/gabriel-garcia-marquez/cuentos/'
    }, {
        'author_name': 'garmendia_s',
        'url': 'https://ciudadseva.com/autor/salvador-garmendia/cuentos/'
    }, {
        'author_name': 'gomez_valderrama',
        'url': 'https://ciudadseva.com/autor/pedro-gomez-valderrama/cuentos/'
    }, {
        'author_name': 'gonzalez_jl',
        'url': 'https://ciudadseva.com/autor/jose-luis-gonzalez/cuentos/'
    }, {
        'author_name': 'gonzalez_zeledon',
        'url': 'https://ciudadseva.com/autor/manuel-gonzalez-zeledon/cuentos/'
    }, {
        'author_name': 'gorodischer',
        'url': 'https://ciudadseva.com/autor/angelica-gorodischer/cuentos/'
    }, {
        'author_name': 'guimaraes_rosa',
        'url': 'https://ciudadseva.com/autor/joao-guimaraes-rosa/cuentos/'
    }, {
        'author_name': 'gutierrez_cm',
        'url': 'https://ciudadseva.com/autor/carlos-maria-gutierrez/cuentos/'
    }, {
        'author_name': 'gutierrez_najera',
        'url': 'https://ciudadseva.com/autor/manuel-gutierrez-najera/cuentos/'
    }, {
        'author_name': 'guzman_n',
        'url': 'https://ciudadseva.com/autor/nicomedes-guzman/cuentos/'
    }, {
        'author_name': 'guzman_ml',
        'url': 'https://ciudadseva.com/autor/martin-luis-guzman/cuentos/'
    }, {
        'author_name': 'guzman_a',
        'url': 'https://ciudadseva.com/autor/augusto-guzman/cuentos/'
    }, {
        'author_name': 'hernandez_e',
        'url': 'https://ciudadseva.com/autor/efren-hernandez/cuentos/'
    }, {
        'author_name': 'ibarguengoitia',
        'url': 'https://ciudadseva.com/autor/jorge-ibarguengoitia/cuentos/'
    }, {
        'author_name': 'jaymes_freire',
        'url': 'https://ciudadseva.com/autor/ricardo-jaimes-freyre/cuentos/'
    }, {
        'author_name': 'lastarria',
        'url': 'https://ciudadseva.com/autor/jose-victorino-lastarria/cuentos/'
    }, {
        'author_name': 'lopez_portillo_y_rojas',
        'url': 'https://ciudadseva.com/autor/jose-lopez-portillo-y-rojas/cuentos/'
    }, {
        'author_name': 'lugones',
        'url': 'https://ciudadseva.com/autor/leopoldo-lugones/cuentos/'
    }, {
        'author_name': 'machado_de_assis',
        'url': 'https://ciudadseva.com/autor/j-m-machado-de-assis/cuentos/'
    }, {
        'author_name': 'mallea',
        'url': 'https://ciudadseva.com/autor/eduardo-mallea/cuentos/'
    }, {
        'author_name': 'marechal',
        'url': 'https://ciudadseva.com/autor/leopoldo-marechal/cuentos/'
    }, {
        'author_name': 'marqués',
        'url': 'https://ciudadseva.com/autor/rene-marques/cuentos/'
    }, {
        'author_name': 'martinez_moreno',
        'url': 'https://ciudadseva.com/autor/carlos-martinez-moreno/cuentos/'
    }, {
        'author_name': 'menendez_leal',
        'url': 'https://ciudadseva.com/autor/alvaro-menendez-leal/cuentos/'
    }, {
        'author_name': 'mujica_lainez',
        'url': 'https://ciudadseva.com/autor/manuel-mujica-lainez/cuentos/'
    }, {
        'author_name': 'novas_calvo',
        'url': 'https://ciudadseva.com/autor/lino-novas-calvo/cuentos/'
    }, {
        'author_name': 'onetti',
        'url': 'https://ciudadseva.com/autor/juan-carlos-onetti/cuentos/'
    }, {
        'author_name': 'palma',
        'url': 'https://ciudadseva.com/autor/ricardo-palma/cuentos/'
    }, {
        'author_name': 'parra',
        'url': 'https://ciudadseva.com/autor/teresa-de-la-parra/cuentos/'
    }, {
        'author_name': 'payno',
        'url': 'https://ciudadseva.com/autor/manuel-payno/cuentos/'
    }, {
        'author_name': 'pita_rodriguez',
        'url': 'https://ciudadseva.com/autor/felix-pita-rodriguez/cuentos/'
    }, {
        'author_name': 'pocaterra',
        'url': 'https://ciudadseva.com/autor/jose-rafael-pocaterra/cuentos/'
    }, {
        'author_name': 'quiroga',
        'url': 'https://ciudadseva.com/autor/horacio-quiroga/cuentos/'
    }, {
        'author_name': 'revueltas',
        'url': 'https://ciudadseva.com/autor/jose-revueltas/cuentos/'
    }, {
        'author_name': 'roa_bastos',
        'url': 'https://ciudadseva.com/autor/augusto-roa-bastos/cuentos/'
    }, {
        'author_name': 'rojas',
        'url': 'https://ciudadseva.com/autor/manuel-rojas/cuentos/'
    }, {
        'author_name': 'rueda',
        'url': 'https://ciudadseva.com/autor/manuel-rueda/cuentos/'
    }, {
        'author_name': 'sinan',
        'url': 'https://ciudadseva.com/autor/rogelio-sinan/cuentos/'
    }, {
        'author_name': 'soto',
        'url': 'https://ciudadseva.com/autor/pedro-juan-soto/cuentos/'
    }, {
        'author_name': 'tapia_y_rivera',
        'url': 'https://ciudadseva.com/autor/alejandro-tapia-y-rivera/cuentos/'
    }, {
        'author_name': 'tario',
        'url': 'https://ciudadseva.com/autor/francisco-tario/cuentos/'
    }, {
        'author_name': 'tellez',
        'url': 'https://ciudadseva.com/autor/hernando-tellez/cuentos/'
    }, {
        'author_name': 'tizon',
        'url': 'https://ciudadseva.com/autor/hector-tizon/cuentos/'
    }, {
        'author_name': 'uslar_pietri',
        'url': 'https://ciudadseva.com/autor/arturo-uslar-pietri/cuentos/'
    }, {
        'author_name': 'viana',
        'url': 'https://ciudadseva.com/autor/javier-de-viana/cuentos/'
    }, {
        'author_name': 'wilms_montt',
        'url': 'https://ciudadseva.com/autor/teresa-wilms-montt/cuentos/'
    }]
    links_path = "./datasets/links/links_"

    scraper = Scraper(browser='Chrome')
    for autor in autores:
        author_name = autor['author_name']
        url = autor['url']
        print(f'Scraping author {author_name} from {url}...')
        text = scraper.get_links(url=url)
        with open(links_path+author_name+".txt", "w") as f:
            for link in text:
                f.write(link + "\n")
        print("Written links to ",f)

        ds = build_text_dataset(links_file=links_path+author_name+".txt")
        df = pd.DataFrame(ds)
        if save:
            with open("./datasets/"+author_name+"_full_texts.pkl", "wb") as f:
                pickle.dump(df, f)
                print("[INFO] Saved dataset in: ", f)

    scraper.close()


if __name__ == "__main__":
    print(">>>> Building dataset")
    run()
    print(">>>> Bye!")
