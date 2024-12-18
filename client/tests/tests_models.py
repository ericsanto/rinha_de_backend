from django.test import TestCase
from client.models import ClientUser
import datetime

class ClientUserTest(TestCase):

    def setUp(self) -> None:
        
        self.user = ClientUser.objects.create(
                first_name = "eric",
                last_name = "santos",
                username = "eric",
                date_of_birth = datetime.date(2002, 4, 12),
                address = "rua dr evandro",
                cpf = "06271954588",
                email = "eric@mail.com"
                )

    def test_str_return_model(self):

        self.assertEqual(str(self.user), "eric santos")
