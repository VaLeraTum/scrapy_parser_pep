import csv
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.count = {}

    def process_item(self, item, spider):
        status = item['status']
        self.count[status] = (self.count.get(status, 0) + 1)
        return item

    def close_spider(self, spider):
        time = datetime.strftime(datetime.now(), '%Y-%m-%dT%H-%M-%S')
        path = BASE_DIR / 'results'
        filename = 'status_summary_' + time + '.csv'
        with open(path / filename, mode='w', encoding='utf-8') as file:
            csv.writer(file).writerows(
                (
                    ['Статус', 'Колличество'],
                    *self.count.items(),
                    ['Total', sum(self.count.values())]
                )
            )
