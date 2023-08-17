from django.test import TestCase,Client
from .models import Menu

class MenuTests(TestCase):
    def setUp(self):
        self.client=Client()

    def test_add_dish(self):
        data = {"dishname": "dal", "price": 100, "available": "yes"}
        resp = self.client.post("/crud/createmenu", data, content_type="application/json")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(Menu.objects.count(), 1)

    def test_get(self):
        resp=self.client.get("/crud/getmenu")
        self.assertEqual(resp.status_code,200)
        self.assertIsInstance(resp.json(),list)

    def test_Update(self):
        menu=Menu.objects.create(dishname="dal",price=100,available="no")
        data={"available":"no"}
        resp=self.client.patch(f"/crud/updatemenu/{menu.id}",data,content_type="application/json")
        self.assertEqual(resp.status_code,200)
        self.assertEqual(menu.available,"no")
    
    def test_Delete(self):
        menu=Menu.objects.create(dishname="dal",price=100,available="no")
        resp=self.client.delete(f"/crud/deletemenu/{menu.id}")
        self.assertEqual(resp.status_code,200)
        self.assertEqual(Menu.objects.count(),0)



