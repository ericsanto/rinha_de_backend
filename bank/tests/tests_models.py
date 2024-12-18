from django.test import TestCase
from bank.models import Bank


class BankModelTestCase(TestCase):

    def setUp(self) -> None:
        
        self.bank = Bank.objects.create(
                name = "Banco do Brasil",
                bank_code = "1"
                )


    def test_str_return(self):
        self.assertEqual(str(self.bank), "Banco do Brasil")
