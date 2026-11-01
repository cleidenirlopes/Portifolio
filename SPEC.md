# Technical Specifications (SPEC)
**Data-Centric UI Refactor Directive**

## 1. Design Tokens & Aesthetic: "Glassmorphism & High Contrast"
- **Primary Background (Void):** `#121212` (Deep Charcoal) - Sets the foundation.
- **Secondary Surface (Cards/Modules):** `#1A2238` (Navy Slate) - Provides contrast for interactive elements.
- **Accent Color:** `#2b88c6` (Electric Blue) - Used directly for all interaction points (buttons/links/hover states).
- **Typography:** Enforce font weights (300 for body, 400 for structural text, 700 for headers). Maximize contrast in the 'About Me' text (`#ffffff` instead of `#e0e0e0` or `#b0b0b0`).

## 2. Structural Architecture Refinements
The portfolio will embrace a true Data-Centric UI architecture, enhancing hierarchy and structural alignment.

### A. Hero & Global Layout
- **Particle System:** Reduce `particles.js` opacity (`opacity.value`) to exactly `0.2` to function strictly as a subtle texture rather than an active animation.
- **About Me / Hero Alignment:** Increase contrast and ensure absolute visual centering. Correct the "displacement issue" by applying rigorous flex alignment and removing any unbalanced padding/margins.

### B. Project Cards (Grid & Glassmorphism)
- **CSS Grid:** Enforce a strict `grid-template-columns: repeat(3, 1fr)` for the Projects section.
- **Card Structure:** 
  - Apply `border-radius: 12px` to all project cards.
  - Implement a true CSS Glassmorphism hover effect on the overlay: `background: rgba(26, 34, 56, 0.7); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);`.

## 3. Execution Protocol
- **No Overwriting/Simplification:** Do not simplify structure. Maintain the robust HTML data model and apply targeted CSS/style modifications.
- **Link Integrity & Mobile:** The mobile layout must gracefully fallback to a 1 or 2-column grid without breaking the glassmorphism or link paths. No text lists allowed.
- **Deployment Strategy:** Deploy to Netlify via `netlify deploy --prod --dir=.` after verifying changes locally.
