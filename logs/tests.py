from django.test import TestCase
from .models import Zone, Log, ZoneConnection
from survivors.models import Survivor


class ZoneTest(TestCase):
    def setUp(self) -> None:
        self.instance = Zone.objects.create(name="Resident Evil", is_safe=False)

    def test_model_creation(self):
        new_instance = Zone.objects.create(name="Resident Evil", is_safe=False)
        self.assertEqual(new_instance.name, "Resident Evil")
        self.assertEqual(new_instance.is_safe, False)


class LogTest(TestCase):
    def setUp(self) -> None:
        self.zone = Zone.objects.create(name="Resident Evil", is_safe=False)
        self.survivor = Survivor.objects.create()
        self.instance = Log.objects.create(
            survivor=self.survivor,
            zone=self.zone,
            note="Waling Dead",
            zombie_amount=10,
        )

    def test_model_creation(self):
        new_instance = Log.objects.create(
            survivor=self.survivor,
            zone=self.zone,
            note="Waling Dead",
            zombie_amount=10,
        )
        self.assertEqual(new_instance.survivor, self.survivor)
        self.assertEqual(new_instance.zone, self.zone)
        self.assertEqual(new_instance.note, "Waling Dead")
        self.assertEqual(new_instance.zombie_amount, 10)


class SurvivorTest(TestCase):
    def setUp(self) -> None:
        self.instance = Survivor.objects.create(username="nimamze", password="2181")

    def test_model_creation(self):
        new_instance = Survivor.objects.create(username="emma", password="2181")
        self.assertEqual(new_instance.username, "emma")
        self.assertEqual(new_instance.password, "2181")
        self.assertEqual(new_instance.is_verified, False)
        self.assertEqual(new_instance.need_puzzle, False)


class ZoneConnectionTest(TestCase):
    def setUp(self) -> None:
        self.first_zone = Zone.objects.create(name="Resident Evil 1", is_safe=False)
        self.second_zone = Zone.objects.create(name="Resident Evil 2", is_safe=False)
        self.survivor = Survivor.objects.create()
        self.instance = ZoneConnection.objects.create(
            note="Resident Evil",
            seen_zombie=True,
            survivor=self.survivor,
            from_zone=self.first_zone,
            to_zone=self.second_zone,
        )

    def test_model_creation(self):
        self.third_zone = Zone.objects.create(name="Resident Evil 3", is_safe=False)
        self.forth_zone = Zone.objects.create(name="Resident Evil 4", is_safe=False)
        new_instance = ZoneConnection.objects.create(
            note="Resident Evil",
            seen_zombie=True,
            survivor=self.survivor,
            from_zone=self.third_zone,
            to_zone=self.forth_zone,
        )
        self.assertEqual(new_instance.note, "Resident Evil")
        self.assertEqual(new_instance.seen_zombie, True)
        self.assertEqual(new_instance.survivor, self.survivor)
        self.assertEqual(new_instance.from_zone, self.third_zone)
        self.assertEqual(new_instance.to_zone, self.forth_zone)
