# Figma Make Prompt -- Time University LP

以下の仕様に従って、会員登録ランディングページを作成してください。

---

## サイト概要
- サイト種別: Single-page landing page
- 目的: 無料会員登録のコンバージョン
- ターゲット: 日本のビジネスパーソン（25-50歳）、経営者・マネージャー・ナレッジワーカー
- 言語: 日本語（一部英語）
- トーン: PROFESSIONAL / MINIMAL / ACADEMIC

---

## デザインシステム

### カラーパレット
- Primary: #4ECDC4（ティール）
- Primary Dark: #26A69A
- Accent: #FF7043（CTA用オレンジ）
- Accent Dark: #E64A19
- Background: #F5F5F5
- Surface (Cards): #FFFFFF
- Text: #333333
- Text Secondary: #6C757D
- Border: #E9ECEF
- Hero/Quote背景: #0D1117 → #161B22 のダークグラデーション

### フォント
- 見出し: Playfair Display (700, italic)
- 本文: Inter + Noto Sans JP (300, 400, 500, 600, 700)

### タイポグラフィスケール
- Display: 64px / 700 / Playfair Display（Hero title）
- H1: 40px / 700 / Playfair Display（Section titles）
- H2: 28px / 600 / Inter（Sub-section titles）
- H3: 20px / 600 / Inter（Card titles）
- Body Large: 18px / 400（Lead paragraphs）
- Body: 16px / 400（Default text）
- Body Small: 14px / 400（Captions）
- Overline: 11px / 700 / letter-spacing 3px（Section labels）

### スペーシング（8px grid）
4px / 8px / 12px / 16px / 24px / 32px / 48px / 64px / 96px / 128px

### コンポーネント
- **CTAボタン**: 高さ56px, padding 0 40px, 角丸12px, 背景#FF7043, ホバー時translateY(-2px)+shadow
- **カード**: 角丸16px, padding 32px, shadow 0 1px 3px rgba(0,0,0,0.04), ホバーtranslateY(-4px)
- **入力フィールド**: 高さ52px, 角丸10px, ボーダー1.5px solid #E9ECEF, フォーカス時ティールリング
- **コンテナ**: max-width 1120px, 中央寄せ

---

## ページ構成 (10セクション)

### Section 1: Hero
- 背景: ダークグラデーション（#0D1117 → #16213e → #0f3460）
- 全画面高さ、中央寄せ
- Overline: "COURSE CATALOG 2026-2027"（#4ECDC4, 11px, letter-spacing 4px）
- Headline: "Time University"（Playfair Display, 64px, white）
- Subhead: "The Science, Practice, and Philosophy of Time"（Playfair Display, 20px, italic, rgba白70%）
- Lead: "時間を科学する。"（Inter, 18px, white）
- Body: "ドラッカーが1966年に「時間を記録せよ」と書いてから58年。その提言を学問として体系化する、日本初の無料教育プログラム。"（14px, rgba白60%）
- CTA: "無料で会員登録する"（#FF7043ボタン）

### Section 2: Problem Statement
- 背景: #F5F5F5
- Overline: "THE PROBLEM"
- Headline: "あなたの「忙しい」の正体"（Playfair Display, 40px）
- 3カラムのカード:
  - Card 1: "47秒"（大きな数字, #4ECDC4）+ "現代人の注意持続時間。2004年の2.5分から急落した。" + "Gloria Mark, UCI (2023)"
  - Card 2: "55時間"（大きな数字, #4ECDC4）+ "この壁を超えると、追加の労働は生産性ゼロ。" + "Pencavel, Stanford (2015)"
  - Card 3: "49%"（大きな数字, #4ECDC4）+ "すべての中断のうち、自分自身が引き起こしている割合。" + "Gloria Mark, UCI (2023)"

### Section 3: Intellectual Lineage
- 背景: ダーク（#0D1117）
- Overline: "INTELLECTUAL LINEAGE"
- Headline: "思想の系譜"（white）
- 横並びのタイムライン: 5ノード
  - 1966 / Drucker / 「汝の時間を知れ」
  - 2001 / Allen / GTD
  - 2016 / Newport / Deep Work
  - 2024 / TimeCrowd / デジタル実装
  - 2026 / Time University / 体系的教育
- ノード間を線で接続
- 引用ブロック:
  - "Effective executives do not start with their tasks. They start with their time."
  - -- Peter F. Drucker, The Effective Executive (1966)

