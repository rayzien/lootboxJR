/**
 * Advanced Burger Menu for Owoloot.
 * Features a centralized navigation panel, system status, and creator credits.
 * Pushes content to prevent overlap and uses clean SVGs instead of emojis.
 */
document.addEventListener("DOMContentLoaded", () => {
    // Add overflow-x hidden to body to prevent scrollbars when pushing content
    document.body.style.overflowX = 'hidden';
    document.body.style.transition = 'margin-right 0.4s cubic-bezier(0.77, 0, 0.175, 1)';
    document.body.style.marginRight = '0';

    // Container for the floating toggle button
    const menuContainer = document.createElement("div");
    menuContainer.className = "burger-menu-container";
    menuContainer.style.cssText = "position: fixed; top: 1.5rem; right: 2rem; z-index: 1001;";
    
    // SVGs for icons instead of emojis
    const closeIcon = `
        <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>
    `;
    const burgerIcon = `
        <svg viewBox="0 0 24 24" width="24" height="24" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
            <line x1="3" y1="12" x2="21" y2="12"></line>
            <line x1="3" y1="6" x2="21" y2="6"></line>
            <line x1="3" y1="18" x2="21" y2="18"></line>
        </svg>
    `;

    const btn = document.createElement("button");
    btn.innerHTML = burgerIcon;
    btn.style.cssText = "background: rgba(31, 40, 51, 0.8); backdrop-filter: blur(8px); border: 1px solid rgba(102, 252, 241, 0.3); border-radius: 50%; width: 50px; height: 50px; color: #fff; cursor: pointer; transition: all 0.3s ease; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 15px rgba(0,0,0,0.3);";
    
    btn.addEventListener("mouseover", () => {
        if (!isOpen) {
            btn.style.transform = "scale(1.1)";
            btn.style.borderColor = "rgba(102, 252, 241, 0.8)";
        }
    });
    btn.addEventListener("mouseout", () => {
        if (!isOpen) {
            btn.style.transform = "scale(1)";
            btn.style.borderColor = "rgba(102, 252, 241, 0.3)";
        }
    });

    // The sliding side panel
    const sidePanel = document.createElement("div");
    sidePanel.className = "side-panel-nav";
    sidePanel.style.cssText = "position: fixed; top: 0; right: -320px; width: 320px; height: 100vh; background: rgba(11, 12, 16, 0.95); backdrop-filter: blur(15px); z-index: 1000; display: flex; flex-direction: column; padding: 6rem 2.5rem 2.5rem; transition: right 0.4s cubic-bezier(0.77, 0, 0.175, 1); border-left: 1px solid rgba(102, 252, 241, 0.2); box-shadow: -10px 0 30px rgba(0,0,0,0.5); font-family: 'Outfit', sans-serif;";
    
    sidePanel.innerHTML = `
        <div style="margin-bottom: 3rem;">
            <h2 style="color: #fff; font-size: 2.2rem; font-weight: 800; margin-bottom: 0.5rem; background: linear-gradient(135deg, #66fcf1, #45a29e); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">Owoloot</h2>
            <div style="display: flex; align-items: center; gap: 0.6rem; font-size: 0.95rem; color: #c5c6c7; font-weight: 300;">
                <div style="width: 10px; height: 10px; background-color: #4CAF50; border-radius: 50%; box-shadow: 0 0 12px #4CAF50; animation: pulse 2s infinite;"></div>
                System Status: <span style="color: #4CAF50; font-weight: 600;">Online</span>
            </div>
        </div>
        
        <div style="display: flex; flex-direction: column; gap: 1.5rem; flex-grow: 1;">
            <a href="/" class="panel-link" style="color: #fff; text-decoration: none; font-size: 1.3rem; font-weight: 500; display: flex; align-items: center; transition: all 0.2s;">
                Home
            </a>
            <a href="/config" class="panel-link" style="color: #fff; text-decoration: none; font-size: 1.3rem; font-weight: 500; display: flex; align-items: center; transition: all 0.2s;">
                Configuration
            </a>
            <a href="/settings" class="panel-link" style="color: #fff; text-decoration: none; font-size: 1.3rem; font-weight: 500; display: flex; align-items: center; transition: all 0.2s;">
                Settings
            </a>
        </div>

        <div style="margin-top: auto; padding-top: 2rem; border-top: 1px solid rgba(255,255,255,0.1); text-align: center; color: #888; font-size: 0.9rem;">
            Created by <span style="color: #66fcf1; font-weight: 600;">pheonix14</span>
        </div>

        <style>
            @keyframes pulse {
                0% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0.7); }
                70% { box-shadow: 0 0 0 10px rgba(76, 175, 80, 0); }
                100% { box-shadow: 0 0 0 0 rgba(76, 175, 80, 0); }
            }
        </style>
    `;

    let isOpen = false;

    btn.addEventListener("click", () => {
        isOpen = !isOpen;
        
        // Find existing navbar if it exists to slide it as well
        const nav = document.querySelector('nav > div');

        if (isOpen) {
            sidePanel.style.right = "0";
            btn.innerHTML = closeIcon;
            btn.style.transform = "rotate(90deg)";
            btn.style.background = "rgba(102, 252, 241, 0.1)";
            
            // Push content so it doesn't overlap
            if (window.innerWidth > 600) {
                document.body.style.marginRight = "320px";
                if(nav) {
                    nav.style.transition = "padding-right 0.4s cubic-bezier(0.77, 0, 0.175, 1)";
                    nav.style.paddingRight = "calc(3rem + 320px)";
                }
            }
        } else {
            sidePanel.style.right = "-320px";
            btn.innerHTML = burgerIcon;
            btn.style.transform = "rotate(0deg)";
            btn.style.background = "rgba(31, 40, 51, 0.8)";
            
            // Reset content push
            document.body.style.marginRight = "0";
            if(nav) nav.style.paddingRight = "3rem";
        }
    });

    // Add elements to DOM
    menuContainer.appendChild(btn);
    document.body.appendChild(menuContainer);
    document.body.appendChild(sidePanel);

    // Hover effects for the links
    const links = document.querySelectorAll('.panel-link');
    links.forEach(link => {
        link.addEventListener('mouseover', () => {
            link.style.color = '#66fcf1';
            link.style.transform = 'translateX(10px)';
        });
        link.addEventListener('mouseout', () => {
            link.style.color = '#fff';
            link.style.transform = 'translateX(0)';
        });
    });
});
