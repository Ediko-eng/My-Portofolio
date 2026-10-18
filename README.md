# Edmilson Fabio Valente — Interactive Room Portfolio

*A no-framework, single-page interactive portfolio designed as an engineer's room in an Iron Man / Stark-tech style — live at https://ediko-eng.github.io/My-Portofolio/*

---

## 📖 Project Overview
This repository contains the source code for my personal portfolio. Instead of a traditional scrolling page, the whole portfolio lives inside an **interactive SVG room**: every object — the desk, monitors, shelf, window, note board, robotic arm and the holographic AI — is clickable and opens a panel (About, Skills, Projects, ML Lab, Contact, Timor-Leste).

The site showcases my work in **AI & Machine Learning**, **Web Development** and **Software Engineering**, with zero frameworks and zero build steps: pure HTML, CSS, JavaScript and SVG.

## 🚀 Key Features
* **Interactive room scene:** hand-built SVG environment with 10 clickable hotspots that open accessible dialog panels.
* **E.D.D.I — holographic AI assistant:** a wireframe assistant beside the window that types responses, rotates through lines, and speaks them via the Web Speech API (audio toggle).
* **Stark-tech HUD:** arc-reactor header, corner brackets, system status readouts, scanlines and a light-sweep overlay.
* **Rotating motivational quotes:** a HUD banner, a random quote on the loader, and extra lines woven into the AI's dialogue.
* **Day / Night mode:** toggle persisted with `localStorage('room-mode')`.
* **Loader:** animated "powering the arc reactor" progress screen that runs while assets load.
* **Self-hosted variable fonts:** Inter, JetBrains Mono and Pixelify Sans (no external font CDNs).
* **Fully responsive:** the room scales to a 16:9 stage; on phones a fallback button nav appears and decorative overlays are hidden.
* **SEO / accessibility:** semantic markup, Open Graph + JSON-LD data, ARIA-labelled dialogs, focus restore, ESC/backdrop close, `prefers-reduced-motion` support and a `noscript` fallback.

## 🛠️ Tech Stack
* **HTML5:** semantic structure, dialogs, JSON-LD structured data.
* **CSS3:** custom properties for theming, keyframe animations, `clip-path`/masks, backdrop filters, responsive media queries.
* **JavaScript (Vanilla):** panel routing, typewriter effects, loader, speech synthesis, quote rotation — no libraries.
* **SVG:** the entire room illustration (gradients, glow filters, clip paths) drawn by hand in `index.html`.

## 📁 Repository Structure
* **`index.html`** — markup for the room SVG, hotspots, HUD, panels and mobile nav.
* **`style.css`** — full design system: tokens, room styling, animations, responsive breakpoints.
* **`script.js`** — loader, mode toggle, panels, typewriter, E.D.D.I dialogue/voice, quote rotation.
* **`fonts/`** — self-hosted variable font files (Inter, JetBrains Mono, Pixelify Sans).
* **`flag-timor-leste.svg`** — Timor-Leste flag used in the scene and panels.
* **`favicon.svg` / `og-image.png` / `Image.png`** — branding assets.
* **`README.md`** / **`LICENSE.md`** — this file and the MIT license.

## ⚙️ How to Run Locally
No build step required — just serve the folder statically:

```bash
# Python
python -m http.server 8000
# or PHP
php -S 127.0.0.1:8000
```
Then open `http://localhost:8000`.

## 🚀 Deployment (GitHub Pages)
The site is published from this repository:
1. Push to the `main` branch of `Ediko-eng/My-Portofolio`.
2. Go to **Settings → Pages**.
3. Under **Source**, select `main` / root and **Save**.
4. Live at: `https://ediko-eng.github.io/My-Portofolio/`

## 📬 Contact Information
Feel free to reach out for collaborations or inquiries:
* **Email:** [edmilsonfabiovalente@gmail.com](mailto:edmilsonfabiovalente@gmail.com)
* **GitHub:** [@Ediko-eng](https://github.com/Ediko-eng)
* **LinkedIn:** [Edmilson Fabio Valente](https://www.linkedin.com/in/edmilson-fabio-valente-297687310/)

---
**Author:** Edmilson Fabio Valente
**Focus:** AI & Web Developer · Dili, Timor-Leste
**License:** [MIT License](https://github.com/Ediko-eng/My-Portofolio/blob/main/LICENSE.md)
