document.addEventListener("DOMContentLoaded", () => {
    const currentLanguage = document.documentElement.lang || "";
    const reveals = document.querySelectorAll(".reveal");
    const previewShots = document.querySelectorAll(".site-shot");
    const autofitTitles = document.querySelectorAll("[data-autofit-title]");

    const fitTitle = (element) => {
        if (!currentLanguage.startsWith("ko")) {
            element.style.removeProperty("font-size");
            return;
        }

        const min = Number.parseFloat(element.dataset.autofitMin || "2.6");
        const max = Number.parseFloat(element.dataset.autofitMax || "6.2");
        let low = min;
        let high = max;
        let best = min;

        element.style.fontSize = `${max}rem`;

        for (let index = 0; index < 18; index += 1) {
            const mid = (low + high) / 2;
            element.style.fontSize = `${mid}rem`;

            if (element.scrollWidth <= element.clientWidth) {
                best = mid;
                low = mid;
            } else {
                high = mid;
            }
        }

        element.style.fontSize = `${best}rem`;
    };

    const fitAllTitles = () => {
        autofitTitles.forEach((element) => fitTitle(element));
    };

    previewShots.forEach((image) => {
        image.addEventListener("error", () => {
            const preview = image.closest("[data-preview-shell]");
            if (preview) {
                preview.classList.add("is-fallback");
            }
        });
    });

    fitAllTitles();

    if ("ResizeObserver" in window) {
        const resizeObserver = new ResizeObserver(() => {
            fitAllTitles();
        });

        autofitTitles.forEach((element) => {
            const container = element.parentElement;
            if (container) {
                resizeObserver.observe(container);
            }
        });
    } else {
        window.addEventListener("resize", fitAllTitles);
    }

    if (!("IntersectionObserver" in window)) {
        reveals.forEach((item) => item.classList.add("is-visible"));
        return;
    }

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) {
                    return;
                }

                entry.target.classList.add("is-visible");
                observer.unobserve(entry.target);
            });
        },
        {
            threshold: 0.12,
            rootMargin: "0px 0px -8% 0px",
        },
    );

    reveals.forEach((item) => observer.observe(item));
});
