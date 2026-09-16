import re

with open('ref.html', 'r', encoding='utf-8') as f:
    ref = f.read()

with open('pages/accounts.html', 'r', encoding='utf-8') as f:
    acc = f.read()

# Extract head and beginning of body from ref
ref_head = re.search(r'<head>.*?</head>', ref, flags=re.DOTALL).group(0)

# Replace cursor and loader stuff in ref_head just in case they were left (they were removed, but let's be sure)
ref_head = ref_head.replace('<title>XTREME — New Era</title>', '<title>XTREME — Accounts</title>')

# Add some custom styles for Accounts on top of ref_head
custom_styles = '''
        /* ─── ACCOUNTS UI ─── */
        .accounts-section {
            position: relative; z-index: 10; min-height: 100vh;
            padding: 120px 40px; display: flex; flex-direction: column;
            align-items: center; justify-content: flex-start;
        }
        .acc-container {
            width: 100%; max-width: 950px; background: rgba(0, 0, 0, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.08); padding: 40px;
            backdrop-filter: blur(12px); margin-top: 40px;
        }
        .acc-header {
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;
        }
        .acc-h1 {
            font-family: 'Playfair Display', serif; font-size: clamp(32px, 5vw, 64px);
            font-weight: 900; line-height: 1.05; color: #fff;
        }
        .acc-h1 em { font-style: italic; color: var(--c2); }
        .acc-subtitle {
            font-family: 'Space Grotesk', sans-serif; font-size: 13px; font-weight: 300;
            color: rgba(255, 255, 255, .55); line-height: 1.7; margin-bottom: 32px;
        }
        .input-group { margin-bottom: 24px; }
        .input-label {
            display: block; font-family: 'Space Grotesk', sans-serif; font-size: 11px;
            letter-spacing: .15em; text-transform: uppercase; color: var(--c1);
            margin-bottom: 8px;
        }
        .input-row { display: flex; gap: 12px; }
        .modern-input {
            flex: 1; padding: 14px 20px; background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.15); color: #fff;
            font-family: 'Space Grotesk', sans-serif; font-size: 13px; outline: none;
            transition: border-color 0.3s;
        }
        .modern-input:focus { border-color: var(--c2); }
        
        .limit-badge {
            display: inline-flex; align-items: center; padding: 6px 12px;
            font-size: 11px; font-family: 'Space Grotesk', sans-serif;
            background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); color: #fff;
        }
        .limit-badge.warning { background: rgba(255, 45, 85, 0.15); border-color: var(--c1); color: var(--c1); }
        
        .profile-card {
            display: flex; align-items: center; gap: 16px; padding: 16px 20px;
            background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08);
            margin-bottom: 32px;
        }
        .profile-avatar {
            width: 48px; height: 48px; border-radius: 50%; background: var(--c1);
            display: flex; align-items: center; justify-content: center; font-weight: 800; font-family: 'Bebas Neue', sans-serif; font-size: 20px;
        }
        .profile-details h3 { font-family: 'Space Grotesk', sans-serif; font-size: 15px; font-weight: 700; color: #fff; margin-bottom: 4px; }
        .profile-details p { font-family: 'Space Grotesk', sans-serif; font-size: 11px; color: rgba(255,255,255,0.5); }
        
        .section-header-wrap {
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; margin-top: 32px;
        }
        .section-title {
            font-family: 'Space Grotesk', sans-serif; font-size: 13px; font-weight: 700; color: #fff;
            text-transform: uppercase; letter-spacing: .15em;
        }
        
        .item-grid {
            display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 12px;
            margin-bottom: 24px;
        }
        .select-card {
            background: rgba(0,0,0,0.4); padding: 16px 20px;
            border: 1px solid rgba(255,255,255,0.1); cursor: pointer; transition: all 0.2s;
            display: flex; align-items: center; justify-content: space-between;
        }
        .select-card:hover { border-color: rgba(10,255,228,0.4); background: rgba(10,255,228,0.04); }
        .select-card.selected {
            border-color: var(--c2); background: rgba(10,255,228,0.12);
        }
        .select-card.disabled {
            opacity: 0.4; cursor: not-allowed; border-color: rgba(255,255,255,0.05);
        }
        .select-name { font-family: 'Space Grotesk', sans-serif; font-weight: 600; font-size: 12px; color: #fff; }
        .select-check {
            width: 16px; height: 16px; border: 1px solid rgba(255,255,255,0.3);
            display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; color: transparent; transition: color 0.2s, border-color 0.2s;
        }
        .select-card.selected .select-check { border-color: var(--c2); color: var(--c2); }
        
        .alert-box {
            padding: 16px 20px; font-size: 12px; font-family: 'Space Grotesk', sans-serif;
            margin-bottom: 24px; display: none; border-left: 3px solid;
        }
        .alert-box.error { background: rgba(255, 45, 85, 0.1); border-color: var(--c1); color: #fff; }
        .alert-box.success { background: rgba(10, 255, 228, 0.1); border-color: var(--c2); color: #fff; }
        
        .save-bar {
            margin-top: 40px; display: flex; justify-content: flex-end; gap: 16px; border-top: 1px solid rgba(255, 255, 255, 0.08); padding-top: 24px;
        }
'''

