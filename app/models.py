from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

STATE_CHOICES = (
    ('Altai Territory', 'Altai Territory'),
    ('Amur Region', 'Amur Region'),
    ('Arkhangelsk Region', 'Arkhangelsk Region'),
    ('Astrakhan Region', 'Astrakhan Region'),
    ('Belgorod Region', 'Belgorod Region'),
    ('Bryansk Region', 'Bryansk Region'),
    ('Chechen Republic', 'Chechen Republic'),
    ('Chelyabinsk Region', 'Chelyabinsk Region'),
    ('Chukotka Autonomous Area', 'Chukotka Autonomous Area'),
    ('Chuvash Republic', 'Chuvash Republic'),
    ('City of Sevastopol', 'City of Sevastopol'),
    ('City of St Petersburg', 'City of St Petersburg'),
    ('Donetsk Republic', 'Donetsk Republic'),
    ('Irkutsk Region', 'Irkutsk Region'),
    ('Ivanovo Region', 'Ivanovo Region'),
    ('Jewish Autonomous Region', 'Jewish Autonomous Region'),
    ('Kabardino-Balkarian Republic', 'Kabardino-Balkarian Republic'),
    ('Kaliningrad Region', 'Kaliningrad Region'),
    ('Kaluga Region', 'Kaluga Region'),
    ('Kamchatka Territory', 'Kamchatka Territory'),
    ('Karachayevo-Circassian Republic', 'Karachayevo-Circassian Republic'),
    ('Kemerovo Region — Kuzbass', 'Kemerovo Region — Kuzbass'),
    ('Khabarovsk Territory', 'Khabarovsk Territory'),
    ('Khanty-Mansi Autonomous Area – Yugra', 'Khanty-Mansi Autonomous Area – Yugra'),
    ('Kherson Region', 'Kherson Region'),
    ('Kirov Region', 'Kirov Region'),
    ('Komi Republic', 'Komi Republic'),
    ('Kostroma Region', 'Kostroma Region'),
    ('Krasnodar Territory', 'Krasnodar Territory'),
    ('Krasnoyarsk Territory', 'Krasnoyarsk Territory'),
    ('Kurgan Region', 'Kurgan Region'),
    ('Kursk Region', 'Kursk Region'),
    ('Leningrad Region', 'Leningrad Region'),
    ('Lipetsk Region', 'Lipetsk Region'),
    ('Lugansk Republic', 'Lugansk Republic'),
    ('Magadan Region', 'Magadan Region'),
    ('Moscow', 'Moscow'),
    ('Moscow Region', 'Moscow Region'),
    ('Murmansk Region', 'Murmansk Region'),
    ('Nenets Autonomous Area', 'Nenets Autonomous Area'),
    ('Nizhny Novgorod Region', 'Nizhny Novgorod Region'),
    ('Novgorod Region', 'Novgorod Region'),
    ('Novosibirsk Region', 'Novosibirsk Region'),
    ('Omsk Region', 'Omsk Region'),
    ('Orel Region', 'Orel Region'),
    ('Orenburg Region', 'Orenburg Region'),
    ('Penza Region', 'Penza Region'),
    ('Perm Territory', 'Perm Territory'),
    ('Primorye Territory', 'Primorye Territory'),
    ('Pskov Region', 'Pskov Region'),
    ('Republic of Adygea', 'Republic of Adygea'),
    ('Republic of Altai', 'Republic of Altai'),
    ('Republic of Bashkortostan', 'Republic of Bashkortostan'),
    ('Republic of Buryatia', 'Republic of Buryatia'),
    ('Republic of Crimea', 'Republic of Crimea'),
    ('Republic of Dagestan', 'Republic of Dagestan'),
    ('Republic of Ingushetia', 'Republic of Ingushetia'),
    ('Republic of Kalmykia', 'Republic of Kalmykia'),
    ('Republic of Karelia', 'Republic of Karelia'),
    ('Republic of Khakassia', 'Republic of Khakassia'),
    ('Republic of Mari El', 'Republic of Mari El'),
    ('Republic of Mordovia', 'Republic of Mordovia'),
    ('Republic of North Ossetia-Alania', 'Republic of North Ossetia-Alania'),
    ('Republic of Sakha (Yakutia)', 'Republic of Sakha (Yakutia)'),
    ('Republic of Tatarstan', 'Republic of Tatarstan'),
    ('Republic of Tyva', 'Republic of Tyva'),
    ('Republic of Udmurtia', 'Republic of Udmurtia'),
    ('Rostov Region', 'Rostov Region'),
    ('Ryazan Region', 'Ryazan Region'),
    ('Sakhalin Region', 'Sakhalin Region'),
    ('Samara Region', 'Samara Region'),
    ('Saratov Region', 'Saratov Region'),
    ('Smolensk Region', 'Smolensk Region'),
    ('Stavropol Territory', 'Stavropol Territory'),
    ('Sverdlovsk Region', 'Sverdlovsk Region'),
    ('Tambov Region', 'Tambov Region'),
    ('Tomsk Region', 'Tomsk Region'),
    ('Trans-Baikal Territory', 'Trans-Baikal Territory'),
    ('Tula Region', 'Tula Region'),
    ('Tver Region', 'Tver Region'),
    ('Tyumen Region', 'Tyumen Region'),
    ('Ulyanovsk Region', 'Ulyanovsk Region'),
    ('Vladimir Region', 'Vladimir Region'),
    ('Volgograd Region', 'Volgograd Region'),
    ('Vologda Region', 'Vologda Region'),
    ('Voronezh Region', 'Voronezh Region'),
    ('Yamal-Nenets Autonomous Area', 'Yamal-Nenets Autonomous Area'),
    ('Yaroslavl Region', 'Yaroslavl Region'),
    ('Zaporozhye Region', 'Zaporozhye Region'),
)

CATEGORY_CHOICES = (
    ('NB', 'Notebooks'),
    ('PC', 'PCs'),
    ('PH', 'Phones'),
    ('MN', 'Monitors'),
    ('WF', 'Wi-Fi routers'),
    ('IP', 'IP cameras'),
    # ('AC', 'Accessories'),
)


class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')

    def __str__(self):
        return self.title


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    # mobile_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # mobile_number = models.CharField(validators=[mobile_regex], max_length=17, blank=True)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price


STATUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('Packed', 'Packed'),
    ('On the way', 'On the way'),
    ('Delivered', 'Delivered'),
    ('Cancel','Cancel'),
    ('Pending','Pending'),
)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    yapay_order_id = models.CharField(max_length=100, blank=True, null=True)
    yapay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    yapay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATE_CHOICES, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, default='')

    @property
    def total_cost(self):
        return  self.quantity * self.product.discounted_price


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

