# pooling mod
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tgb.settings')
django.setup()

from tgBot.pooling import start_pooling

if __name__ == '__main__':
    # start pooling
    start_pooling()
