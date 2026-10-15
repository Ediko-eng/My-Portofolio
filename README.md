# 🚀 Personal Portfolio: Edmilson Valente

*A Django-powered personal website featuring a modern "Glassmorphism" design, a
content-managed admin, and a working contact form.*

---

## 📖 Project Overview

This repository contains the source code for my professional portfolio, built with
**Django**. It showcases my expertise in **AI & Machine Learning**, **Web Development**,
and **Software Engineering**, with a premium, responsive "Cyberpunk-inspired" design.

Content (profile, skills, and projects) is stored in the database and editable through
the Django admin — no code changes needed to update the site.

## ✨ Features

* **Database-backed content:** `Profile`, `Skill`, and `Project` models managed in the admin.
* **Contact form:** saves messages to the database *and* emails them via Gmail SMTP.
* **Dynamic background & Glassmorphism UI:** animated CSS gradient with frosted-glass cards.
* **Light / dark theme** respecting the OS preference, with a manual toggle.
* **SEO ready:** meta tags, Open Graph / Twitter cards, favicon, and JSON-LD `Person` schema.
* **Responsive:** optimized for desktop, tablet, and mobile.

## 🛠️ Tech Stack

* **Backend:** Python 3.13, Django 5.2
* **Database:** SQLite (local) · PostgreSQL (production, via `DATABASE_URL`)
* **Static files:** WhiteNoise
* **Server:** Gunicorn
* **Frontend:** HTML5, CSS3 (Grid/Flexbox, animations), vanilla JavaScript, Font Awesome

## 📁 Project Structure

```
manage.py
portfolio/            # Project settings, URLs, WSGI/ASGI
core/                 # App: models, admin, views, forms, URLs, seed command
  ├── migrations/
  └── management/commands/seed_content.py
templates/
  ├── base.html       # Shared layout (head, header, footer)
  └── core/home.html  # Homepage sections
static/               # css/, js/, img/ (served by WhiteNoise in production)
build.sh              # Render build script
render.yaml           # Render Blueprint (web service + Postgres)
```

## 🚀 Local Development

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure environment (optional locally; SQLite + console email are defaults)
copy .env.example .env      # Windows

# 3. Apply migrations and load the current content
python manage.py migrate
python manage.py seed_content

# 4. Create an admin account and run the server
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/ — the admin lives at http://127.0.0.1:8000/admin/.

The `seed_content` command is idempotent and can be re-run safely.

## ☁️ Deploy on Render

The repo ships with `render.yaml` (Blueprint) and `build.sh`, so the whole stack —
web service **and** managed Postgres — is provisioned in one step.

1. In Render, choose **New → Blueprint** and point it at this repository
   (`main` branch). Render creates the web service and the database automatically.
2. Set the secret environment variables in the dashboard:
   * `EMAIL_HOST_USER` — your Gmail address
   * `EMAIL_HOST_PASSWORD` — a Google **app password**
   * `DEFAULT_FROM_EMAIL` and `CONTACT_RECIPIENT` — the recipient address
   * *(optional)* `DJANGO_SUPERUSER_USERNAME`, `DJANGO_SUPERUSER_EMAIL`,
     `DJANGO_SUPERUSER_PASSWORD` — auto-creates the admin user on first deploy
3. Deploy. `build.sh` runs `collectstatic`, `migrate`, and `seed_content` automatically.

If you skipped the superuser variables, create the admin via the Render **Shell**:

```bash
python manage.py createsuperuser
```

> Note: `ALLOWED_HOSTS` and `CSRF_TRUSTED_ORIGINS` include `.onrender.com`, and the app
> auto-detects `RENDER_EXTERNAL_HOSTNAME`, so the site works without hardcoding its URL.
> Set `SITE_URL` to your final custom domain for correct canonical / Open Graph links.

### Render free tier notes

* The web service **sleeps** after ~15 minutes of inactivity; the first request
  afterwards takes a few seconds to wake it up.
* The free Postgres database **expires after 30 days** — upgrade the plan or migrate
  the data before then.

## 🔁 GitHub Pages redirect

The old static site is replaced by a tiny redirect page (`pages/index.html`) that
forwards `ediko-eng.github.io/My-Portofolio/` to the live Render URL. The
`.github/workflows/pages.yml` workflow builds and deploys it on every push to `main`.

To point it at your deployment, set an Actions **variable**:

1. GitHub → **Settings → Secrets and variables → Actions → Variables**.
2. New variable: name `RENDER_URL`, value your live URL
   (e.g. `https://my-portfolio-xxxx.onrender.com`).
3. Re-run the **Deploy redirect page to GitHub Pages** workflow (or push to `main`).

Until `RENDER_URL` is set, the redirect falls back to the GitHub repository.

> GitHub Pages must be set to source **GitHub Actions** (Settings → Pages → Build and
> deployment → Source: GitHub Actions). Django itself runs on Render, not on Pages.

## 🌿 Branches

* `main` — production branch, deployed by Render.
* `django` — kept in sync with `main`.

## 📬 Contact Information

* **Email:** [edmilsonfabiovalente@gmail.com](mailto:edmilsonfabiovalente@gmail.com)
* **GitHub:** [@Ediko-eng](https://github.com/Ediko-eng)
* **LinkedIn:** [Edmilson Fabio Valente](https://www.linkedin.com/in/edmilson-fabio-valente-297687310/)

---

**Author:** Edmilson Fabio Valente
**Focus:** AI & Web Developer
**License:** [MIT License](https://github.com/Ediko-eng/My-Portofolio/blob/main/LICENSE.md)
