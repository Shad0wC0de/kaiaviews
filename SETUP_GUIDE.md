# BINI Video Search — GitHub Setup Guide

## What you'll end up with
A free public website (e.g. `https://yourusername.github.io/bini-search/`) that
lets anyone search and filter all your BINI YouTube video metadata.

---

## Step 1 — Create a GitHub account (skip if you have one)
1. Go to https://github.com and click **Sign up**
2. Follow the steps to create a free account

---

## Step 2 — Create a new repository
1. Once logged in, click the **+** button (top-right) → **New repository**
2. Fill in:
   - **Repository name:** `bini-search` (or any name you like)
   - **Description:** BINI YouTube Video Archive (optional)
   - **Visibility:** ✅ Public  ← this is required for GitHub Pages (free tier)
   - Leave everything else as default
3. Click **Create repository**

---

## Step 3 — Upload your files
1. On your new repo page, click **Add file** → **Upload files**
2. Upload ALL of the following files at once:
   - `video metadata 1.csv`
   - `video metadata 2.csv`
   - `video metadata 3.csv`
   - `video metadata 4.csv`
   - `video metadata 5.csv`
   - `video metadata 6.csv`
   - `video metadata 7.csv`
   - `video metadata 8.csv`
   - `video metadata 9.csv`
   - `index.html`
3. Scroll down and click **Commit changes**

---

## Step 4 — Edit index.html with your username & repo name
1. In your repo, click on **index.html**
2. Click the **pencil icon** (Edit this file) — top right of the file view
3. Find these two lines near the top of the `<script>` section:

   ```js
   const GITHUB_USER = "YOUR_USERNAME";
   const GITHUB_REPO = "YOUR_REPO_NAME";
   ```

4. Replace `YOUR_USERNAME` with your actual GitHub username
   and `YOUR_REPO_NAME` with `bini-search` (or whatever you named it)

   Example:
   ```js
   const GITHUB_USER = "maricel";
   const GITHUB_REPO = "bini-search";
   ```

5. Click **Commit changes** → **Commit directly to the main branch** → **Commit changes**

---

## Step 5 — Enable GitHub Pages
1. In your repo, click **Settings** (top tab)
2. In the left sidebar, click **Pages**
3. Under **Source**, select:
   - Branch: **main**
   - Folder: **/ (root)**
4. Click **Save**
5. Wait ~1–2 minutes, then refresh the page
6. You'll see a green banner with your site URL:
   `https://YOUR_USERNAME.github.io/bini-search/`

---

## Step 6 — Open your site 🎉
Visit the URL from Step 5 and your BINI Video Search is live!

---

## Updating data later
When you run your Python script again and get new CSV files:
1. Go to your repo → click **Add file** → **Upload files**
2. Upload the new CSV files (they'll overwrite the old ones automatically)
3. Click **Commit changes** — the site updates within seconds

---

## Notes
- The site is fully static — no server, no database, no cost
- All searching/filtering happens in the visitor's browser
- If you have more or fewer than 9 CSV files, edit the line in index.html:
  `const NUM_FILES = 9;`  ← change 9 to however many files you have
