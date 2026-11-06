---
id: hs-02-cryptography
title: 密碼學基礎與 AES
course: hardware-security
type: lesson
status: needs-review
created: 2026-11-06
updated: 2026-11-06
sources: [HS-002, HS-005]
tags: [硬體安全, 課程]
---
# 密碼學基礎與 AES

## 先分清密碼工具的任務
| 工具 | 解決的問題 | 不能直接推論 |
| --- | --- | --- |
| 對稱式密碼 Symmetric Cryptography | 共享祕密金鑰下的資料加解密 | 金鑰分配已經解決 |
| 公開金鑰密碼 Public-key Cryptography | 用不同但相關的公開與私密金鑰建立機制 | 公鑰不需驗證來源 |
| 數位簽章 Digital Signature | 驗證訊息完整性與簽署來源 | 訊息因此變成機密 |
| 雜湊 Hash Function | 把訊息映射為固定長度摘要 | 摘要本身等於身分認證 |

混合式系統把金鑰建立與大量資料保護分工。這也是[ML-KEM](07-pqc.md)不能直接視為「把整份檔案加密」的原因。[HS-002，PDF p.2–14、47–58](../../../sources/hs-002.md)

## DH、RSA 與 ECC：困難問題不同
Diffie–Hellman 金鑰交換在模數群中，讓雙方各保留私密指數，交換公開值後得到相同結果：`A=g^a mod p`、`B=g^b mod p`、`K=B^a=A^b mod p`。旁觀者能看見 A、B，但求私密指數涉及離散對數問題。基本 DH 本身不認證對方身分。[HS-002，PDF p.15–23](../../../sources/hs-002.md)

RSA 的教材模型用 `n=pq`、`φ(n)=(p−1)(q−1)`，選互質的 e 並令 `ed≡1 mod φ(n)`；加密 `y=x^e mod n`，解密 `x=y^d mod n`。這是理解數學關係的簡化模型，未包括實務填充與完整協定。[HS-002，PDF p.24–30](../../../sources/hs-002.md)

橢圓曲線密碼（ECC）的運算是點加法與純量乘法 `Q=dP`。曲線群有無窮遠點作單位元素；`dP` 是重複群運算，不能把它當座標逐項相乘。ECDH 利用 `a(bP)=b(aP)`。有限域的座標運算都受模數限制。[HS-002，PDF p.31–43](../../../sources/hs-002.md)

| 機制 | 核心關係 | 課內應辨認 |
| --- | --- | --- |
| DH | 指數運算的交換關係 | 公開值與私密指數不同 |
| RSA | 模指數與互逆指數 | p、q 與 n、e 的公開性不同 |
| ECC | 橢圓曲線群純量乘法 | 點、純量與有限域元素不同 |

講義中的短金鑰範例與早期金鑰長度建議用於教學，不作當前部署建議。[HS-002，PDF p.18、23–43](../../../sources/hs-002.md)

## 簽章、雜湊與隨機性
簽章用私鑰簽署、公開金鑰驗證；驗證需重新計算訊息摘要並檢查簽章關係。教材 p.49 的 valid／invalid 條件標示相反；依驗證語意應為相等時有效、不相等時無效，不照抄排版錯字。[HS-002，PDF p.47–54，本文更正說明](../../../sources/hs-002.md)

雜湊的三個性質：原像抗性（Preimage Resistance）難由摘要找原訊息；第二原像抗性（Second-preimage Resistance）難針對已知訊息找同摘要替代品；碰撞抗性（Collision Resistance）難找任意兩個不同訊息有同摘要。理想 n-bit 雜湊的通用碰撞搜尋約為 `2^(n/2)`，與原像搜尋不同。[HS-002，PDF p.55–58](../../../sources/hs-002.md)

真正亂數產生器（TRNG）從物理過程取熵；偽亂數產生器（PRNG）從種子決定性展開；密碼學 PRNG 還要滿足不可預測性。看似均勻或通過簡單統計，不足以證明適合密碼用途。一次性密碼本（OTP）還要求真正隨機、與訊息獨立、保密、長度足夠且只用一次。[HS-002，PDF p.64–70](../../../sources/hs-002.md)

## AES 的大小、狀態與回合
AES 是區塊密碼（Block Cipher），**區塊長度固定 128 bits＝16 bytes**；金鑰可為 128／192／256 bits，對應 10／12／14 回合。AES-256 不是處理 256-bit 區塊。狀態（State）以 4×4 bytes 表示，教材採欄優先排列，讀圖時不能將列、欄順序互換。[HS-002，PDF p.71–76](../../../sources/hs-002.md)

| 階段 | 步驟 | 理解方式 |
| --- | --- | --- |
| 起始 | AddRoundKey | 與第一把 round key 做 XOR |
| 一般回合 | SubBytes → ShiftRows → MixColumns → AddRoundKey | 非線性替換、位置重排、欄內混合、加入金鑰 |
| 最後回合 | SubBytes → ShiftRows → AddRoundKey | **沒有 MixColumns** |

SubBytes 的 S-box 是非線性、一對一的 byte 替換；ShiftRows 改變 byte 位置；MixColumns 在有限域 `GF(2^8)` 中混合一欄。整數乘法、一般加法不能直接代替其有限域運算。[HS-002，PDF p.76–81](../../../sources/hs-002.md)

## 為什麼作業選第一輪 S-box
第一輪 AddRoundKey 後，第 b 個 byte 為 `p_b XOR k_b`，接著 S-box 的輸出為 `S(p_b XOR k_b)`。因此在 MixColumns 擴散前，一個輸出 byte 只涉及一個明文 byte 與一個 key byte。這是兩份作業的中間值來源，不表示整個 AES 能拆成互不相干的十六套加密。[HS-002，PDF p.75–81；HS-005，PDF p.4、13](../../../sources/hs-005.md)

[作業一](../assignments/assignment-01-snr.md)使用已知實驗金鑰分組；[作業二](../assignments/assignment-02-cpa.md)則比較候選金鑰的預測與量測。兩者都依賴實作的洩漏關係。[HS-005，PDF p.9–15](../../../sources/hs-005.md)

## 演算法與實作的界線
平方乘法（Square-and-multiply）、點倍加法（Double-and-add）與查表式 S-box 都是計算同一數學結果的實作選擇。操作流程、記憶體存取與電路切換可能留下側通道；這不等同密碼數學關係被推翻。Kerckhoffs 原則要求安全性不依賴把演算法藏起來。[HS-002，PDF p.28–29、41、77、82–85](../../../sources/hs-002.md)

## 來源與範圍
[HS-002](../../../sources/hs-002.md)：87 頁講義主題式重整，公式為理解用；未將舊效能表、金鑰建議或量子電腦發展敘述當作現況。[HS-005](../../../sources/hs-005.md)補上作業模型的教材連結。
