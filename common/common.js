/**
 * Common utilities and shared functions for Owoloot frontend.
 */
console.log("Common scripts initialized.");

// Utility to add smooth fadeIn animations to elements dynamically
function animateEntrance(element, delay = 0) {
    element.style.opacity = '0';
    element.style.transform = 'translateY(20px)';
    element.style.transition = `all 0.6s ease-out ${delay}s`;
    
    setTimeout(() => {
        element.style.opacity = '1';
        element.style.transform = 'translateY(0)';
    }, 50);
}