### Section 4: 5 Schools
- 背景: #F5F5F5
- Overline: "CURRICULUM"
- Headline: "5 Schools, 26 Courses"
- 5枚のカード（グリッド: デスクトップ3+2、タブレット2+2+1、モバイル1列）

各カード:
- School番号（Overline形式, 各Schoolに固有色）
  - School 1: #5C6BC0 / School 2: #26A69A / School 3: #FF7043 / School 4: #4ECDC4 / School 5: #7E57C2
- School名（H3, 20px bold）
- 説明文（14px, gray）
- コース数バッジ（例: "5 Courses"）

School 1: Philosophy of Time -- 時間の有限性・価値・歴史。なぜ時間を大切にすべきかのマインドセットを形成する。5 Courses
School 2: Science of Time -- 注意・集中・認知科学。なぜ中断が危険なのかを神経科学のエビデンスで解明する。5 Courses
School 3: Time Management -- 個人の時間管理から組織の時間設計へ。158研究のメタ分析と週4日制の実証データ。6 Courses
School 4: Time Engineering -- 計測・データ・改善サイクル。「計測なき改善なし」を体感するハンズオンラボ。5 Courses
School 5: Future of Time -- AI時代の時間再配分。浮いた時間はどこへ消えるか。「節約」と「設計」の違い。5 Courses

### Section 5: Evidence
- 背景: ダーク（#0D1117）
- 4つの大きな数字を横並び
  - 5 / Schools
  - 26 / Courses
  - 31+ / Academic Sources
  - 8 / University Partners（予定）
- 数字は64px Playfair Display, #4ECDC4
- ラベルは14px, rgba白50%

### Section 6: Faculty
- 背景: #F5F5F5
- Overline: "FACULTY"
- Headline: "Academic Partners（予定）"
- 7枚のカード（グリッド）
- 各カード: 名前（太字）、所属（小さく灰色）、専門/役職（#26A69A）
  1. 一川 誠 / 千葉大学 教授 / 日本時間学会 会長
  2. 井坂 康志 / ものつくり大学 教授 / ドラッカー学会 共同代表
  3. 河原 純一郎 / 北海道大学 教授 / 認知心理学
  4. 島津 明人 / 慶應義塾大学 教授 / ワーク・エンゲイジメント
  5. 大湾 秀雄 / 早稲田大学 教授 / ピープルアナリティクス
  6. 森川 正之 / 一橋大学 特任教授 / RIETI
  7. 伊達 洋駆 / ビジネスリサーチラボ / 東京大学

### Section 7: Member Benefits
- 背景: #F5F5F5
- Overline: "MEMBERSHIP"
- Headline: "すべて無料"
- 5枚のカード（アイコン + タイトル + 説明）
  1. 全コンテンツ無料アクセス -- 5 Schools, 26 Coursesのすべて
  2. Weekly Digest -- 毎週月曜に届く、今週の推奨コンテンツ
  3. 月1回ライブ講義 -- ゲスト講師によるオンライン講義。アーカイブ視聴可
  4. Podcast -- AI生成の音声コンテンツで、移動中にも学べる
  5. コミュニティ -- 会員同士の知見共有と議論の場

### Section 8: Registration Form
- 背景: white カード（max-width 560px, 中央寄せ）
- Overline: "JOIN US"
- Headline: "会員登録"
- Sub: "1分で完了。クレジットカード不要。"
- フォームフィールド:
  - メールアドレス（必須）
  - 氏名（必須）
  - 所属企業（任意）
  - 役職（任意）
- CTA: "無料で登録する"（#FF7043、フル幅）
- 注記: "※ いつでも解除できます"（12px, gray）

### Section 9: Closing Quote
- 背景: ダーク（#0D1117）
- 大きな引用符（Playfair Display, #4ECDC4 30%透過）
- "削減された時間を何に使うかは、使う人間が決める。"（Playfair Display, 24px, italic, white）

### Section 10: Footer
- 背景: #F5F5F5
- "Time University"（Playfair Display, 18px）
- "Powered by TimeCrowd | タイムクラウド株式会社"
- "The Science, Practice, and Philosophy of Time"

---

## レスポンシブ
- Desktop: 1200px+（3カラムグリッド）
- Tablet: 768-1199px（2カラムグリッド）
- Mobile: <768px（1カラム、Display 36px, H1 28px）

## アニメーション
- スクロールで各セクションがフェードイン（opacity 0→1, translateY 30px→0, 0.7s）
- カードは0.1s間隔でstagger
- ホバーでカードが4px持ち上がる
