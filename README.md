# Uthiru Farm Feeds — Django site

A storefront website for an animal feeds shop at **Uthiru 87, Waiyaki Way,
Nairobi**. Built with Django, so you manage products, prices, and stock
through Django's built-in admin panel — no code editing needed for
day-to-day updates.

No order/inquiry forms on the public site by design (that was a deliberate
scope choice) — visitors just browse products, prices, and shop info.

## Project structure

```
feedshop/
├── manage.py
├── requirements.txt
├── db.sqlite3                 # created after you run migrate
├── feedshop/                  # project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py / asgi.py
├── shop/                      # the app
│   ├── models.py              # Category, Product
│   ├── admin.py                # registers models with Django admin
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── management/commands/seed_products.py
├── templates/
│   ├── base.html
│   └── shop/home.html
└── static/
    ├── css/style.css
    └── js/script.js
```

## Run it

```bash
cd feedshop
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # set your own admin username/password
python manage.py seed_products     # optional: loads sample categories & products
python manage.py runserver
```

Visit **http://127.0.0.1:8000** for the site, and
**http://127.0.0.1:8000/admin** to manage products.

## Managing products

Everything on the price board and product grid comes straight from the
database via `Category` and `Product` models. To add, edit, or remove a
product:

1. Go to `/admin` and log in with the superuser account you created.
2. Open **Products** (or **Categories** to add a new animal type).
3. Add/edit an entry, set `in_stock` on or off, mark a product `featured`
   to show a "Popular" tag — save, then refresh the site.

**Important:** the sample prices loaded by `seed_products` are
placeholders so the page has something to display. They are not real,
current market prices — update them in `/admin` to reflect what you
actually charge.

## Editing shop details

- **Address, hours, phone:** these are plain text in
  `templates/base.html` and `templates/shop/home.html` — search for
  "Uthiru 87" or "+254 700 000 000" and replace with your real number.
- **Map:** the location section currently shows an illustrative SVG
  graphic, not a real map (no Google Maps API key was available while
  building this). Get a real embed by going to Google Maps, searching
  your shop, choosing **Share → Embed a map**, and pasting the
  `<iframe>` it gives you in place of the SVG in
  `templates/shop/home.html` (search for `class="map-card"`).
- **Colors, fonts, layout:** all in `static/css/style.css`, using CSS
  variables at the top of the file (`--soil`, `--wheat`, `--green`,
  `--rust`, etc.) so you can retheme quickly.

## A note on how this was built

Django wasn't available to actually run and test in the environment
this was built in (no network access to install it), so the migration
file was written by hand to match the models exactly, and every Python
file was checked for syntax errors — but the project has **not** been
run end-to-end the way the earlier Flask project was. Run through the
steps above once and if anything doesn't come up cleanly, send me the
exact error and I'll fix it.

## Going further

- Add `django-environ` or similar to move `SECRET_KEY` out of
  `settings.py` before deploying anywhere public.
- Set `DEBUG = False` and configure `ALLOWED_HOSTS` properly for
  production.
- Add a real Google Maps embed (see above).
- If you later want an order/inquiry form or WhatsApp click-to-chat
  button, that's a small addition — just ask.
