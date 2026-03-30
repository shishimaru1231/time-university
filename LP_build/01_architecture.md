# PROMPT 1: Architecture -- Time University LP

## Site Type
Single-page landing page (SPA) for member registration

## Target Audience
- 日本のビジネスパーソン（25-50歳）
- 経営者、マネージャー、ナレッジワーカー
- 「忙しい」「時間が足りない」と感じている人

## Page Hierarchy (Top → Bottom)

```
1. Hero
2. Problem Statement（問題提起）
3. Intellectual Lineage（思想の系譜）
4. 5 Schools Overview（カリキュラム概要）
5. Evidence（数字・エビデンス）
6. Faculty（講師陣）
7. Member Benefits（会員特典）
8. Registration Form（会員登録）
9. Closing Quote
10. Footer
```

## User Flows (3 Journeys)

### Journey A: 直感型（スクロール→即登録）
Hero → CTA Click → Form → Submit
- ファーストビューで刺さった人が即座に登録

### Journey B: 探索型（じっくり読む→登録）
Hero → Problem → Lineage → Schools → Evidence → Faculty → Benefits → Form → Submit
- 全セクション読んでから判断

### Journey C: 懐疑型（証拠を確認→登録）
Hero → Evidence（数字で納得）→ Faculty（権威で信頼）→ Form → Submit
- エビデンスと権威付けで判断する人

## Key Interactions
- Hero CTA → スムーススクロールで登録フォームへ
- School cards → ホバーでアクセントカラーのボーダー表示
- Faculty cards → ホバーで少し持ち上がる
- Form submit → 完了メッセージ表示（ダミー）
- Scroll → セクションごとのフェードインアニメーション

## Responsive Breakpoints
- Desktop: 1200px+
- Tablet: 768px - 1199px
- Mobile: < 768px

## Performance Requirements
- Single HTML file (no external JS framework)
- Google Fonts only external dependency
- CSS animations only (no JS animation library)
- Intersection Observer for scroll animations
