(function () {
    const toggle = document.getElementById('menu-toggle');
    const close = document.getElementById('menu-close');
    const menu = document.getElementById('side-menu');
    const backdrop = document.getElementById('side-menu-backdrop');

    if (!toggle || !close || !menu || !backdrop) {
        return;
    }

    function setMenu(open) {
        menu.classList.toggle('is-open', open);
        menu.setAttribute('aria-hidden', String(!open));
        toggle.setAttribute('aria-expanded', String(open));
        backdrop.hidden = !open;
        document.body.classList.toggle('menu-open', open);
    }

    toggle.addEventListener('click', function () {
        setMenu(!menu.classList.contains('is-open'));
    });

    close.addEventListener('click', function () {
        setMenu(false);
    });

    backdrop.addEventListener('click', function () {
        setMenu(false);
    });

    document.querySelectorAll('[data-menu-link]').forEach(function (link) {
        link.addEventListener('click', function () {
            setMenu(false);
        });
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && menu.classList.contains('is-open')) {
            setMenu(false);
            toggle.focus();
        }
    });
}());