ref_head = ref_head.replace('</style>', custom_styles + '\n    </style>')

ref_body_start = re.search(r'<body.*?>.*?<!-- NAV -->.*?</nav>', ref, flags=re.DOTALL).group(0)

# Extract JS from acc
acc_script = re.search(r'<script>(.*?)</script>', acc, flags=re.DOTALL).group(0)

new_html = f'''<!DOCTYPE html>
<html lang="en">
{ref_head}
<body>
    <!-- BACKGROUNDS -->
    <div id="bg-wrap">
        <img id="bg-img" src="" alt="" class="fade-in">
    </div>
    <div class="bg-grain"></div>
    <div class="bg-color-bleed" id="colorBleed"></div>
    <div class="vignette"></div>

    <!-- XTREME WATERMARK -->
    <div id="wm">XTREME</div>
    
    <!-- NOTIFICATION TOAST -->
    <div id="notif-toast">
        <button class="notif-close" onclick="closeToast()">&times;</button>
        <div class="notif-title" id="nt-title">XTREME</div>
        <div class="notif-body" id="nt-body">Welcome to the new era.</div>
    </div>

    <!-- NAV -->
    <nav id="navbar">
        <a href="/" class="logo">XTREME</a>
        <ul class="nav-links">
            <li><a href="/" data-symbol="◈">Dashboard</a></li>
            <li><a href="/accounts" data-symbol="◉">Accounts</a></li>
            <li><a href="/settings" data-symbol="◫">Settings</a></li>
        </ul>
        <div class="nav-right">
            <button class="notif-btn" onclick="requestNotif()" title="Enable notifications">
                ◉
                <div class="notif-dot"></div>
            </button>
            <button class="ham" id="ham" onclick="toggleMenu()">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>
    
    <!-- FULL MENU OVERLAY -->
    <div id="menu-overlay">
        <div class="menu-inner">
            <p class="menu-tag">◈ Navigation ◈</p>
            <ul class="menu-nav">
                <li><a href="/" onclick="closeMenu()"><span class="sym">◈</span>Dashboard</a></li>
                <li><a href="/accounts" onclick="closeMenu()"><span class="sym">◉</span>Accounts</a></li>
                <li><a href="/settings" onclick="closeMenu()"><span class="sym">◫</span>Settings</a></li>
            </ul>
        </div>
    </div>
    
    <section class="accounts-section">
        <div class="acc-container">
            <div class="acc-header">
                <h1 class="acc-h1">Account<br><em>Configuration</em></h1>
                <a href="/" class="btn-ghost">Back to Dash</a>
            </div>
            
            <p class="acc-subtitle">Connect your Discord account to fetch servers and select target channels for OwO commands. Strict limits: Max 2 servers &amp; Max 10 channels.</p>
            
            <div class="alert-box" id="alert-box"></div>
            
            <div class="input-group">
                <label class="input-label">◈ Discord Account Token</label>
                <div class="input-row">
                    <input type="password" id="token-input" class="modern-input" placeholder="Enter Discord Token (e.g. MTAx...)" />
                    <button class="btn-primary" onclick="connectAccount()"><span>Connect</span></button>
                </div>
            </div>
            
            <!-- PROFILE DISPLAY -->
            <div class="profile-card" id="profile-card" style="display:none;">
                <div class="profile-avatar" id="prof-avatar">OWO</div>
                <div class="profile-details">
                    <h3 id="prof-name">Account Loading...</h3>
                    <p id="prof-id">ID: ----------</p>
                </div>
            </div>
            
            <!-- SERVER SELECTION SECTION -->
            <div class="section-header-wrap">
                <span class="section-title">◈ Select Target Servers</span>
                <span class="limit-badge" id="server-badge">0 / 2 Servers Selected</span>
            </div>
            <div class="item-grid" id="servers-grid">
                <p style="color:rgba(255,255,255,0.4); font-size:12px; font-family:'Space Grotesk';">Connect a Discord token to fetch servers.</p>
            </div>
            
            <!-- CHANNEL SELECTION SECTION -->
            <div class="section-header-wrap">
                <span class="section-title">⬡ Select Target Channels</span>
                <span class="limit-badge" id="channel-badge">0 / 10 Channels Selected</span>
            </div>
            <div class="item-grid" id="channels-grid">
                <p style="color:rgba(255,255,255,0.4); font-size:12px; font-family:'Space Grotesk';">Select a server above to fetch text channels.</p>
            </div>
            
            <div class="save-bar">
                <button class="btn-primary" onclick="saveConfiguration()"><span>◈ Save Targets</span></button>
            </div>
        </div>
    </section>
    
    <footer>
        <div class="footer-top">
            <div class="footer-logo">XTREME</div>
            <ul class="footer-links">
                <li><a href="#">◈ Instagram</a></li>
                <li><a href="#">⬡ Twitter</a></li>
            </ul>
        </div>
        <div class="footer-bottom">
            <p class="footer-copy">© 2025 XTREME STUDIO — ALL RIGHTS RESERVED</p>
            <p class="footer-copy" id="bgCredit">Background: Artwork Collection</p>
        </div>
    </footer>
    
{acc_script}

    <script>
        /* ══ RE-USE REF.HTML BG LOGIC ══ */
        const BG_IMAGES = [
            'https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=1600',
            'https://images.unsplash.com/photo-1579547944212-c4f4961a8dd8?w=1600'
        ];
        const WM_FONTS = ["'Bebas Neue',sans-serif", "'Orbitron',sans-serif"];
        const WM_SIZES = ['12vw', '14vw'];
        const COLORS = [ ['#ff2d55', '#0affe4'], ['#ff6b35', '#c7ff3a'] ];

        const bgImg = document.getElementById('bg-img');
        const wm = document.getElementById('wm');
        const colorBleed = document.getElementById('colorBleed');
        let bgIdx = 0; let colorIdx = 0;

        function applyColors(i) {{
            const [c1, c2] = COLORS[i % COLORS.length];
            document.documentElement.style.setProperty('--c1', c1);
            document.documentElement.style.setProperty('--c2', c2);
            colorBleed.style.background = `radial-gradient(ellipse at 30% 70%, ${{c1}}44, transparent 60%), radial-gradient(ellipse at 70% 30%, ${{c2}}33, transparent 60%)`;
        }}
        function setWatermark() {{ wm.style.fontFamily = WM_FONTS[0]; wm.style.fontSize = WM_SIZES[0]; }}
        function loadBg(idx) {{
            const url = BG_IMAGES[idx % BG_IMAGES.length];
            const tmp = new Image();
            tmp.onload = () => {{
                bgImg.classList.remove('fade-in'); bgImg.classList.add('fade-out');
                setTimeout(() => {{
                    bgImg.src = url; bgImg.classList.remove('fade-out'); bgImg.classList.add('fade-in');
                }}, 600);
            }};
            tmp.src = url;
        }}
        setWatermark(); applyColors(colorIdx); loadBg(bgIdx);

        let menuOpen = false;
        function toggleMenu() {{
            menuOpen = !menuOpen;
            document.getElementById('ham').classList.toggle('open', menuOpen);
            document.getElementById('menu-overlay').classList.toggle('open', menuOpen);
            document.body.style.overflow = menuOpen ? 'hidden' : '';
        }}
        function closeMenu() {{ toggleMenu(); }}
        
        window.addEventListener('scroll', () => {{
            document.getElementById('navbar').classList.toggle('scrolled', window.scrollY > 60);
        }});
        function requestNotif() {{}}
    </script>
</body>
</html>
'''

with open('pages/accounts.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
