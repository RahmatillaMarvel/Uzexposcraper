from itemadapter import ItemAdapter
import dateparser

class UzexposcraperPipeline:
    def process_item(self, item, spider):


        adapter = ItemAdapter(item)

        creation_date = adapter.get('creation_date')
        if creation_date:
            creation_date = creation_date.replace('\n', '').strip()

            # Sentyabr -> Sentabr
            creation_date = creation_date.replace('Sentyabr', 'Sentabr')

            # Oktyabr -> Oktabr
            creation_date = creation_date.replace('Oktyabr', 'Oktabr')
            
            # I used the dateparser library to parse the date.
            adapter['creation_date'] = creation_date.replace('\n', '').strip()
            parsed_date = dateparser.parse(creation_date, languages=['uz', 'ru', 'en'])
            if parsed_date:
                adapter['creation_date'] = parsed_date.strftime('%Y-%m-%d')
            else:
                print(f"Error parsing date: {creation_date}")

        return item
