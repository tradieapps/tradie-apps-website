# Tradie Apps website

Plain HTML site for QuoteWalk and Invomile, with three free calculators. No build step and no tracking.
Nothing is sent anywhere, and the calculators run in the visitor's browser.

## Put it online (GitHub Pages, free)
1. On github.com, click **New repository**. Name it `tradieapps`, set it to **Public**, and click Create.
2. Click **uploading an existing file**. Drag in **everything inside this folder** (not the folder itself), then click **Commit changes**.
3. Go to **Settings → Pages**. Under "Build and deployment", choose **Deploy from a branch**, pick branch **main** and folder **/ (root)**, then click Save.
4. Wait 1–2 minutes. Your site will be at `https://YOUR-USERNAME.github.io/tradieapps/`

## One small edit: privacy policy links
Open `assets/site.js` on GitHub (click the pencil icon) and paste your two privacy policy URLs between the quotes:
    qwPrivacy: "https://...",
    imPrivacy: "https://..."
Until you do, the privacy links stay hidden.

## Later: your own domain
Buy the domain, then send Claude this zip again. It will add the CNAME file, sitemap.xml and Google setup in one go.

`_source/` holds the page templates (GitHub Pages ignores it). Claude uses it to rebuild the site.
