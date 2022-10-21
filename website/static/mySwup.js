var swup = new Swup({
    cache: false,
    pageClassPrefix: '',
    scroll: true,
    debugMode: false,
    preload: true,
    support: true,
    plugins: [
        new SwupSlideTheme(),
        new SwupProgressPlugin(
            {
                className: 'swup-progress-bar',
                transition: 300,
                delay: 0,
                initialValue: 0.25,
                hideImmediately: true
            }
        ),
    ],
    animateHistoryBrowsing: true,
});
