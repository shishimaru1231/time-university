#!/usr/bin/env python3
"""Time University 必読論文リスト PDF生成スクリプト"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# 日本語フォント登録
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiKakuGo-W5"))
pdfmetrics.registerFont(UnicodeCIDFont("HeiseiMin-W3"))

FONT_GOTHIC = "HeiseiKakuGo-W5"
FONT_MINCHO = "HeiseiMin-W3"

# TimeCrowdカラー
PRIMARY = HexColor("#4ECDC4")
PRIMARY_DARK = HexColor("#26A69A")
ACCENT = HexColor("#FF7043")
TEXT_COLOR = HexColor("#333333")
BG_LIGHT = HexColor("#F5F5F5")
WHITE = HexColor("#FFFFFF")
GRAY = HexColor("#999999")

# スタイル定義
style_title = ParagraphStyle(
    "Title", fontName=FONT_GOTHIC, fontSize=22,
    textColor=PRIMARY_DARK, spaceAfter=4*mm, alignment=TA_CENTER
)
style_subtitle = ParagraphStyle(
    "Subtitle", fontName=FONT_GOTHIC, fontSize=10,
    textColor=GRAY, spaceAfter=8*mm, alignment=TA_CENTER
)
style_school = ParagraphStyle(
    "School", fontName=FONT_GOTHIC, fontSize=14,
    textColor=PRIMARY_DARK, spaceBefore=6*mm, spaceAfter=3*mm
)
style_section = ParagraphStyle(
    "Section", fontName=FONT_GOTHIC, fontSize=10,
    textColor=ACCENT, spaceBefore=4*mm, spaceAfter=2*mm
)
style_paper_title = ParagraphStyle(
    "PaperTitle", fontName=FONT_GOTHIC, fontSize=9,
    textColor=TEXT_COLOR, leading=13
)
style_paper_detail = ParagraphStyle(
    "PaperDetail", fontName=FONT_MINCHO, fontSize=7.5,
    textColor=HexColor("#555555"), leading=11, leftIndent=3*mm
)
style_paper_finding = ParagraphStyle(
    "PaperFinding", fontName=FONT_MINCHO, fontSize=7.5,
    textColor=TEXT_COLOR, leading=11, leftIndent=3*mm, spaceBefore=1*mm
)
style_priority = ParagraphStyle(
    "Priority", fontName=FONT_GOTHIC, fontSize=7,
    textColor=WHITE, alignment=TA_CENTER
)
style_footer = ParagraphStyle(
    "Footer", fontName=FONT_MINCHO, fontSize=7,
    textColor=GRAY, alignment=TA_CENTER
)

# 論文データ
data = [
    {
        "school": "School 1: Philosophy of Time -- 時間の有限性・価値",
        "desc": "「時間を大切にすべき理由」を知的に理解する",
        "papers": [
            {
                "id": "PHI-100",
                "title": "Peter Drucker (1966) 'The Effective Executive' Ch.2 \"Know Thy Time\"",
                "source": "Harper & Row, 1966 / Harper Business, 2006",
                "finding": "時間管理3ステップ: 記録 → 整理 → まとめる。「時間は最も希少な資源であり、時間を管理できなければ、何も管理できない」。Time University全体のOrigin Story。",
                "priority": "必読"
            },
            {
                "id": "PHI-101",
                "title": "Oliver Burkeman (2021) 'Four Thousand Weeks: Time Management for Mortals'",
                "source": "Farrar, Straus and Giroux, 2021",
                "finding": "人生は約4,000週間。生産性ハックに依存するのではなく、時間の有限性を直視することで、本当に重要なことに時間を使う哲学。",
                "priority": "必読"
            },
            {
                "id": "PHI-102",
                "title": "Miura et al. (2025) 日本版知覚的時間貧困尺度の開発",
                "source": "PLOS ONE, 20(4), e0320807, 2025",
                "finding": "横浜市の就労世帯10,000人対象の縦断調査。日本初の信頼性ある時間貧困測定ツール（α=0.90）。時間貧困は睡眠・余暇と負の相関、育児と正の相関。",
                "priority": "高"
            },
            {
                "id": "PHI-103",
                "title": "Whillans et al. (2017-2019) 時間貧困と幸福度の研究群",
                "source": "PNAS (2017) / Science Advances (2019) / HBS Working Paper",
                "finding": "4か国の大規模調査: 時間節約サービスにお金を使う人は生活満足度が高い。時間をお金より重視する人は慢性的に幸福感が高い。",
                "priority": "高"
            },
            {
                "id": "PHI-104",
                "title": "Zhu, Yang & Hsee (2018) The Mere Urgency Effect",
                "source": "Journal of Consumer Research, 45(3), 673-690, 2018",
                "finding": "「緊急だが重要でないタスク」を「緊急でないが重要なタスク」より優先する心理的バイアスを実験的に実証。アイゼンハワーマトリクスの心理学的基盤。",
                "priority": "高"
            },
            {
                "id": "PHI-105",
                "title": "John Pencavel (2015) The Productivity of Working Hours",
                "source": "IZA Discussion Paper 8129, 2015",
                "finding": "週50時間超で1時間あたり生産性が急落。55時間以上ではそれ以上働いても成果は増えない。週70時間の労働者の成果は55時間と同等。",
                "priority": "高"
            },
            {
                "id": "PHI-106",
                "title": "Cal Newport (2024) 'Slow Productivity'",
                "source": "Portfolio/Penguin, 2024",
                "finding": "3原則: (1) より少ないことをする (2) 自然なペースで働く (3) 品質に執着する。Economist Best Book of 2024選出。",
                "priority": "高"
            },
        ]
    },
    {
        "school": "School 2: Science of Time -- 注意・集中・認知科学",
        "desc": "注意と集中のメカニズムを理解し、「時間の質」を設計する",
        "papers": [
            {
                "id": "SCI-201",
                "title": "Gloria Mark (2023) 'Attention Span'",
                "source": "Hanover Square Press, 2023",
                "finding": "UCI教授の20年間の研究集大成。スクリーン上の注意持続時間: 2004年2.5分 → 最新47秒（中央値40秒）。自己中断が全中断の49%。中断からの復帰に平均25分。",
                "priority": "必読"
            },
            {
                "id": "SCI-202",
                "title": "Sophie Leroy (2009) Why Is It So Hard to Do My Work?",
                "source": "Organizational Behavior and Human Decision Processes, 109(2), 2009",
                "finding": "「注意残余（Attention Residue）」概念を提唱。前のタスクが未完了のまま次に移ると、認知資源が前のタスクに引きずられパフォーマンスが低下する。",
                "priority": "必読"
            },
            {
                "id": "SCI-203",
                "title": "Leroy, Glomb & Schmidt (2018) Ready-to-Resume Plan",
                "source": "Organization Science, 29(3), 380-397, 2018",
                "finding": "中断前に再開計画をメモする手法で注意残余が有意に減少、中断タスクの正答率79%向上。即座に実務で使える知見。",
                "priority": "高"
            },
            {
                "id": "SCI-204",
                "title": "Alameda, Sanabria & Ciria (2022) フロー状態の神経基盤 系統的レビュー",
                "source": "Cortex, 154, 348-364, 2022",
                "finding": "25研究・471名をレビュー。前頭領域（DLPFC, MPFC, IFG）の重要な役割を確認。一過性低前頭化仮説と同期化理論の2つの理論的枠組みを整理。",
                "priority": "高"
            },
            {
                "id": "SCI-205",
                "title": "Rosen, Oh et al. (2024) 創造的フロー状態の神経画像研究",
                "source": "Neuropsychologia, 196, 108824, 2024",
                "finding": "32名のジャズギタリスト対象のEEG研究。高フロー状態は実行制御領域の活動低下に関連。「豊富な経験」+「コントロールの解放」の2要因モデル。",
                "priority": "高"
            },
            {
                "id": "SCI-206",
                "title": "Liebherr et al. (2022) スマートフォン通知の認知コスト",
                "source": "Psychophysiology関連, PMC, 2022",
                "finding": "通知の頻度とチェック回数がスクリーンタイム総量より注意散漫の強い予測因子。短時間のマインドフルネスで通知の認知制御への悪影響を緩和可能。",
                "priority": "高"
            },
            {
                "id": "SCI-207",
                "title": "Lu, Van der Linden & Bakker (2025) フローの神経科学的基盤",
                "source": "NeuroImage, 2025年3月",
                "finding": "学習の進捗がフロー体験とタスクエンゲージメントを予測。進捗の蓄積とともに認知制御が形成されることをEEGで実証。",
                "priority": "中"
            },
        ]
    },
    {
        "school": "School 3: Time Management -- 組織設計・フレームワーク",
        "desc": "個人の時間管理から組織の時間設計へスケールする",
        "papers": [
            {
                "id": "MGT-301",
                "title": "Aeon, Faber & Panaccio (2021) Does Time Management Work? メタ分析",
                "source": "PLOS ONE, 16(1), e0245066, 2021",
                "finding": "158研究・53,957名の包括的メタ分析。時間管理はウェルビーイングへの効果がパフォーマンス向上より大きい。1990年代初頭から効果は年々強化。",
                "priority": "必読"
            },
            {
                "id": "MGT-302",
                "title": "Biwer et al. (2023) ポモドーロ休憩 vs 自己調整休憩の比較",
                "source": "British Journal of Educational Psychology, 93(S2), 353-367, 2023",
                "finding": "87名の大学生で比較。組織的休憩群は自己調整群より集中力・モチベーションが高く、同等のタスク完了量をより短時間で達成。",
                "priority": "高"
            },
            {
                "id": "MGT-303",
                "title": "Schor et al. (2023) UK 4-Day Week Pilot",
                "source": "Autonomy Institute / 4 Day Week Global, 2023",
                "finding": "英国61社・約2,900名の大規模パイロット。病欠65%減、バーンアウト71%低減、離職率57%減少。参加企業の92%が継続。",
                "priority": "必読"
            },
            {
                "id": "MGT-304",
                "title": "Schor et al. (2024) Making It Stick: UK 4-Day Week 1年後フォローアップ",
                "source": "Autonomy Institute / Cambridge, 2024",
                "finding": "パイロット終了1年後の追跡調査。大多数が週4日制を継続し、生産性維持と従業員ウェルビーイング向上の長期的エビデンスを提供。",
                "priority": "高"
            },
            {
                "id": "MGT-305",
                "title": "Bloom et al. (2024) ハイブリッドワーク Trip.com実験",
                "source": "Nature, 2024年6月",
                "finding": "1,612名のRCT。週2日在宅で離職率33%減少。生産性・キャリア昇進への悪影響ゼロ。管理職の在宅勤務への認識が-2.6%から+1.0%に改善。",
                "priority": "高"
            },
            {
                "id": "MGT-306",
                "title": "日本マイクロソフト (2019) ワークライフチョイス チャレンジ 2019 夏",
                "source": "Microsoft News Center Japan, 2019年10月",
                "finding": "金曜全社休業トライアル。生産性40%向上（社員1人あたり売上）、印刷枚数58.7%減、電力消費23.1%減。社員92%が支持。",
                "priority": "高"
            },
            {
                "id": "MGT-307",
                "title": "Shangguan (2025) Productivity and Working Hours Within Teams",
                "source": "International Economic Review, 66(4), 1645-1664, 2025",
                "finding": "日本の建築設計事務所データ。生産性向上の59.7%はチーム内の時間再配分によるもの。5人チームの最上位貢献者がチーム総労働時間の60%超を投入。",
                "priority": "高"
            },
            {
                "id": "MGT-308",
                "title": "Kotynkova Krotka (2025) Flexible Work and Time Poverty",
                "source": "Time & Society, 2024/2025",
                "finding": "柔軟な勤務形態が時間的自律性を高めず、常時接続の期待を強化し時間貧困を再生産する「自律性のパラドックス」を発見。",
                "priority": "高"
            },
        ]
    },
    {
        "school": "School 4: Time Engineering -- 計測・データ・改善サイクル",
        "desc": "時間を計測し、データに基づいて改善するスキルを身につける（TimeCrowd直接領域）",
        "papers": [
            {
                "id": "ENG-401",
                "title": "黒田祥子 (2017) 労働時間と生産性に関する研究",
                "source": "各種学術論文",
                "finding": "日本における労働時間と生産性の関係を実証的に分析。長時間労働が生産性を下げるメカニズムを日本のデータで確認。",
                "priority": "高"
            },
            {
                "id": "ENG-402",
                "title": "Microsoft New Future of Work Report (2024/2025)",
                "source": "Microsoft Research, 2024-2025",
                "finding": "コア業務外の活動が1日275回の中断を生み、会議の60%がアドホック。AIは既存ワークフローへの追加ではなく、ナレッジワークの本質的再設計を要求。",
                "priority": "中"
            },
            {
                "id": "ENG-403",
                "title": "Pedersen, Muhr & Dunne (2024) 週4日企業のポモドーロ導入事例",
                "source": "Time & Society, 33(4), 417-437, 2024",
                "finding": "ポモドーロが生産性の「個人化」と「集団化」の両方を促進。時間管理技術は必ずしもビジネス的搾取の道具ではないことを示す反証事例。",
                "priority": "中"
            },
        ]
    },
    {
        "school": "School 5: Future of Time -- AI時代の時間再配分",
        "desc": "AI時代に「時間を設計する」とはどういうことかを考える",
        "papers": [
            {
                "id": "FUT-501",
                "title": "Brynjolfsson, Li & Raymond (2023/2025) Generative AI at Work",
                "source": "NBER WP 31161 (2023) -> Quarterly Journal of Economics, 140(2), 2025",
                "finding": "5,179名のCSエージェント実験。AI導入で解決件数14%増。新人では34%改善だが熟練者への効果は最小限。AIは優秀な労働者のベストプラクティスを組織に拡散。",
                "priority": "必読"
            },
            {
                "id": "FUT-502",
                "title": "Noy & Zhang (2023) ChatGPTのライティング生産性実験",
                "source": "Science, 2023年7月",
                "finding": "444名のRCT。ChatGPT使用群はライティング作業時間40%短縮、品質18%向上。生産性格差を圧縮（低能力者への恩恵が大）。",
                "priority": "必読"
            },
            {
                "id": "FUT-503",
                "title": "Dell'Acqua et al. (2023) Navigating the Jagged Technological Frontier",
                "source": "HBS Working Paper 24-013, 2023 -> Organization Science (forthcoming)",
                "finding": "BCGコンサルタント758名。AI能力範囲内のタスクで完了数12.2%増、速度25.1%向上、品質40%以上向上。「ケンタウロス型」と「サイボーグ型」の利用パターン。",
                "priority": "必読"
            },
            {
                "id": "FUT-504",
                "title": "Lee et al. (2025) 生成AIと批判的思考の低下",
                "source": "CHI 2025 Conference, 2025年4月",
                "finding": "319名から936事例を収集。GenAI信頼が高いほど批判的思考が低下。分析で72%、統合で76%が「少ない努力」と報告。認知スキル空洞化リスクを警告。",
                "priority": "高"
            },
            {
                "id": "FUT-505",
                "title": "HBR (2025) How Is Your Team Spending the Time Saved by Gen AI?",
                "source": "Harvard Business Review, 2025年3月",
                "finding": "AIで節約された時間が余暇や創造的思考ではなく「仕事の膨張」に吸収されるパラドックス。従業員は指示されずとも自発的にペースを速め範囲を広げる。",
                "priority": "高"
            },
            {
                "id": "FUT-506",
                "title": "森川正之 (2024) 日本企業・労働者のAI利用と生産性",
                "source": "RIETI Discussion Paper 24-J-011 / 24-E-074, 2024",
                "finding": "日本のAI利用企業は2018年の3%から2023年に10%に増加。利用者の約2/3が業務効率化を報告、主観的生産性向上は平均20%超。",
                "priority": "高"
            },
            {
                "id": "FUT-507",
                "title": "Peng et al. (2023) GitHub Copilotの開発者生産性",
                "source": "arXiv:2302.06590, 2023",
                "finding": "95名のRCT。Copilot使用群はHTTPサーバー実装タスクを55.8%速く完了。経験の少ない・年齢の高い開発者への恩恵が大きい。",
                "priority": "中"
            },
        ]
    },
    {
        "school": "補足: ドラッカー研究 -- 思想の系譜",
        "desc": "Time University全体の思想的基盤を深く理解するための文献",
        "papers": [
            {
                "id": "DRK-01",
                "title": "Peter Drucker (1999) 'Management Challenges for the 21st Century'",
                "source": "Harper Business, 1999",
                "finding": "「20世紀最大の功績は肉体労働の生産性50倍向上。21世紀に必要なのは知識労働の生産性向上」。知識労働者の生産性を高める6つの要因を提示。",
                "priority": "高"
            },
            {
                "id": "DRK-02",
                "title": "井坂康志 (2024) 『ピーター・ドラッカー -- 「マネジメントの父」の実像』",
                "source": "岩波新書, 2024年12月",
                "finding": "ドラッカー学会共同代表による最新評伝。2005年のドラッカーへの最後の外国人インタビューの知見を含む。",
                "priority": "高"
            },
            {
                "id": "DRK-03",
                "title": "吉松隆 (2017) 『ドラッカーの時間管理術』",
                "source": "アチーブメント出版, 2017",
                "finding": "ドラッカーと共に日本で研修事業を立ち上げた著者による、ドラッカーの時間管理思想の実践的体系化。",
                "priority": "中"
            },
            {
                "id": "DRK-04",
                "title": "Cal Newport (2016) 'Deep Work'",
                "source": "Grand Central Publishing, 2016",
                "finding": "ドラッカーの「時間をまとめる」提言を現代に展開。深い集中のためのブロック確保を理論化。ドラッカーを明示的に参照。",
                "priority": "高"
            },
        ]
    }
]


def build_pdf(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm,
        topMargin=15*mm, bottomMargin=15*mm,
    )
    story = []

    # --- タイトルページ ---
    story.append(Spacer(1, 30*mm))
    story.append(Paragraph("Time University", style_title))
    story.append(Paragraph("必読論文・文献リスト", ParagraphStyle(
        "TitleJP", fontName=FONT_GOTHIC, fontSize=16,
        textColor=TEXT_COLOR, spaceAfter=6*mm, alignment=TA_CENTER
    )))
    story.append(Spacer(1, 4*mm))

    # 区切り線
    line_data = [["" * 60]]
    line_table = Table(line_data, colWidths=[120*mm])
    line_table.setStyle(TableStyle([
        ("LINEBELOW", (0, 0), (-1, -1), 1.5, PRIMARY),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))
    story.append(line_table)
    story.append(Spacer(1, 6*mm))

    # サマリー
    summary_style = ParagraphStyle(
        "Summary", fontName=FONT_MINCHO, fontSize=9,
        textColor=TEXT_COLOR, leading=15, alignment=TA_CENTER
    )

    total_papers = sum(len(s["papers"]) for s in data)
    must_read = sum(1 for s in data for p in s["papers"] if p["priority"] == "必読")
    high = sum(1 for s in data for p in s["papers"] if p["priority"] == "高")

    story.append(Paragraph(
        f"全 {total_papers} 文献 / 必読 {must_read} 件 / 高優先度 {high} 件",
        summary_style
    ))
    story.append(Spacer(1, 3*mm))
    story.append(Paragraph(
        "5 Schools + ドラッカー研究補足",
        summary_style
    ))
    story.append(Spacer(1, 20*mm))

    # Schools概要テーブル
    overview_data = [
        [
            Paragraph("School", ParagraphStyle("TH", fontName=FONT_GOTHIC, fontSize=8, textColor=WHITE)),
            Paragraph("テーマ", ParagraphStyle("TH", fontName=FONT_GOTHIC, fontSize=8, textColor=WHITE)),
            Paragraph("文献数", ParagraphStyle("TH", fontName=FONT_GOTHIC, fontSize=8, textColor=WHITE)),
        ]
    ]
    for s in data:
        name = s["school"].split(" -- ")[0] if " -- " in s["school"] else s["school"]
        theme = s["school"].split(" -- ")[1] if " -- " in s["school"] else ""
        overview_data.append([
            Paragraph(name, ParagraphStyle("TD", fontName=FONT_GOTHIC, fontSize=7.5, textColor=TEXT_COLOR)),
            Paragraph(theme, ParagraphStyle("TD", fontName=FONT_MINCHO, fontSize=7.5, textColor=TEXT_COLOR)),
            Paragraph(str(len(s["papers"])), ParagraphStyle("TD", fontName=FONT_GOTHIC, fontSize=8, textColor=TEXT_COLOR, alignment=TA_CENTER)),
        ])

    overview_table = Table(overview_data, colWidths=[50*mm, 80*mm, 20*mm])
    overview_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), PRIMARY_DARK),
        ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, BG_LIGHT]),
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#DDDDDD")),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(overview_table)

    story.append(Spacer(1, 15*mm))
    story.append(Paragraph(
        "タイムクラウド株式会社 / 2026年3月",
        ParagraphStyle("Date", fontName=FONT_GOTHIC, fontSize=8, textColor=GRAY, alignment=TA_CENTER)
    ))

    story.append(PageBreak())

    # --- 各Schoolの論文リスト ---
    for school_data in data:
        story.append(Paragraph(school_data["school"], style_school))
        story.append(Paragraph(school_data["desc"], ParagraphStyle(
            "SchoolDesc", fontName=FONT_MINCHO, fontSize=8,
            textColor=GRAY, spaceAfter=3*mm
        )))

        # 区切り線
        sep = Table([[""]], colWidths=[174*mm])
        sep.setStyle(TableStyle([
            ("LINEBELOW", (0, 0), (-1, -1), 0.8, PRIMARY),
        ]))
        story.append(sep)
        story.append(Spacer(1, 2*mm))

        for paper in school_data["papers"]:
            # 優先度バッジ色
            if paper["priority"] == "必読":
                badge_color = ACCENT
            elif paper["priority"] == "高":
                badge_color = PRIMARY_DARK
            else:
                badge_color = GRAY

            # 論文タイトル行（テーブルで優先度バッジと並べる）
            badge = Paragraph(paper["priority"], style_priority)
            badge_table = Table([[badge]], colWidths=[12*mm])
            badge_table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (0, 0), badge_color),
                ("ALIGN", (0, 0), (0, 0), "CENTER"),
                ("VALIGN", (0, 0), (0, 0), "MIDDLE"),
                ("TOPPADDING", (0, 0), (0, 0), 1),
                ("BOTTOMPADDING", (0, 0), (0, 0), 1),
                ("ROUNDEDCORNERS", [2, 2, 2, 2]),
            ]))

            title_para = Paragraph(
                f"<b>{paper['id']}</b>  {paper['title']}",
                style_paper_title
            )

            row = Table(
                [[badge_table, title_para]],
                colWidths=[14*mm, 158*mm]
            )
            row.setStyle(TableStyle([
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]))
            story.append(row)

            # 出典
            story.append(Paragraph(paper["source"], style_paper_detail))

            # 知見
            story.append(Paragraph(paper["finding"], style_paper_finding))
            story.append(Spacer(1, 3*mm))

        story.append(Spacer(1, 2*mm))

    # --- 凡例 ---
    story.append(Spacer(1, 5*mm))
    legend_data = [
        [
            Paragraph("優先度の凡例", ParagraphStyle("LH", fontName=FONT_GOTHIC, fontSize=8, textColor=TEXT_COLOR)),
            "", ""
        ],
        [
            Paragraph("必読", ParagraphStyle("L", fontName=FONT_GOTHIC, fontSize=7, textColor=WHITE)),
            Paragraph("Time Universityの根幹をなす文献。最優先で読む", ParagraphStyle("LD", fontName=FONT_MINCHO, fontSize=7.5, textColor=TEXT_COLOR)),
            ""
        ],
        [
            Paragraph("高", ParagraphStyle("L", fontName=FONT_GOTHIC, fontSize=7, textColor=WHITE)),
            Paragraph("各Schoolの主要論拠。講義設計の核となるエビデンス", ParagraphStyle("LD", fontName=FONT_MINCHO, fontSize=7.5, textColor=TEXT_COLOR)),
            ""
        ],
        [
            Paragraph("中", ParagraphStyle("L", fontName=FONT_GOTHIC, fontSize=7, textColor=WHITE)),
            Paragraph("補足的な研究。深掘り時に参照", ParagraphStyle("LD", fontName=FONT_MINCHO, fontSize=7.5, textColor=TEXT_COLOR)),
            ""
        ],
    ]
    legend_table = Table(legend_data, colWidths=[20*mm, 130*mm, 20*mm])
    legend_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 1), (0, 1), ACCENT),
        ("BACKGROUND", (0, 2), (0, 2), PRIMARY_DARK),
        ("BACKGROUND", (0, 3), (0, 3), GRAY),
        ("ALIGN", (0, 1), (0, 3), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("SPAN", (0, 0), (2, 0)),
        ("LINEBELOW", (0, 0), (2, 0), 0.5, HexColor("#DDDDDD")),
    ]))
    story.append(legend_table)

    doc.build(story)
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    output = "/Users/wadashinya/00.works/74_時間設計論講義/TimeUniversity_必読論文リスト.pdf"
    build_pdf(output)
