import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

passcard = Passcard.objects.all()


if __name__ == '__main__':
    # Программируем здесь
    print(passcard)  # noqa: T001

