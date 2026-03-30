# PROMPT 2: Design System -- Time University

## Brand Attributes
MINIMAL / LUXURY / ACADEMIC

## Color Palette

### Primary
| Token | Hex | Usage |
|-------|-----|-------|
| --primary | #4ECDC4 | Accent highlights, links, active states |
| --primary-dark | #26A69A | Hover states, section backgrounds |
| --primary-light | rgba(78,205,196,0.08) | Subtle background tints |

### Accent
| Token | Hex | Usage |
|-------|-----|-------|
| --accent | #FF7043 | CTA buttons, key callouts |
| --accent-dark | #E64A19 | Button hover |
| --accent-light | rgba(255,112,67,0.08) | Subtle accent backgrounds |

### Neutrals
| Token | Hex | Usage |
|-------|-----|-------|
| --bg | #F5F5F5 | Page background |
| --surface | #FFFFFF | Cards, content areas |
| --text | #333333 | Body text |
| --text-secondary | #6C757D | Supporting text |
| --text-tertiary | #ADB5BD | Placeholder, metadata |
| --border | #E9ECEF | Dividers, card borders |

### Dark Theme (Hero, Quote blocks)
| Token | Hex | Usage |
|-------|-----|-------|
| --dark-bg | #0D1117 | Hero background base |
| --dark-surface | #161B22 | Cards on dark bg |
| --dark-text | #E6EDF3 | Text on dark |
| --dark-text-secondary | rgba(255,255,255,0.5) | Secondary on dark |

## Typography Scale (9 levels)

| Level | Size | Weight | Line Height | Font | Usage |
|-------|------|--------|-------------|------|-------|
| Display | 64px / 4rem | 700 | 1.1 | Playfair Display | Hero title |
| H1 | 40px / 2.5rem | 700 | 1.2 | Playfair Display | Section titles |
| H2 | 28px / 1.75rem | 600 | 1.3 | Inter | Sub-section titles |
| H3 | 20px / 1.25rem | 600 | 1.4 | Inter | Card titles |
| Body Large | 18px / 1.125rem | 400 | 1.7 | Inter + Noto Sans JP | Lead paragraphs |
| Body | 16px / 1rem | 400 | 1.7 | Inter + Noto Sans JP | Default text |
| Body Small | 14px / 0.875rem | 400 | 1.6 | Inter + Noto Sans JP | Captions, metadata |
| Label | 12px / 0.75rem | 600 | 1.4 | Inter | Tags, overlines |
| Overline | 11px / 0.6875rem | 700 | 1.2 | Inter | Section labels (letter-spacing: 3px) |

### Mobile overrides
- Display: 36px / 2.25rem
- H1: 28px / 1.75rem
- H2: 22px / 1.375rem

## Spacing System (8px grid)

| Token | Value | Usage |
|-------|-------|-------|
| --space-1 | 4px | Inline spacing |
| --space-2 | 8px | Tight spacing |
| --space-3 | 12px | Input padding |
| --space-4 | 16px | Card padding (mobile) |
| --space-5 | 24px | Card padding, section gap |
| --space-6 | 32px | Between elements |
| --space-7 | 48px | Section padding (mobile) |
| --space-8 | 64px | Section padding |
| --space-9 | 96px | Hero padding |
| --space-10 | 128px | Major section gap |

## Component Specs

### Button (CTA)
- Height: 56px
- Padding: 0 40px
- Border-radius: 12px
- Font: 16px / 600 / Inter
- Background: var(--accent)
- Hover: var(--accent-dark), translateY(-2px), shadow
- Transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)
- Box-shadow: 0 4px 14px rgba(255,112,67,0.3)
- Hover shadow: 0 8px 25px rgba(255,112,67,0.4)

### Card
- Background: var(--surface)
- Border-radius: 16px
- Padding: 32px
- Box-shadow: 0 1px 3px rgba(0,0,0,0.04)
- Hover: translateY(-4px), box-shadow: 0 12px 40px rgba(0,0,0,0.08)
- Transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1)
- Border: 1px solid transparent → hover: 1px solid var(--primary)

### Input
- Height: 52px
- Padding: 0 16px
- Border: 1.5px solid var(--border)
- Border-radius: 10px
- Font: 15px / 400
- Focus: border-color var(--primary), box-shadow 0 0 0 3px var(--primary-light)
- Transition: all 0.2s

### Section Container
- Max-width: 1120px
- Padding: 0 24px (mobile: 0 16px)
- Margin: 0 auto

## Animation
- Scroll reveal: opacity 0 → 1, translateY(30px → 0), duration 0.7s
- Stagger children: delay 0.1s per item
- Easing: cubic-bezier(0.4, 0, 0.2, 1)
- Use Intersection Observer with threshold 0.1

## Icons
- SVG inline only (no icon library)
- Stroke-width: 1.5
- Size: 24px default, 32px for feature icons
- Color: currentColor
