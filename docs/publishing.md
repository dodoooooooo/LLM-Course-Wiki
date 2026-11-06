# GitHub Pages 分支發布

完整原始專案與已授權公開的教材保留在 `main`。網站使用 Settings → Pages → Build and deployment → **Deploy from a branch**，來源 **gh-pages / (root)**。此設定仍會由 GitHub 自動產生 Pages 建置／部署工作，不保證可避開平台端限制。

原自訂工作流程移到 `docs/archived-workflows/pages.yml.disabled` 留存，不在 `.github/workflows/` 執行。原有 build／check 由本機發布指令保留；專案沒有其他獨立檢查 workflow 需要停用。

## 更新網站

在原專案根目錄依序執行：

```sh
python3 scripts/build.py
python3 scripts/check.py
git add .
git commit -m "更新課程內容"
git push origin main
python3 scripts/publish_pages.py
```

提交前先檢查變更與新教材的公開權限。發布指令要求 main 乾淨且與 origin/main 一致，會再次 build／check，僅把 `dist/index.html` 與空白 `.nojekyll` 組成網站分支，不複製 raw、Notebook、來源程式或教材目錄。圖片與 Wiki 資料已內嵌在 HTML。

首次 gh-pages 提交沒有 main 父提交；後續只延續網站分支歷史，不切換工作目錄、不使用強制推送。產物相同時不建立新提交，避免重複觸發。遠端分支若有額外檔案則停止，避免覆蓋人工內容。

推送成功只表示檔案已上傳。請在 [Actions](https://github.com/dodoooooooo/LLM-Course-Wiki/actions) 確認自動 Pages 工作完成，再開啟 [網站](https://dodoooooooo.github.io/LLM-Course-Wiki/)。若平台回報帳戶或帳務限制，停止重試，不提高預算或修改付款設定；由擁有人處理平台限制後再評估發布。未成功前仍可雙擊 main 根目錄 `index.html` 離線使用。
