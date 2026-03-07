# 咪嚕谷 · 技能參數查詢

依職業群拆成獨立 JSON 的靜態網頁，適合部署在 Vercel。

## 專案結構

- `index.html` — 首頁，選擇職業群後按需載入該職業的 JSON
- `data/index.json` — 職業群清單（id、名稱、檔案名）
- `data/job-XX.json` — 各職業群技能資料（一個職業一個檔案）
- `scripts/parse_skills.py` — 從 `技能參數.md` 解析並產生上述 JSON
- `vercel.json` — Vercel 設定（cleanUrls、rewrites 避免首頁 404）

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

會覆寫 `data/*.json` 與 `data/index.json`。

## 部署到 Vercel（避免 404）

1. 將此專案推送到 GitHub（或 Vercel 支援的 Git）。
2. 在 [Vercel](https://vercel.com) 新增專案，匯入該 repo。
3. **必做**：在專案 **Settings → General → Root Directory**：
   - 若你的 repo 根目錄就是「網站」資料夾（裡面有 `index.html`、`data/`、`vercel.json`），留空即可。
   - 若 repo 根目錄是上一層（例如還有 `技能參數.md`、`網站` 子資料夾等），請把 **Root Directory** 設成 **`網站`**（或你放 index.html 的那個資料夾名稱），讓 Vercel 的部署根目錄就是「網站」。
4. **建議**：**Settings → General → Framework Preset** 選 **Other**（不要選 Next.js、Vite 等），這樣不會跑 build，直接當靜態檔部署。
5. 儲存後重新 **Redeploy**，再開首頁網址應可正常顯示。

若仍 404，請確認在 Vercel 的部署根目錄下能看到 `index.html` 和 `data/index.json`（在 Vercel 的 Deployments → 該次部署 → 點進去看檔案列表）。
