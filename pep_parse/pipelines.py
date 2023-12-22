import csv
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent
NOW_TIME = datetime.strftime(datetime.now(), '%Y-%m-%dT%H-%M-%S')
FILENAME = 'status_summary_' + NOW_TIME + '.csv'


class PepParsePipeline:
    def open_spider(self, spider):
        self.count = {}

    def process_item(self, item, spider):
        status = item['status']
        self.count[status] = (self.count.get(status, 0) + 1)
        return item

    def close_spider(self, spider):
        path = BASE_DIR / 'results'
        with open(path / FILENAME, mode='w', encoding='utf-8') as file:
            csv.writer(file).writerows(
                (
                    ['Статус', 'Колличество'],
                    *self.count.items(),
                    ['Total', sum(self.count.values())]
                )
            )
