gsap.registerPlugin(ScrollTrigger);
gsap.registerPlugin(ScrollToPlugin);
gsap.registerPlugin(TextPlugin);

// Scroll arrow animations
$("#scrollReminder").on("click", function() {
    gsap.to(window, { duration: .75, scrollTo: ".content-1" });
});

function scrollArrow() {
    var tl = gsap.timeline({
        repeat: -1,
        repeatDelay: 1
    })

    tl.from(".scroll-arrow", {
        opacity: 0
    });

    tl.to(".scroll-arrow", {
        y: 8,
        ease: "power1.inOut"
    }, "<");

    tl.to(".scroll-arrow", {
        opacity: 0
    });
}

// Hero typing effect
function typingEffect(textList) {
    var words = textList,
        tl = gsap.timeline(),
        wordCount = words.length,
        lastWord = "Alexandria"

    tl.set("#iam", {
        text: "",
    })

    for (let i = 0; i < wordCount; i++) {
        word = words[i];
        tl.to("#iam", {
            duration: word.length * 0.1,
            text: word,
            ease: "slow(0.25, 0.9)",
            repeat: 1,
            yoyo: true,
        }, "+=.25")
    }

    tl.to("#iam", {
        duration: lastWord.length * 0.1,
        text: lastWord,
        ease: "slow(0.25, 0.9)",
        repeat: false,
        yoyo: false,
    })

    tl.from(".hero-sub-heading", {
        opacity: 0,
        y: -10,
        ease: "elastic.out(1, 0.5)",
    }, "+=0")

    tl.from("#scroll-reminder", {
        opacity: 0,
        y: -56,
        onComplete: scrollArrow()
    })

    tl.to(".type-cursor", {
        opacity: 0,
        ease: "power1.inOut",
        repeat: -1,
        yoyo: true,
    }, "+=0")

    // if ( !document.cookie.includes("subscribed_email=True") ) {
    //     tl.add(function(){ $('#emailPrompt').modal('show') })
    // }

}

typingEffect(iamList);

// Parallax sections
gsap.utils.toArray("section.parallax").forEach((section, i) => {
    section.bg = section.querySelector(".section-bg");

    section.bg.style.backgroundPosition = `50% ${-innerHeight / 2}px`;

    gsap.to(section.bg, {
        backgroundPosition: `50% ${innerHeight / 2}px`,
        ease: "none",
        scrollTrigger: {
            trigger: section,
            scrub: true
        }
    });
});

// Quote border
// gsap.timeline({
//         scrollTrigger: {
//             trigger: "section.quote .quote-text",
//             toggleActions: "play reset play reset",
//         }
//     })
//     .from("section.quote .qb-bottom-left", {
//         scaleX: 0,
//         duration: .25,
//     })
//     .from("section.quote .qb-left", {
//         scaleY: 0,
//         duration: .25,
//     })
//     .from("section.quote .qb-top", {
//         scaleX: 0,
//         duration: .5,
//     })
//     .from("section.quote .qb-right", {
//         scaleY: 0,
//         duration: .25,
//     })
//     .from("section.quote .qb-bottom-right", {
//         scaleX: 0,
//         duration: .25,
//     })

// Stat border
// gsap.timeline({
//         scrollTrigger: {
//             trigger: "section.stat .stat-text",
//             toggleActions: "play reset play reset",
//         }
//     })
//     .from("section.stat .qb-bottom-left", {
//         scaleX: 0,
//         duration: .25,
//     })
//     .from("section.stat .qb-left", {
//         scaleY: 0,
//         duration: .25,
//     })
//     .from("section.stat .qb-top", {
//         scaleX: 0,
//         duration: .5,
//     })
//     .from("section.stat .qb-right", {
//         scaleY: 0,
//         duration: .25,
//     })
//     .from("section.stat .qb-bottom-right", {
//         scaleX: 0,
//         duration: .25,
//     })