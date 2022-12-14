from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests

from core.models import Fixture


class Command(BaseCommand):
    help = 'Load data from wage file'

    def handle(self, *args, **kwargs):
        raise NotImplementedError