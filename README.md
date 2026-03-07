# 咪嚕谷 · 技能參數查詢

依職業群拆成獨立 JSON 的靜態網頁，適合部署在 Vercel。

## 專案結構

- `index.html` — 首頁，選擇職業群後按需載入該職業的 JSON
- `public/data/index.json` — 職業群清單（id、名稱、檔案名）
- `public/data/job-XX.json` — 各職業群技能資料（一個職業一個檔案）
- `scripts/parse_skills.py` — 從 `技能參數.md` 解析並產生上述 JSON
- `vercel.json` — Vercel 設定（cleanUrls）

## 本地預覽

在專案根目錄用任意靜態伺服器即可，例如：

```bash
# 若已安裝 Node.js
npx serve .

# 或 Python
python -m http.server 8080
```

然後開啟 http://localhost:8080（或 serve 顯示的網址），選職業群即可看到技能參數。

## 重新產生 JSON（更新技能資料時）

1. 更新 `技能參數.md`
2. 執行：

```bash
python scripts/parse_skills.py
```

會覆寫 `public/data/*.json` 與 `public/data/index.json`。

## 部署到 Vercel

1. 將此專案推送到 GitHub（或連到 Vercel 支援的 Git）
2. 在 [Vercel](https://vercel.com) 新增專案，匯入此 repo
3. 根目錄維持本專案目錄，Build 設定可留空（純靜態）
4. 部署後即可用產生的網址存取

若專案根目錄就是「網站」資料夾，在 Vercel 的 **Root Directory** 設成此資料夾即可。
