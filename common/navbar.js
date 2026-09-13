/**
 * Navbar injection and styling for Owoloot pages.
 */
document.addEventListener("DOMContentLoaded", () => {
    const nav = document.createElement("nav");
    
    // Create a beautiful glassmorphism navbar dynamically
    nav.innerHTML = `
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 1.5rem 3rem; width: 100%; position: absolute; top: 0; left: 0; z-index: 100;">
            <div style="font-weight: 800; font-size: 1.8rem; letter-spacing: -1px; background: linear-gradient(135deg, #fff, #aaa); -webkit-background-clip: text; -webkit-text-fill-color: transparent; cursor: pointer;" onclick="window.location.href='/'">
                Owoloot
            </div>
            <div class="nav-links" style="display: flex; gap: 2rem; align-items: center;">
                <a href="/" class="nav-item">Home</a>
                <a href="/config" class="nav-item">Config</a>
                <a href="/settings" class="nav-item">Settings</a>
            </div>
        </div>
        <style>
            .nav-item {
                color: #c5c6c7;
                text-decoration: none;
                font-weight: 600;
                font-size: 1.1rem;
                transition: color 0.3s ease;
                position: relative;
            }
            .nav-item:hover {
                color: #ffffff;
            }
            .nav-item::after {
                content: '';
                position: absolute;
                bottom: -5px;
                left: 0;
                width: 0%;
                height: 2px;
                background: #66fcf1;
                transition: width 0.3s ease;
            }
            .nav-item:hover::after {
                width: 100%;
            }
            @media (max-width: 768px) {
                .nav-links {
                    display: none !important;
                }
            }
        </style>
    `;
    
    // Inject at the very top of the body
    document.body.insertBefore(nav, document.body.firstChild);
});
